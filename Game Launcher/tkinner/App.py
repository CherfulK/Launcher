import tkinter as tk
from tkinter.constants import CENTER, OUTSIDE
from typing import Collection
import PyPDF2
from PIL import Image, ImageTk
import os, time


root = tk.Tk()

canvas = tk.Canvas(root, width=400, height=250, OUTSIDE=None)
canvas.grid(columnspan=3)

def open_file():
    print("Launching!")
    time.sleep(3)
    os.system("valorant.bat")

def open_file2():
    print("Launching!")
    time.sleep(3)
    os.system("RL.bat")

def open_file3():
    print("Launching!")
    time.sleep(3)
    os.system("fnbr.bat")

Valo = tk.Label(root, text="Valoant", font="Ariel")
Valo.grid(columnspan=3, column=1, row=1)






#Valorant Button
valorant_text = tk.StringVar()
valorant_btn = tk.Button(root, textvariable=valorant_text, command=lambda:open_file(), font="Ariel", bg="RED", fg="white", height=2, width=23)
valorant_text.set("Launch")
valorant_btn.grid(column=1, row=2)

#Rocket League Button
RocketLeague_text = tk.StringVar()
RL_btn = tk.Button(root, textvariable=RocketLeague_text, command=lambda:open_file2(), font="Ariel", bg="BLUE", fg="white", height=2, width=23)
RocketLeague_text.set("Launch")
RL_btn.grid(column=0, row=2)

#fn Button
fn_text = tk.StringVar()
fn_btn = tk.Button(root, textvariable=fn_text, command=lambda:open_file3(), font="Ariel", bg="PURPLE", fg="white", height=2, width=23)
fn_text.set("Launch")
fn_btn.grid(column=3, row=2)

root.mainloop()