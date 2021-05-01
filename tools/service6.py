import pandas as pd
import sys
import json
import training_digital_signal
import training_frequency
import training_one_hot
import training_ordinal
import training_properties
import training_tape
import launcher_classification_models
import launcher_prediction_models
import numpy as np
from sklearn.preprocessing import MinMaxScaler

from Bio import SeqIO

#input data from command line
def exec(time):
	#input data from command line
	try:
		dataset = "../src/public/jobs/service6/"+time+"/dataset.fasta"		
		response_data = pd.read_csv("../src/public/jobs/service6/"+time+"/response.csv")
		config_file_parameters = "../src/public/jobs/service6/"+time+"/dict_response_input.json"
		path_output = "../src/public/jobs/service6/"+time+"/"
	except:
		return "error"
	
	
	total_sequences = []
	mean_sequences = []
	try:
		for record in SeqIO.parse(dataset, "fasta"):
			total_sequences.append(record.seq)
			mean_sequences.append(len(record.seq))				
	except:
		return "error"

	dict_response_service = {}

	path_encodings_properties = "encoding_AAIndex/"

	#process fasta file
	data_sequences = []
	print("Process data")

	try:
		#read fasta file
		for record in SeqIO.parse(dataset, "fasta"):
			sequence = ""
			for residue in record.seq:
				sequence+=residue
			data_sequences.append(sequence)

		data_sequences = pd.DataFrame(data_sequences, columns=["sequence"])
		dict_response_service.update({"process_fasta":"OK"})
	except:
		dict_response_service.update({"process_fasta":"ERROR"})
		return "error"

	print("Encoding sequences")

	with open(config_file_parameters) as json_file:

		data_encodings = ""

		data = json.load(json_file)

		type_encoding = int(data["type_encoding"])
		type_property = int(data["type_property"])
		type_response = int(data["type_response"])
		algorithm = int(data["algorithm"])

		#encoding dataset by type encoding
		if type_encoding == 1:#one hot encoding

			one_hot_encoding = training_one_hot.one_hot_encoding(data_sequences)
			one_hot_encoding.apply_encoding()
			data_encodings = one_hot_encoding.dataset_export

		elif type_encoding == 2:#ordinal encoding

			ordinal_encoding = training_ordinal.ordinal_encoding(data_sequences)
			ordinal_encoding.apply_encoding()
			data_encodings = ordinal_encoding.dataset_export

		elif type_encoding == 3:#frequency of residues

			frequency_encoding = training_frequency.frequency_encoding(data_sequences)
			frequency_encoding.apply_encoding()
			data_encodings = frequency_encoding.dataset_export

		elif type_encoding == 4:#physicochemical properties

			property_encoding = training_properties.property_encoding(data_sequences, type_property, path_encodings_properties)
			property_encoding.apply_encoding()
			data_encodings = property_encoding.dataset_export

		elif type_encoding == 5:#digital signal

			digital_encoding = training_digital_signal.property_encoding(data_sequences, type_property, path_encodings_properties)
			digital_encoding.apply_encoding()
			data_encodings = digital_encoding.dataset_export

		else:#tape

			tape_encoding = training_tape.encoding_tape(data_sequences)
			tape_encoding.apply_encoding()
			data_encodings = tape_encoding.dataset_encoding()

		if len(data_encodings) == len(data_sequences):
			dict_response_service.update({"encoding_process":"OK"})	
		else:
			dict_response_service.update({"encoding_process":"ERROR"})
			return "error"


		if dict_response_service["encoding_process"]!= "ERROR":

			#scale dataset
			scaler = MinMaxScaler()
			scaler.fit(data_encodings)
			dataset_scaler = scaler.transform(data_encodings)

			if type_response == 1:
				print("Process Classification")
				launcher_class = launcher_classification_models.launcher_classification(data_encodings, response_data['response'], algorithm, path_output)
				launcher_class.apply_algorithm()
				return ({"process": "ok", "total_sequences": len(set(total_sequences)),"mean_sequences": "%.4f" % np.mean(mean_sequences), "type_encoding": type_encoding, "type_property": type_property, "type_response": type_response, "algorithm": algorithm})
			else:
				print("Process Regression")
				launcher_class = launcher_prediction_models.launcher_prediction(data_encodings, response_data['response'], algorithm, path_output)
				launcher_class.apply_algorithm()
				return ({"process": "ok", "total_sequences": len(set(total_sequences)),"mean_sequences": "%.4f" % np.mean(mean_sequences), "type_encoding": type_encoding, "type_property": type_property, "type_response": type_response, "algorithm": algorithm})





