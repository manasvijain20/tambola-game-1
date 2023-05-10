import socket
from tkinter import *
from threading import Thread
import random
from PIL import ImageTk, Image

SERVER = None
PORT = None
IP_ADDRESS = None
playerName = None
nameEntry = None
nameWindow = None
canvas1 = None
screen_width = None
screen_height = None

def askPlayerName():
    global playerName
    global nameEntry
    global nameWindow
    global canvas1
    global screen_height
    global screen_width

    nameWindow  = Tk()
    nameWindow.title("Tambola")
    nameWindow.geometry('800x600')

    screen_width = nameWindow.winfo_screenwidth()
    screen_height = nameWindow.winfo_screenheight()

    bg = ImageTk.PhotoImage(file = "./background.png")

    canvas1 = Canvas( nameWindow, width = 500,height = 500)
    canvas1.pack(fill = "both", expand = True)
    canvas1.create_image( 0, 0, image = bg, anchor = "nw")
    canvas1.create_text( screen_width/3, screen_height/5, text = "Enter Name", font=("Chalkboard SE",50), fill="black")

    nameEntry = Entry(nameWindow, width=15, justify='center', font=('Chalkboard SE', 30), bd=5, bg='white')
    nameEntry.place(x = screen_width/2.8 - 220, y=screen_height/5.5 + 100)

    button = Button(nameWindow, text="Save", font=("Chalkboard SE", 30),width=11, command=saveName, height=2, bg="#80deea", bd=3)
    button.place(x = screen_width/3.1 - 130, y=screen_height/2 - 30)

    nameWindow.resizable(True, True)
    nameWindow.mainloop()

def saveName():
    global SERVER
    global playerName
    global nameWindow
    global nameEntry

    playerName = nameEntry.get()
    nameEntry.delete(0, END)
    nameWindow.destroy()

    SERVER.send(playerName.encode())

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    PORT  = 5500
    IP_ADDRESS = '127.0.0.1'

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))
    askPlayerName()

setup()
