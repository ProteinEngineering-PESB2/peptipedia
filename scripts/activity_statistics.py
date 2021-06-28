from pymongo import MongoClient
import numpy as np
client = MongoClient('localhost', 27017)
db = client['Peptipedia']
col = db['peptides']
update_col = db['statistics']

#full_activities = ['Therapeutic', 'Antimicrobial', 'Antifungal', 'Anti Yeast', 'Antibacterial', 'Anti Gram(-)', 'Anti Gram(+)', 'Anti MRSA', 'Antilisterial', 'Bacteriocins', 'Anti Tuberculosis', 'Antibiofilm', 'Anuro defense', 'Antiprotozoal', 'Antimalarial/antiplasmodial', 'Antiviral', 'Anti HIV', 'Anti HSV', 'Anticancer', 'Anti Tumour', 'Toxic', 'Insecticidal', 'Spermicidal', 'Antiparasitic', 'Cytolytic', 'Hemolytic', 'Metabolic', 'Antiinflammatory', 'Antihypertensive', 'Enzyme inhibitor', 'Bioactive', 'Antioxidant', 'Immunological', 'Immunomodulatory', 'Wound healing', 'Cell degranulating', 'Sensorial', 'Quorum sensing', 'Chemotactic', 'Cell-cell communication', 'Defense', 'Neurological', 'Antinociceptive', 'Brain peptide', 'Neuropeptide', 'Drug delivery vehicle', 'Cell-penetrating', 'Other', 'Signal Peptide', 'Cancer cell', 'Mammallian cell', 'Proteolytic', 'Transit', 'Propeptide', 'Surface-immobilized', 'Milk Peptide']
activities = ['Propeptide', 'Signal', 'Transit', 'Cell sensing', 'Drug delivery vehicle', 'Therapeutic', 'Other activity', 'Neurological activity', 'Immunological activity', 'non_activity']

total_sequences = []
total_organism = []
total_uniprot = []
description = 'desc'
full_description = 'full_desc'
hist_molecular_weigth = []
hist_charge = []
hist_charge_density = []
hist_isoelectric = []
hist_inestability = []
hist_aromaticity = []
hist_aliphatic_index = []
hist_hydrophobic_ratio = []
hist_hydrophobicity_profile = []
hist_hydrophobic_profile = []
hist_momment = []
mean = []
maximum = []
minimum = []
std = []
variance = []
quartile1 = []
quartile3 = []

for activity in activities:
  for documento in col.find({}):
    if documento[activity] == '1.0' or documento[activity] == '1':
      if(documento['sequence'] != ''):
        total_sequences.append(documento['sequence'])
      if(documento['organism_value'] != ''):
        total_organism.append(documento['organism_value'])
      if(documento['uniprot_code'] != ''):
        total_uniprot.append(documento['uniprot_code'])
      if(documento['molecular_weigth'] != '' and documento['molecular_weigth'] != "-"):
        hist_molecular_weigth.append(float(documento['molecular_weigth']))
      if(documento['charge'] != '' and documento['charge'] != "-"):
        hist_charge.append(float(documento['charge']))



      if(documento['charge_density'] != '' and documento['charge_density'] != "-"):
        hist_charge_density.append(float(documento['charge_density']))
      if(documento['isoelectric_point'] != '' and documento['isoelectric_point'] != "-"):
        hist_isoelectric.append(float(documento['isoelectric_point']))
      if(documento['instability_index'] != '' and documento['instability_index'] != "-"):
        hist_inestability.append(float(documento['instability_index']))
      if(documento['aromaticity'] != '' and documento['aromaticity'] != "-"):
        hist_aromaticity.append(float(documento['aromaticity']))

      if(documento['aliphatic_index'] != '' and documento['aliphatic_index'] != "-"):
        hist_aliphatic_index.append(float(documento['aliphatic_index']))
      if(documento['hydrophobic_ratio'] != '' and documento['hydrophobic_ratio'] != "-"):
        hist_hydrophobic_ratio.append(float(documento['hydrophobic_ratio']))
      if(documento['hydrophobicity_profile'] != '' and documento['hydrophobicity_profile'] != "-"):
        hist_hydrophobicity_profile.append(float(documento['hydrophobicity_profile']))
      if(documento['hydrophobic_profile'] != '' and documento['hydrophobic_profile'] != "-"):
        hist_hydrophobic_profile.append(float(documento['hydrophobic_profile']))
        
      if(documento['momment'] != '' and documento['momment'] != "-"):
        hist_momment.append(float(documento['momment']))

  if (hist_molecular_weigth and hist_charge and hist_charge_density and hist_isoelectric and hist_inestability and hist_aromaticity and hist_aliphatic_index and hist_hydrophobic_ratio and hist_hydrophobicity_profile and hist_hydrophobic_profile and hist_momment):
    
    mean.extend([
    "%.4f" % (np.mean(hist_molecular_weigth)),
    "%.4f" % (np.mean(hist_charge)),
    "%.4f" % (np.mean(hist_charge_density)),
    "%.4f" % (np.mean(hist_isoelectric)),
    "%.4f" % (np.mean(hist_inestability)),
    "%.4f" % (np.mean(hist_aromaticity)),
    "%.4f" % (np.mean(hist_aliphatic_index)),
    "%.4f" % (np.mean(hist_hydrophobic_ratio)),
    "%.4f" % (np.mean(hist_hydrophobicity_profile)),
    "%.4f" % (np.mean(hist_hydrophobic_profile)),
    "%.4f" % (np.mean(hist_momment))
    ])
  

    minimum.extend([
        "%.4f" % (np.amin(hist_molecular_weigth)),
        "%.4f" % (np.amin(hist_charge)),
        "%.4f" % (np.amin(hist_charge_density)),
        "%.4f" % (np.amin(hist_isoelectric)),
        "%.4f" % (np.amin(hist_inestability)),
        "%.4f" % (np.amin(hist_aromaticity)),
        "%.4f" % (np.amin(hist_aliphatic_index)),
        "%.4f" % (np.amin(hist_hydrophobic_ratio)),
        "%.4f" % (np.amin(hist_hydrophobicity_profile)),
        "%.4f" % (np.amin(hist_hydrophobic_profile)),
        "%.4f" % (np.amin(hist_momment))
        ])

    maximum.extend([
        "%.4f" % (np.amax(hist_molecular_weigth)),
        "%.4f" % (np.amax(hist_charge)),
        "%.4f" % (np.amax(hist_charge_density)),
        "%.4f" % (np.amax(hist_isoelectric)),
        "%.4f" % (np.amax(hist_inestability)),
        "%.4f" % (np.amax(hist_aromaticity)),
        "%.4f" % (np.amax(hist_aliphatic_index)),
        "%.4f" % (np.amax(hist_hydrophobic_ratio)),
        "%.4f" % (np.amax(hist_hydrophobicity_profile)),
        "%.4f" % (np.amax(hist_hydrophobic_profile)),
        "%.4f" % (np.amax(hist_momment))
        ])

    std.extend([
        "%.4f" % (np.std(hist_molecular_weigth)),
        "%.4f" % (np.std(hist_charge)),
        "%.4f" % (np.std(hist_charge_density)),
        "%.4f" % (np.std(hist_isoelectric)),
        "%.4f" % (np.std(hist_inestability)),
        "%.4f" % (np.std(hist_aromaticity)),
        "%.4f" % (np.std(hist_aliphatic_index)),
        "%.4f" % (np.std(hist_hydrophobic_ratio)),
        "%.4f" % (np.std(hist_hydrophobicity_profile)),
        "%.4f" % (np.std(hist_hydrophobic_profile)),
        "%.4f" % (np.std(hist_momment))
        ])

    variance.extend([
        "%.4f" % (np.var(hist_molecular_weigth)),
        "%.4f" % (np.var(hist_charge)),
        "%.4f" % (np.var(hist_charge_density)),
        "%.4f" % (np.var(hist_isoelectric)),
        "%.4f" % (np.var(hist_inestability)),
        "%.4f" % (np.var(hist_aromaticity)),
        "%.4f" % (np.var(hist_aliphatic_index)),
        "%.4f" % (np.var(hist_hydrophobic_ratio)),
        "%.4f" % (np.var(hist_hydrophobicity_profile)),
        "%.4f" % (np.var(hist_hydrophobic_profile)),
        "%.4f" % (np.var(hist_momment))
        ])

    quartile1.extend([
        "%.4f" % (np.percentile(hist_molecular_weigth, 25)),
        "%.4f" % (np.percentile(hist_charge, 25)),
        "%.4f" % (np.percentile(hist_charge_density, 25)),
        "%.4f" % (np.percentile(hist_isoelectric, 25)),
        "%.4f" % (np.percentile(hist_inestability, 25)),
        "%.4f" % (np.percentile(hist_aromaticity, 25)),
        "%.4f" % (np.percentile(hist_aliphatic_index, 25)),
        "%.4f" % (np.percentile(hist_hydrophobic_ratio, 25)),
        "%.4f" % (np.percentile(hist_hydrophobicity_profile, 25)),
        "%.4f" % (np.percentile(hist_hydrophobic_profile, 25)),
        "%.4f" % (np.percentile(hist_momment, 25))
        ])

    quartile3.extend([
        "%.4f" % (np.percentile(hist_molecular_weigth, 75)),
        "%.4f" % (np.percentile(hist_charge, 75)),
        "%.4f" % (np.percentile(hist_charge_density, 75)),
        "%.4f" % (np.percentile(hist_isoelectric, 75)),
        "%.4f" % (np.percentile(hist_inestability, 75)),
        "%.4f" % (np.percentile(hist_aromaticity, 75)),
        "%.4f" % (np.percentile(hist_aliphatic_index, 75)),
        "%.4f" % (np.percentile(hist_hydrophobic_ratio, 75)),
        "%.4f" % (np.percentile(hist_hydrophobicity_profile, 75)),
        "%.4f" % (np.percentile(hist_hydrophobic_profile, 75)),
        "%.4f" % (np.percentile(hist_momment, 75))
        ])
  else:
        print("Error")

  update_col.update_one({
      'Name': activity
    },{
      '$set': {
      'Mean': mean,
      'Std': std,
      'Max': maximum,
      'Min': minimum,
      'Variance': variance,
      'Quartile1': quartile1,
      'Quartile3': quartile3,
      'Description': description,
      'Full_description' : full_description,
      'Hist_molecular_weigth': hist_molecular_weigth,
      'Hist_charge': hist_charge,
      'Hist_charge_density': hist_charge_density,
      'Hist_isoelectric': hist_isoelectric,
      'Hist_inestability': hist_inestability,
      'Hist_aromaticity': hist_aromaticity,
      'Hist_aliphatic_index': hist_aliphatic_index,
      'Hist_hydrophobic_ratio': hist_hydrophobic_ratio,
      'Hist_hydrophobicity_profile': hist_hydrophobicity_profile,
      'Hist_hydrophobic_profile': hist_hydrophobic_profile,
      'Hist_momment': hist_momment,
      'Total_sequences': len(set(total_sequences)),
      'Total_organisms': len(set(total_organism)),
      'Total_uniprot': len(set(total_uniprot))
    }
  }, upsert=False)
  total_sequences = []
  total_organism = []
  total_uniprot = []
  total_pdb = []
  description = 'desc'
  full_description = 'full_desc'
  hist_molecular_weigth = []
  hist_charge = []
  hist_charge_density = []
  hist_isoelectric = []
  hist_inestability = []
  hist_aromaticity = []
  hist_aliphatic_index = []
  hist_hydrophobic_ratio = []
  hist_hydrophobicity_profile = []
  hist_hydrophobic_profile = []
  hist_momment = []
  mean = []
  maximum = []
  minimum = []
  std = []
  variance = []
  quartile1 = []
  quartile3 = []