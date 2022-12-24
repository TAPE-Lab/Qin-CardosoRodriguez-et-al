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

# Colour palette
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

colours = colours_genotype | colours_media | colours_ligand | colours_inhibitor
