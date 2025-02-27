'''Esercizio 5
Si supponga di poter acquistare barrette di cioccolato da un distributore automatico al costo di 1 euro ciascuna. Ogni barretta acquistata contiene un buono sconto, e con 6 buoni sconto si ottiene una barretta gratuita.
Scrivere un programma che: Acquisisca in input un valore N (numero di euro disponibili).
Calcoli e mostri in output il numero totale di barrette che si possono ottenere, considerando anche quelle ottenute con i buoni sconto. Mostri quanti buoni sconto avanzano al termine dell'acquisto.
Esempio:
Se l'utente inserisce N = 6, può acquistare 6 barrette ottenendo 6 buoni sconto, che gli permettono di riscattare 1 ulteriore barretta gratuita, per un totale di 7 barrette. Alla fine, non rimarranno buoni sconto inutilizzati. Il programma deve continuare a scambiare i buoni con nuove barrette finché ce ne sono abbastanza per ottenere almeno una barretta gratuita.'''

barrette = 0
buono = 0

while True:
    euro:int = input("inserisci denaro")

    if euro == 0:
        print("Hai terminato i soldi")
        break
    
    barrette = euro
    buono = euro
    
    while buono >= 6:
        barrettaAgg = buono // 6
        barrette += barrettaAgg
        buono = buono % 6
        print(f"Hai acquistato n.:{barrette}")
        print(f"Buoni sconto n.:{buono}")
        