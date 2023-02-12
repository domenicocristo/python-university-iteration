"""
La funzione predefinita eval valuta un'espressione sotto forma di stringa, usando
l'interprete Python.

Scrivete una funzione di nome eval_ciclo che chieda iterativamente all'utente di inserire un dato,
prenda il dato inserito e lo valuti con eval, infine visualizzi il risultato.

Deve continuare fino a quando l'utente non scriva 'fatto'.
"""

def eval_ciclo():
    while True:
        user_input = input("Inserisci un'espressione o scrivi 'fatto' per uscire: ")
        risultato = eval(user_input)
        if risultato == 'fatto':
            break
        print(risultato)

eval_ciclo()