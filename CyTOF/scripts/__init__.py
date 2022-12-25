from calendar import c
from tokenize import group
from matplotlib.pyplot import bar
import pandas as pd
import os

sample_folder = "/Users/xiaoqin/Dropbox/TAPE LAB/Manuscripts/Qin & Cardoso Rodriguez et al/SupplementaryMaterials/Qin-CardosoRodriguez-et-al_analysis/CyTOF"
os.chdir(sample_folder)

# Non-marker
non_marker = pd.read_csv("./ref/non_marker.txt", header=None)[0].tolist()

# Epithelial cell-type markers
cell_type_markers = pd.read_csv("./ref/epi_cell_type_markers.csv", header=None)[
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
)
