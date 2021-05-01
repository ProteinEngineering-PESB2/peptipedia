'''
script que permite el testeo de las clases de aprendizaje supervisado para prediccion de elementos
'''

import sys
import pandas as pd
import MLP

def main():

    print "Init data"
    data = pd.read_csv(sys.argv[1])
    columnas=data.columns.tolist()
    x=columnas[len(columnas)-1]
    response=data[x]
    y=columnas[0:len(columnas)-1]
    dataset=data[y]

    mlpModel = MLP.MLP(dataset,response, 'relu', 'adam', 'constant', 1,1,1, 0.001, 200, True)
    mlpModel.trainingMethod()
    return 0

if __name__ == '__main__':
    main()
