from math import sqrt
import numpy as np

def prob(vec,pos):
    """calcula la probabilidad de una particula un una posición, se ingresa un vector de complejos y la posición
    """
    comp=vec[pos]
    norvec2=round(normveccomp(vec)**2,0)
    nornum2=round(abs(comp)**2,0)
    return nornum2/norvec2

def normveccomp(vec):
    sumatoria=[]
    for i in range(len(vec)):
        sumatoria.append(round(abs(vec[i])**2,0))
    return sqrt(sum(sumatoria))

def normalizavec(vec):
    return numpy.linalg.norm(vec)

def prodinterno(vec1,vec2):
    return numpy.inner(vec1,vec2)

def probtransi(vec1,vec2):
    normvec1=normalizavec(vec1)
    normvec2=normalizavec(vec2)
    comp=prodinterno(normvec1,normvec2)
    norma=True ## se debe cambiar, buscar comando
    return round(norma**2,0)