'''Esercizio 3C-4. Scrivere un programma in Python che permetta all'utente di inserire il nome di un animale e, utilizzando un match statement, identifichi a quale categoria esso appartiene. L'animale deve essere classificato in una delle seguenti categorie:
- Mammiferi: cane, gatto, cavallo, elefante, leone.
- Rettili: serpente, lucertola, tartaruga, coccodrillo.
- Uccelli: aquila, pappagallo, gufo, falco.
- Pesci: squalo, trota, salmone, carpa.
Se l'animale non appartiene a nessuna delle categorie sopra elencate,  mostrare un messaggio indicante che il programma non è in grado di classificare l'animale inserito.'''

animale = input("inserisci il nome di un animale: ")

match animale:
    case "cane" | "gatto" | "cavallo" | "elefante" | "leone":
        print(f"{animale.categoria()} è un Mammifero. ")
    case "serpente" | "lucertola" | "tartaruga" | "coccodrillo":
        print(f"{animale.categoria()} è un Rettile.")
    case "acquila" | "pappagallo" | "gufo" | "falco":
        print (f"{animale.categoria()} è un uccello.")
    case "squalo" | "trota" | "salmone" | "carpa":
        print(f"{animale.categoria()} è un pesce.")
    case _:
        print(f"Non sono riuscito a classificare l'animale '{animale}'.")
