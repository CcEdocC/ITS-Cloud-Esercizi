'''Esercizio 9
Il valore di π può essere approssimato utilizzando la seguente serie infinita:
π = 4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...
Scrivere un programma che calcoli il valore di π utilizzando questa serie e determini quanti termini sono necessari per ottenere approssimazioni sempre più accurate. Quindi:
progettare un algoritmo che mostri in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.14;
modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.141;
modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.1415;
modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.14159.
Nota: Il programma deve iterare fino a raggiungere ciascuna delle soglie indicate, contando il numero di termini necessari.'''
                                                                                   
pi = 0
termi = 0
n = 1

while abs(pi - 3.14) >= 0.01:
    if termi % 2 == 0:
        pi += 4 / n
    else:
        pi -= 4 / n
    n += 2
    termi += 1
print("Numero di termini per π ≈ 3.14:", termi)

pi = 0
termi = 0
n = 1

while abs(pi - 3.141) >= 0.01:
    if termi % 2 == 0:
        pi += 4 / n
    else:
        pi -= 4 / n
    n += 2
    termi += 1
print("Numero di termini per π ≈ 3.141:", termi)

pi = 0
termi = 0
n = 1

while abs(pi - 3.1415) >= 0.01:
    if termi % 2 == 0:
        pi += 4 / n
    else:
        pi -= 4 / n
    n += 2
    termi += 1
print("Numero di termini per π ≈ 3.1415:", termi)

pi = 0
termi = 0
n = 1

while abs(pi - 3.14159) >= 0.01:
    if termi % 2 == 0:
        pi += 4 / n
    else:
        pi -= 4 / n
    n += 2
    termi += 1
print("Numero di termini per π ≈ 3.14159:", termi)

