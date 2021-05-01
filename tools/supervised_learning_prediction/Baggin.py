
'''
Author:
mailto:
Name Classs:
Description:
Dependences:
'''

from sklearn.ensemble import BaggingRegressor

class Baggin(object):

    def __init__ (self,dataset,response,n_estimators, bootstrap):
        self.dataset=dataset
        self.response=response
        self.n_estimators=n_estimators
        self.bootstrap = bootstrap

    def trainingMethod(self):
        self.model= BaggingRegressor(n_estimators=self.n_estimators, bootstrap=self.bootstrap, n_jobs=-1)
        self.bagginModel=self.model.fit(self.dataset,self.response)
        self.predicctions = self.bagginModel.predict(self.dataset)
        self.r_score = self.bagginModel.score(self.dataset, self.response)
