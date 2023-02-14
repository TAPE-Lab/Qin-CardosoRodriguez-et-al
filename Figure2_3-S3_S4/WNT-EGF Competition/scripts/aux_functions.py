import numpy as np
import pandas as pd
import scprep
import re

from MultiscaleEMD import MetricTree
from sklearn.preprocessing import OneHotEncoder

# Arcsinh transform the data
def arcsinh_transf(no_arc, markers, cofactor):
    # Apply the arcsinh only to those columns (don't want to change time or any other)
    arc = no_arc.apply(lambda x: np.arcsinh(x / cofactor) if x.name in markers else x)
    return arc


# EMD calculation
def calculate_emd(
    markers, compare_from, compare_to, metadata_columns, emd_df, emd_infodict
):
    emd_df = pd.DataFrame(columns=metadata_columns + ["marker", "EMD_arc"])
    for marker in markers:
        for metadata_column in metadata_columns:
            emd_infodict[metadata_column] = compare_from.loc[
                :, metadata_column
            ].tolist()[0]

        emd_infodict["marker"] = marker

        if (compare_from[marker].median() - compare_to[marker].median()) >= 0:
            emd_infodict["EMD_arc"] = scprep.stats.EMD(
                compare_from[marker], compare_to[marker]
            )
        else:
            emd_infodict["EMD_arc"] = -scprep.stats.EMD(
                compare_from[marker], compare_to[marker]
            )
        # Add EMD score to the output dataframe
        emd_df.loc[len(emd_df)] = emd_infodict

    return emd_df


# Subset dataframe based on column values
def master_df_subset(emd_df_master, markers_to_keep):
    df_subset = emd_df_master.drop(
        emd_df_master.columns.difference(markers_to_keep), axis=1
    )
    return df_subset


# From CyGNAL:
# Filtering
def filter_columns(renamed_columns):
    reg_filter = re.compile("^\d+[A-Za-z]+$")  # Removes columns with just isotope
    filtered_columns = []  # Stores the columns that where deemed unnecessary
    columns_to_keep = []  # Columns that the reduced file should have
    for i in renamed_columns:
        if reg_filter.search(i):
            filtered_columns.append(i)
        else:
            columns_to_keep.append(i)
    return columns_to_keep, filtered_columns


# Renaming
def rename_columns(df_file_cols):
    reg_rename = re.compile("(__[a-z].*$|__\d.*$|_\(.*$|___.*$)")
    # First two options match ending constructs with double underscores
    # Third option matches endings within brackets
    df_file_cols_processed = []
    df_file_cols_renamed = []
    df_file_cols_final = []

    for i in df_file_cols:  # First pass to remove most issues
        try:
            df_file_cols_processed.append(reg_rename.sub("", i))
        except:
            df_file_cols_processed.append(i)
    # Second pass to remove trailing underscores
    for i in df_file_cols_processed:
        try:
            df_file_cols_renamed.append(re.sub(r"_$", "", i))
        except:
            df_file_cols_renamed.append(i)
    # Third pass replace '__' with '_'
    for i in df_file_cols_renamed:
        try:
            df_file_cols_final.append(re.sub(r"__", "_", i))
        except:
            df_file_cols_final.append(i)
    # Keeping with Xiao's convention, rename Event # to Cell_Index
    for n, i in enumerate(df_file_cols_final):
        if i == "Event #":
            df_file_cols_final[n] = "Cell_Index"

    return df_file_cols_final


# Trellis


def l1_embeddings(cts, edge_weights):
    return np.array(
        [np.asarray(cts)[i, :] * np.asarray(edge_weights) for i in range(len(cts))]
    )


def leaf_runner(
    data,
    labels,
    tree_type,
    n_trees,
    leaf_phases,
    df_tree,
    norm_per_subtree=False,
    random_state=42,
    **kwargs
):
    """Creates tree embeddings for each sample based on tree parameters.

    Parameters:

        data: [# cells x # features] data matrix
        labels: [# cells x # distributions] (potentially sparse) describing membership of cells to distributions
        tree_type: type of tree to build over the features
        n_trees: how many trees to build
        leaf_phases:
        df_tree:
        norm_per_subtree: whether to treat each subtree as a separate distribution,
                          this essentially weights each subtree equally, rather than weighting
                          based on how many cells are in each subtree (default)

    Returns:
        leaf_embeds: [# distributions x (n_trees x n_nodes)] embeddings one per distribution where L1 distrance
                     between embeddings represents tree EMD
        leaf_trees: Tree objects for each tree
        leaf_ids: Leaf label for each tree node [n_nodes] containing the strings of the leaf_phases
    """
    leaf_embeds = []
    leaf_trees = []
    leaf_ids = []
    # note that we only build a tree for each leaf phase leaving out proliferating vs. not
    rs = random_state
    for leaf in leaf_phases:
        mask = np.array(df_tree[leaf])
        sub_data = data[mask]
        sub_labels = labels[mask]
        if norm_per_subtree:
            d = np.array(sub_labels.sum(axis=0)).flatten()
            # Fix divide by zero errors
            d = np.clip(d, a_min=1e-8, a_max=None)
            sub_labels = sub_labels.tocoo()
            sub_labels.data = sub_labels.data / (d[sub_labels.col])
            sub_labels = sub_labels.tocsr()
        embeds = []
        mts = []
        for i in range(n_trees):
            mt = MetricTree(tree_type=tree_type, random_state=rs, **kwargs)
            counts, edge_weights = mt.fit_transform(
                X=sub_data,
                y=sub_labels,
            )
            embeds.extend(l1_embeddings(counts, edge_weights).T)
            mts.append(mt)
        embeds = np.array(embeds).T
        leaf_embeds.append(embeds)
        leaf_trees.append(mts)
        leaf_ids.append([leaf] * embeds.shape[1])
        rs += 1
    leaf_embeds = np.concatenate(leaf_embeds, axis=1)
    leaf_ids = np.concatenate(leaf_ids)
    return leaf_embeds, leaf_trees, leaf_ids


def tree_runner(data, labels, tree_type, n_trees, random_state=42, **kwargs):
    """Creates tree embeddings for each sample based on tree parameters.

    This ignores known cell state structure and simply builds a tree over the entire dataset.

    Parameters:

        data: [# cells x # features] data matrix
        labels: [# cells x # distributions] (potentially sparse) describing membership of cells to distributions
        tree_type: type of tree to build over the features
        n_trees: how many trees to build
        norm_per_subtree: whether to treat each subtree as a separate distribution,
                          this essentially weights each subtree equally, rather than weighting
                          based on how many cells are in each subtree (default)

    Returns:
        leaf_embeds: [# distributions x (n_trees x n_nodes)] embeddings one per distribution where L1 distrance
                     between embeddings represents tree EMD
        leaf_trees: Tree objects for each tree
    """
    embeds = []
    mts = []
    for i in range(n_trees):
        mt = MetricTree(tree_type=tree_type, random_state=random_state + i, **kwargs)
        counts, edge_weights = mt.fit_transform(
            X=data,
            y=labels,
        )
        embeds.extend(l1_embeddings(counts, edge_weights).T)
        mts.append(mt)
    embeds = np.array(embeds).T
    return embeds, mt
