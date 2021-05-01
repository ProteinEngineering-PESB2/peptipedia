import sys
from modlamp.descriptors import PeptideDescriptor, GlobalDescriptor
import json
from modlamp.plot import plot_profile, helical_wheel
from Bio import SeqIO
import os

def exec(peptide, time_node):
	file = open("../src/public/jobs/service1/service1.fasta", "w") 
	file.write(peptide)
	file.close()
	fasta = SeqIO.parse("../src/public/jobs/service1/service1.fasta", "fasta")
	if(any(fasta) == False): #False when `fasta` is empty
		return "error"
	cantidad = 0
	for record in SeqIO.parse("../src/public/jobs/service1/service1.fasta", "fasta"):
		cantidad = cantidad+1
	if (cantidad == 1):
		properties = {}
		for record in SeqIO.parse("../src/public/jobs/service1/service1.fasta", "fasta"):
			properties[str(record.id)] = {}
			#save properties

			properties[str(record.id)]["length"] = len(record.seq)

			#formula
			try:
				desc = GlobalDescriptor(str(record.seq))
				desc.formula(amide=True)
				properties[str(record.id)]["formula"] = desc.descriptor[0][0]
			except:
				properties[str(record.id)]["formula"] = "-"

			#molecular weigth
			try:
				desc = GlobalDescriptor(str(record.seq))
				desc.calculate_MW(amide=True)
				properties[str(record.id)]["molecular_weigth"] = float("%.4f" % desc.descriptor[0][0])
			except:
				properties[str(record.id)]["molecular_weigth"] = "-"

			#boman_index
			try:
				desc = GlobalDescriptor(str(record.seq))
				desc.boman_index()
				properties[str(record.id)]["boman_index"] = float("%.4f" % desc.descriptor[0][0])				
			except:
				properties[str(record.id)]["boman_index"] = "-"

			#charge
			try:
				desc = GlobalDescriptor(str(record.seq))
				desc.calculate_charge(ph=7, amide=True)
				properties[str(record.id)]["charge"] = float("%.4f" % desc.descriptor[0][0])
			except:
				properties[str(record.id)]["charge"] = "-"
				

			#charge density
			try:
				desc = GlobalDescriptor(str(record.seq))
				desc.charge_density(ph=7, amide=True)
				properties[str(record.id)]["charge_density"] = float("%.4f" % desc.descriptor[0][0])
			except:
				properties[str(record.id)]["charge_density"] = "-"

			#estimate isoelectric point
			try:
				desc = GlobalDescriptor(str(record.seq))
				desc.isoelectric_point()
				properties[str(record.id)]["isoelectric_point"] = float("%.4f" % desc.descriptor[0][0])
			except:
				properties[str(record.id)]["isoelectric_point"] = "-"

			#estimate inestability index
			try:
				desc = GlobalDescriptor(str(record.seq))
				desc.instability_index()
				properties[str(record.id)]["instability_index"] = float("%.4f" % desc.descriptor[0][0])
			except:
				properties[str(record.id)]["instability_index"] = "-"

			#estimate aromaticity
			try:
				desc = GlobalDescriptor(str(record.seq))
				desc.aromaticity()
				properties[str(record.id)]["aromaticity"] = float("%.4f" % desc.descriptor[0][0])
			except:
				properties[str(record.id)]["aromaticity"] = "-"

			#estimate aliphatic_index
			try:
				desc = GlobalDescriptor(str(record.seq))
				desc.aliphatic_index()
				properties[str(record.id)]["aliphatic_index"] = float("%.4f" % desc.descriptor[0][0])
			except:
				properties[str(record.id)]["aliphatic_index"] = "-"

			#estimate hydrophobic_ratio
			try:
				desc = GlobalDescriptor(str(record.seq))
				desc.hydrophobic_ratio()
				properties[str(record.id)]["hydrophobic_ratio"] = float("%.4f" % desc.descriptor[0][0])	
			except:
				properties[str(record.id)]["hydrophobic_ratio"] = "-"

			#profile hydrophobicity
			try:
				desc = PeptideDescriptor(str(record.seq), scalename='Eisenberg')
				desc.calculate_profile(prof_type='H')
				properties[str(record.id)]["hydrophobicity_profile"] = float("%.4f" % desc.descriptor[0][0])
			except:
				properties[str(record.id)]["hydrophobicity_profile"] = "-"

			#profile hydrophobic
			try:
				desc = PeptideDescriptor(str(record.seq), scalename='Eisenberg')
				desc.calculate_profile(prof_type='uH')
				properties[str(record.id)]["hydrophobic_profile"] = float("%.4f" % desc.descriptor[0][0])
			except:
				properties[str(record.id)]["hydrophobic_profile"] = "-"

			#moment
			try:
				desc = PeptideDescriptor(str(record.seq), scalename='Eisenberg')
				desc.calculate_moment()
				properties[str(record.id)]["calculate_moment"] = float("%.4f" % desc.descriptor[0][0])
			except:
				properties[str(record.id)]["calculate_moment"] = "-"

			try:
				os.mkdir("../src/public/jobs/service1/"+time_node)
			except:
				print("Error")
			
			#generate plot profile
			plot_profile(str(record.seq), scalename='eisenberg', filename= "../src/public/jobs/service1/"+time_node+"/profile.png")

			#generate helical wheel
			helical_wheel(str(record.seq), colorcoding='charge', lineweights=False, filename= "../src/public/jobs/service1/"+time_node+"/helical.png")
			
			return(properties)
	
	if (cantidad > 1):
		properties = {}
		for record in SeqIO.parse("../src/public/jobs/service1/service1.fasta", "fasta"):
			properties[str(record.id)] = {}

			properties[str(record.id)]["length"] = len(record.seq)
			
			#formula
			try:
				desc = GlobalDescriptor(str(record.seq))
				desc.formula(amide=True)
				properties[str(record.id)]["formula"] = desc.descriptor[0][0]
			except:
				properties[str(record.id)]["formula"] = "-"

			#molecular weigth
			try:
				desc = GlobalDescriptor(str(record.seq))
				desc.calculate_MW(amide=True)
				properties[str(record.id)]["molecular_weigth"] = float("%.4f" % desc.descriptor[0][0])
			except:
				properties[str(record.id)]["molecular_weigth"] = "-"

			#boman_index
			try:
				desc = GlobalDescriptor(str(record.seq))
				desc.boman_index()
				properties[str(record.id)]["boman_index"] = float("%.4f" % desc.descriptor[0][0])				
			except:
				properties[str(record.id)]["boman_index"] = "-"

			#charge
			try:
				desc = GlobalDescriptor(str(record.seq))
				desc.calculate_charge(ph=7, amide=True)
				properties[str(record.id)]["charge"] = float("%.4f" % desc.descriptor[0][0])
			except:
				properties[str(record.id)]["charge"] = "-"
				

			#charge density
			try:
				desc = GlobalDescriptor(str(record.seq))
				desc.charge_density(ph=7, amide=True)
				properties[str(record.id)]["charge_density"] = float("%.4f" % desc.descriptor[0][0])
			except:
				properties[str(record.id)]["charge_density"] = "-"

			#estimate isoelectric point
			try:
				desc = GlobalDescriptor(str(record.seq))
				desc.isoelectric_point()
				properties[str(record.id)]["isoelectric_point"] = float("%.4f" % desc.descriptor[0][0])
			except:
				properties[str(record.id)]["isoelectric_point"] = "-"

			#estimate inestability index
			try:
				desc = GlobalDescriptor(str(record.seq))
				desc.instability_index()
				properties[str(record.id)]["instability_index"] = float("%.4f" % desc.descriptor[0][0])
			except:
				properties[str(record.id)]["instability_index"] = "-"

			#estimate aromaticity
			try:
				desc = GlobalDescriptor(str(record.seq))
				desc.aromaticity()
				properties[str(record.id)]["aromaticity"] = float("%.4f" % desc.descriptor[0][0])
			except:
				properties[str(record.id)]["aromaticity"] = "-"

			#estimate aliphatic_index
			try:
				desc = GlobalDescriptor(str(record.seq))
				desc.aliphatic_index()
				properties[str(record.id)]["aliphatic_index"] = float("%.4f" % desc.descriptor[0][0])
			except:
				properties[str(record.id)]["aliphatic_index"] = "-"

			#estimate hydrophobic_ratio
			try:
				desc = GlobalDescriptor(str(record.seq))
				desc.hydrophobic_ratio()
				properties[str(record.id)]["hydrophobic_ratio"] = float("%.4f" % desc.descriptor[0][0])	
			except:
				properties[str(record.id)]["hydrophobic_ratio"] = "-"

			#profile hydrophobicity
			try:
				desc = PeptideDescriptor(str(record.seq), scalename='Eisenberg')
				desc.calculate_profile(prof_type='H')
				properties[str(record.id)]["hydrophobicity_profile"] = float("%.4f" % desc.descriptor[0][0])
			except:
				properties[str(record.id)]["hydrophobicity_profile"] = "-"

			#profile hydrophobic
			try:
				desc = PeptideDescriptor(str(record.seq), scalename='Eisenberg')
				desc.calculate_profile(prof_type='uH')
				properties[str(record.id)]["hydrophobic_profile"] = float("%.4f" % desc.descriptor[0][0])
			except:
				properties[str(record.id)]["hydrophobic_profile"] = "-"

			#moment
			try:
				desc = PeptideDescriptor(str(record.seq), scalename='Eisenberg')
				desc.calculate_moment()
				properties[str(record.id)]["calculate_moment"] = float("%.4f" % desc.descriptor[0][0])
			except:
				properties[str(record.id)]["calculate_moment"] = "-"

		return(properties)
