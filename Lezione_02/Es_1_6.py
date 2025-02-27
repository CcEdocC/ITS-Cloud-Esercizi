# Menu ITS
menu = {
    "Pizza": 9.00,
    "Pasta": 10.50,
    "Zuppa": 7.00,
    "Hamburger": 15.50,
    "Cotoletta": 10.00,
    "Salmone": 20.20,
    "Patatine Fritte": 5.50,
    "Patate al forno": 5.50,
    "Verdura del giorno": 7.00,
    "Cheesecake": 6.00,
    "Tiramisu'": 6.00,
    "Focaccia con Nutella": 6.00,
    "Coca Cola": 3.50,
    "Acqua": 1.50,
    "Vino": 5.00
}

# Ordine del cliente
ordine = {
    "Primo": "Pizza",
    "Secondo": "Hamburger",
    "Contorno": "Patatine Fritte",
    "Bevanda": "Coca Cola",
    "Dolce": "Cheesecake"
}

# Calcolo del conto totale
conto_totale = 0
for item in ordine.values():
    conto_totale += menu[item]

# Visualizzazione del conto
print("Ordine del cliente:")
for categoria, piatto in ordine.items():
    print(f"{categoria}: {piatto} - {menu[piatto]:.2f} euro")

print(f"Totale da pagare: {conto_totale:.2f} euro")