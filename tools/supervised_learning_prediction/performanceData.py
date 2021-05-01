'''
clase con la responsabilidad de calcular distintas medidas de desempeno asociadas a la respuesta generada
'''

from scipy.stats import pearsonr
from scipy.stats import spearmanr
from scipy.stats import kendalltau
import math

class performancePrediction(object):

    def __init__(self, realValues, predictValues):

        self.realValues = realValues
        self.predictValues = predictValues

    #metodo que permite calcular el coeficiente de pearson...
    def calculatedPearson(self):

        response = pearsonr(self.realValues, self.predictValues)
        if math.isnan(response[0]):
            r1 = 'ERROR'
        else:
            r1 = response[0]

        if math.isnan(response[1]):
            r2 = 'ERROR'
        else:
            r2 = response[1]

        dictResponse = {"pearsonr": r1, "pvalue": r2}
        return dictResponse

    #metodo que permite calcular el coeficiente de spearman...
    def calculatedSpearman(self):

        response = spearmanr(self.realValues, self.predictValues)

        if math.isnan(response[0]):
            r1 = 'ERROR'
        else:
            r1 = response[0]

        if math.isnan(response[1]):
            r2 = 'ERROR'
        else:
            r2 = response[1]

        dictResponse = {"spearmanr": r1, "pvalue": r2}
        return dictResponse

    #metodo que permite calcular el kendalltau...
    def calculatekendalltau(self):

        response = kendalltau(self.realValues, self.predictValues)

        if math.isnan(response[0]):
            r1 = 'ERROR'
        else:
            r1 = response[0]

        if math.isnan(response[1]):
            r2 = 'ERROR'
        else:
            r2 = response[1]

        dictResponse = {"kendalltau": r1, "pvalue": r2}
        return dictResponse
