from datetime import datetime
import json, time

def check_year(year):
    if int(year)>0:
        try:
            with open("finances.json", "r") as infile:
                finances = json.load(infile)
                
                if year in finances:
                    income = expense = 0
                    for entry in finances[str(year)]: #for 2024 in finances.json
                        value = int(entry['value'])
                        print(entry['name'] + ": " + str(value))
                        if entry['type'] == "Uscita":
                            expense += value
                        elif entry['type'] == "Entrata":
                            income += value
                    print("Soldi spesi:" + str(expense))
                    print("Soldi guadagnati: " + str(income)+"\n")
                    return True
                else:
                    print("L'anno selezionato non esiste\n")
                    time.sleep(1.5)
                    return False
                    
        except FileNotFoundError:
            print("File non esistente")
        

def view_financial_report():
    year = input("Per quale anno vuoi visualizzare il tuo resoconto? ")
    if(not(check_year(year))):
        view_financial_report()