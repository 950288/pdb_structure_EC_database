import json
import requests

def get():

    # read from train_sequences.fasta get the list of entries
    file = open("./Train/train_sequences.fasta", "r")

    entries = []

    # get the list of entries
    for line in file:
        if line.startswith('>'):
            entries.append(line[1:line.find(' ')])

    entries_len = len(entries)

    # get the length of the pdb_list.txt
    pdb_list_len = 0

    with open("pdb_list.txt", "r") as file:
        pdb_list_len = len(file.readlines())

    # append to the pdb_list.txt
    with open("pdb_list.txt", "a") as file:

        print("pdb_list_len: " + str(pdb_list_len))

        # for each entry, get the PDB
        for index, Entry in enumerate(entries[pdb_list_len:]):

            print("" + str(index + 1 + pdb_list_len) + "/" + str(entries_len) + " entry: " + Entry ,end='')

            URL = 'https://rest.uniprot.org/uniprotkb/search?query=accession:' + Entry + '&fields=accession,structure_3d'

            X = requests.get(URL)

            data = json.loads(X.text)

            try:
                structure_id = data["results"][0]["uniProtKBCrossReferences"][0]["id"]
            except:
                # retrieve from AlphaFold

                URL = 'https://alphafold.ebi.ac.uk/api/uniprot/summary/' + Entry + '.json'

                X = requests.get(URL)

                data = json.loads(X.text)

                try:
                    structure_id = data["structures"][0]["summary"]["model_identifier"]
                
                except:
                    structure_id = "UnFound"

            print("\tstructure_id: " + structure_id)

            # write and save
            file.write(Entry + "\t" + structure_id + "\n")
            file.flush()

    return 0

if __name__ == '__main__':

    # if connection is lost, try again in 5 minutes
    while True:
        try:
            if get() == 0:
                break
        except:
            import time
            for i in range(300):
                print("\rretry in " + str(300 - i) + " seconds", end='')
                time.sleep(1)
            print("\rretrying..." + " " * 10)            




