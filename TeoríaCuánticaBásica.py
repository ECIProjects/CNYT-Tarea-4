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
    return np.linalg.norm(vec)

def prodinterno(vec1,vec2):
    return np.inner(vec1,vec2)

def amplitrans(vec1,vect2):
    norm_1 = np.linalg.norm(vec1)
    norm_2 = np.linalg.norm(vect2)
    for i in range(len(vec1)):
        vec1[i] = vec1[i] / norm_1
        vect2[i] = vect2[i] / norm_2
    inner_prod = 0
    for i in range(len(vec1)):
        multi = vect2[i] * vec1[i].conjugate()
        inner_prod += multi
    return inner_prod

def probtransi(vec1,vect2):
    return abs(amplitrans(vec1,vect2))**2

def suma(a,b):
    """retorna la suma entre dos numeros complejos"""
    return (a[0]+b[0]),(a[1]+b[1])

def producto(a,b):
    """retorna el producto entre dos numeros complejos"""
    if a==(0,0) and b==(0,0):
        return a
    elif a[0]==b[0] and a[1]==(b[1]*-1):
        return (a[0]**2)+(a[1]**2),0
    return ((a[0]*b[0])-(a[1]*b[1])),((a[0]*b[1])+(a[1]*b[0]))

def valmultvecrealcomp(arr1,arr2):
    sumai=(0,0)
    sumatoria=0
    x=False
    for i in range(len(arr1)):
        try:
            sumai=suma(sumai,producto(arr1[i],arr2[i]))
            x=True
        except TypeError:
            sumatoria+=arr1[i]*arr2[i]
    if x:
        return sumai
    return sumatoria

def accmatvec(mat,vec):
    resp=[]
    for i in range(len(mat)):
        x=mat[i]
        for j in range(len(x)):
            y=(valmultvecrealcomp(mat[i],vec))
        resp.append(y)
    return resp

def valoresperado(mat,vec):
    if ishermitian(mat):
        omega=accmatvec(mat,vec)
        return prodinterno(omega,vec)
    raise Exception("Matriz no es hermitiana")

def ishermitian(mat):
    h=np.matrix.H(mat)
    return h==mat


#a=[1j,1]
#b=[1,-1j]
#print("proba",probtransi(a,b))
#print("ampli",amplitrans(a,b))
#c=[[1,-1j],[1j,2]]
#d=[0.707107,0.707107j]
#print(valoresperado(c,d))

