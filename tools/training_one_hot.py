import pandas as pd

class one_hot_encoding(object):
	
	def __init__(self, data_sequences):
		self.data_sequences = data_sequences

		self.residues = ["A","R","N","D","C","Q","E","G","H","I","L","K","M","F","P","S","T","W","Y","V"]
		self.residues.sort()
		self.dict_residues = {}
		for i in range(len(self.residues)):
			self.dict_residues.update({self.residues[i]:i})

	def create_vector(self, residue):
		
		vector_encoding = [0 for x in range(20)]
		vector_encoding[self.dict_residues[residue]] = 1

		return vector_encoding

	def apply_encoding(self):

		matrix_encoding = []
		length_data = []

		for sequence in self.data_sequences['sequence']:
			try:
			
				sequence = sequence.replace(" ", "")
				sequence = sequence.replace("O", "")
				row_encoding = []

				for residue in sequence:
					residue_encoding = self.create_vector(residue)
					for data in residue_encoding:
						row_encoding.append(data)

				length_data.append(len(row_encoding))
				matrix_encoding.append(row_encoding)
			except:
				pass

		#create zero padding
		for i in range(len(matrix_encoding)):

			for j in range(len(matrix_encoding[i]),max(length_data)):
				matrix_encoding[i].append(0)

		header = ["P_"+str(i) for i in range(len(matrix_encoding[0]))]

		self.dataset_export = pd.DataFrame(matrix_encoding, columns=header)