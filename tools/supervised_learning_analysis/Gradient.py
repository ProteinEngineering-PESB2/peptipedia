
'''
Author:
mailto:
Name Classs:
Description:
Dependences:
'''

from sklearn.ensemble import GradientBoostingClassifier
from supervised_learning_analysis import responseTraining

class Gradient(object):

    def __init__ (self,dataset,target,n_estimators, loss, min_samples_split, min_samples_leaf, validation):
        self.dataset=dataset
        self.target=target
        self.n_estimators=n_estimators
        self.loss = loss
        self.min_samples_leaf = min_samples_leaf
        self.min_samples_split = min_samples_split
        self.validation=validation

    def trainingMethod(self, kindDataSet):

        self.model= GradientBoostingClassifier(n_estimators=self.n_estimators)
        self.GradientAlgorithm= self.model.fit(self.dataset,self.target)

        params = "n_estimators:%d-loss:%s-min_samples_leaf:%d-min_samples_split:%d" % (self.n_estimators, self.loss, self.min_samples_leaf, self.min_samples_split)
        self.performanceData = responseTraining.responseTraining(self.GradientAlgorithm, 'Gradient', params, self.validation)

        if kindDataSet == 1:
            self.performanceData.estimatedMetricsPerformance(self.dataset, self.target)
        else:
            self.performanceData.estimatedMetricsPerformanceMultilabels(self.dataset, self.target)
