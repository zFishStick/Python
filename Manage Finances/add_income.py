from datetime import datetime
import json

def check_date(data):
    date_format = "%d/%m/%Y"
    try:
        datetime.strptime(data, date_format)
        return True
    except ValueError:
        return False
    
def check_value(value):
    try:
        return int(value) > 0
    except ValueError:
        return False
    

def add_income():
    name = input("Nome: ")
    data = input("Data (gg/mm/aaaa): ")
    value = input("Valore: ")
    
    if check_date(data) and check_value(value):
        # Estrai l'anno dalla data
        year = data.split("/")[-1] #-1 indica l'ultimo elemento dell'array

        # Lettura del file esistente (se presente)
        try:
            with open("finances.json", "r") as infile:
                finances = json.load(infile)
        except FileNotFoundError:
            finances = {}  # Se il file non esiste, inizializza come dizionario vuoto

        # Se l'anno non esiste nel dizionario, lo creiamo come chiave con un array vuoto
        if year not in finances:
            finances[year] = []

        # Aggiungi la nuova entrata all'anno corrispondente
        new_entry = {
            "type": "Entrata",
            "name": name,
            "date": data,
            "value": int(value),
        }
        finances[year].append(new_entry)

        # Scrittura su file
        with open("finances.json", "w") as outfile:
            json.dump(finances, outfile, indent=4)
        
        print("Entrata aggiunta con successo!\n")
    else:
        print("Errore: data o valore non validi.\n")
