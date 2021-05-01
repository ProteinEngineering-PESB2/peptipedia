import torch
from tape import ProteinBertModel, TAPETokenizer
import numpy as np
import sys
import pandas as pd
import os

class encoding_tape(object):
	
	def __init__(self, dataset_sequences):
		
		self.dataset_sequences = dataset_sequences
		self.model = ProteinBertModel.from_pretrained('bert-base')
		self.tokenizer = TAPETokenizer(vocab='iupac')  # iupac is the vocab for TAPE models, use unirep for the UniRep model

	def apply_encoding(self):

		matrix_encoding = []
		for i in range(len(self.dataset_sequences)):

			try:
				token_ids = torch.tensor([self.tokenizer.encode(self.dataset_sequences['sequence'][i])])
				output = self.model(token_ids)
				sequence_output = output[0]
				
				matrix_data = []

				for element in sequence_output[0].cpu().detach().numpy():
					matrix_data.append(element)	

				encoding_avg = []

				for k in range(len(matrix_data[0])):
					array_value = []
					for j in range(len(matrix_data)):
						array_value.append(matrix_data[j][k])

					encoding_avg.append(np.mean(array_value))	
				matrix_encoding.append(encoding_avg)
			except:
				pass

		header = ["P_"+str(i+1) for i in range(len(matrix_encoding[0])-1)]
		self.dataset_encoding = pd.DataFrame(matrix_encoding, columns=header)



		