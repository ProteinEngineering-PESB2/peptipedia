
'''
Author:
mailto:
Name Classs:
Description:
Dependences:
'''

from sklearn.neural_network import MLPRegressor

class MLP(object):

    def __init__ (self,dataset,response,activation, solver, learning_rate, hidden_layer_sizes_a,hidden_layer_sizes_b,hidden_layer_sizes_c, alpha, max_iter, shuffle):
        self.dataset=dataset
        self.response=response
        self.activation=activation
        self.solver=solver
        self.learning_rate=learning_rate
        self.hidden_layer_sizes=[hidden_layer_sizes_a,hidden_layer_sizes_b,hidden_layer_sizes_c]
        self.alpha = alpha
        self.max_iter = max_iter
        self.shuffle = shuffle

    def trainingMethod(self):

        self.model=MLPRegressor(hidden_layer_sizes=self.hidden_layer_sizes,activation=self.activation,solver=self.solver,learning_rate=self.learning_rate)
        self.MLPModel=self.model.fit(self.dataset,self.response)
        self.predicctions = self.MLPModel.predict(self.dataset)
        self.r_score = self.MLPModel.score(self.dataset, self.response)
