
'''
Author:
mailto:
Name Classs:
Description:
Dependences:
'''

from sklearn.ensemble import RandomForestRegressor

class RandomForest(object):
    def __init__(self, dataset,response,n_estimators,criterion, min_samples_split, min_samples_leaf, bootstrap):
        self.dataset=dataset
        self.response=response
        self.n_estimators=n_estimators
        self.criterion=criterion
        self.min_samples_split = min_samples_split
        self.min_samples_leaf = min_samples_leaf
        self.bootstrap = bootstrap

    def trainingMethod(self):
        self.model=RandomForestRegressor(n_estimators=self.n_estimators,criterion=self.criterion, min_samples_leaf=self.min_samples_leaf, min_samples_split=self.min_samples_split, bootstrap=self.bootstrap, n_jobs=-1)
        self.randomForesModel=self.model.fit(self.dataset,self.response)
        self.predicctions = self.randomForesModel.predict(self.dataset)
        self.r_score = self.randomForesModel.score(self.dataset, self.response)
