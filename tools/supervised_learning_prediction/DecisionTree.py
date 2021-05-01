
'''
Author:
mailto:
Name Classs:
Description:
Dependences:
'''

from sklearn import tree

class DecisionTree(object):

    def __init__ (self, dataset, response, criterion, splitter):
        self.dataset=dataset
        self.response=response
        self.criterion=criterion
        self.splitter=splitter

    def trainingMethod(self):
        self.model=tree.DecisionTreeRegressor(criterion=self.criterion,splitter=self.splitter)
        self.DecisionTreeAlgorithm=self.model.fit(self.dataset,self.response)
        self.predicctions = self.DecisionTreeAlgorithm.predict(self.dataset)
        self.r_score = self.DecisionTreeAlgorithm.score(self.dataset, self.response)
