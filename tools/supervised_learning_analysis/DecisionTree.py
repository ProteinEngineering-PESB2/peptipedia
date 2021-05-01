
'''
Author:
mailto:
Name Classs:
Description:
Dependences:
'''

from sklearn import tree
from supervised_learning_analysis import responseTraining

class DecisionTree(object):

    def __init__ (self, dataset, target, criterion, splitter,validation):
        self.dataset=dataset
        self.target=target
        self.criterion=criterion
        self.splitter=splitter
        self.validation=validation

    def trainingMethod(self, kindDataSet):
        self.model=tree.DecisionTreeClassifier(criterion=self.criterion,splitter=self.splitter)
        self.DecisionTreeAlgorithm=self.model.fit(self.dataset,self.target)

        if kindDataSet == 1:
            params = "criterion:%s-splitter:%s" % (self.criterion,self.splitter)
            self.performanceData = responseTraining.responseTraining(self.DecisionTreeAlgorithm, 'DecisionTree', params, self.validation)
            self.performanceData.estimatedMetricsPerformance(self.dataset, self.target)

        else:
            params = "criterion:%s-splitter:%s" % (self.criterion,self.splitter)
            self.performanceData = responseTraining.responseTraining(self.DecisionTreeAlgorithm, 'DecisionTree', params, self.validation)
            self.performanceData.estimatedMetricsPerformanceMultilabels(self.dataset, self.target)
