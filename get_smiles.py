import sys
from rdkit.Chem import PandasTools

### Purpose is to read an SDF file and output a file containing the
###     SMILES code and name of each molecule
# Usage: python3 get_smiles.py input_file.sdf output_file.csv

sdf = sys.argv[1]
outfile = open(sys.argv[2], "w")
df = PandasTools.LoadSDF(sdf, smilesName='SMILES')
for idx,row in df.iterrows():
    print(row['SMILES'], row['ID'])
    print(row['SMILES'], row['ID'], file=outfile)
