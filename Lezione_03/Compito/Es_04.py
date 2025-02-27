'''Esercizio 4
Scrivere un programma che consenta all'utente di inserire una sequenza di numeri reali non negativi (sia interi che decimali). L'inserimento termina quando viene fornito un numero negativo, che funge da sentinella e non deve essere considerato nei calcoli.
Il programma deve: 
Calcolare la media dei soli numeri interi inseriti. Utilizzate la funzione is_integer() per verificare se il numero inserito è un intero.
Determinare e visualizzare il numero più grande e il numero più piccolo tra tutti quelli inseriti (sia interi che decimali).'''

numeri_interi = 0
somma_interi = 0
minimo = None
massimo = None

while True:
    numero = float(input("Inserisci un numero (negativo per terminare): "))
    if numero < 0:
        break
    
    if numero.is_integer():
        numeri_interi += 1
        somma_interi += int(numero)
    
    if minimo is None or numero < minimo:
        minimo = numero
    
    if massimo is None or numero > massimo:
        massimo = numero

if numeri_interi > 0:
    media = somma_interi / numeri_interi
   
    print(f"La media dei numeri interi è: {media}")
else:
    
    print("Non sono stati inseriti numeri interi.")

print(f"Il numero più piccolo è: {minimo}")
print(f"Il numero più grande è: {massimo}")
