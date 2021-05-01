from supervised_learning_prediction import AdaBoost
from supervised_learning_prediction import Baggin
from supervised_learning_prediction import DecisionTree
from supervised_learning_prediction import Gradient
from supervised_learning_prediction import knn_regression
from supervised_learning_prediction import MLP
from supervised_learning_prediction import NuSVR
from supervised_learning_prediction import RandomForest
from supervised_learning_prediction import SVR

from supervised_learning_prediction import performanceData

import pandas as pd
import json
from joblib import dump, load

class execAlgorithm(object):

    #constructor de la clase
    def __init__(self, dataSet, response_data, pathResponse, algorithm):

        self.dataSet = dataSet
        self.pathResponse = pathResponse
        self.algorithm = algorithm  
        self.response_data = response_data      

        self.responseExec = {}#diccionario con la respuesta para formar el json

    #ejecucion del algoritmo
    def execAlgorithmByOptions(self):

        if self.algorithm == 1:#AdaBoost

            errorData = {}
            self.responseExec.update({"algorithm": "AdaBoostRegressor"})
            paramsData = {}
            paramsData.update({"n_estimators": "linear"})
            paramsData.update({"loss": 100})
            self.responseExec.update({"Params": paramsData})

            try:
            #instancia al objeto...
                AdaBoostObject = AdaBoost.AdaBoost(self.dataSet, self.response_data, 100, "linear")
                AdaBoostObject.trainingMethod()

                performance = {}
                performance.update({"r_score":AdaBoostObject.r_score})
                performance.update({"predict_values": [value for value in AdaBoostObject.predicctions]})
                performance.update({"real_values": [value for value in AdaBoostObject.response]})            

                #calculamos las medidas asociadas a la data de interes...
                performanceValues = performanceData.performancePrediction([float(value) for value in self.response_data], [float(value) for value in AdaBoostObject.predicctions])
                pearsonValue = performanceValues.calculatedPearson()
                spearmanValue = performanceValues.calculatedSpearman()
                kendalltauValue = performanceValues.calculatekendalltau()

                #los agregamos al diccionario
                performance.update({"pearson":pearsonValue})
                performance.update({"spearman":spearmanValue})
                performance.update({"kendalltau":kendalltauValue})

                self.responseExec.update({"Performance": performance})
                errorData.update({"Process" : "OK"})

                #exportamos el modelo en formato joblib
                nameModel =self.pathResponse+"modelExport.joblib"
                dump(AdaBoostObject.AdaBoostModel, nameModel)

            except:
                errorData.update({"Process" : "ERROR"})
                pass

            self.responseExec.update({"errorExec": errorData})

            #exportamos tambien el resultado del json            
            with open(self.pathResponse+"responseTraining.json", 'w') as fp:
                json.dump(self.responseExec, fp)


        if self.algorithm == 2:#Bagging

            errorData = {}
            self.responseExec.update({"algorithm": "BaggingRegressor"})
            paramsData = {}
            paramsData.update({"n_estimators": 100})
            paramsData.update({"bootstrap": True})
            self.responseExec.update({"Params": paramsData})

            #try:
            #instancia al objeto...
            baggingObject = Baggin.Baggin(self.dataSet, self.response_data, 100, True)
            baggingObject.trainingMethod()

            performance = {}
            performance.update({"r_score":baggingObject.r_score})
            performance.update({"predict_values": [value for value in baggingObject.predicctions]})
            performance.update({"real_values": [value for value in baggingObject.response]})            

            #calculamos las medidas asociadas a la data de interes...
            performanceValues = performanceData.performancePrediction([float(value) for value in self.response_data], [float(value) for value in baggingObject.predicctions])
            pearsonValue = performanceValues.calculatedPearson()
            spearmanValue = performanceValues.calculatedSpearman()
            kendalltauValue = performanceValues.calculatekendalltau()

            #los agregamos al diccionario
            performance.update({"pearson":pearsonValue})
            performance.update({"spearman":spearmanValue})
            performance.update({"kendalltau":kendalltauValue})

            self.responseExec.update({"Performance": performance})
            errorData.update({"Process" : "OK"})

            #exportamos el modelo en formato joblib
            nameModel =self.pathResponse+"modelExport.joblib"
            dump(baggingObject.bagginModel, nameModel)

            #except:
            #    errorData.update({"Process" : "ERROR"})
            #    pass

            self.responseExec.update({"errorExec": errorData})

            #exportamos tambien el resultado del json            
            with open(self.pathResponse+"responseTraining.json", 'w') as fp:
                json.dump(self.responseExec, fp)

        if self.algorithm == 3:#DecisionTree

            errorData = {}
            self.responseExec.update({"algorithm": "DecisionTreeRegressor"})
            paramsData = {}
            paramsData.update({"criterion": "mse"})
            paramsData.update({"splitter": "best"})
            self.responseExec.update({"Params": paramsData})

            try:
            #instancia al objeto...
                decisionObject = DecisionTree.DecisionTree(self.dataSet, self.response_data, "mse", "best")
                decisionObject.trainingMethod()

                performance = {}
                performance.update({"r_score":decisionObject.r_score})
                performance.update({"predict_values": [value for value in decisionObject.predicctions]})
                performance.update({"real_values": [value for value in decisionObject.response]})            

                #calculamos las medidas asociadas a la data de interes...
                performanceValues = performanceData.performancePrediction([float(value) for value in self.response_data], [float(value) for value in decisionObject.predicctions])
                pearsonValue = performanceValues.calculatedPearson()
                spearmanValue = performanceValues.calculatedSpearman()
                kendalltauValue = performanceValues.calculatekendalltau()

                #los agregamos al diccionario
                performance.update({"pearson":pearsonValue})
                performance.update({"spearman":spearmanValue})
                performance.update({"kendalltau":kendalltauValue})

                self.responseExec.update({"Performance": performance})
                errorData.update({"Process" : "OK"})

                #exportamos el modelo en formato joblib
                nameModel =self.pathResponse+"modelExport.joblib"
                dump(decisionObject.DecisionTreeAlgorithm, nameModel)

            except:
                errorData.update({"Process" : "ERROR"})
                pass

            self.responseExec.update({"errorExec": errorData})

            #exportamos tambien el resultado del json            
            with open(self.pathResponse+"responseTraining.json", 'w') as fp:
                json.dump(self.responseExec, fp)





        if self.algorithm == 4:#Gradient

            errorData = {}
            self.responseExec.update({"algorithm": "GradientBoostingRegressor"})
            paramsData = {}
            paramsData.update({"n_estimators": 10})
            paramsData.update({"loss": "ls"})
            paramsData.update({"criterion": "friedman_mse"})
            paramsData.update({"min_samples_leaf": 1})
            paramsData.update({"min_samples_split": 2})
            self.responseExec.update({"Params": paramsData})

            try:
                #instancia al objeto...
                gradientObject = Gradient.Gradient(self.dataSet, self.response_data, 10, "ls", "friedman_mse", 2, 1)
                gradientObject.trainingMethod()

                performance = {}
                performance.update({"r_score":gradientObject.r_score})
                performance.update({"predict_values": [value for value in gradientObject.predicctions]})
                performance.update({"real_values": [value for value in gradientObject.response]})            

                    #calculamos las medidas asociadas a la data de interes...
                performanceValues = performanceData.performancePrediction([float(value) for value in self.response_data], [float(value) for value in gradientObject.predicctions])
                pearsonValue = performanceValues.calculatedPearson()
                spearmanValue = performanceValues.calculatedSpearman()
                kendalltauValue = performanceValues.calculatekendalltau()

                    #los agregamos al diccionario
                performance.update({"pearson":pearsonValue})
                performance.update({"spearman":spearmanValue})
                performance.update({"kendalltau":kendalltauValue})

                self.responseExec.update({"Performance": performance})
                errorData.update({"Process" : "OK"})

                    #exportamos el modelo en formato joblib
                nameModel =self.pathResponse+"modelExport.joblib"
                dump(gradientObject.GradientAlgorithm, nameModel)

            except:
                errorData.update({"Process" : "ERROR"})
                pass

            self.responseExec.update({"errorExec": errorData})

            #exportamos tambien el resultado del json            
            with open(self.pathResponse+"responseTraining.json", 'w') as fp:
                json.dump(self.responseExec, fp)                

        if self.algorithm == 5:#KNN

            errorData = {}
            self.responseExec.update({"algorithm": "KNeighborsRegressor"})
            paramsData = {}
            paramsData.update({"n_neighbors": 5})
            paramsData.update({"algorithm": "auto"})
            paramsData.update({"metric": "minkowski"})
            paramsData.update({"weights": "uniform"})
            self.responseExec.update({"Params": paramsData})

            try:
                #instancia al objeto...
                knnObject = knn_regression.KNN_Model(self.dataS , self.response_data, 5, "auto", "minkowski", "uniform")
                knnObject.trainingMethod()

                performance = {}
                performance.update({"r_score":knnObject.r_score})
                performance.update({"predict_values": [value for value in knnObject.predicctions]})
                performance.update({"real_values": [value for value in knnObject.response]})            

                    #calculamos las medidas asociadas a la data de interes...
                performanceValues = performanceData.performancePrediction([float(value) for value in self.response_data], [float(value) for value in knnObject.predicctions])
                pearsonValue = performanceValues.calculatedPearson()
                spearmanValue = performanceValues.calculatedSpearman()
                kendalltauValue = performanceValues.calculatekendalltau()

                    #los agregamos al diccionario
                performance.update({"pearson":pearsonValue})
                performance.update({"spearman":spearmanValue})
                performance.update({"kendalltau":kendalltauValue})

                self.responseExec.update({"Performance": performance})
                errorData.update({"Process" : "OK"})

                    #exportamos el modelo en formato joblib
                nameModel =self.pathResponse+"modelExport.joblib"
                dump(knnObject.KNN_model, nameModel)

            except:
                errorData.update({"Process" : "ERROR"})
                pass

            self.responseExec.update({"errorExec": errorData})

            #exportamos tambien el resultado del json            
            with open(self.pathResponse+"responseTraining.json", 'w') as fp:
                json.dump(self.responseExec, fp)                


        if self.algorithm == 6:#NuSVR

            errorData = {}
            self.responseExec.update({"algorithm": "NuSVR"})
            paramsData = {}
            paramsData.update({"kernel":"rbf"})
            paramsData.update({"nu":0.01})
            paramsData.update({"degree":3})
            paramsData.update({"gamma":0.01})
            self.responseExec.update({"Params": paramsData})

            try:
                #instancia al objeto...
                nuSVM = NuSVR.NuSVRModel(self.dataSet, self.response_data,"rbf", 3, 0.01, 0.01)
                nuSVM.trainingMethod()

                performance = {}
                performance.update({"r_score":nuSVM.r_score})
                performance.update({"predict_values": [value for value in nuSVM.predicctions]})
                performance.update({"real_values": [value for value in nuSVM.response]})            

                    #calculamos las medidas asociadas a la data de interes...
                performanceValues = performanceData.performancePrediction([float(value) for value in self.response_data], [float(value) for value in nuSVM.predicctions])
                pearsonValue = performanceValues.calculatedPearson()
                spearmanValue = performanceValues.calculatedSpearman()
                kendalltauValue = performanceValues.calculatekendalltau()

                    #los agregamos al diccionario
                performance.update({"pearson":pearsonValue})
                performance.update({"spearman":spearmanValue})
                performance.update({"kendalltau":kendalltauValue})

                self.responseExec.update({"Performance": performance})
                errorData.update({"Process" : "OK"})

                    #exportamos el modelo en formato joblib
                nameModel =self.pathResponse+"modelExport.joblib"
                dump(nuSVM.SVRAlgorithm, nameModel)

            except:
                errorData.update({"Process" : "ERROR"})
                pass

            self.responseExec.update({"errorExec": errorData})

            #exportamos tambien el resultado del json            
            with open(self.pathResponse+"responseTraining.json", 'w') as fp:
                json.dump(self.responseExec, fp)                


        if self.algorithm == 7:#RF

            errorData = {}
            self.responseExec.update({"algorithm": "RandomForestRegressor"})
            paramsData = {}
            paramsData.update({"n_estimators":200})
            paramsData.update({"criterion":"mse"})
            paramsData.update({"min_samples_split":2})
            paramsData.update({"min_samples_leaf":1})
            paramsData.update({"bootstrap":True})
            self.responseExec.update({"Params": paramsData})

            try:
                #instancia al objeto...
                rf = RandomForest.RandomForest(self.dataSet,self.response_data, 200,"mse", 2, 1, True)
                rf.trainingMethod()

                performance = {}
                performance.update({"r_score":rf.r_score})
                performance.update({"predict_values": [value for value in rf.predicctions]})
                performance.update({"real_values": [value for value in rf.response]})            

                    #calculamos las medidas asociadas a la data de interes...
                performanceValues = performanceData.performancePrediction([float(value) for value in self.response_data], [float(value) for value in rf.predicctions])
                pearsonValue = performanceValues.calculatedPearson()
                spearmanValue = performanceValues.calculatedSpearman()
                kendalltauValue = performanceValues.calculatekendalltau()

                    #los agregamos al diccionario
                performance.update({"pearson":pearsonValue})
                performance.update({"spearman":spearmanValue})
                performance.update({"kendalltau":kendalltauValue})

                self.responseExec.update({"Performance": performance})
                errorData.update({"Process" : "OK"})

                    #exportamos el modelo en formato joblib
                nameModel =self.pathResponse+"modelExport.joblib"
                dump(rf.randomForesModel, nameModel)

            except:
                errorData.update({"Process" : "ERROR"})
                pass

            self.responseExec.update({"errorExec": errorData})

            #exportamos tambien el resultado del json            
            with open(self.pathResponse+"responseTraining.json", 'w') as fp:
                json.dump(self.responseExec, fp)                


        if self.algorithm == 8:#SVR

            errorData = {}
            self.responseExec.update({"algorithm": "SVR"})
            paramsData = {}
            paramsData.update({"kernel":"rbf"})
            paramsData.update({"degree":3})
            paramsData.update({"gamma":0.01})
            self.responseExec.update({"Params": paramsData})

            try:
                #instancia al objeto...
                svm = SVR.SVRModel(self.dataSet,self.response_data,"rbf", 3, 0.01)
                svm.trainingMethod()

                performance = {}
                performance.update({"r_score":svm.r_score})
                performance.update({"predict_values": [value for value in svm.predicctions]})
                performance.update({"real_values": [value for value in svm.response]})            

                    #calculamos las medidas asociadas a la data de interes...
                performanceValues = performanceData.performancePrediction([float(value) for value in self.response_data], [float(value) for value in svm.predicctions])
                pearsonValue = performanceValues.calculatedPearson()
                spearmanValue = performanceValues.calculatedSpearman()
                kendalltauValue = performanceValues.calculatekendalltau()

                    #los agregamos al diccionario
                performance.update({"pearson":pearsonValue})
                performance.update({"spearman":spearmanValue})
                performance.update({"kendalltau":kendalltauValue})

                self.responseExec.update({"Performance": performance})
                errorData.update({"Process" : "OK"})

                    #exportamos el modelo en formato joblib
                nameModel =self.pathResponse+"modelExport.joblib"
                dump(svm.SVRAlgorithm, nameModel)

            except:
                errorData.update({"Process" : "ERROR"})
                pass

            self.responseExec.update({"errorExec": errorData})

            #exportamos tambien el resultado del json            
            with open(self.pathResponse+"responseTraining.json", 'w') as fp:
                json.dump(self.responseExec, fp)                
