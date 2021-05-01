'''
clase que permite representar una respuesta de un algoritmo de entrenamiento con respecto a sus parametros
'''

from sklearn.model_selection import cross_validate, cross_val_predict, cross_val_score
from sklearn.metrics import accuracy_score, cohen_kappa_score, f1_score, precision_score, recall_score, fbeta_score, make_scorer
from sklearn.model_selection import LeaveOneOut
from sklearn.metrics import accuracy_score, average_precision_score
from sklearn.metrics import make_scorer

import numpy as np

class responseTraining(object):

    def __init__(self, clf, algorithm, params, validation):

        self.clf = clf
        self.ListScore = ['accuracy', 'recall', 'precision', 'f1']
        self.ftwo_scorer = make_scorer(fbeta_score, beta=2)

        self.algorithm = algorithm
        self.params = params
        if validation == -1:
            self.validation = LeaveOneOut()
            self.validationName = "LeaveOneOut"
        else:
            self.validation = validation
            self.validationName = str(validation)

    #metodo que permite obtener las medidas de desempeno en el caso de que sean multiples clases
    def estimatedMetricsPerformanceMultilabels(self, dataInput, dataClass):

        accuracyResponse = cross_val_score(self.clf, dataInput, dataClass, cv=self.validation, scoring='accuracy')
        accuracyValue = np.mean(accuracyResponse)

        f1_weightedResponse = cross_val_score(self.clf, dataInput, dataClass, cv=self.validation, scoring='f1_weighted')
        f1_weighted = np.mean(f1_weightedResponse)

        recall_weightedResponse = cross_val_score(self.clf, dataInput, dataClass, cv=self.validation, scoring='recall_weighted')
        recall_weighted = np.mean(recall_weightedResponse)

        precision_weightedResponse = cross_val_score(self.clf, dataInput, dataClass, cv=self.validation, scoring='precision_weighted')
        precision_weighted = np.mean(precision_weightedResponse)

        self.scoreData = []
        #descriptores method
        self.scoreData.append(self.algorithm)
        self.scoreData.append(self.params)
        self.scoreData.append(self.validationName)

        self.scoreData.append(accuracyValue)
        self.scoreData.append(recall_weighted)
        self.scoreData.append(precision_weighted)
        self.scoreData.append(f1_weighted)

    #funcion que permite estimar las metricas de control para el modelo generado... con validacion CV=10
    def estimatedMetricsPerformance(self, dataInput, dataClass):

        self.scoreData = []
        #descriptores method
        self.scoreData.append(self.algorithm)
        self.scoreData.append(self.params)
        self.scoreData.append(self.validation)

        for element in self.ListScore:
            scores = cross_val_score(self.clf, dataInput, dataClass, cv=self.validation, scoring=element)
            meanScore = np.mean(scores)
            self.scoreData.append(meanScore)

        self.scoreData.append(meanScore)
