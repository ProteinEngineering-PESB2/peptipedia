
'''
Author:
mailto:
Name Classs:
Description:
Dependences:
'''

from sklearn.ensemble import AdaBoostClassifier
from supervised_learning_analysis import responseTraining

class AdaBoost(object):

    def __init__ (self, dataset, target, n_estimators, algorithm,validation):
        self.dataset=dataset
        self.target=target
        self.n_estimators=n_estimators
        self.algorithm=algorithm
        self.validation=validation

    def trainingMethod(self, kindDataSet):

        self.model= AdaBoostClassifier(n_estimators=self.n_estimators,algorithm=self.algorithm)
        self.AdaBoostAlgorithm= self.model.fit(self.dataset,self.target)

        if kindDataSet ==1:#binary
            params = "algorithm:%s-n_estimators:%d" % (self.algorithm, self.n_estimators)
            self.performanceData = responseTraining.responseTraining(self.AdaBoostAlgorithm, 'AdaBoost', params, self.validation)
            self.performanceData.estimatedMetricsPerformance(self.dataset, self.target)
        else:
            params = "algorithm:%s-n_estimators:%d" % (self.algorithm, self.n_estimators)
            self.performanceData = responseTraining.responseTraining(self.AdaBoostAlgorithm, 'AdaBoost', params, self.validation)
            self.performanceData.estimatedMetricsPerformanceMultilabels(self.dataset, self.target)
            
