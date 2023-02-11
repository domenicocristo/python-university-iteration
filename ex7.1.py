# Un modo per calcolare le radici quadrate è il metodo di Newton.
# y = (x + a/x) / 2

# Copiate il ciclo del paragrafo 7.5 e incapsulatelo in una funzione di nome mia_radq
# che prenda a come parametro, scelga un valore appropriato di x, e restituisca una stima 
# del valore della radice quadrata di a.

import math

def mia_radq(a):
    epsilon = 0.0000001
    x = 1
    while True:
        y = (x + a/x) / 2
        if abs(y - x) < epsilon:
            break
        x = y
    return x

# Scrivete una funzione di nome test_radq che stampi una tabella come quella del paragrafo 7.1,
# che abbia nella prima colonna un numero (a), 
# nella seconda la radice quadrata di a calcolata con mia_radq,
# nella terza la radice quadrata calcolata con math.sqrt 
# e nella quarta il valore assoluto della differenza tra le due stime.

def test_radq():
    print("a\tmia_radq(a)\t\tmath.sqrt(a)\t\tdiff")
    print("-\t----------\t\t------------\t\t----")
    for i in range(1, 10):
        a = i
        radq = mia_radq(a)
        sqrt = math.sqrt(a)
        diff = abs(radq - sqrt)
        print("{:.1f}\t{:.11f}\t\t{:.11f}\t\t{:.11f}".format(a, radq, sqrt, diff))

test_radq()