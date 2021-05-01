import pandas as pd
import sys
import json
import edlib
from Bio import SeqIO

def exec(peptide, time_node):
    file = open("../src/public/jobs/service3/service3.fasta", "w") 
    file.write(peptide)
    file.close()
    fasta = SeqIO.parse("../src/public/jobs/service3/service3.fasta", "fasta")
    if(any(fasta) == False): #False when `fasta` is empty
        return "error"
    count = 0
    for record in SeqIO.parse("../src/public/jobs/service3/service3.fasta", "fasta"):
        sequence_input = str(record.seq)
        count = count+1
    print(count)
    print(sequence_input)
    if (count > 1):
        return "error"
    dataset = pd.read_csv("data_values_activity_non_modified.csv")

    dict_response = []
    for i in range(len(dataset)):

        align_result = edlib.align(sequence_input, dataset['sequence'][i], mode = "HW", task = "path")
        view_alignment = edlib.getNiceAlignment(align_result, sequence_input, dataset['sequence'][i])
        dict_aligment = {"input_sequence":view_alignment['query_aligned'], "space_format":view_alignment['matched_aligned'], "compare_sequence": view_alignment['target_aligned'], "id_sequence" : str(dataset['index_sequence'][i]), 'distance_sequences':str(align_result['editDistance'])}
        
        dict_response.append(dict_aligment)

    dict_data_results = {"summary_alignment":dict_response}

    #export result alignment
    return dict_data_results
