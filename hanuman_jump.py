#________________________IMPORT______________________
import tkinter as tk
from PIL import ImageTk, Image
#============================ CONSTANTS ============================
WINDOW_WIDTH=1420
WINDOW_HEIGHT=800
GRAVITY_FORCE = 9
JUMP_FORCE = 30
SPEED = 7
TIMED_LOOP = 6

#============================ VARIABLES ============================

keyPressed = []

#============================ GLOBAL ============================
score=0

#________________MAIN WINDOW________________
window=tk.Tk()
window.geometry(str(WINDOW_WIDTH)+ "x" + str(WINDOW_HEIGHT))
window.title("HANUMAN JUMP")
frame=tk.Frame(window,width=WINDOW_WIDTH,height=WINDOW_HEIGHT)
frame.pack()
canvas=tk.Canvas(frame,width=WINDOW_WIDTH,height=WINDOW_HEIGHT)
canvas.pack()

#____________IMPORT IMAGES____________
bg=ImageTk.PhotoImage(file="IMAGES/bg_home.png")
start=ImageTk.PhotoImage(file="IMAGES/start.png")
help=ImageTk.PhotoImage(file="IMAGES/help.png")
exit=ImageTk.PhotoImage(file="IMAGES/exit.png")
player=ImageTk.PhotoImage(file="IMAGES/player.png")

#______________HOME PAGE___________
def home():
    canvas.create_image(0,0,image=bg,anchor="nw")
    canvas.create_image(600,410,image=start,anchor="nw",tags="start")
    canvas.create_image(590,500,image=help,anchor="nw",tags="help")
    canvas.create_image(570,590,image=exit,anchor="nw",tags="exit")
home()

#________________KEY EVENTS_______________
canvas.tag_bind=("start","<Button-1>",start)
canvas.tag_bind=("help","<Button-1>",help)
canvas.tag_bind=("exit","<Button-1>",exit)
#========================= DISPLAY WINDOW =================
canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
window.mainloop()