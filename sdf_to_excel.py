#!/usr/bin/env python

### Script originally designed for data analysis of virtual screening results
### Purpose is to format an Excel file for logging observations of virtual screen
###     hits and deciding whether to purchase individual compounds

# Usage: python3 sdf_to_excel.py input_file.sdf output_file.xlsx

import sys
import pandas as pd
from rdkit.Chem import PandasTools as pt
pt.RenderImagesInAllDataFrames()

### Input is an SDF file containing multiple/many compounds

df = pt.LoadSDF(sys.argv[1])

### Properties contain the 1) name and 2) structure of the molecule
### Slice the DataFrame already loaded in and output to a new one
### Create empty columns for grade (i.e. ranking) and a decision to purchase

properties = ['ID','ROMol']
df2 = pd.DataFrame(df[properties])
df2['Grade'] = ''
df2['Purchase?'] = ''

### Outputs sliced DataFrame to Excel-readable format
### Requires installation of openpyxl and xlsxwriter

pt.SaveXlsxFromFrame(df2, sys.argv[2], molCol='ROMol')
