import pandas as pd
import sys
from scipy.spatial import distance

def get_row_from_dataset(dataset, index):

	row_dataset = [dataset[value][index] for value in dataset.keys() if value != "id_sequence_by_algorithm"]

	return row_dataset

dataset = pd.read_csv(sys.argv[1])#mis secuencias codificadas
name_output = sys.argv[2]

matrix_distance = []

for i in range(len(dataset)):

	print("Process distance for sequence: ", i)
	row = []

	for j in range(len(dataset)):

		if i==j:
			row.append(0)

		else:
			vector1 = get_row_from_dataset(dataset, i)
			vector2 = get_row_from_dataset(dataset, j)
			distance_value = distance.correlation(vector1, vector2)
			row.append(distance_value)

	matrix_distance.append(row)

header = ["D_"+str(i+1) for i in range(len(dataset))]

dataset_export = pd.DataFrame(matrix_distance, columns=header)
dataset_export.to_csv(name_output, index=False, sep=",")
