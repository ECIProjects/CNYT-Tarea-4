from math import sqrt

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

def probtransi():
