import pandas as pd

# curl https://huggingface.co/datasets/jglaser/pdb_protein_ligand_complexes/resolve/main/data/pdb_test.p
# curl https://huggingface.co/datasets/jglaser/pdb_protein_ligand_complexes/resolve/main/data/pdb_train.p

test = pd.read_pickle('pdb_test.p')

pdb_id = test.iloc[:,0]

print(pdb_id)

# save them into a tsv file:
pdb_id.to_csv('pdb_id.tsv', sep='\t', index=False, header=False)

