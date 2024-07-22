from tkinter import *
import random
import string

def create_password():
    alphabet = string.ascii_letters + string.punctuation
    
    input_length = psw_length.get()
    print(input_length)


    i = 0
    password = ""   
    while i < int(input_length):
        password += random.choice(alphabet)
        i += 1

    print(password)
    Label(main_frame, text="Password generata: ").grid(row=3, column=0, padx=5, pady=5)
    copiable_text = StringVar(value=password)
    generated_password = Entry(main_frame, textvariable=copiable_text)
    generated_password.grid(row=3, column=1, padx=5, pady=5)
    return password



root = Tk()  # create root window
root.title("Password generator")

# Create Frame widget
main_frame = Frame(root, width=500, height=500)
main_frame.grid(row=0, column=0, padx=10, pady=5)

main_title = Label(main_frame, text="Password Generator").grid(row=0, columnspan=2, padx=5, pady=5)

Label(main_frame, text="Length").grid(row=1, column=0, padx=5, pady=5)

psw_length = Entry(main_frame, width=30)
psw_length.grid(row=1, column=1)

button = Button(main_frame, text="Crea password", command=create_password)
button.grid(row=2, columnspan=2)

root.mainloop()