'''
script que permite implementar support vector machine para regresiones o predicciones de valores
a partir de set de datos de interes.
'''


'''
Author:
mailto:
Name Classs:
Description:
Dependences:
'''

#modules import
from sklearn.svm import SVR

class SVRModel(object):

    #building
    def __init__(self,dataset, response, kernel, degree, gamma):

        #init attributes values...
        self.dataset=dataset
        self.response=response
        self.kernel=kernel
        self.degree = degree
        self.gamma = gamma

    #instance training...
    def trainingMethod(self):

        self.model=SVR(kernel=self.kernel, degree=self.degree, gamma=self.gamma)
        self.SVRAlgorithm =self.model.fit(self.dataset,self.response)
        self.predicctions = self.SVRAlgorithm.predict(self.dataset)
        self.r_score = self.SVRAlgorithm.score(self.dataset, self.response)
        
