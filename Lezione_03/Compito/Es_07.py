'''Esercizio 7
Scrivere un programma che inizializzate due liste a e b della stessa lunghezza n, entrambe contenenti valori interi, calcoli la somma incrociata degli elementi.
Esempio:
a[1] + b[n-1], a[2] + b[n-2], ...
Memorizzare ogni somma incrociata in una nuova lista c e, quindi, visualizzare in output le liste a, b, c.'''

n = int(input("Inserisci la lunghezza delle liste: "))

a = []
b = []
print("Inserisci gli elementi per la lista a:")

for i in range(n):
   
    a.append(int(input(f"a[{i+1}]: ")))

print("Inserisci gli elementi per la lista b:")

for i in range(n):
   
    b.append(int(input(f"b[{i+1}]: ")))

c = []

for i in range(n):
    
    c.append(a[i] + b[n-i-1])

print(f"Lista a: {a}")
print(f"Lista b: {b}")
print(f"Lista c (somma incrociata): {c}")

