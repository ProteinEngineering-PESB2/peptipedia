
'''
Author:
mailto:
Name Classs:
Description:
Dependences:
'''

from sklearn.ensemble import BaggingClassifier
from supervised_learning_analysis import responseTraining

class Baggin(object):

    def __init__ (self,dataset,target,n_estimators, bootstrap, validation):
        self.dataset=dataset
        self.target=target
        self.n_estimators=n_estimators
        self.bootstrap = bootstrap
        self.validation=validation

    def trainingMethod(self, kindDataSet):

        self.model= BaggingClassifier(n_estimators=self.n_estimators, bootstrap=self.bootstrap, n_jobs=-1)
        self.BagginAlgorithm= self.model.fit(self.dataset,self.target)

        if kindDataSet ==1:#binary
            params = "n_estimators:%d-bootstrap:%s" % (self.n_estimators, self.bootstrap)
            self.performanceData = responseTraining.responseTraining(self.BagginAlgorithm, 'Baggin', params, self.validation)
            self.performanceData.estimatedMetricsPerformance(self.dataset, self.target)
        else:
            params = "n_estimators:%d-bootstrap:%s" % (self.n_estimators, self.bootstrap)
            self.performanceData = responseTraining.responseTraining(self.BagginAlgorithm, 'Baggin', params, self.validation)
            self.performanceData.estimatedMetricsPerformanceMultilabels(self.dataset, self.target)
            
