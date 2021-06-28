from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['Peptipedia']
col = db['peptides']
update_col = db['statistics']


#full_activities = ['Therapeutic', 'Antimicrobial', 'Antifungal', 'Anti Yeast', 'Antibacterial', 'Anti Gram(-)', 'Anti Gram(+)', 'Anti MRSA', 'Antilisterial', 'Bacteriocins', 'Anti Tuberculosis', 'Antibiofilm', 'Anuro defense', 'Antiprotozoal', 'Antimalarial/antiplasmodial', 'Antiviral', 'Anti HIV', 'Anti HSV', 'Anticancer', 'Anti Tumour', 'Toxic', 'Insecticidal', 'Spermicidal', 'Antiparasitic', 'Cytolytic', 'Hemolytic', 'Metabolic', 'Antiinflammatory', 'Antihypertensive', 'Enzyme inhibitor', 'Bioactive', 'Antioxidant', 'Immunological', 'Immunomodulatory', 'Wound healing', 'Cell degranulating', 'Sensorial', 'Quorum sensing', 'Chemotactic', 'Cell-cell communication', 'Defense', 'Neurological', 'Antinociceptive', 'Brain peptide', 'Neuropeptide', 'Drug delivery vehicle', 'Cell-penetrating', 'Other', 'Signal Peptide', 'Cancer cell', 'Mammallian cell', 'Proteolytic', 'Transit', 'Propeptide', 'Surface-immobilized', 'Milk Peptide']
activities = ['Propeptide', 'Signal', 'Transit', 'Cell sensing', 'Drug delivery vehicle', 'Therapeutic', 'Other activity', 'Neurological activity', 'Immunological activity', 'non_activity']


update_col.insert_one({
    'Name': "Total number of records"
})
update_col.insert_one({
    'Name': "Total Uniprot codes"
})
update_col.insert_one({
    'Name': "Total number of organism"
})
update_col.insert_one({
    'Name': "PieChart1"
})
update_col.insert_one({
    'Name': "Glossary"
})
update_col.insert_one({
    'Name': "Histogram1"
})

for activity in activities:
    update_col.insert_one({
    'Name': activity
})

