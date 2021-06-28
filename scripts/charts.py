from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['Peptipedia']
col = db['peptides']
update_col = db['statistics']

#pie chart de todas las actividades
total_per_activity = []
#full_activities = ['Therapeutic', 'Antimicrobial', 'Antifungal', 'Anti Yeast', 'Antibacterial', 'Anti Gram(-)', 'Anti Gram(+)', 'Anti MRSA', 'Antilisterial', 'Bacteriocins', 'Anti Tuberculosis', 'Antibiofilm', 'Anuro defense', 'Antiprotozoal', 'Antimalarial/antiplasmodial', 'Antiviral', 'Anti HIV', 'Anti HSV', 'Anticancer', 'Anti Tumour', 'Toxic', 'Insecticidal', 'Spermicidal', 'Antiparasitic', 'Cytolytic', 'Hemolytic', 'Metabolic', 'Antiinflammatory', 'Antihypertensive', 'Enzyme inhibitor', 'Bioactive', 'Antioxidant', 'Immunological', 'Immunomodulatory', 'Wound healing', 'Cell degranulating', 'Sensorial', 'Quorum sensing', 'Chemotactic', 'Cell-cell communication', 'Defense', 'Neurological', 'Antinociceptive', 'Brain peptide', 'Neuropeptide', 'Drug delivery vehicle', 'Cell-penetrating', 'Other', 'Signal Peptide', 'Cancer cell', 'Mammallian cell', 'Proteolytic', 'Transit', 'Propeptide', 'Surface-immobilized', 'Milk Peptide']
activities = ['Propeptide', 'Signal', 'Transit', 'Cell sensing', 'Drug delivery vehicle', 'Therapeutic', 'Other activity', 'Neurological activity', 'Immunological activity', 'non_activity']

for element in activities:
    total_flag = 0
    for documento in col.find({}):
        if (documento[element] == '1.0' or documento[element] == '1'):
            total_flag = total_flag+1
    total_per_activity.append(total_flag)

update_col.update_one({
  'Name': "PieChart1"
},{
  '$set': {
    'Value': total_per_activity,
    'Labels': activities
  }
}, upsert=False)

print('grafico de torta insertado con exito')
    
            
#histograma del largo de todas las secuencias
total_lenght_sequences = []
for documento in col.find({}):
    if (documento['length'] != ""):
        total_lenght_sequences.append(float(documento['length']))
update_col.update_one({
  'Name': "Histogram1"
},{
  '$set': {
    'Value': total_lenght_sequences
  }
}, upsert=False)

print('histograma insertado con exito')

