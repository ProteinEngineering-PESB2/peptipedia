
'''
Author:
mailto:
Name Classs:
Description:
Dependences:
'''

from sklearn.naive_bayes import GaussianNB
from supervised_learning_analysis import responseTraining

class Gaussian(object):

    def __init__(self,dataset,target,validation):
        self.dataset=dataset
        self.target=target
        self.validation=validation

    def trainingMethod(self, kindDataSet):

        self.model=GaussianNB()
        self.GaussianNBAlgorithm=self.model.fit(self.dataset,self.target)

        if kindDataSet == 1:
            params = 'Params:default'
            self.performanceData = responseTraining.responseTraining(self.GaussianNBAlgorithm, 'GaussianNB', params, self.validation)
            self.performanceData.estimatedMetricsPerformance(self.dataset, self.target)
        else:
            params = 'Params:default'
            self.performanceData = responseTraining.responseTraining(self.GaussianNBAlgorithm, 'GaussianNB', params, self.validation)
            self.performanceData.estimatedMetricsPerformanceMultilabels(self.dataset, self.target)
