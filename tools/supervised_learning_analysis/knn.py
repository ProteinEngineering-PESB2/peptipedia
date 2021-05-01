
'''
Author:
mailto:
Name Classs:
Description:
Dependences:
'''

#modules import
from sklearn.neighbors import KNeighborsClassifier
from supervised_learning_analysis import responseTraining

class knn(object):

    #building class...
    def __init__(self, dataset, response, n_neighbors, algorithm, metric,  weights, validation):

        #init attributes values...
        self.dataset = dataset
        self.response = response
        self.n_neighbors = n_neighbors
        self.algorithm = algorithm
        self.metric = metric
        self.weights = weights
        self.validation = validation

    #instance training...
    def trainingMethod(self, kindDataSet):

        self.model = KNeighborsClassifier(n_neighbors=self.n_neighbors, weights=self.weights, algorithm=self.algorithm, metric=self.metric, n_jobs=-1)#instancia
        self.knnAlgorithm = self.model.fit(self.dataset, self.response)

        #training...
        params = "algorithm:%s-metric:%s-neighbors:%d-weights:%s" % (self.algorithm, self.metric, self.n_neighbors, self.weights)
        self.performanceData = responseTraining.responseTraining(self.knnAlgorithm, 'KNN', params, self.validation)

        if kindDataSet == 1:
            self.performanceData.estimatedMetricsPerformance(self.dataset, self.response)
        else:
            self.performanceData.estimatedMetricsPerformanceMultilabels(self.dataset, self.response)
