'''
Esercizio 3C-7. Si scriva un programma in python che computi la statistica di otto lanci di una moneta.
Per ciascuno dei lanci effettuati, l'utente inserisce "t" o "T" se è uscito "testa", mentre inserisce "c" o "C" se è uscito "croce".
Il programma deve mostrare in output il numero totale e la percentuale dei risultati "testa" e "croce".
NOTA.
Le percentuali devono essere mostrate in output obbligatoriamente con 2 cifre decimali.
Usare il match statement.
Expected Output:
Per ciascun lancio della moneta inserisci "t" o "T" se e' uscito "testa" mentre inserisci "c" o "C" se e' uscito "croce".
Lancio 1: t
Lancio 2: c
Lancio 3: t
Lancio 4: t
Lancio 5: c
Lancio 6: c
Lancio 7: t
Lancio 8: t

Totale "testa": 5
Percentaule "testa": 62.50%
Totale "croce": 3
Percentuale "croce": 37.50%
'''
testa = 0
croce = 0
lancio = 1  

print("Per ciascun lancio della moneta inserisci 't' o 'T' se e' uscito 'testa' mentre inserisci 'c' o 'C' se e' uscito 'croce'.")

while lancio <= 8:
    
    risultato = input(f"Lancio {lancio}: ")
    
    match risultato:
        case 't'| 'T':  
            testa += 1  
        case 'c'| 'C': 
            croce += 1  
        case _:
            print("Input non valido, inserisci 't' o 'c'.")
    lancio += 1 

percentuale_testa = (testa / 8) * 100
percentuale_croce = (croce / 8) * 100

print(f"\nTotale 'testa': {testa}")
print(f"Percentuale 'testa': {percentuale_testa:.2f}%")
print(f"Totale 'croce': {croce}")
print(f"Percentuale 'croce': {percentuale_croce:.2f}%")

