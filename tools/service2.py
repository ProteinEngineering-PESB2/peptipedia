import pandas as pd
import sys
from Bio import SeqIO
import json
from scipy.fft import fft
import numpy as np
from joblib import dump, load
from sklearn.preprocessing import MinMaxScaler
import os

def make_corrections_to_classification(dataset_responses):

	for i in range(len(dataset_responses)):
		if dataset_responses['Allergen'][i] == 1:
			dataset_responses['Immunological-activity'][i] = 1

		if dataset_responses['Anti-Angiogenic'][i] == 1:
			dataset_responses['Anticancer'][i] = 1
			dataset_responses['Therapeutic'][i] = 1

		if dataset_responses['Antibacterial-antibiotic'][i] == 1:
			dataset_responses['Antimicrobial'][i] = 1
			dataset_responses['Therapeutic'][i] = 1

		if dataset_responses['Antibiofilm'][i] == 1:
			dataset_responses['Antibacterial-antibiotic'][i] = 1
			dataset_responses['Antimicrobial'][i] = 1
			dataset_responses['Therapeutic'][i] = 1

		if dataset_responses['Anticancer'][i] == 1:
			dataset_responses['Therapeutic'][i] = 1

		if dataset_responses['Anti-Diabetic'][i] == 1:
			dataset_responses['Metabolic'][i] = 1
			dataset_responses['Therapeutic'][i] = 1

		if dataset_responses['Antifungal'][i] == 1:
			dataset_responses['Antimicrobial'][i] = 1
			dataset_responses['Therapeutic'][i] = 1
		
		if dataset_responses['anti_gram_negative'][i] == 1:
			dataset_responses['Antibacterial-antibiotic'][i] = 1
			dataset_responses['Antimicrobial'][i] = 1
			dataset_responses['Therapeutic'][i] = 1

		if dataset_responses['anti_gram_positive'][i] == 1:
			dataset_responses['Antibacterial-antibiotic'][i] = 1
			dataset_responses['Antimicrobial'][i] = 1
			dataset_responses['Therapeutic'][i] = 1

		if dataset_responses['Anti-HIV'][i] == 1:
			dataset_responses['Antiviral'][i] = 1
			dataset_responses['Antimicrobial'][i] = 1
			dataset_responses['Therapeutic'][i] = 1

		if dataset_responses['Antihypertensive'][i] == 1:
			dataset_responses['Metabolic'][i] = 1
			dataset_responses['Therapeutic'][i] = 1

		if dataset_responses['Antimicrobial'][i] == 1:			
			dataset_responses['Therapeutic'][i] = 1		

		if dataset_responses['Antiparasitic'][i] == 1:
			dataset_responses['Toxic'][i] = 1
			dataset_responses['Therapeutic'][i] = 1

		if dataset_responses['Antiprotozoal'][i] == 1:
			dataset_responses['Antimicrobial'][i] = 1
			dataset_responses['Therapeutic'][i] = 1

		if dataset_responses['Anti-TB'][i] == 1:
			dataset_responses['Antibacterial-antibiotic'][i] = 1
			dataset_responses['Antimicrobial'][i] = 1
			dataset_responses['Therapeutic'][i] = 1

		if dataset_responses['Antitumour'][i] == 1:
			dataset_responses['Anticancer'][i] = 1
			dataset_responses['Therapeutic'][i] = 1
		
		if dataset_responses['Antiviral'][i] == 1:
			dataset_responses['Antimicrobial'][i] = 1
			dataset_responses['Therapeutic'][i] = 1

		if dataset_responses['Anuro-defense'][i] == 1:
			dataset_responses['Antimicrobial'][i] = 1
			dataset_responses['Therapeutic'][i] = 1

		if dataset_responses['Bacteriocins'][i] == 1:
			dataset_responses['Antibacterial-antibiotic'][i] = 1
			dataset_responses['Antimicrobial'][i] = 1
			dataset_responses['Therapeutic'][i] = 1

		if dataset_responses['Brain-peptide'][i] == 1:
			dataset_responses['Neurological-activity'][i] = 1
		
		if dataset_responses['Cancer-cell'][i] == 1:
			dataset_responses['Other-activity'][i] = 1

		if dataset_responses['Cytolytic'][i] == 1:
			dataset_responses['Toxic'][i] = 1
			dataset_responses['Therapeutic'][i] = 1

		if dataset_responses['Defense'][i] == 1:
			dataset_responses['Sensorial'][i] = 1

		if dataset_responses['Hemolytic'][i] == 1:
			dataset_responses['Cytolytic'][i] = 1
			dataset_responses['Toxic'][i] = 1
			dataset_responses['Therapeutic'][i] = 1		

		if dataset_responses['Immunomodulatory'][i] == 1:
			dataset_responses['Immunological-activity'][i] = 1

		if dataset_responses['Insecticidal'][i] == 1:
			dataset_responses['Toxic'][i] = 1
			dataset_responses['Therapeutic'][i] = 1

		if dataset_responses['Mammallian-cell'][i] == 1:
			dataset_responses['Other-activity'][i] = 1

		if dataset_responses['Metabolic'][i] == 1:
			dataset_responses['Therapeutic'][i] = 1

		if dataset_responses['Neuropeptide'][i] == 1:
			dataset_responses['Neurological-activity'][i] = 1

		if dataset_responses['Quorum-sensing'][i] == 1:
			dataset_responses['Sensorial'][i] = 1

		if dataset_responses['Regulatory'][i] == 1:
			dataset_responses['Metabolic'][i] = 1
			dataset_responses['Therapeutic'][i] = 1

		if dataset_responses['Toxic'][i] == 1:			
			dataset_responses['Therapeutic'][i] = 1

	return dataset_responses

def encoding_process(matrix_sequences, file_encoding):

	matrix_encoding = []

	for i in range(len(matrix_sequences)):
		sequence = matrix_sequences[i]		
		sequence_encoding = encoding_sequence(sequence, file_encoding['component_1'])
		matrix_encoding.append(sequence_encoding)

	#make zero padding
	#create zero padding
	for i in range(len(matrix_encoding)):
		for j in range(len(matrix_encoding[i]),256):
			matrix_encoding[i].append(0)

	#apply fast fourier transformation
	matrix_digitized = []

	for row in matrix_encoding:
		yf = fft(row)
		matrix_digitized.append(np.abs(yf[0:256//2]))

	return matrix_digitized

def encoding_sequence(sequence, value_property):

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

def evaluate_sequence(sequence):

	response=0

	for element in sequence:
		if element not in ["A","R","N","D","C","Q","E","G","H","I","L","K","M","F","P","S","T","W","Y","V"]:
			response=1
			break

	return response

def exec(peptide, time):
	file = open("../src/public/jobs/service2/service2.fasta", "w") 
	file.write(peptide)
	file.close()
	fasta = SeqIO.parse("../src/public/jobs/service2/service2.fasta", "fasta")
	if(any(fasta) == False): #False when `fasta` is empty
		return "error"
	else:
		os.mkdir("../src/public/jobs/service2/"+time, mode=0o777)	
	#config input information data
	fasta_file = "../src/public/jobs/service2/service2.fasta"

	path_output = "../src/public/jobs/service2/"+time+"/"#carpeta donde se guardan los resultados.

	#path to read models

	#path_read_models = "/media/ceql/Externo/training_process/" #carpeta donde se encuentran todos los modelos.
	path_read_models = "../training_process/" 
	
	#path to read encoding strategie
	path_encoding_data = "encoding_AAIndex/"

	#path to read csv resources 

	#path_csv_resources = "/media/ceql/Externo/csv_resources/"
	path_csv_resources = "../csv_resources/"

	#process fasta file input and get sequences to make classification data
	print("Preprocessing data input")

	#arrays to save sequences to process element
	sequences_array_in = []
	id_sequences_array_in = []

	sequences_array_not_in = []
	id_sequences_array_not_in = []

	response_status=0
	dict_summary = {}

	T = 1.0/float(256)
	xf = np.linspace(0.0, 1.0/(2.0*T), 256//2)

	list_binary_models = ["Allergen", "Anti-Angiogenic", "Antibacterial-antibiotic", "Antibiofilm", "Anticancer", "Anti-Diabetic", "Antifungal", "anti_gram_negative", "anti_gram_positive", "Anti-HIV", "Antihypertensive", "Antimicrobial", "Antiparasitic", "Antiprotozoal", "Anti-TB", "Antitumour", "Antiviral", "Anuro-defense", "Bacteriocins", "Brain-peptide", "Cancer-cell", "Cytolytic", "Defense", "Drug-delivery-vehicle", "Hemolytic", "Immunological-activity", "Immunomodulatory", "Insecticidal", "Mammallian-cell", "Metabolic", "Neurological-activity", "Neuropeptide", "Other-activity", "Propeptide", "Quorum-sensing", "Regulatory", "Sensorial", "Signal", "Therapeutic", "Toxic", "Transit"]
	list_properties = ["alpha-structure_group", "betha-structure_group", "energetic_group", "hydropathy_group", "hydrophobicity_group", "index_group", "secondary_structure_properties_group", "volume_group"]

	try:
		print("Read fasta file")
		#read fasta file
		for record in SeqIO.parse(fasta_file, "fasta"):
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
		response_status=1
		pass

	classify_status = {}

	if response_status == 0:

		print("Check status read: OK")

		if len(sequences_array_in)>0:

			print("Create dataset to save classification of results")
			matrix_response = []

			for i in range(len(id_sequences_array_in)):

				row = [id_sequences_array_in[i]]

				#add 0 values for each activity to analysis
				for j in range(len(list_binary_models)):
					row.append(0)

				matrix_response.append(row)

			#create dataset to save information data
			header = ["id_sequence"]

			for j in range(len(list_binary_models)):
				header.append(list_binary_models[j])

			dataset_export_responses = pd.DataFrame(matrix_response, columns=header)

			print("Process models by activity")		
			
			for activity in list_binary_models:

				try:
					print("Process activity: ", activity)

					response_ok=[0 for sequence in sequences_array_in]
					response_not=[0 for sequence in sequences_array_in]			

					for property_value in list_properties:

						print("Process property: ", property_value)
						file_encoding = pd.read_csv(path_encoding_data+property_value+"/data_component.csv")
						matrix_digitized = encoding_process(sequences_array_in, file_encoding)

						print("Read resources csv to scalling data")

						data_scalling = pd.read_csv(path_csv_resources+activity+"/"+property_value+"_digital_data.csv")
						data_scalling = data_scalling.drop(columns=["id_sequence"])

						print("Scaler dataset")

						scaler = MinMaxScaler()
						scaler.fit(data_scalling)
						dataset_scaler = scaler.transform(matrix_digitized)

						print("Apply predictive model")
						
						#using model
						clf = load(path_read_models+activity+"/modelExport"+ property_value+".joblib")
						responses = clf.predict(dataset_scaler)				
						
						for i in range(len(responses)):

							if responses[i] == 1:
								response_ok[i]+=1
							else:
								response_not[i]+=1

					#make support response
					response_model = []

					for i in range(len(response_ok)):

						if response_ok[i] >response_not[i]:
							response_model.append(1)
						else:
							response_model.append(0)

					dataset_export_responses[activity] = response_model			
					classify_status.update({activity:"OK-PROCESS"})
				except:
					classify_status.update({activity:"ERROR-PROCESS"})
					pass

			dict_summary.update({"status_classification":classify_status})
			print("Make correcction supported by our categorization")
			dataset_export_responses = make_corrections_to_classification(dataset_export_responses)

			dict_summary.update({"status":"PROCESS_OK"})
			print("Export summary responses")
			dataset_export_responses.to_csv(path_output+"export_category_data.csv", index=False)
			
		else:
			dict_summary.update({"status":"NO_SEQUENCE_TO_ENCODING"})	
		
	else:
		dict_summary.update({"status":"ERROR_PREPROCESING"})
		
	#export JSON summary
	return dict_summary
	#with open(path_output+"summary_preprocess.json", 'w') as fp:
	#	json.dump(dict_summary, fp)