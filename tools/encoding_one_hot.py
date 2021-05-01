import pandas as pd
import sys

def create_vector(residue, dict_residues):

	vector_encoding = [0 for x in range(20)]
	vector_encoding[dict_residues[residue]] = 1

	return vector_encoding

dataset = pd.read_csv(sys.argv[1])
path_output = sys.argv[2]

matrix_encoding = []
length_data = []

residues = ["A","R","N","D","C","Q","E","G","H","I","L","K","M","F","P","S","T","W","Y","V"]
residues.sort()
dict_residues = {}
for i in range(len(residues)):
	dict_residues.update({residues[i]:i})

for sequence in dataset['sequence']:
	sequence = sequence.replace(" ", "")
	sequence = sequence.replace("O", "")
	row_encoding = []

	for residue in sequence:
		residue_encoding = create_vector(residue, dict_residues)
		for data in residue_encoding:
			row_encoding.append(data)

	length_data.append(len(row_encoding))
	matrix_encoding.append(row_encoding)

#create zero padding
for i in range(len(matrix_encoding)):

	for j in range(len(matrix_encoding[i]),max(length_data)):
		matrix_encoding[i].append(0)

header = ["P_"+str(i) for i in range(len(matrix_encoding[0]))]

dataset_export = pd.DataFrame(matrix_encoding, columns=header)
dataset_export['id_sequence_by_algorithm'] = dataset['id_sequence_by_algorithm']
dataset_export.to_csv(path_output+"encoding_OneHot.csv", index=False)
