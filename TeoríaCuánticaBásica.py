from math import sqrt
import numpy as np


def normveccomp(vec):
    sumatoria = []
    for i in range(len(vec)):
        sumatoria.append(round(abs(vec[i])**2, 0))
    return sqrt(sum(sumatoria))


def normalizavec(vec):
    """ingresa un vector y lo retorna normalizado
    """
    n = np.linalg.norm(vec)
    for i in range(len(vec)):
        vec[i] = vec[i] / n
    return vec


def prodinterno(vec1, vec2):
    """ingresan dos vectores o matrices, retorna el producto interno
    """
    return np.inner(vec1, vec2)


def amplitrans(vec1, vect2):
    """ingresan dos vectores, retorna la amplitud de transición
    """
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


def probtransi(vec, vecpos):
    """ingresan el vector y algún vector propio, retorna la probabilidad de que el primero transite al segundo
    """
    pos = vecpos.index(1)
    normapow2 = 0
    for i in vec:
        normapow2 += abs(i) ** 2
    conj = (abs(vec[pos]))**2
    probtrans = conj / normapow2
    return probtrans


def accmatvec(mat, vec):
    """ingresa una matriz y un vector, retorna la acción de la matriz sobre el vector
    """
    matriz = np.array(mat)
    vector = np.array(vec)
    prod = matriz.dot(vector)
    return prod


def valoresperado(mat, vec):
    """ingresa un observable un vector key, retorna la media o valor esperado
    """
    if ishermitian(mat):
        if np.linalg.norm(vec) != 1:
            vec = normalizavec(vec)
        prodmatvec = accmatvec(mat, vec)
        media = prodinterno(prodmatvec, vec)
        return media
    raise Exception("Observable no es matriz hermitiana")


def ishermitian(mat):
    """verifica si un matriz es hermitiana
    """
    h = np.conjugate(mat)
    return np.array_equal(mat, np.transpose(h))


def adjunmat(mat):
    """ingresa una matriz y retorna su adjunta
    """
    h = np.conjugate(mat)
    return np.transpose(h)


def varianza(mat, vec):
    """ingresa el observable y el vector ket, retorna la varianza
    """
    media = valoresperado(mat, vec)
    ide = np.identity(len(vec))
    medid = media * np.matrix(ide)
    resta = np.matrix(mat) - np.matrix(medid)
    prod = np.matrix(resta).dot(np.matrix(resta))
    vari = valoresperado(prod, vec)
    return vari


def valprop(mat):
    """ingresa una matriz y retorna su o sus valores propios
    """
    matriz = np.array(mat)
    val, vec = np.linalg.eig(matriz)
    return val


def calcini(serie, estado):
    """ingresa una serie de matrices Un y el estado final, retorna el estado inicial
    """
    serieinv = serie[::-1]
    nmat = len(serie)
    for i in range(nmat):
        adjser = adjunmat(serieinv[i])
        estado = accmatvec(adjser, estado)
    return estado


