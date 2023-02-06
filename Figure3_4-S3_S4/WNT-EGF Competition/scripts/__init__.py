from calendar import c
from tokenize import group
from matplotlib.pyplot import bar
import pandas as pd
import os

sample_folder = "/Users/xiaoqin/Dropbox/TAPE LAB/Manuscripts/Qin & Cardoso Rodriguez et al/SupplementaryMaterials/Qin-CardosoRodriguez-et-al_analysis/"
os.chdir(sample_folder)

# Non-marker
non_marker = pd.read_csv("./Data/non_marker.txt", header=None)[0].tolist()

# Epithelial cell-type markers
cell_type_markers = pd.read_csv("./Data/epi_cell_type_markers.csv", header=None)[
    0
].tolist()

# CellChat Follow-up
colours_genotype = {
    "WT": "#87A076",
    "A": "#576441",
    "K": "#9B7F3C",
    "KP": "#8B6240",
    "AK": "#6C8DC6",
    "AKP": "#436DB8",
    "Fib": "red",
}

colours_media = {
    "Ctrl": "#E6DCCB",
    "WNT3A": "#6E925E",
    "EGF": "#DBC636",
    "WNT5A": "#00663A",
    "SEMA3A": "#008996",
    "TGFB2": "#931651",
    "TGFB1": "#932192",
    "IGF1": "#7A80FF",
    "NRG1": "#BD911E",
    "EREG": "#FEAA11",
    "OPN": "#005392",
    # WENR Permutation
    "W": "#6E925E",
    "E": "#DBC636",
    "N": "#BAA18B",
    "R": "#71B3E7",
    "ENR": "#FDC950",
    "WNR": "#41512E",
    "WER": "#348794",
    "WEN": "#207176",
    "WENR": "#E48C2AFF",
}

colours_format = {"monoculture": "#079601", "co-culture": "#FF2600"}

colours_signal_cluster = {
    # Control
    "WT_Ctrl": "#E6DCCB",
    # WNT ON - extrinsic EGF
    "WT_W": "red",
    "WT_WNR": "red",
    # WNT ON + intrinsic beta-cat (A)
    "A_W": "red",
    "A_WNR": "red",
    "A_WER": "red",
    "A_WEN": "red",
    "A_WENR": "red",
    # Equilibrium: WT - WNT3A
    "WT_E": "#9F3F2D",
    "WT_N": "#9F3F2D",
    "WT_R": "#9F3F2D",
    "WT_ENR": "#9F3F2D",
    # Equilibrum: WT + W + E
    "WT_WEN": "#9F3F2D",
    "WT_WER": "#9F3F2D",
    "WT_WENR": "#9F3F2D",
    # Equilibrium: shAPC - WNT3A
    "A_Ctrl": "#9F3F2D",
    "A_E": "#9F3F2D",
    "A_N": "#9F3F2D",
    "A_R": "#9F3F2D",
    "A_ENR": "#9F3F2D",
    # KRAS ON, WNT OFF, Beta-Cat OFF
    "K_Ctrl": "#426EB8",
    "K_E": "#426EB8",
    "K_N": "#426EB8",
    "KP_Ctrl": "#426EB8",
    "KP_E": "#426EB8",
    "KP_N": "#426EB8",
    # KRAS ON, WNT ON, Beta-Cat OFF
    "K_W": "#464865",
    "K_WEN": "#464865",
    "KP_W": "#464865",
    "KP_WEN": "#464865",
    ###
    # KRAS + RS1 / shAPC (Cancer)
    # Intrinsic >> Extrinsic
    ###
    "K_R": "blue",
    "K_ENR": "blue",
    "K_WNR": "blue",
    "K_WER": "blue",
    "K_WENR": "blue",
    "KP_R": "blue",
    "KP_ENR": "blue",
    "KP_WNR": "blue",
    "KP_WER": "blue",
    "KP_WENR": "blue",
    "AK_Ctrl": "blue",
    "AK_W": "blue",
    "AK_E": "blue",
    "AK_N": "blue",
    "AK_R": "blue",
    "AK_ENR": "blue",
    "AK_WNR": "blue",
    "AK_WER": "blue",
    "AK_WEN": "blue",
    "AK_WENR": "blue",
    "AKP_Ctrl": "blue",
    "AKP_W": "blue",
    "AKP_E": "blue",
    "AKP_N": "blue",
    "AKP_R": "blue",
    "AKP_ENR": "blue",
    "AKP_WNR": "blue",
    "AKP_WER": "blue",
    "AKP_WEN": "blue",
    "AKP_WENR": "blue",
    # ---
    # co-culture control
    # ---
    "WT-Fib_Ctrl": "#E6BFA3",
    # co-culture -E
    "WT-Fib_W": "pink",
    "WT-Fib_N": "pink",
    "WT-Fib_R": "pink",
    "WT-Fib_WNR": "pink",
    # co-culture + E
    "WT-Fib_ENR": "salmon",
    "WT-Fib_E": "salmon",
    "WT-Fib_WER": "salmon",
    "WT-Fib_WEN": "salmon",
    "WT-Fib_WENR": "salmon",
}

# Signal Perturbation
colours_ligand = {
    "Ctrl": "#E6DCCB",
    "WNT3A": "#6E925E",
    "EREG": "#FEAA11",
    "TGFb1": "#932192",
}

colours_inhibitor = {
    "Ctrl": "#E6DCCB",
    "CA3": "#D76144",
    "CHIR99021": "#93ADB4",
    "ICG001": "#2EB0B2",
    "Dasatinib": "#7A80FF",
    "Trametinib": "#7B00FF",
    "GDC0941": "#CD0578",
    "PF573228": "#990090",
    "SIS3": "#AE9576",
}

# WNT-EGF Competition
colours_EGF_WNT_ratio = {  # RdYlGn
    "--": "#E6DCCB",  # Control
    "-": "#DBC636",  # EGF only
    "0.0": "#6E925E",  # WNT only
    "0.1": "#1a9850",
    "0.25": "#66bd63",
    "0.4": "#a6d96a",
    "0.5": "#d9ef8b",
    "1.0": "#ffffbf",
    "2.5": "#fee08b",
    "5.0": "#fdae61",
}

colours_culture = {
    "WNT-0_EGF-0": "#E6DCCB",
    "WNT-10_EGF-0": "#ACE895",
    "WNT-20_EGF-0": "#A0D78B",
    "WNT-50_EGF-0": "#84B273",
    "WNT-100_EGF-0": "#6E925E",
    "EGF-10_WNT-0": "#FFF180",
    "EGF-25_WNT-0": "#E7DA79",
    "EGF-40_WNT-0": "#CFCD58",
    "EGF-50_WNT-0": "#DBC636",
}

colours = (
    colours_genotype
    | colours_media
    | colours_ligand
    | colours_inhibitor
    | colours_EGF_WNT_ratio
    | colours_culture
    | colours_signal_cluster
    | colours_format
)
