
'''
Author:
mailto:
Name Classs:
Description:
Dependences:
'''

from sklearn.naive_bayes import BernoulliNB
from supervised_learning_analysis import responseTraining

class Bernoulli (object):

    def __init__(self,dataset,target,validation):
        self.dataset=dataset
        self.target=target
        self.validation=validation

    def trainingMethod(self, kindDataSet):
        self.model=BernoulliNB()
        self.BernoulliNBAlgorithm=self.model.fit(self.dataset,self.target)

        if kindDataSet ==1:#binary
            params = "Param:Default"
            self.performanceData = responseTraining.responseTraining(self.BernoulliNBAlgorithm, 'BernoulliNB', params, self.validation)
            self.performanceData.estimatedMetricsPerformance(self.dataset, self.target)
        else:
            params = "Param:Default"
            self.performanceData = responseTraining.responseTraining(self.BernoulliNBAlgorithm, 'BernoulliNB', params, self.validation)
            self.performanceData.estimatedMetricsPerformanceMultilabels(self.dataset, self.target)
