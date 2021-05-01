import pandas as pd
from scipy.fft import fft
import numpy as np

class property_encoding(object):
	
	def __init__(self, dataset_sequences, type_property, path_inputs_encodings):
		
		self.dataset_sequences = dataset_sequences
		self.type_property = type_property
		self.list_clusters = ["alpha-structure_group", "betha-structure_group", "energetic_group", "hydropathy_group", "hydrophobicity_group", "index_group", "secondary_structure_properties_group", "volume_group"]
		self.path_inputs_encodings = path_inputs_encodings

	def encoding_sequence(self, sequence, value_property):

		#order in database
		array_residues = ['A', 'R', 'N', 'D', 'C', 'E', 'Q', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']
		sequence_encoding = []

		for residue in sequence:		
			encoding_value =-1
			index=-1
			for i in range(len(array_residues)):
				if array_residues[i] == residue:
					index=i
					break

			sequence_encoding.append(value_property[index])

		return sequence_encoding

	def apply_encoding(self):

		cluster = self.list_clusters[self.type_property]

		dataset_cluster = pd.read_csv(self.path_inputs_encodings+cluster+"/data_component.csv")

		matrix_sequence_encoding = []
		length_data = []

		for i in range(len(self.dataset_sequences)):
			try:
				sequence = self.dataset_sequences['sequence'][i]		
				sequence_encoding = self.encoding_sequence(sequence, dataset_cluster['component_1'])		
				matrix_sequence_encoding.append(sequence_encoding)
				length_data.append(len(sequence_encoding))
			except:
				pass

		#make zero padding		
		for i in range(len(matrix_sequence_encoding)):

			for j in range(len(matrix_sequence_encoding[i]),max(length_data)):
				matrix_sequence_encoding[i].append(0)

		#to matrix apply digital signal processing
		matrix_signal = []
		number_sample = len(matrix_sequence_encoding[0])

		for i in range(len(matrix_sequence_encoding)):

			T = 1.0/float(number_sample)
			x = np.linspace(0.0, number_sample*T, number_sample)
			yf = fft(matrix_sequence_encoding[i])
			xf = np.linspace(0.0, 1.0/(2.0*T), number_sample//2)
			matrix_signal.append(np.abs(yf[0:number_sample//2]))
		
		header = ["P_"+str(i) for i in range(len(matrix_signal[0]))]
		self.dataset_export = pd.DataFrame(matrix_signal, columns=header)