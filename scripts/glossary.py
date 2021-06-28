from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['Peptipedia']
col = db['peptides']
update_col = db['statistics']



update_col.update_one({
  'Name': "Glossary"
},{
  '$set': {
    #actividades
    'Allergenic': "Activates allergic reactions by stimulating immune system",
    'Anticancer': "Peptides that are selective and toxic to cancer cells. It can destroy these cells by apoptosis, necrosis, or antitumor activity.",
    'AntiGramL': "This activity is based on mechanisms that damage the membrane of cells or intracellular targets in Gram-positive bacteria.",
    'AntiGramP': "This activity is based on mechanisms that damage the membrane of cells or intracellular targets in Gram-negative bacteria.",
    'AntiHIV': "Peptide with activity against the HIV virus.These molecules generally target the process of HIV fusion, viral reverse transcriptase or protease/integrase dimerization.",
    'AntiMRSA': "Activity against Methicillin-resistant Staphylococcus aureus.",
    'AntiTB': "The most common mechanism is the disruption of the cell envelope, although some especific intracellular targets have also been reported.",
    'AntiHSV': "Depending on the sequence of the peptide, the mechanism of action can target the viral cell or host defenses.",
    'Antibacterialantibiotic': "Peptides with activity against bacteria. Depending on the sequence, it could attack Gram-positive or Gram-negative bacteria, even a broad spectrum of both.",
    'Antibiofilm': "The activity is based on the inhibition of biofilm formation or its degradation.",
    'Antidiabetic': "Useful to treat the diabetes disease.",
    'Antifungal': "The mechanism focuses on the attack of a specific compound on the membrane / cell wall of fungi, the induction of the apoptosis process or other intracellular targets. Although, some broad spectrum mechanisms (membrane and intracellular targets) have also reported antifungal properties.",
    'Antihypertensive': "Able to regulate blood pressure.",
    'Antiinflammatory': "Useful for inflammation and pain.",
    'Antilisterial': "Activity against Listeria monocytogenes.",
    'Antimalarialantiplasmodial': "Activity against Plasmodium.",
    'Antimicrobial': "Activity against unicellular organisms, such as fungi, protozoo, bacteria, virus, among others.",
    'Antinociceptive': "Able to block noxious stimulus (analgesic effect).",
    'Antioncogenic': "This activity is related to supress tumour angiogenesis (the most common mechanism are mentioned in the anticancer and antitumour activities).",
    'Antioxidant': "The mechanism of action could be based on reducing lipid oxidation, radical scavenging and reactive oxygen species, among others.",
    'Antiparasitic': "Activity against eukaryotic parasites. The mechanism of action will depend on the parasite and the structure of the peptide.",
    'Antiprotozoal': "Activity against protozoa. The mechanism of action could be based on an interaction with the cell membrane, intercellular targets, or triggering autophagic / apoptotic processes.",
    'Antitumour': "The most common mechanism of these peptides are the inhibition of tumour angiogenesis, induction of apoptosis, destruction of cell membrane and inmune regulation.",
    'Antiviral': "Activity against DNA or RNA virus. The mechanism of action focuses on blocking the attachment of the virus to the host cell or its replication.",
    'Antiyeast': "Activity against yeasts. The mechanism of action could target specific membrane compounds or intracellular targets (similar to antifungal activity).",
    'Bacteriocins': "Bacterial peptides with antibacterial activity. The mechanism of action will depend on the sequence and its target.",
    'Bioactive': "Active protein-derived peptides that may have physiological health benefits.",
    'Bloodbrainbarriercrossing': "Able to cross the blood-brain barrier.",
    'Brainpeptide': "Brain peptides are synthesized and released by neuronal and non-neuronal cells that function as intercellular signaling molecules,serving as neurotransmitters,  neuromodulators, neurohormones, cytokines, chemokines or growth factors.",
    'Cancercell': "Cells with an abnormal cell division that can lead to cancer disease.",
    'Cellcellcomunication': "Communication between cells. It could be based on local signals (adjacent cells) or long distance signals, which involve the use of hormones.",
    'Celldegranulating': "Process in which a cell releases cytotoxic molecules from a granule.",
    'Cellpenetrating': "Amino acid sequence able to cross cell membranes.",
    'Chemotactic': "Able to mobilize organisms using chemical concentrations.",
    'Cytolytic': "Process that generates cell rupture by chemical or biological agents.",
    'Defense': "Response mechanism against foreign substances or organisms. It could be based on the innate immune system or the adaptive immune system.",
    'Anurodefense': "Peptides involved in the defense mechanism of the Anura order. In general, this molecules have antimicrobial properties and can be found in the host natural defenses, such as skin secretions.",
    'Drugdeliveryvehicle': "Sustance that helps a drug to be safely delivered to its therapeutic target, reducing toxics effects or degradation. Some examples are emulsions, polymers, semi-solidal products, nanoparticles and encapsulations, among others.",
    'Enzymeinhibitor': "Molecule that binds to an enzyme in order to decrease its activity.",
    'Hemolytic': "Rupture of red blood cells.",
    'Hormonal': "Useful to regulate hormone activities.",
    'Immunomodulatory': "Modulatory activity for innate and/or adaptive immune responses.",
    'Insecticidal': "Cytotoxic for insect cells.",
    'Mammaliancell': "Cells isolated or derived from  mammal tissue. Immortalized cell lines are commonly used as in vitro model for testing toxic compounds or for the production of eukaryotics proteins.",
    'Metabolic': "Useful for regulation of metabolism and homeostasis.",
    'Neuropeptide': "A neuronal signalling molecules involved in the regulation of physiological processes and behaviour.",
    'Neurologicalactivity': "Activity related to the neurons or the nervous system. This group includes neuropeptides, brain peptides and antinociceptive activities.",
    'Propeptide': "Precursor with no biological activity. This molecule can be activated after a post-translational modification, such as the cleavage of a region or the addition of another molecule. Some of the molecules in this group could be in the 'therapeutic category' in their active form.",
    'Proteolytic': "Activity related to the breakdown of proteins into peptides or aminoacids.",
    'Quorumsensing': "Regulates gene expression for cell population regulation.",
    'Regulatoryactivity': "The molecule is involved in regulatory process in a cell or organism.",
    'Cell sensing': "Activities related to cell detection mechanisms, such as quorum sensing, chemotactic movement, cell-to-cell communication, defense mechanisms, among others.",
    'Signal': "Used as a post-translational modification or translocation, because these peptides are useful for marking the protein secretion pathway and target location. These molecules are commonly used for the recombinant protein production, diagnosis and vaccination.",
    'Sodiumchannelblocker': "Molecule that inhibits the sodium influx through the sodium channel.",
    'Spermicidal': "This molecules can affect the mobility or viability of sperm.",
    'Surfaceimmobilized': "The molecule is immobilized in inorganic materials such as glass, titanium oxide, resin beads, silicone surfaces, among others. The activity of the peptide could be affected after the immobilization process.",
    'Therapeutic': "Able to be used for sickness treatments. The specific activity of this peptides will depend on the therapeutic target. This category include antimicrobial, anticancer, toxic, metabolic and bioactive peptides.",
    'Toxic': "Cytotoxic activity against eukaryote organism cells.",
    'Transit': "Involved in the transport of a protein encoded by a nuclear gene to a particular organelle, such as mitochondrion, chloroplast, peroxisome, among others.",
    'Woundhealing': "These peptides can enhance angiogenesis process and stimulate tissue response to an injury, immunomodulatory activity, collagen boosting or extracellular matrix production, among other mechanisms.",
    'Immunologicalactivity': "Activities related to the immune response against foreign substances. It could be related to defense mechanisms, immunomodulatory activities and wound healing, allergenic reactions, cell degranulation mechanism, among others.",
    'Nonactivity': "Peptide with no activity reported in the databases used in this application.",
    'Otheractivity': "The activities of this group are not directly related to the other main categories. Includes 4 main subdivisions: mammalian and cancer cell peptides, protein peptides, and surface immobilized peptides.",
    'AntiAngiogenic': "These molecules could be used in cancer disease treatments. In this case, the molecule would block the growth of blood vessels that provide nutrients and oxygen for tumor growth.",
    #propiedades
    'Molecularweight': "Mass of a given molecule. For proteins and peptide its usually measured in Daltons or kiloDaltons (Da/KDa) or sequence length in amino acids (aa).",
    'Charge': "Net value of the electrical charge of a molecule. In proteins, it depends on the amino acid profile and the protonation state through the pH of the medium.",
    'Chargedensity': "Amount of electrical charge in a defined unit of length, such as surface area or volume. The overall charge density of a protein will depend on the composition of the amino acid sequence and the pH of the medium.",
    'Isoelectricpoint': "The pH of a solution at which the net charge of a protein becomes zero. Values ​​above this point will result in a negatively charged surface of the protein. Below this point, the surface would be positively charged.",
    'Inestability': "Net balance of forces that determines whether a protein will remain in its native folded conformation or in an unfolded state. Some factors that affect the stability of a protein are the composition of the aminoacid sequence, the pH and temperature of the medium, among others.",
    'Aromaticity': "Represents the content of aromatic aminoacids in a protein, such as phenylalanine, tryptophan and tyrosine, measured as their relative frequency.",
    'Aliphaticindex': "Describe the relative volume occupied by aliphatic side chains (alanine, valine, leucine and isoleucine) in a protein. An increase of this parameter is associated with a increase of thermostability for globular proteins.",
    'Hydrophobicratio': "Relative frequency of the amino acids A,C,F,I,L,M and V.",
    'Hydrophobicityprofile': "Chart showing the local hydrophobicity of the amino acid sequence as a function of position."
  }
}, upsert=False)

print('ok')