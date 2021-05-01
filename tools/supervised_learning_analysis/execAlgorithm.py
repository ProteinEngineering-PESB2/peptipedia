'''
script que permite procesar la ejecucion de un algoritmo de aprendizaje supervisado para crear el entrenamiento del modelo
recibe los parametros asociados a la configuracion del modelo y ejecuta los complementos a los resultados obtenidos

Orden de los algoritmos

1 Adaboost
2 Bagging
3 Bernoulli
4 Decision Tree
5 Gaussian
6 Gradient
7 KNN
8 MLP
9 NuSVC
10 RF
11 SVC

Cada uno posee diferentes parametros con respecto a su ejecucion...

'''

#importamos los algoritmos...
from supervised_learning_analysis import AdaBoost
from supervised_learning_analysis import Baggin
from supervised_learning_analysis import BernoulliNB
from supervised_learning_analysis import DecisionTree
from supervised_learning_analysis import GaussianNB
from supervised_learning_analysis import Gradient
from supervised_learning_analysis import knn
from supervised_learning_analysis import MLP
from supervised_learning_analysis import NuSVM
from supervised_learning_analysis import RandomForest
from supervised_learning_analysis import SVM

#importamos los metodos para generar el resto de los resultados
from supervised_learning_analysis import createConfusionMatrix
from supervised_learning_analysis import createLearningCurve

#manipulacion de datos
import pandas as pd
import json
from joblib import dump, load

class execAlgorithm(object):

    #constructor de la clase
    def __init__(self, data, response_data, pathResponse, algorithm, validation):

        self.data = data
        self.pathResponse = pathResponse
        self.algorithm = algorithm
        self.validation = validation#validacion del algoritmo (valor de CV)
        self.response_data = response_data

        self.classArray = []#contiene el nombre de las clases
        self.response = {}

        #procesamos el data set para obtener las clases y los atributos
        self.createDataSet()        

    #metodo que permite formar el set de datos y el target con la informacion...
    def createDataSet(self):
        
        self.classArray = list(set(self.response_data))
        

    #metodo que permite evaluar la ejecucion del algoritmo con respecto a los parametros de entrada
    def execAlgorithmByOptions(self):

        if self.algorithm == 1:#Adaboost

            self.response.update({"algorithm": "AdaBoostClassifier"})
            paramsData = {}
            paramsData.update({"n_estimators": 10})
            paramsData.update({"algorithm": "SAME"})
            self.response.update({"Params": paramsData})            
            nameValidation = str(self.validation)
            self.response.update({"Validation": "Cross Validation: " + nameValidation})

            #instancia al objeto...
            errorData = {}
            try:
                AdaBoostObject = AdaBoost.AdaBoost(self.data, self.response_data, 10, "SAMME", self.validation)
                if len(self.classArray)>2:
                    AdaBoostObject.trainingMethod(2)#multilabel
                else:
                    AdaBoostObject.trainingMethod(1)#binary
                performance = {}
                performance.update({"accuracy":AdaBoostObject.performanceData.scoreData[3]})
                performance.update({"recall": AdaBoostObject.performanceData.scoreData[4]})
                performance.update({"precision": AdaBoostObject.performanceData.scoreData[5]})
                performance.update({"f1": AdaBoostObject.performanceData.scoreData[6]})

                self.response.update({"Performance": performance})
                errorData.update({"exec_algorithm": "OK"})

                #exportamos el modelo en formato joblib
                nameModel =self.pathResponse+"modelExport.joblib"
                dump(AdaBoostObject.AdaBoostAlgorithm, nameModel)
            
            except:
                errorData.update({"exec_algorithm": "ERROR"})
                pass


            #trabajamos con la matriz de confusion
            try:
                #confusion matrix data
                confusionMatrixDemo = createConfusionMatrix.confusionMatrix(self.data, self.response_data, AdaBoostObject.model, self.validation, self.classArray)
                responseMatrix = confusionMatrixDemo.createConfusionMatrix()
                self.response.update({"matrixConfusionResponse":responseMatrix})
                errorData.update({"confusionMatrix" : "ok"})
            except:
                errorData.update({"confusionMatrix" : "error"})
                pass

            try:
                #learning curve
                learningCurveDemo = createLearningCurve.curveLearning(self.data, self.response_data, AdaBoostObject.model, self.validation, self.pathResponse)
                learningCurveDemo.createLearningCurve()
                errorData.update({"curveLearning" : "ok"})
            except:
                errorData.update({"curveLearning" : "error"})
                pass

            self.response.update({"errorExec": errorData})

            print(self.response)
            #exportamos tambien el resultado del json            
            with open(self.pathResponse+"/responseTraining.json", 'w') as fp:
                json.dump(self.response, fp)

        if self.algorithm == 2:#Bagging

            self.response.update({"algorithm": "Bagging"})
            paramsData = {}
            paramsData.update({"n_estimators": 100})
            paramsData.update({"bootstrap": True})
            self.response.update({"Params": paramsData})            
            nameValidation = str(self.validation)
            self.response.update({"Validation": "Cross Validation: " + nameValidation})

            #instancia al objeto...
            errorData = {}
            try:
                bagginObject = Baggin.Baggin(self.data,self.response_data,100, True,self.validation)                
                if len(self.classArray)>2:
                    bagginObject.trainingMethod(2)
                else:
                    bagginObject.trainingMethod(1)
                performance = {}
                performance.update({"accuracy":bagginObject.performanceData.scoreData[3]})
                performance.update({"recall": bagginObject.performanceData.scoreData[4]})
                performance.update({"precision": bagginObject.performanceData.scoreData[5]})
                performance.update({"f1": bagginObject.performanceData.scoreData[6]})

                self.response.update({"Performance": performance})
                errorData.update({"exec_algorithm": "OK"})

                #exportamos el modelo en formato joblib
                nameModel =self.pathResponse+"modelExport.joblib"
                dump(bagginObject.BagginAlgorithm, nameModel)
            
            except:
                errorData.update({"exec_algorithm": "ERROR"})
                pass


            #trabajamos con la matriz de confusion
            try:
                #confusion matrix data
                confusionMatrixDemo = createConfusionMatrix.confusionMatrix(self.data, self.response_data, bagginObject.model, self.validation, self.classArray)
                responseMatrix = confusionMatrixDemo.createConfusionMatrix()
                self.response.update({"matrixConfusionResponse":responseMatrix})
                errorData.update({"confusionMatrix" : "ok"})
            except:
                errorData.update({"confusionMatrix" : "error"})
                pass

            try:
                #learning curve
                learningCurveDemo = createLearningCurve.curveLearning(self.data, self.response_data, bagginObject.model, self.validation, self.pathResponse)
                learningCurveDemo.createLearningCurve()
                errorData.update({"curveLearning" : "ok"})
            except:
                errorData.update({"curveLearning" : "error"})
                pass

            self.response.update({"errorExec": errorData})

            print(self.response)
            #exportamos tambien el resultado del json            
            with open(self.pathResponse+"/responseTraining.json", 'w') as fp:
                json.dump(self.response, fp)

        if self.algorithm == 3:#Bernoulli

            self.response.update({"algorithm": "BernoulliNB"})            
            self.response.update({"Params": "-"})            
            nameValidation = str(self.validation)
            self.response.update({"Validation": "Cross Validation: " + nameValidation})

            #instancia al objeto...
            errorData = {}
            try:
                bernoulliNB = BernoulliNB.Bernoulli(self.data, self.response_data, self.validation)
                if len(self.classArray)>2:
                    bernoulliNB.trainingMethod(2)
                else:
                    bernoulliNB.trainingMethod(1)
                performance = {}
                performance.update({"accuracy":bernoulliNB.performanceData.scoreData[3]})
                performance.update({"recall": bernoulliNB.performanceData.scoreData[4]})
                performance.update({"precision": bernoulliNB.performanceData.scoreData[5]})
                performance.update({"f1": bernoulliNB.performanceData.scoreData[6]})

                self.response.update({"Performance": performance})
                errorData.update({"exec_algorithm": "OK"})

                #exportamos el modelo en formato joblib
                nameModel =self.pathResponse+"modelExport.joblib"
                dump(bernoulliNB.BernoulliNBAlgorithm, nameModel)
            
            except:
                errorData.update({"exec_algorithm": "ERROR"})
                pass


            #trabajamos con la matriz de confusion
            try:
                #confusion matrix data
                confusionMatrixDemo = createConfusionMatrix.confusionMatrix(self.data, self.response_data, bernoulliNB.model, self.validation, self.classArray)
                responseMatrix = confusionMatrixDemo.createConfusionMatrix()
                self.response.update({"matrixConfusionResponse":responseMatrix})
                errorData.update({"confusionMatrix" : "ok"})
            except:
                errorData.update({"confusionMatrix" : "error"})
                pass

            try:
                #learning curve
                learningCurveDemo = createLearningCurve.curveLearning(self.data, self.response_data, bernoulliNB.model, self.validation, self.pathResponse)
                learningCurveDemo.createLearningCurve()
                errorData.update({"curveLearning" : "ok"})
            except:
                errorData.update({"curveLearning" : "error"})
                pass

            self.response.update({"errorExec": errorData})

            print(self.response)
            #exportamos tambien el resultado del json            
            with open(self.pathResponse+"/responseTraining.json", 'w') as fp:
                json.dump(self.response, fp)

        if self.algorithm == 4:#DecisionTree

            self.response.update({"algorithm": "DecisionTree"})
            paramsData = {}
            paramsData.update({"criterion": "gini"})
            paramsData.update({"splitter": "best"})            
            self.response.update({"Params": paramsData})            
            nameValidation = str(self.validation)
            self.response.update({"Validation": "Cross Validation: " + nameValidation})

            #instancia al objeto...
            errorData = {}
            try:
                decisionTreeObject = DecisionTree.DecisionTree(self.data, self.response_data, "gini", "best",self.validation)
                if len(self.classArray)>2:
                    decisionTreeObject.trainingMethod(2)
                else:
                    decisionTreeObject.trainingMethod(1)
                performance = {}
                performance.update({"accuracy":decisionTreeObject.performanceData.scoreData[3]})
                performance.update({"recall": decisionTreeObject.performanceData.scoreData[4]})
                performance.update({"precision": decisionTreeObject.performanceData.scoreData[5]})
                performance.update({"f1": decisionTreeObject.performanceData.scoreData[6]})

                self.response.update({"Performance": performance})
                errorData.update({"exec_algorithm": "OK"})

                #exportamos el modelo en formato joblib
                nameModel =self.pathResponse+"modelExport.joblib"
                dump(decisionTreeObject.DecisionTreeAlgorithm, nameModel)
            
            except:
                errorData.update({"exec_algorithm": "ERROR"})
                pass


            #trabajamos con la matriz de confusion
            try:
                #confusion matrix data
                confusionMatrixDemo = createConfusionMatrix.confusionMatrix(self.data, self.response_data, decisionTreeObject.model, self.validation, self.classArray)
                responseMatrix = confusionMatrixDemo.createConfusionMatrix()
                self.response.update({"matrixConfusionResponse":responseMatrix})
                errorData.update({"confusionMatrix" : "ok"})
            except:
                errorData.update({"confusionMatrix" : "error"})
                pass

            try:
                #learning curve
                learningCurveDemo = createLearningCurve.curveLearning(self.data, self.response_data, decisionTreeObject.model, self.validation, self.pathResponse)
                learningCurveDemo.createLearningCurve()
                errorData.update({"curveLearning" : "ok"})
            except:
                errorData.update({"curveLearning" : "error"})
                pass

            self.response.update({"errorExec": errorData})

            print(self.response)
            #exportamos tambien el resultado del json            
            with open(self.pathResponse+"/responseTraining.json", 'w') as fp:
                json.dump(self.response, fp)
                

        if self.algorithm == 5:#Gaussian

            self.response.update({"algorithm": "GaussianNB"})            
            self.response.update({"Params": "-"})            
            nameValidation = str(self.validation)
            self.response.update({"Validation": "Cross Validation: " + nameValidation})

            #instancia al objeto...
            errorData = {}
            try:
                gaussianObject = GaussianNB.Gaussian(self.data, self.response_data, self.validation)
                if len(self.classArray)>2:
                    gaussianObject.trainingMethod(2)
                else:
                    gaussianObject.trainingMethod(1)
                performance = {}
                performance.update({"accuracy":gaussianObject.performanceData.scoreData[3]})
                performance.update({"recall": gaussianObject.performanceData.scoreData[4]})
                performance.update({"precision": gaussianObject.performanceData.scoreData[5]})
                performance.update({"f1": gaussianObject.performanceData.scoreData[6]})

                self.response.update({"Performance": performance})
                errorData.update({"exec_algorithm": "OK"})

                #exportamos el modelo en formato joblib
                nameModel =self.pathResponse+"modelExport.joblib"
                dump(gaussianObject.GaussianNBAlgorithm, nameModel)
            
            except:
                errorData.update({"exec_algorithm": "ERROR"})
                pass


            #trabajamos con la matriz de confusion
            try:
                #confusion matrix data
                confusionMatrixDemo = createConfusionMatrix.confusionMatrix(self.data, self.response_data, gaussianObject.model, self.validation, self.classArray)
                responseMatrix = confusionMatrixDemo.createConfusionMatrix()
                self.response.update({"matrixConfusionResponse":responseMatrix})
                errorData.update({"confusionMatrix" : "ok"})
            except:
                errorData.update({"confusionMatrix" : "error"})
                pass

            try:
                #learning curve
                learningCurveDemo = createLearningCurve.curveLearning(self.data, self.response_data, gaussianObject.model, self.validation, self.pathResponse)
                learningCurveDemo.createLearningCurve()
                errorData.update({"curveLearning" : "ok"})
            except:
                errorData.update({"curveLearning" : "error"})
                pass

            self.response.update({"errorExec": errorData})

            print(self.response)
            #exportamos tambien el resultado del json            
            with open(self.pathResponse+"/responseTraining.json", 'w') as fp:
                json.dump(self.response, fp)
                
        if self.algorithm == 6:#Gradient

            self.response.update({"algorithm": "GradientBoostingClassifier"})            
            paramsData = {}
            paramsData.update({"n_estimators":10})
            paramsData.update({"loss":"deviance"})
            paramsData.update({"min_samples_leaf":2})
            paramsData.update({"min_samples_split":1})

            self.response.update({"Params": paramsData})

            nameValidation = str(self.validation)
            self.response.update({"Validation": "Cross Validation: " + nameValidation})

            #instancia al objeto...
            errorData = {}
            try:
                gradientObject = Gradient.Gradient(self.data,self.response_data, 10, 'deviance', 2, 1,self.validation)
                if len(self.classArray)>2:
                    gradientObject.trainingMethod(2)
                else:
                    gradientObject.trainingMethod(1)
                performance = {}
                performance.update({"accuracy":gradientObject.performanceData.scoreData[3]})
                performance.update({"recall": gradientObject.performanceData.scoreData[4]})
                performance.update({"precision": gradientObject.performanceData.scoreData[5]})
                performance.update({"f1": gradientObject.performanceData.scoreData[6]})

                self.response.update({"Performance": performance})
                errorData.update({"exec_algorithm": "OK"})

                #exportamos el modelo en formato joblib
                nameModel =self.pathResponse+"modelExport.joblib"
                dump(gradientObject.GradientAlgorithm, nameModel)
            
            except:
                errorData.update({"exec_algorithm": "ERROR"})
                pass


            #trabajamos con la matriz de confusion
            try:
                #confusion matrix data
                confusionMatrixDemo = createConfusionMatrix.confusionMatrix(self.data, self.response_data, gradientObject.model, self.validation, self.classArray)
                responseMatrix = confusionMatrixDemo.createConfusionMatrix()
                self.response.update({"matrixConfusionResponse":responseMatrix})
                errorData.update({"confusionMatrix" : "ok"})
            except:
                errorData.update({"confusionMatrix" : "error"})
                pass

            try:
                #learning curve
                learningCurveDemo = createLearningCurve.curveLearning(self.data, self.response_data, gradientObject.model, self.validation, self.pathResponse)
                learningCurveDemo.createLearningCurve()
                errorData.update({"curveLearning" : "ok"})
            except:
                errorData.update({"curveLearning" : "error"})
                pass

            self.response.update({"errorExec": errorData})

            print(self.response)
            #exportamos tambien el resultado del json            
            with open(self.pathResponse+"/responseTraining.json", 'w') as fp:
                json.dump(self.response, fp)
                
        if self.algorithm == 7:#KNN

            self.response.update({"algorithm": "KNeighborsClassifier"})            
            paramsData = {}
            paramsData.update({"n_neighbors":5})
            paramsData.update({"algorithm":"auto"})
            paramsData.update({"metric":"minkowski"})
            paramsData.update({"weights":"uniform"})

            self.response.update({"Params": paramsData})

            nameValidation = str(self.validation)
            self.response.update({"Validation": "Cross Validation: " + nameValidation})

            #instancia al objeto...
            errorData = {}
            try:
                knnObect = knn.knn(self.data, self.response_data, 5, "auto", "minkowski", "uniform", self.validation)
                if len(self.classArray)>2:
                    knnObect.trainingMethod(2)
                else:
                    knnObect.trainingMethod(1)
                performance = {}
                performance.update({"accuracy":knnObect.performanceData.scoreData[3]})
                performance.update({"recall": knnObect.performanceData.scoreData[4]})
                performance.update({"precision": knnObect.performanceData.scoreData[5]})
                performance.update({"f1": knnObect.performanceData.scoreData[6]})

                self.response.update({"Performance": performance})
                errorData.update({"exec_algorithm": "OK"})

                #exportamos el modelo en formato joblib
                nameModel =self.pathResponse+"modelExport.joblib"
                dump(knnObect.knnAlgorithm, nameModel)
            
            except:
                errorData.update({"exec_algorithm": "ERROR"})
                pass


            #trabajamos con la matriz de confusion
            try:
                #confusion matrix data
                confusionMatrixDemo = createConfusionMatrix.confusionMatrix(self.data, self.response_data, knnObect.model, self.validation, self.classArray)
                responseMatrix = confusionMatrixDemo.createConfusionMatrix()
                self.response.update({"matrixConfusionResponse":responseMatrix})
                errorData.update({"confusionMatrix" : "ok"})
            except:
                errorData.update({"confusionMatrix" : "error"})
                pass

            try:
                #learning curve
                learningCurveDemo = createLearningCurve.curveLearning(self.data, self.response_data, knnObect.model, self.validation, self.pathResponse)
                learningCurveDemo.createLearningCurve()
                errorData.update({"curveLearning" : "ok"})
            except:
                errorData.update({"curveLearning" : "error"})
                pass

            self.response.update({"errorExec": errorData})

            print(self.response)
            #exportamos tambien el resultado del json            
            with open(self.pathResponse+"/responseTraining.json", 'w') as fp:
                json.dump(self.response, fp)
                
        if self.algorithm == 8:#NuSVC

            self.response.update({"algorithm": "NuSVC"})            
            paramsData = {}
            paramsData.update({"kernel":"rbf"})
            paramsData.update({"nu":0.01})
            paramsData.update({"degree":3})
            paramsData.update({"gamma":0.01})

            self.response.update({"Params": paramsData})

            nameValidation = str(self.validation)
            self.response.update({"Validation": "Cross Validation: " + nameValidation})

            #instancia al objeto...
            errorData = {}
            try:
                nuSVM = NuSVM.NuSVM(self.data,self.response_data, "rbf", 0.01, 3, 0.01, self.validation)
                if len(self.classArray)>2:
                    nuSVM.trainingMethod(2)
                else:
                    nuSVM.trainingMethod(1)
                performance = {}
                performance.update({"accuracy":nuSVM.performanceData.scoreData[3]})
                performance.update({"recall": nuSVM.performanceData.scoreData[4]})
                performance.update({"precision": nuSVM.performanceData.scoreData[5]})
                performance.update({"f1": nuSVM.performanceData.scoreData[6]})

                self.response.update({"Performance": performance})
                errorData.update({"exec_algorithm": "OK"})

                #exportamos el modelo en formato joblib
                nameModel =self.pathResponse+"modelExport.joblib"
                dump(nuSVM.NuSVMAlgorithm, nameModel)
            
            except:
                errorData.update({"exec_algorithm": "ERROR"})
                pass


            #trabajamos con la matriz de confusion
            try:
                #confusion matrix data
                confusionMatrixDemo = createConfusionMatrix.confusionMatrix(self.data, self.response_data, nuSVM.model, self.validation, self.classArray)
                responseMatrix = confusionMatrixDemo.createConfusionMatrix()
                self.response.update({"matrixConfusionResponse":responseMatrix})
                errorData.update({"confusionMatrix" : "ok"})
            except:
                errorData.update({"confusionMatrix" : "error"})
                pass

            try:
                #learning curve
                learningCurveDemo = createLearningCurve.curveLearning(self.data, self.response_data, nuSVM.model, self.validation, self.pathResponse)
                learningCurveDemo.createLearningCurve()
                errorData.update({"curveLearning" : "ok"})
            except:
                errorData.update({"curveLearning" : "error"})
                pass

            self.response.update({"errorExec": errorData})

            print(self.response)
            #exportamos tambien el resultado del json            
            with open(self.pathResponse+"/responseTraining.json", 'w') as fp:
                json.dump(self.response, fp)
                
        if self.algorithm == 9:#RandomForest

            self.response.update({"algorithm": "RandomForest"})            
            paramsData = {}
            paramsData.update({"n_estimators":200})
            paramsData.update({"criterion":"gini"})
            paramsData.update({"min_samples_split":2})
            paramsData.update({"min_samples_leaf":1})
            paramsData.update({"bootstrap":True})

            self.response.update({"Params": paramsData})

            nameValidation = str(self.validation)
            self.response.update({"Validation": "Cross Validation: " + nameValidation})

            #instancia al objeto...
            errorData = {}
            try:
                rf = RandomForest.RandomForest(self.data,self.response_data, 200,"gini", 2, 1, True, self.validation)
                if len(self.classArray)>2:
                    rf.trainingMethod(2)
                else:
                    rf.trainingMethod(1)
                performance = {}
                performance.update({"accuracy":rf.performanceData.scoreData[3]})
                performance.update({"recall": rf.performanceData.scoreData[4]})
                performance.update({"precision": rf.performanceData.scoreData[5]})
                performance.update({"f1": rf.performanceData.scoreData[6]})

                self.response.update({"Performance": performance})
                errorData.update({"exec_algorithm": "OK"})

                #exportamos el modelo en formato joblib
                nameModel =self.pathResponse+"modelExport.joblib"
                dump(rf.RandomForestAlgorithm, nameModel)
            
            except:
                errorData.update({"exec_algorithm": "ERROR"})
                pass


            #trabajamos con la matriz de confusion
            try:
                #confusion matrix data
                confusionMatrixDemo = createConfusionMatrix.confusionMatrix(self.data, self.response_data, rf.model, self.validation, self.classArray)
                responseMatrix = confusionMatrixDemo.createConfusionMatrix()
                self.response.update({"matrixConfusionResponse":responseMatrix})
                errorData.update({"confusionMatrix" : "ok"})
            except:
                errorData.update({"confusionMatrix" : "error"})
                pass

            try:
                #learning curve
                learningCurveDemo = createLearningCurve.curveLearning(self.data, self.response_data, rf.model, self.validation, self.pathResponse)
                learningCurveDemo.createLearningCurve()
                errorData.update({"curveLearning" : "ok"})
            except:
                errorData.update({"curveLearning" : "error"})
                pass

            self.response.update({"errorExec": errorData})

            print(self.response)
            #exportamos tambien el resultado del json            
            with open(self.pathResponse+"/responseTraining.json", 'w') as fp:
                json.dump(self.response, fp)
                
        if self.algorithm == 10:#SVC

            self.response.update({"algorithm": "SVC"})            
            paramsData = {}
            paramsData.update({"kernel":"rbf"})
            paramsData.update({"C_value":0.1})
            paramsData.update({"degree":3})
            paramsData.update({"gamma":0.01})

            self.response.update({"Params": paramsData})

            nameValidation = str(self.validation)
            self.response.update({"Validation": "Cross Validation: " + nameValidation})

            #instancia al objeto...
            errorData = {}
            try:
                svm = SVM.SVM(self.data, self.response_data, "rbf", 0.1, 3, 0.01, self.validation)
                if len(self.classArray)>2:
                    svm.trainingMethod(2)
                else:
                    svm.trainingMethod(1)
                performance = {}
                performance.update({"accuracy":svm.performanceData.scoreData[3]})
                performance.update({"recall": svm.performanceData.scoreData[4]})
                performance.update({"precision": svm.performanceData.scoreData[5]})
                performance.update({"f1": svm.performanceData.scoreData[6]})

                self.response.update({"Performance": performance})
                errorData.update({"exec_algorithm": "OK"})

                #exportamos el modelo en formato joblib
                nameModel =self.pathResponse+"modelExport.joblib"
                dump(svm.SVMAlgorithm, nameModel)
            
            except:
                errorData.update({"exec_algorithm": "ERROR"})
                pass


            #trabajamos con la matriz de confusion
            try:
                #confusion matrix data
                confusionMatrixDemo = createConfusionMatrix.confusionMatrix(self.data, self.response_data, svm.model, self.validation, self.classArray)
                responseMatrix = confusionMatrixDemo.createConfusionMatrix()
                self.response.update({"matrixConfusionResponse":responseMatrix})
                errorData.update({"confusionMatrix" : "ok"})
            except:
                errorData.update({"confusionMatrix" : "error"})
                pass

            try:
                #learning curve
                learningCurveDemo = createLearningCurve.curveLearning(self.data, self.response_data, svm.model, self.validation, self.pathResponse)
                learningCurveDemo.createLearningCurve()
                errorData.update({"curveLearning" : "ok"})
            except:
                errorData.update({"curveLearning" : "error"})
                pass

            self.response.update({"errorExec": errorData})

            print(self.response)
            #exportamos tambien el resultado del json            
            with open(self.pathResponse+"/responseTraining.json", 'w') as fp:
                json.dump(self.response, fp)
                
