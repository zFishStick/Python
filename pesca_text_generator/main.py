from tkinter import *
import customtkinter
import keyboard
from PIL import Image

mobile_width = 1080 / 3
mobile_height = 1920 / 3

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")        
        self.geometry(f"{int(mobile_width)}x{int(mobile_height)}")

        # Creazione del font usando CTkFont
        self.custom_font = customtkinter.CTkFont(family="Marykate", size=30, weight="bold")
        self.text_font = customtkinter.CTkFont(family="Bryndan_Write", size=24, weight="bold")
        
        self.auxFrame = customtkinter.CTkFrame(self,
                                            width=300,
                                            height=520,   
                                            corner_radius=16,                            
                                            fg_color="#f2b28c")
        self.auxFrame.place(relx=0.5, rely=0.05, anchor="n")
    
        self.textBox = self.create_textbox()
        self.create_title()
        self.create_button()
        
    # Title
    def create_title(self):
        
        self.label_frame = customtkinter.CTkFrame(self.textBox,
                                                    height=50,
                                                    width=250,
                                                    corner_radius=16,
                                                    fg_color="#d2665a",
                                                    #bg_color="#f2b28c"
                                                    )
        
        self.label_frame.place(relx=0.5, rely=0.01, anchor="n")
        
        self.title_label = customtkinter.CTkLabel(self.label_frame,
                                                  text="La Pesca del Giorno",
                                                  text_color="white",
                                                  font=self.custom_font,
                                                  #bg_color="#d2665a"
                                                  )
        self.title_label.place(relx=0.5, rely=0.25, anchor="n")
            
    # Textbox
    def create_textbox(self):
        self.textbox = customtkinter.CTkTextbox(self.auxFrame,
                                                width=290,
                                                height=490,
                                                corner_radius=16,
                                                font=self.text_font,
                                                fg_color="#f2b28c",
                                                text_color="black")
        
        self.textbox.insert("0.0", "")
        self.textbox.place(relx=0.5, rely=0.51, anchor="center")
        self.textbox.bind("<KeyPress>", self.prevent_backspace)
        
        self.my_image = customtkinter.CTkImage(light_image=Image.open('peach_king.png'), size=(220, 250))
        
        self.image_label = customtkinter.CTkLabel(self.auxFrame, image=self.my_image, text="")
        self.image_label.place(relx=0.5, rely=0.99, anchor="s")


    def prevent_backspace(self, event):
        current_position = self.textbox.index("insert")
        if keyboard.read_key() == "backspace" and current_position == "2.0":
            return "break"

        return None

    # Button
    def create_button(self):
        self.button = customtkinter.CTkButton(self,
                                              text="Scarica",
                                              font=self.custom_font,
                                              command=self.button_callback)
        self.button.place(relx=0.5, rely=0.9, anchor="n")

    def button_callback(self):
        print("button pressed")

app = App()
app.mainloop()
