import pandas as pd
import sys
from Bio import SeqIO
import json

def create_export_file(sequence_array, index_array, output_file):

	dataFrame = pd.DataFrame()
	dataFrame['id_sequence_by_fasta'] = index_array
	dataFrame['id_sequence_by_algorithm'] = [i+1 for i in range(len(sequence_array))]
	dataFrame['sequence'] = sequence_array

	dataFrame.to_csv(output_file, index=False)

def evaluate_sequence(sequence):

	response=0

	for element in sequence:
		if element not in ["A","R","N","D","C","Q","E","G","H","I","L","K","M","F","P","S","T","W","Y","V"]:
			response=1
			break

	return response

#input parameters
fasta_seq = sys.argv[1]
path_output = sys.argv[2]

#arrays to save sequences to process element
sequences_array_in = []
id_sequences_array_in = []

sequences_array_not_in = []
id_sequences_array_not_in = []

response=0
try:
	#read fasta file
	for record in SeqIO.parse(fasta_seq, "fasta"):
		sequence = ""
		for residue in record.seq:
			sequence+=residue

		#check sequence based on simple criterion
		if evaluate_sequence(sequence) == 0:		
			sequences_array_in.append(sequence)
			id_sequences_array_in.append(record.id)

		else:
			sequences_array_not_in.append(sequence)
			id_sequences_array_not_in.append(record.id)		
except:
	response=1
	pass

if response == 0:

	#process summary
	dict_summary = {"response_preprocess":"OK", "Total sequences": len(sequences_array_in)+len(sequences_array_not_in), "Sequences to process":len(sequences_array_in), "Ignored sequences":len(sequences_array_not_in)}

	#create export files
	create_export_file(sequences_array_in, id_sequences_array_in, path_output+"input_sequences_to_process.csv")
	create_export_file(sequences_array_not_in, id_sequences_array_not_in, path_output+"ignored_sequences.csv")

else:
	dict_summary={"response_preprocess":"ERROR"}
	
#export JSON summary
with open(path_output+"summary_preprocess.json", 'w') as fp:
    json.dump(dict_summary, fp)

