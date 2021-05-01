
'''
Author:
mailto:
Name Classs:
Description:
Dependences:
'''

from sklearn.ensemble import RandomForestClassifier
from supervised_learning_analysis import responseTraining

class RandomForest(object):
    def __init__(self, dataset,target,n_estimators,criterion, min_samples_split, min_samples_leaf, bootstrap, validation):
        self.dataset=dataset
        self.target=target
        self.n_estimators=n_estimators
        self.criterion=criterion
        self.min_samples_split = min_samples_split
        self.min_samples_leaf = min_samples_leaf
        self.bootstrap = bootstrap
        self.validation=validation

    def trainingMethod(self, kindDataSet):
        self.model=RandomForestClassifier(n_estimators=self.n_estimators,criterion=self.criterion, min_samples_leaf=self.min_samples_leaf, min_samples_split=self.min_samples_split, bootstrap=self.bootstrap, n_jobs=-1)
        self.RandomForestAlgorithm=self.model.fit(self.dataset,self.target)

        params = "criterion:%s-n_estimators:%d-min_samples_leaf:%d-min_samples_split:%d-bootstrap:%s" % (self.criterion ,self.n_estimators, self.min_samples_leaf, self.min_samples_split, self.bootstrap)
        self.performanceData = responseTraining.responseTraining(self.RandomForestAlgorithm, 'RandomForest', params, self.validation)

        if kindDataSet == 1:
            self.performanceData.estimatedMetricsPerformance(self.dataset, self.target)
        else:
            self.performanceData.estimatedMetricsPerformanceMultilabels(self.dataset, self.target)
