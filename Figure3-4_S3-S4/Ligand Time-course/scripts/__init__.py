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
colours_cell_type = {
    "PCK": "#7CC06F",
    "LRIG1": "#000099",
    "CLU": "#BA261A",
    "FABP2": "#2B6419",
}


colours_media = {
    "Ctrl": "#E6DCCB",
    "EGF": "#DBC636",
    "EREG": "#FEAA11",
    "WNT3A": "#6E925E",
    "TGFb1": "#932192",
}

colours_time_point = {
    "15min": "#f8cd82",
    "30min": "#ff9248",
    "60min": "#ff7249",
    "120min": "#ff5349",
}

colours = colours_cell_type | colours_time_point | colours_media
