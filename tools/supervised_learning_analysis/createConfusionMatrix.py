'''
script que permite crear una matriz de confusion dado un modelo
'''

import matplotlib
matplotlib.use('Agg')
import numpy as np
from sklearn.model_selection import LeaveOneOut
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_validate
from sklearn.metrics import confusion_matrix
import itertools
import pandas as pd
import json

class confusionMatrix(object):

    def __init__(self, dataSet, target, modelData, cv_values, classList):

        self.dataSet = dataSet
        self.target = target
        self.modelData = modelData        
        self.classList = classList
        self.cv_values = cv_values

    #metodo que permite exportar la matriz a un csv y adiciona las filas y columnas correspondientes a fiabilidad y bakanosidad
    def exportConfusionMatrix(self, matrix):
        
        #calculamos la bakanosidad del modelo (en base a los valores de la primera columna)
        bakanosidad = []
        for i in range(len(matrix)):
            sumRow = sum(matrix[i])
            value = (matrix[i][i]/float(sumRow))*100
            bakanosidad.append(value)

        #calculamos la fiabilidad del modelo...
        transpose = matrix.transpose()
        fiabilidad = []
        for i in range(len(transpose)):
            sumRow = sum(transpose[i])
            value = (transpose[i][i]/float(sumRow))*100
            fiabilidad.append(value)


        header = list(set(self.target))
        header = [str(value) for value in header]

        matrixData = []
        for element in matrix:#obtenemos las columnas
            rowSum = sum(element)
            row = []
            for value in element:
                dataInValue = value
                row.append(str(dataInValue))
            matrixData.append(row)
        dictResponse = {"sensitivity": fiabilidad, "specificity":bakanosidad, "matrix":matrixData, "header": header}

        return dictResponse

    #metodo que permite generar la matriz de confusion...
    def createConfusionMatrix(self):

        self.predictions = cross_val_predict(self.modelData, self.dataSet, self.target, cv=self.cv_values)
        matrix = confusion_matrix(self.target, self.predictions)
        dictResponse = self.exportConfusionMatrix(matrix)
        return dictResponse
