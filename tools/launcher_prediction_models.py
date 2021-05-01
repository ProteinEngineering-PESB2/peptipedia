import pandas as pd
from supervised_learning_prediction import execModelPrediction

class launcher_prediction(object):
	
	def __init__(self, dataset, response, algorithm, path_response):
		self.dataset = dataset
		self.response = response
		self.algorithm = algorithm
		self.path_response = path_response	
	
	def apply_algorithm(self):

		exec_process = execModelPrediction.execAlgorithm(self.dataset, self.response, self.path_response, self.algorithm)
		exec_process.execAlgorithmByOptions()


