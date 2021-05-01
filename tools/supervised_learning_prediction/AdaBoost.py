
'''
Author:
mailto:
Name Classs:
Description:
Dependences:
'''

from sklearn.ensemble import AdaBoostRegressor

class AdaBoost(object):

    def __init__ (self, dataset, response, n_estimators, loss):
        self.dataset=dataset
        self.response=response
        self.n_estimators=n_estimators
        self.loss=loss

    def trainingMethod(self):
         self.model= AdaBoostRegressor(n_estimators=self.n_estimators,loss=self.loss)
         self.AdaBoostModel=self.model.fit(self.dataset,self.response)
         self.predicctions = self.AdaBoostModel.predict(self.dataset)
         self.r_score = self.AdaBoostModel.score(self.dataset, self.response)
