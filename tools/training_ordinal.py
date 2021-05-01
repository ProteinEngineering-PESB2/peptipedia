import pandas as pd

class ordinal_encoding(object):
	
	def __init__(self, dataset_sequences):
		self.dataset_sequences = dataset_sequences

		self.residues = ["A","R","N","D","C","Q","E","G","H","I","L","K","M","F","P","S","T","W","Y","V"]
		self.residues.sort()
		self.dict_residues = {}
		for i in range(len(self.residues)):
			self.dict_residues.update({self.residues[i]:i})

	def apply_encoding(self):

		length_data = []
		matrix_encoding = []
		
		for sequence in self.dataset_sequences['sequence']:
			try:
				sequence = sequence.replace(" ", "")
				sequence = sequence.replace("O", "")
				row_encoding = []

				for residue in sequence:
					residue_encoding = self.dict_residues[residue]
					row_encoding.append(residue_encoding)

				length_data.append(len(row_encoding))
				matrix_encoding.append(row_encoding)
			except:
				index.append(sequence)
				pass					

		#create zero padding
		for i in range(len(matrix_encoding)):

			for j in range(len(matrix_encoding[i]),max(length_data)):
				matrix_encoding[i].append(0)

		header = ["P_"+str(i) for i in range(len(matrix_encoding[0]))]

		self.dataset_export = pd.DataFrame(matrix_encoding, columns=header)