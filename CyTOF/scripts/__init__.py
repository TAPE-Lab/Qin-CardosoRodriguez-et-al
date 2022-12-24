from calendar import c
from tokenize import group
from matplotlib.pyplot import bar
import pandas as pd
import os

sample_folder = "/Users/xiaoqin/Dropbox/UCL/Experiments/CyTOF/Signal Perturbation/Signal Perturbation - Analysis"
os.chdir(sample_folder)

# Non-marker
non_marker = pd.read_csv("./ref/non_marker.txt", header=None)[0].tolist()

# Epithelial cell-type markers
# cell_type_markers = pd.read_csv("./ref/epi_cell_type_markers.csv", header=None)[
#     0
# ].tolist()

# Colour palette
colours_genotype = {
    "WT": "#87A076",
    "A": "#576441",
    "K": "#9B7F3C",
    "AK": "#6C8DC6",
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

# colours_inhibitor = {
#     "Ctrl": "#E6DCCB",
#     "CA3": "#AE9576",
#     "CHIR99021": "#93ADB4",
#     "Dasatinib": "#2F76C5",
#     "ICG001": "#2EB0B2",
#     "GDC0941": "#0055C5",
#     "PF573228": "#70A2C5",
#     "SIS3": "#797979",
#     "Trametinib": "#D76144",
# }

colours = colours_genotype | colours_ligand | colours_inhibitor
