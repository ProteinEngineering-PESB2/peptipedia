from pymongo import MongoClient
import numpy as np
client = MongoClient('localhost', 27017)
db = client['Peptipedia']
col = db['peptides']
update_col = db['activities']

full_activities = ['Propeptide', 'Signal', 'Transit', 'Antimicrobial', 'Antihypertensive', 'Allergen', 'Anti Angiogenic', 'Quorum sensing', 'Antiviral', 'Antibiofilm', 'Anti Gram(+)', 'Anti Gram(-)', 'Antibacterial/antibiotic', 'Antifungal', 'Antiparasitic', 'Antitumour', 'Antiprotozoal', 'Cell-penetrating', 'Neuropeptide', 'Sensorial', 'Blood-brain barrier crossing', 'Anti Diabetic', 'Toxic', 'Chemotactic', 'Antilisterial', 'Hemolytic', 'Cytolytic', 'Cancer cell', 'Insecticidal', 'Anti HIV', 'Antiinflammatory', 'Mammallian cell', 'Wound healing', 'Anti HSV', 'Enzyme inhibitor', 'Antinociceptive', 'Proteolytic', 'Immunomodulatory', 'Drug delivery vehicle', 'Cell-cell communication', 'Anti TB', 'Anuro defense', 'Therapeutic', 'Other activity', 'Neurological activity', 'Immunological activity', 'Metabolic', 'Antimalarial/antiplasmodial', 'Anticancer', 'Regulatory', 'Anti Yeast', 'Anti MRSA', 'Bacteriocins', 'Bioactive', 'Antioxidant', 'Defense', 'Brain peptide', 'Surface-immobilized', 'non_activity']

for activity in full_activities:
    for documento in col.find({}):
        if documento[activity] == '1.0' or documento[activity] == '1':
            update_col.insert_one({
                'activity': activity,
                'sequence': documento['sequence'],
                'is_modify': documento['is_modify'],
                'length': documento['length'],
                'in_ADP': documento['in_ADP'],
                'in_AHTPDB': documento['in_AHTPDB'],
                'in_AllergenOnline': documento['in_AllergenOnline'],
                'in_AntiAngioPred': documento['in_AntiAngioPred'],
                'in_AntiTbPdb': documento['in_AntiTbPdb'],
                'in_ArachnoServer': documento['in_ArachnoServer'],
                'in_AVPdb': documento['in_AVPdb'],
                'in_BaAMPs': documento['in_BaAMPs'],
                'in_BioDaDpep': documento['in_BioDaDpep'],
                'in_BIOPEP': documento['in_BIOPEP'],
                'in_BrainPeps': documento['in_BrainPeps'],
                'in_CAMP': documento['in_CAMP'],
                'in_ConoServer': documento['in_ConoServer'],
                'in_CPPsite': documento['in_CPPsite'],
                'in_DADP': documento['in_DADP'],
                'in_DBAASP': documento['in_DBAASP'],
                'in_DRAMP': documento['in_DRAMP'],
                'in_Erop-Moscow': documento['in_Erop-Moscow'],
                'in_Hemolytik': documento['in_Hemolytik'],
                'in_HIPdb': documento['in_HIPdb'],
                'in_LAMP2': documento['in_LAMP2'],
                'in_NeuroPedia': documento['in_NeuroPedia'],
                'in_PhytAMP': documento['in_PhytAMP'],
                'in_quorum-peps': documento['in_quorum-peps'],
                'in_SATPdb': documento['in_SATPdb'],
                'in_SPdb': documento['in_SPdb'],
                'in_TumorHoPe': documento['in_TumorHoPe'],
                'in_YADAMP': documento['in_YADAMP'],
                'in_uniprot': documento['in_uniprot'],
                'Virus_antiviral': documento['Virus_antiviral'],
                'Family_virus': documento['Family_virus'],
                'Source_viral': documento['Source_viral'],
                'IC50_antiviral': documento['IC50_antiviral'],
                'unit_IC50_antiviral': documento['unit_IC50_antiviral'],
                'uniprot_code': documento['uniprot_code'],
                'peptide_name': documento['peptide_name'],
                'ic50_anti_hipertensive': documento['ic50_anti_hipertensive'],
                'source_anti_hipertensive': documento['source_anti_hipertensive'],
                'taxonomy': documento['taxonomy'],
                'organism_value': documento['organism_value'],
                'gene_name': documento['gene_name'],
                'Target-tumor': documento['Target-tumor'],
                'IC50_for_antiHIV': documento['IC50_for_antiHIV'],
                'IC50_for_antiHIV_unit': documento['IC50_for_antiHIV_unit'],
                'PMID_identifer': documento['PMID_identifer'],
                'in_BACTIBASE': documento['in_BACTIBASE'],
                'id_sequence': documento['id_sequence'],
                'formula': documento['formula'],
                'molecular_weigth': documento['molecular_weigth'],
                'boman_index': documento['boman_index'],
                'charge': documento['charge'],
                'charge_density': documento['charge_density'],
                'isoelectric_point': documento['isoelectric_point'],
                'instability_index': documento['instability_index'],
                'aromaticity': documento['aromaticity'],
                'aliphatic_index': documento['aliphatic_index'],
                'hydrophobic_ratio': documento['hydrophobic_ratio'],
                'hydrophobicity_profile': documento['hydrophobicity_profile'],
                'hydrophobic_profile': documento['hydrophobic_profile'],
                'momment': documento['momment'],
            })
        

