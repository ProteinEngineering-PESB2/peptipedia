import pandas as pd
import sys
import os

dataset = pd.read_csv(sys.argv[1])
path_output = sys.argv[2]

path_encoding = sys.argv[3]

activities = ['Signal','Transit','Antimicrobial','Antihypertensive','Allergen','Anti Angiogenic','Quorum sensing','Antiviral','Antibiofilm','Anti Gram(+)','Anti Gram(-)','Antibacterial/antibiotic','Antifungal','Antiparasitic','Antitumour','Antiprotozoal','Cell-penetrating','Neuropeptide','Sensorial','Blood-brain barrier crossing','Anti Diabetic','Toxic','Chemotactic','Antilisterial','Hemolytic','Cytolytic','Cancer cell','Insecticidal','Anti HIV','Antiinflammatory','Mammallian cell','Wound healing','Anti HSV','Enzyme inhibitor','Antinociceptive','Proteolytic','Immunomodulatory','Drug delivery vehicle','Cell-cell communication','Anti TB','Anuro defense','Therapeutic','Other activity','Neurological activity','Immunological activity','Metabolic','Antimalarial/antiplasmodial','Anticancer','Regulatory','Anti Yeast','Anti MRSA','Bacteriocins','Bioactive','Antioxidant','Defense','Brain peptide','Surface-immobilized']
list_properties = ["alpha-structure_group", "betha-structure_group", "energetic_group", "hydropathy_group", "hydrophobicity_group", "index_group", "secondary_structure_properties_group", "volume_group"]

print("Search id sequences by activity")

#search index of sequences by activitiy and save information using hash structure
for activity in activities:
	print("Process activity: ", activity)
	array_index = []

	print("Search sequences activity: ", activity)

	for i in range(len(dataset)):

		if dataset[activity][i] == 1 and dataset['is_modify'][i] == 0:
			array_index.append(dataset['id_sequence'][i])

	#search index by activity and reply the process to get dataset by activity
	tmp_reading = pd.read_csv(path_encoding+list_properties[0]+"_digital_data.csv")
	print("Search index and save information about activity: ", activity)

	index_array_encoding = []

	for index in array_index:
		for i in range(len(tmp_reading)):
			if tmp_reading['id_sequence'][i] == index:
				index_array_encoding.append(i)
				break

	print("Create dir by activity")

	if "+" in activity:
		name_folder = "Gram_positive"

	elif "-" in activity:
		name_folder = "Gram_negative"

	else:
		name_folder = activity.replace(" ", "_").replace("/", "-")

	command = "mkdir -p %s%s" % (path_output, name_folder)
	os.system(command)

	print("Export encoding DSP using properties")

	for property_value in list_properties:

		data_property = pd.read_csv(path_encoding+property_value+"_digital_data.csv")

		values_data = [data_property.iloc[index] for index in index_array_encoding]

		values_data = pd.DataFrame(values_data)
		values_data.to_csv(path_output+name_folder+"/"+property_value+"_digital_data.csv", index=False)

