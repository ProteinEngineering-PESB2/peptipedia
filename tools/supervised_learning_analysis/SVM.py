
'''
Author:
mailto:
Name Classs:
Description:
Dependences:
'''

#modules import
from sklearn import svm
from supervised_learning_analysis import responseTraining

class SVM(object):

    #building
    def __init__(self,dataset, target, kernel, C_value, degree, gamma, validation):

        #init attributes values...
        self.dataset=dataset
        self.target=target
        self.kernel=kernel
        self.validation=validation
        self.C_value = C_value
        self.degree = degree
        self.gamma = gamma

    #instance training...
    def trainingMethod(self, kindDataSet):

        self.model=svm.SVC(kernel=self.kernel, degree=self.degree, gamma=self.gamma, C=self.C_value, probability=True)
        self.SVMAlgorithm =self.model.fit(self.dataset,self.target)

        params = "kernel:%s-C:%f-degree:%f-gamma:%f" % (self.kernel, self.C_value, self.degree, self.gamma)
        self.performanceData = responseTraining.responseTraining(self.SVMAlgorithm, 'SVM', params, self.validation)

        if kindDataSet == 1:
            self.performanceData.estimatedMetricsPerformance(self.dataset, self.target)
        else:
            self.performanceData.estimatedMetricsPerformanceMultilabels(self.dataset, self.target)
