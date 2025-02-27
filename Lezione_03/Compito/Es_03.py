'''Esercizio 3
Scrivere un programma che acquisisca una stringa inserita dall'utente e generi una nuova stringa che corrisponda alla versione invertita della stringa originale. Il programma deve poi visualizzare la stringa ottenuta in output. Per risolvere il problema non si deve utilizzare alcun tipo di funzione, ma esclusivamente i cicli.'''

stringa = input("Inserisci una stringa: ")
invertita = ""

for i in range(len(stringa) - 1, -1, -1):
    invertita += stringa[i]

print(f"La stringa invertita è: {invertita}")
