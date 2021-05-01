
'''
Author:
mailto:
Name Classs:
Description:
Dependences:
'''

from sklearn.neural_network import MLPClassifier
from supervised_learning_analysis import responseTraining

class MLP(object):

    def __init__ (self,dataset,target,activation, solver, learning_rate, hidden_layer_sizes_a,hidden_layer_sizes_b,hidden_layer_sizes_c, alpha, max_iter, shuffle, validation):
        self.dataset=dataset
        self.target=target
        self.activation=activation
        self.solver=solver
        self.learning_rate=learning_rate
        self.hidden_layer_sizes=[hidden_layer_sizes_a,hidden_layer_sizes_b,hidden_layer_sizes_c]
        self.alpha = alpha
        self.max_iter = max_iter
        self.shuffle = shuffle
        self.validation=validation

    def trainingMethod(self, kindDataSet):

        self.model=MLPClassifier(hidden_layer_sizes=self.hidden_layer_sizes,activation=self.activation,solver=self.solver,learning_rate=self.learning_rate)
        self.MLPAlgorithm=self.model.fit(self.dataset,self.target)

        params = "activation:%s-learning_rate:%s-solver:%s-hidden_layer_sizes_a:%d-hidden_layer_sizes_b:%d-hidden_layer_sizes_c:%d-alpha:%f-max_iter:%d-shuffle:%s" % (self.activation, self.learning_rate, self.solver,self.hidden_layer_sizes[0], self.hidden_layer_sizes[1], self.hidden_layer_sizes[2], self.alpha, self.max_iter, self.shuffle)
        self.performanceData = responseTraining.responseTraining(self.MLPAlgorithm, 'MLP', params, self.validation)

        if kindDataSet == 1:
            self.performanceData.estimatedMetricsPerformance(self.dataset, self.target)
        else:
            self.performanceData.estimatedMetricsPerformanceMultilabels(self.dataset, self.target)
