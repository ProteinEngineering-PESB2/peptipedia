import torch
from tape import ProteinBertModel, TAPETokenizer
import numpy as np
import sys
import pandas as pd
import os

dataset = pd.read_csv(sys.argv[1])
path_output = sys.argv[2]

#create dir process to encoding data
os.mkdir(path_output+"embedding")

path_output = path_output+"embedding/"

model = ProteinBertModel.from_pretrained('bert-base')
tokenizer = TAPETokenizer(vocab='iupac')  # iupac is the vocab for TAPE models, use unirep for the UniRep model

matrix_encoding = []
for i in range(len(dataset)):

	token_ids = torch.tensor([tokenizer.encode(dataset['sequence'][i])])
	output = model(token_ids)
	sequence_output = output[0]
	
	matrix_data = []

	for element in sequence_output[0].cpu().detach().numpy():
		matrix_data.append(element)	

	encoding_avg = [dataset['id_sequence_by_algorithm'][i]]

	for k in range(len(matrix_data[0])):
		array_value = []
		for j in range(len(matrix_data)):
			array_value.append(matrix_data[j][k])

		encoding_avg.append(np.mean(array_value))	
	matrix_encoding.append(encoding_avg)
	

header = ["P_"+str(i+1) for i in range(len(matrix_encoding[0])-1)]
header.insert(0, "id_sequence_by_algorithm")

dataset_export = pd.DataFrame(matrix_encoding, columns=header)
dataset_export.to_csv(path_output+"dataset_encoding_by_tape.csv", index=False)

