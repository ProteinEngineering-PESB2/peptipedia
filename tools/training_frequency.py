import pandas as pd

class frequency_encoding(object):
	
	def __init__(self, dataset_sequences):
		
		self.dataset_sequences = dataset_sequences

		self.residues = ["A","R","N","D","C","Q","E","G","H","I","L","K","M","F","P","S","T","W","Y","V"]
		self.residues.sort()
		self.dict_residues = {}
		for i in range(len(self.residues)):
			self.dict_residues.update({self.residues[i]:i})

	def get_frequency(self, sequence, array_data):

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

		row_encoding_data = [array_summary[self.dict_residues[residue]] for residue in sequence]	
		return row_encoding_data

	def apply_encoding(self):

		length_data = []
		matrix_encoding = []

		for sequence in self.dataset_sequences['sequence']:
			try:
				sequence = sequence.replace(" ", "")
				sequence = sequence.replace("O", "")
				row_encoding = self.get_frequency(sequence, self.residues)
				
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
