import requests
import Bio.PDB
from Bio.PDB import PDBIO

pdb_under_600AA = []

# Read the pdb_id.tsv file into a DataFrame
# Remove olignoproteins, and those longer than 600 amino acids
with open('pdb_id.tsv', 'r' ) as f:
    df = f.readlines()
    for pdb in df:
        pdb = pdb.replace('\n','')

        pdbl = Bio.PDB.PDBList()
        pdbl.retrieve_pdb_file(pdb, pdir = "./acahe", )

        parser = Bio.PDB.MMCIFParser()
        structure = parser.get_structure(pdb,"./acahe/" + pdb + '.cif')
          
        model  = next(structure.get_models())

        if len(list(model.get_chains())) > 1:
            print('olignoprotein removed ' + "!" * 10)
            continue
            
        chain_A = next(model.get_chains())   
        length = len(list(chain_A.get_residues()))
        if length < 600:
            # 创建一个 PDBIO 对象，用于保存 pdb 文件
            io = PDBIO()
            # 设置是否保留原子序号，这里设为 False，让其自动生成
            io.set_structure(structure)
            # 将structure保存为一条base64编码的字符串在pdb编号后面
            print(pdb + '\t' + io._get_atom_line())
            # pdb = pdb + '\t' + io._get_atom_line() + '\n'
            # pdb_under_600AA.append(pdb.replace('\n',''))
        else:
            print(length + 'longer than 600 amino acids removed ' + "!" * 10)

# Save the pdb_id.tsv file into a DataFrame
with open('pdb_id_under_600AA.tsv', 'w' ) as f:
    for pdb in pdb_under_600AA:
        f.write(pdb + '\n')


    

    
