
'''
Author:
mailto:
Name Classs:
Description:
Dependences:
'''

#modules import
from sklearn.svm import NuSVC
from supervised_learning_analysis import responseTraining

class NuSVM(object):

    #building
    def __init__ (self,dataset,target,kernel, nu, degree, gamma, validation):

        self.dataset=dataset
        self.target=target
        self.kernel=kernel
        self.validation=validation
        self.nu = nu
        self.degree = degree
        self.gamma = gamma

    def trainingMethod(self, kindDataSet):

        self.model=NuSVC(kernel=self.kernel, degree=self.degree, gamma=self.gamma, nu=self.nu, probability=True)
        self.NuSVMAlgorithm=self.model.fit(self.dataset,self.target)

        params = "kernel:%s-degree:%f-gamma:%f-nu:%f-probability:True" % (self.kernel, self.degree, self.gamma, self.nu)
        self.performanceData = responseTraining.responseTraining(self.NuSVMAlgorithm, 'NuSVM', params, self.validation)

        if kindDataSet == 1:
            self.performanceData.estimatedMetricsPerformance(self.dataset, self.target)
        else:
            self.performanceData.estimatedMetricsPerformanceMultilabels(self.dataset, self.target)
