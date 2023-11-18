#RSA
import math
import random
import numpy as np

def iterarRSA(maxIter, t, dimension, poblacion, bestSolution):
    alfa = 0.1
    beta = 0.005
    for i in range(poblacion.__len__()):
        ES = 2 * random.randint(-1,1) * (1 -(t/maxIter))
        for j in range(dimension):
            r = (bestSolution[j]-poblacion[random.randint(1,poblacion.__len__()-1)][j])/ (bestSolution[j]+math.e)
            m = 0
            for k in range(dimension):
                m += poblacion[i][k]
            m = m/dimension
            p = alfa + (poblacion[i][j]-m)/(bestSolution[j]+math.e)
            n = bestSolution[j] * p
            if i <= maxIter/4:
                poblacion[i][j] = (bestSolution[j] * -n * beta) - (r * random.randint(0,1))
            elif i <= maxIter/2:
                poblacion[i][j] = bestSolution[j] * poblacion[random.randint(1,poblacion.__len__()-1)][j] * ES *  random.randint(0,1)
            elif i<= 3*maxIter/4:
                poblacion[i][j] = bestSolution[j] * p * random.randint(0,1)
            else:
                poblacion[i][j] = (bestSolution[j] * -n * math.e) - (r * random.randint(0,1))

    return np.array(poblacion) 