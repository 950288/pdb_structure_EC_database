import requests
import Bio.PDB

pdb_under_600AA = []

# Read the pdb_id.tsv file into a DataFrame
# remove olignoproteins, and those longer than 600 amino acids
with open('pdb_id.tsv', 'r' ) as f:
    df = f.readlines()
    for pdb in df:
        # Get the length of the protein
        pdb = pdb.replace('\n','')
        print(pdb.replace('\n',''))
        url = 'https://files.rcsb.org/download/' + pdb + '.pdb'
        print(url)
        response = requests.get(url)
        if response.status_code == 200:

            lines = response.text.split('\n')

            parser = Bio.PDB.PDBParser()
            # structure = parser.get_structure(response.text, pdb + '.pdb')
            parser.structure_builder.init_structure(lines)
            parser._parse(lines)
            structure = parser.structure_builder.get_structure()

            print(structure)


            model  = structure.get_models()

            print(model.get_chains())
            if len(model.get_chains()) > 1:
                print('olignoprotein removed !')
                continue
                
        #     print(structure.get_models()[0].get_chains())
        #     # print(int(protein[len(protein)-1][23:31]))
        #     # if int(protein[len(protein)-1][23:31]) < 600:
        #     #     pdb_under_600AA.append(pdb.replace('\n',''))
        #     # else:
        #     #     print(str(int(protein[len(protein)-1][23:31])) + 'longer than 600 amino acids removed !')

        # else :
        #     print('Error: ', response.status_code)
        break

    

    
