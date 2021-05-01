'''
script que recibe un modelo y permite crear la curva roc del modelo con respecto al numero de validaciones
generado
'''

import matplotlib
matplotlib.use('Agg')
import numpy as np
from scipy import interp
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import train_test_split
from sklearn.model_selection import learning_curve
from sklearn.model_selection import ShuffleSplit

class curveLearning(object):

    def __init__(self, dataSet, target, modelData, cv_values, path):

        self.dataSet = dataSet
        self.target = target
        self.modelData = modelData
        self.cv_values = cv_values        
        self.path = path        
        self.pathResponse = self.path+"curveLearning.svg"

    def createLearningCurve(self):

        X = np.array(self.dataSet)
        y = np.array(self.target)

        # Cross validation with 100 iterations to get smoother mean test and train
        # score curves, each time with 20% data randomly selected as a validation set.
        cv = ShuffleSplit(n_splits=100, test_size=self.cv_values/100, random_state=0)
        self.plot_learning_curve(self.modelData, 'Learning Curve', X, y, self.cv_values, ylim=(0.01, 1.01), n_jobs=4)

        plt.savefig(self.pathResponse)

    #funcion que permite crear la curva ROC y exportar la imagen segun corresponda
    def plot_learning_curve(self, estimator, title, X, y, cv, ylim=None, n_jobs=1, train_sizes=np.linspace(.1, 1.0, 5)):

        plt.figure()
        plt.title(title)
        if ylim is not None:
            plt.ylim(*ylim)
        plt.xlabel("Training examples")
        plt.ylabel("Score")
        train_sizes, train_scores, test_scores = learning_curve(estimator, X, y, cv=cv, n_jobs=n_jobs, train_sizes=train_sizes)

        train_scores_mean = np.mean(train_scores, axis=1)
        train_scores_std = np.std(train_scores, axis=1)
        test_scores_mean = np.mean(test_scores, axis=1)
        test_scores_std = np.std(test_scores, axis=1)
        plt.grid()

        plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                         train_scores_mean + train_scores_std, alpha=0.1,
                         color="r")
        plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                         test_scores_mean + test_scores_std, alpha=0.1, color="g")
        plt.plot(train_sizes, train_scores_mean, 'o-', color="r",
                 label="Training score")
        plt.plot(train_sizes, test_scores_mean, 'o-', color="g",
                 label="Cross-validation score")

        plt.legend(loc="best")
        return plt
