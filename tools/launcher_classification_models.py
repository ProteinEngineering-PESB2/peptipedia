import pandas as pd
from supervised_learning_analysis import execAlgorithm

class launcher_classification(object):
	
	def __init__(self, dataset, response, algorithm, path_response):
		self.dataset = dataset
		self.response = response
		self.algorithm = algorithm
		self.path_response = path_response

	def define_k_value(self):

		if len(self.dataset)>250:
			self.k_value = 10
		elif len(self.dataset)<=250 and len(self.dataset)>=150:
			self.k_value = 5
		else:
			self.k_value = 3
	
	def apply_algorithm(self):

		self.define_k_value()

		exec_process = execAlgorithm.execAlgorithm(self.dataset, self.response, self.path_response, self.algorithm, self.k_value)
		exec_process.execAlgorithmByOptions()


