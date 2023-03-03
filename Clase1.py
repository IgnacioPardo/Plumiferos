def suma_de_vectores_3 (v1, v2):
    res = [0] * len(v1)
    if len(v1) == len(v2):
        for i in range(len(v1)):
            res[i] = v1[i] + v2[i]
    return res

def resta_de_vectores_3 (v1, v2):
    res = [0] * len(v1)
    if len(v1) == len(v2):
        for i in range(len(v1)):
            res[i] = v1[i] - v2[i]
    return res

def multiplicacion_de_vectores_3 (v1, v2):
    res = 0
    if len(v1) == len(v2):
        for i in range(len(v1)):
            res = res + v1[i] * v2[i]
    return res