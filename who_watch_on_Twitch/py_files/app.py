# Importa le librerie necessarie
import os
import hashlib
import threading
import tkinter as tk
from PIL import Image, ImageTk
import test as t
import image_test as img_t
import read_file as rf
import requests
from io import BytesIO
import webbrowser
from pyfonts import load_font 
import sys

font = load_font(
   font_url="https://github.com/google/fonts/blob/main/apache/ultra/Ultra-Regular.ttf?raw=true"
)

streamers = rf.get_streamers_from_file()
print(streamers)

root = tk.Tk()
root.title("Chi vuoi guardare oggi?")
root.geometry("500x400")
root.configure(background="#833dff")

if getattr(sys, 'frozen', False):
    icon = Image.open("twitch.png")
else:
    icon = Image.open("py_files\\dist\\twitch.png")


icon_p = ImageTk.PhotoImage(icon)
root.wm_iconphoto(False, icon_p)
root.anchor("center")

main_frame = tk.Frame(root, background="#944CFF", width=470, height=370)
main_frame.grid(row=0, column=0, sticky="nsew")
main_frame.grid_propagate(False)
main_frame.grid_rowconfigure(0, weight=0)
main_frame.grid_columnconfigure(0, weight=1)

label = tk.Label(main_frame, text="Chi vuoi guardare oggi?", font=(font, 24, 'bold'), foreground="white", background="#944CFF", anchor='center')
label.grid(row=0, column=0, columnspan=4, rowspan=1, sticky="nsew")

CACHE_DIR = "image_cache"
if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)

def get_cached_image(url):
    hashed_url = hashlib.md5(url.encode('utf-8')).hexdigest()
    cached_image_path = os.path.join(CACHE_DIR, f"{hashed_url}.png")
    if os.path.exists(cached_image_path):
        return Image.open(cached_image_path)

    response = requests.get(url)
    if response.status_code == 200:
        image_data = BytesIO(response.content)
        image = Image.open(image_data).convert("RGBA")
        rounded_image = img_t.circle_image(image)
        rounded_image.save(cached_image_path)
        return rounded_image

    print(f"Errore nel caricamento dell'immagine: {url}")
    return None

def load_image(button, i):
    tw_image = t.get_streamer_info(1, streamers[i])
    if tw_image:
        image = get_cached_image(tw_image)
        if image:
            img_resized = image.resize((120, 120))
            new_img = ImageTk.PhotoImage(img_resized)
            main_frame.after(0, button.config, {'image': new_img, 'text': ""})
            button.new_img = new_img

# Variabile per tenere traccia se il pulsante è stato premuto
is_pressed = False

def on_button_press(event, streamer_name):
    global is_pressed
    is_pressed = True
    event.widget.bind("<Leave>", lambda e: set_button_release())

def set_button_release():
    global is_pressed
    is_pressed = False

def go_to_streamer(streamer_name):
    if is_pressed:
        channel_url = f"https://www.twitch.tv/{streamer_name}"
        webbrowser.open(channel_url)

#944CFF
def create_btn():
    images = []
    for i, streamer in enumerate(streamers):
        row, col = divmod(i, 2)
        
        streamer_frame = tk.Frame(main_frame, background="#944CFF")
        streamer_frame.grid(row=row*2+1, column=col, padx=50)
        
        streamer_label = tk.Label(streamer_frame, text=streamer, font=(font, 16), background="#944CFF", foreground="white", anchor="center")
        streamer_label.grid(row=row*2, column=col+1, sticky="nsew")
                
        button = tk.Label(streamer_frame, text="Caricamento", borderwidth=0, background="#944CFF", cursor="hand2", anchor="center")
        button.bind("<ButtonPress-1>", lambda event, streamer_name=streamer: on_button_press(event, streamer_name))
        button.bind("<ButtonRelease-1>", lambda event, streamer_name=streamer: go_to_streamer(streamer_name))

        button.grid(row=row*2+1, column=col+1, pady=(0, 20), sticky="nsew")
        

        threading.Thread(target=load_image, args=(button, i)).start()
        images.append(None)

    root.images = images

create_btn()
root.mainloop()
