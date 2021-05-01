import pandas as pd
import sys

#get frequency of residues
def get_frequency(sequence, array_data, dict_residues):

	array_summary = [0 for x in range(20)]
	index=0

	for residue in array_data:
		cont=0
		for residue_data in sequence:
			if residue == residue_data:
				cont+=1
		frequency = float(cont)/float(len(sequence))
		array_summary[index] = frequency
		index+=1

	row_encoding_data = [array_summary[dict_residues[residue]] for residue in sequence]	
	return row_encoding_data

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
	row_encoding = get_frequency(sequence, residues, dict_residues)
	
	length_data.append(len(row_encoding))
	matrix_encoding.append(row_encoding)

#create zero padding
for i in range(len(matrix_encoding)):

	for j in range(len(matrix_encoding[i]),max(length_data)):
		matrix_encoding[i].append(0)

header = ["P_"+str(i) for i in range(len(matrix_encoding[0]))]
dataset_export = pd.DataFrame(matrix_encoding, columns=header)
dataset_export['id_sequence_by_algorithm'] = dataset['id_sequence_by_algorithm']

dataset_export.to_csv(path_output+"encoding_frequency.csv", index=False)
