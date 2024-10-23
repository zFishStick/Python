from add_income import *
from add_expense import *
from view_financial_report import *
import time

exit_program = True

def switch_case(op):
    global exit_program
    if op == "1":
        add_income()
    elif op == "2":
        add_expense()
    elif op == "3":
        view_financial_report()
    elif op == "4":
        exit_program = False
    else:
        print("Comando non riconosciuto, riprova.\n")

while exit_program:
    operation = input("Scegli un'operazione:" +
                      "\n 1) Inserisci entrata" +
                      "\n 2) Inserisci uscita" +
                      "\n 3) Visualizza resoconto" +
                      "\n 4) Esci" +
                      "\n -> ")

    switch_case(operation)
    time.sleep(1)
