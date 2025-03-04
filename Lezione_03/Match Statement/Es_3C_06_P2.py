'''Esercizio 3C-6. Modificare il codice dell'esercizio 3C-4, affinchè si possa scrivere un codice python che consenta all'utente di inserire il nome di un animale ed un habitat. Quando il codice dell'esercizo 3C-4 classifica l'animale inserito in una delle categorie tra mammiferi, rettili, uccelli o pesci, oltre a mostrare un messaggio a schermo, deve salvare tale categoria in una variabile animal_type. Se l'animale inserito non è classificabile in una delle quattro categorie proposte, il valore di animal_type sarà ' "unknown".
Inserire, poi, in un dizionario il nome dell'animale, la categoria a cui esso appartiene (animal_type) e l'habitat.
Verificare con un match statement se l'animale e la categoria a cui esso appartiene possano vivere nell'habitat inserito; dunque, verificare:
- se l'animale può vivere nell'habitat specificato, stampare un messaggio appropriato.
- se l'habitat non è compatibile con l'habitat specificato, stampare un avviso.
- Se l'animale o l'habitat non sono riconosciuti, stampare un messaggio di errore.
Le categorie di classificazione devono essere:
- Mammiferi: cane, gatto, cavallo, elefante, leone, balena, delfino.
- Rettili: serpente, lucertola, tartaruga, coccodrillo.
- Uccelli: aquila, pappagallo, gufo, falco, cigno, anatra, gallina, tacchino.
- Pesci: squalo, trota, salmone, carpa.
Categorie di habitat:
- acqua
- aria
- terra
NOTA.
Il codice deve produrre un risultato sensato, ovvero che l'animale inserito possa effettivamente vivere nell'habitat specificato.
Tenere in considerazione il fatto che alcuni animali tra quelli specificati possono vivere in più di un habitat, mentre altri solo in uno.
Suggeirmento: può essere utile per coprire tutti i possibili casi implementare istruzioni match annidate.'''

mammiferi = ('cane', 'gatto', 'cavallo', 'elefante', 'leone', 'balena', 'delfino')
rettili = ( 'serpente', 'lucertola', 'tartaruga', 'coccodrillo')
uccelli = ('aquila', 'pappagallo', 'gufo', 'falco', 'cigno', 'anatra', 'gallina', 'tacchino')
pesci = ('squalo', 'trota', 'salmone', 'carpa')

animale = input("inserisci il nome di un animale: ")
habitat = input(f"Digita l'habitat in cui vive l'animale {animale}:")

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


if animale in mammiferi:
    animal_type = 'Mammiferi'
elif animale in rettili:
    animal_type = 'Rettili'
elif animale in uccelli:
    animal_type = 'Uccelli'
elif animale in pesci:
    animal_type = 'Pesci'
else:
    animal_type = 'unknown'

dizionario_animale = {'nome': animale, 'categoria': animal_type, 'habitat': habitat}

if animal_type == "unknown":
    print(f"Non so dire in quale categoria classificare l'animale {animale}!")
    print(f"Non sono in grado di fornire informazioni sull'habitat {habitat}.")

else:
    print(f"{animale.capitalize()} appartiene alla categoria dei {animal_type}!")
    if animal_type == 'Mammiferi':
        if habitat == "terra" or habitat == "acqua":
            print(f"L'animale {animale} è uno dei mammiferi che può vivere in {habitat}!")
        else:
            print(f"Non ho mai visto l'animale {animale} vivere nell'habitat {habitat}.")
    elif animal_type == 'Rettili':
        if habitat == "terra":
            print(f"L'animale {animale} è uno dei rettili che può vivere in terra!")
        else:
            print(f"Non ho mai visto l'animale {animale} vivere nell'habitat {habitat}.")
    elif animal_type == 'Uccelli':
        if habitat == "aria":
            print(f"L'animale {animale} è uno degli uccelli che può vivere in aria!")
        else:
            print(f"Non ho mai visto l'animale {animale} vivere nell'habitat {habitat}.")
    elif animal_type == 'Pesci':
        if habitat == "acqua":
            print(f"L'animale {animale} è uno dei pesci che può vivere in acqua!")
        else:
            print(f"Non ho mai visto l'animale {animale} vivere nell'habitat {habitat}.")

