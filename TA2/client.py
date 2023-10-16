import socket
from tkinter import *
from  threading import Thread
import random
from PIL import ImageTk, Image

screen_width = None
screen_height = None

SERVER = None
PORT = None
IP_ADDRESS = None
canvas1 = None

player_name = None
name_entry = None
name_window = None

def ask_player_name():
    global player_name, name_entry, name_window, canvas1, font_size
    name_window  = Tk()
    name_window.title("Ludo Ladder")

    # Get screen width and height in respective variables
    screen_width = name_window.winfo_screenwidth()
    screen_height = name_window.winfo_screenheight()

    # Create responsive font_size as int value of screen_width*0.03
    font_size = int(screen_width * 0.03)

    image = Image.open("./assets/background.png")
    # Use screen_width and screen_height to resize the image to screen size
    image = image.resize((screen_width, screen_height))
    bg = ImageTk.PhotoImage(image)
    
    # Use screen_width and screen_height to resize the canvas to screen size
    canvas1 = Canvas( name_window, width = screen_width,height = screen_width)
    canvas1.pack(fill = "both", expand = True)
    canvas1.create_image( 0, 0, image = bg, anchor = "nw")
    # Use font_size, screen_width, screen_height to make size and position responsive
    canvas1.create_text( screen_width/2, screen_height/5, text = "Enter Name", font=("Chalkboard SE",font_size), fill="white")

    name_entry = Entry(name_window,  justify='center', font=('Chalkboard SE', 10), bd=5, bg='white')
    name_entry.place(relx = 0.25, rely=0.3, relwidth = 0.5)
    
    button = Button(name_window, text="Save", font=("Chalkboard SE", 10), height=1, bg="#80deea", bd=3)
    button.place(relx= 0.33, rely=0.5, relwidth = 0.34)

    name_window.resizable(True, True)
    name_window.mainloop()

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    PORT  = 5000
    IP_ADDRESS = '127.0.0.1'

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    # Call ask_player_name() method
    ask_player_name()

setup()
