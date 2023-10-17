# Cheminformatics-Virtual-Screen-Analysis
Tools utilizable for analyzing virtual screen results after k-means clustering

Cheminformatics Virtual Screen Analysis
---------------------------------------

These scripts are designed to facilitate the process of analyzing results
from a virtual screen. They run in conjunction with a "kmeans.py" script
written by Pat Walters (github repository here:
https://github.com/PatWalters/kmeans/tree/master).

Generally speaking, these are designed to make k-means clustering
(and the analysis of the clustering) easy and straightforward.

1) get_smiles.py
	- This script is simply designed to output a SMILES file, containing
	  the SMILES code and name of all ligands in an SDF file, which,
	  itself, contains all hits from a virtual screen
	- The output .smi file is designed to be used as input for Walters'
	  kmeans.py script.

2) sdf_to_excel.py
	- This script is designed to take an input SDF file containing hits
	  from a virtual screen and output them to an Excel file, which,
	  itself, contains the name and structure of the molecule, as well
	  as empty columns for ranking ("grading") and deciding to purchase
	  each compound.

3) cluster_centers.ipynb
	- This Jupyter notebook is designed to take output from Walters'
	  kmeans.py clustering, filter the results for cluster centers,
	  and output them to a new SDF.
	- Requires SDF containing all hits as additional input.

4) cluster_tophits.ipynb
	- This jupyter notebook operates similarly to clustser_centers.ipynb,
	  but here it is designed to select for the top-scoring hits from
	  each cluster.
	- Still outputs results to a new SDF.
	- Requires SDF containing all hits as additional input.

#####################
### Installations ###
#####################

These scripts mostly depend on use of RDKit, which can be downloaded via:

	conda install -c conda-forge rdkit

Visualizing results in Jupyter also requires mols2grid:

	pip3 install mols2grid

As long as you have pandas, everything else should go smoothly.
