'''Esercizio 10
Scrivere un programma che permetta di analizzare una lista di numeri interi inseriti dall'utente.
Il programma deve:
acquisire una sequenza di numeri interi, terminando l'inserimento quando l'utente digita 0 (che non deve essere considerato nei calcoli);
calcolare e visualizzare la somma di tutti i numeri pari inseriti;
calcolare e visualizzare la media di tutti i numeri dispari inseriti;
determinare e visualizzare il numero con la frequenza più alta (cioè quello che compare più volte nella lista);
se più numeri hanno la stessa frequenza massima, visualizzarli tutti.
Esempio di input e output
Input:
Inserisci un numero (0 per terminare): 4
Inserisci un numero (0 per terminare): 7
Inserisci un numero (0 per terminare): 2
Inserisci un numero (0 per terminare): 7
Inserisci un numero (0 per terminare): 3
Inserisci un numero (0 per terminare): 4
Inserisci un numero (0 per terminare): 0
Output:
Somma dei numeri pari: 10
Media dei numeri dispari: 5.67
Numero più frequente: 7 (2 volte)'''

numeri = [] 
somm_pari = 0    
dispari = [] 
frequenza = {}  

while True:                                                                                               
    num = int(input("Inserisci un numero (0 per terminare): "))
    if num == 0:
        break
    numeri.append(num)

    if num % 2 == 0:
        somm_pari += num
    else:
        dispari.append(num)

    if num in frequenza:
        frequenza[num] += 1
    else:
        frequenza[num] = 1

if len(dispari) > 0:
    media_dispari = sum(dispari) / len(dispari)
else:
    media_dispari = 0  

max_frequenza = max(frequenza.values()) 
numeri_frequenti = [num for num, freq in frequenza.items() if freq == max_frequenza]

print(f"Somma dei numeri pari: {somm_pari}")
print(f"Media dei numeri dispari: {media_dispari:.2f}")
print(f"Numero più frequente: {numeri_frequenti} ({max_frequenza} volte)")

