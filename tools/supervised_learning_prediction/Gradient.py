
'''
Author:
mailto:
Name Classs:
Description:
Dependences:
'''

from sklearn.ensemble import GradientBoostingRegressor

class Gradient(object):

    def __init__ (self,dataset,response,n_estimators, loss, criterion, min_samples_split, min_samples_leaf):
        self.dataset=dataset
        self.response=response
        self.n_estimators=n_estimators
        self.loss = loss
        self.criterion = criterion
        self.min_samples_leaf = min_samples_leaf
        self.min_samples_split = min_samples_split

    def trainingMethod(self):

        self.model= GradientBoostingRegressor(n_estimators=self.n_estimators, loss=self.loss, criterion=self.criterion, min_samples_leaf=self.min_samples_leaf, min_samples_split=self.min_samples_split)
        self.GradientAlgorithm= self.model.fit(self.dataset,self.response)
        self.predicctions = self.GradientAlgorithm.predict(self.dataset)
        self.r_score = self.GradientAlgorithm.score(self.dataset, self.response)
