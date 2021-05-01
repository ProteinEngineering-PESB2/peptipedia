from pymongo import MongoClient
import numpy as np
client = MongoClient('localhost', 27017)
db = client['Peptipedia']
col = db['peptides']
update_col = db['organisms']


#guarda todos los organismos unicos
total_organism = []
for documento in col.find({}):
  if documento['organism_value'] != '':
    total_organism.append(documento['organism_value'])

unique_total_organism = list(set(total_organism))

for element in unique_total_organism:
    update_col.insert_one({
                'organism_value': element
    })
