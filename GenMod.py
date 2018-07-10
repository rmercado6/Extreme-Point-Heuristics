import time
import math

ra = 0  # semilla
rb = 0  # aditivo(magnitud de tiempo)
rc = 0  # divisor(magnitud de tiempo)
rx = 0
rn = 1
cnn = 0 # argumento de función verificadora de si el número es primo o no
cnt = 1 # variable temporal - producto de factores primos
cna = 1 # número a verificar si es primo o no (varia de 3 en delante en ++)
cni = 0 # contador de for de función de mínimo factor
cnc = 3 # número primo - multiplicador de cnt
cns = 0 # número primo siguiente - búsqueda del siguiente número primo
cnm = 0

def randint(n1, n2):
    dif = n2 - n1 + 1
    rn = dif * random()
    rn += n1
    rn = math.floor(rn)
    return rn

def random():
    global rn
    global ra
    global rb
    global rc
    global rx
    global rn

    # print(rn)
    ra = NumGran()
    rx = math.floor((time.time() + rn) / 2500)
    rb = math.floor((time.time() + rn) / 5000)
    rc = time.time()
    rn = ((ra + ((rn + rn))) * rx) + rb
    rn = rn % rc
    rn = time.clock()/rn * 10 ** 23
    rn = rn - math.floor(rn)

    return rn


def NumGran():

    global cnt
    global cnc
    global cna
    global cns
    for cna in range(cnc, 1000000000000):
        if isPrime(cna):
            cnt *= cna
            break
        if cnt > 1000000000000: break


    cns = cnc + 1
    while True:
        if isPrime(cns):
            cnc = cns
            break
        if cns > cnc: break
        cns += 1

    return cnt


def isPrime(cnn):

    if math.isnan(cnn) or not math.isfinite(cnn) or cnn%1 or cnn<2: return False
    if cnn == leastFactor(cnn): return True
    return False

def leastFactor(cnn):

    if cnn == 0: return 0
    if cnn % 1 or cnn * cnn < 2: return 1
    if cnn % 2 == 0: return 2
    if cnn % 3 == 0: return 3
    if cnn % 5 == 0: return 5
    cnm = math.floor(math.sqrt(cnn))
    for cni in range(7, int(cnm), 30):
        if cnn % cni == 0: return cni
        if cnn % (cni + 4) == 0: return cni + 4
        if cnn % (cni + 6) == 0: return cni + 6
        if cnn % (cni + 10) == 0: return cni + 10
        if cnn % (cni + 12) == 0: return cni + 12
        if cnn % (cni + 16) == 0: return cni + 16
        if cnn % (cni + 22) == 0: return cni + 22
        if cnn % (cni + 24) == 0: return cni + 24

    return cnn
