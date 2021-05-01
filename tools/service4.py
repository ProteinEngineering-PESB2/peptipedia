import pandas as pd
import sys
from Bio import SeqIO
import json
import numpy as np
def make_counts(sequence):

	clasical_residues = ["A","R","N","D","C","Q","E","G","H","I","L","K","M","F","P","S","T","W","Y","V"]
	
	array_account = []
	for residue in clasical_residues:
		count=0
		for element in sequence:
			if element==residue:
				count+=1

		array_account.append(count)

	return array_account

def exec(peptide, time, option):
	file = open("../src/public/jobs/service4/service4.fasta", "w") 
	file.write(peptide)
	file.close()
	type_response = int(option)#type output (1 -> % 2 -> count)

	matrix_response = []
	fasta = SeqIO.parse("../src/public/jobs/service4/service4.fasta", "fasta")
	if(any(fasta) == False): #False when `fasta` is empty
		return "error"
	for record in SeqIO.parse("../src/public/jobs/service4/service4.fasta", "fasta"):
		id_sequence = record.id

		sequence = ""

		for residue in record.seq:
			sequence+=residue

		#get representation
		length_data = len(sequence)
		counts_data = make_counts(sequence)

		if type_response==1:
			counts_data = [value*100/length_data for value in counts_data]

		counts_data.insert(0, id_sequence)
		matrix_response.append(counts_data)
		for j in range(len(matrix_response)):
			for i in range(len(matrix_response[j])):
				if (isinstance(matrix_response[j][i], str) == False):
					matrix_response[j][i] = float("%.4f" % matrix_response[j][i])
			
	data_export = pd.DataFrame(matrix_response, columns= ["id_sequence", "A","R","N","D","C","Q","E","G","H","I","L","K","M","F","P","S","T","W","Y","V"])

	#get mean of frequency for all sequences in dataset
	mean_data = [np.mean(data_export[key]) for key in ["A","R","N","D","C","Q","E","G","H","I","L","K","M","F","P","S","T","W","Y","V"]]
	std_data = [np.std(data_export[key]) for key in ["A","R","N","D","C","Q","E","G","H","I","L","K","M","F","P","S","T","W","Y","V"]]

	#create a JSON with information

	error_dict = {"type": 'data', "array": std_data, "visible": "true"}

	data_json = [{"y":mean_data, "x": ["A","R","N","D","C","Q","E","G","H","I","L","K","M","F","P","S","T","W","Y","V"], "type":"bar", "error_y":error_dict}]

	result = data_export.to_json(orient="split")
	parsed = json.loads(result)
	return(json.dumps(parsed, indent=4), data_json)