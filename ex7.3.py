"""
Il matematico Srinivasa Ramanujan scoprì una serie infinita che può essere usata
per generare un'approssimazione di 1/π.

Scrivete una funzione di nome stima_pi che utilizzi la formula per calcolare e restituire una
stima di π. Deve usare un ciclo while per calcolare gli elementi della sommatoria, fino a quando 
l'ultimo termine è più piccolo di 1e-15 (che è la notazione di Python per 10^-15). Controllate il
risultato confrontandolo con math.pi.
"""

import math

def fattoriale(n):
    if n == 0:
        return 1
    else:
        ricorsione = fattoriale(n-1)
        risultato = n * ricorsione
        return risultato

def stima_pi():
    totale = 0
    k = 0
    fattore = 2 * math.sqrt(2) / 9801
    while True:
        num = fattoriale(4*k) * (1103 + 26390*k)   # num = numeratore
        den = fattoriale(k)**4 * 396**(4*k)        # den = denominatore

        totale += num / den
        term = fattore * num/den

        if abs(term) < 1e-15:
            break
        k += 1

    return 1 / (fattore * totale)

print(stima_pi())