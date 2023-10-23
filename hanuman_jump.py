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
levels=ImageTk.PhotoImage(file="IMAGES/levels.png")
back=ImageTk.PhotoImage(file="IMAGES/back.png")
#___________HELP_INSTRUCTION________
instruction_img=Image.open("IMAGES/instruction.png")
instruction_img_size=instruction_img.resize((500,600))
instruct=ImageTk.PhotoImage(instruction_img_size)
#______LEVELS________
bg_levels=Image.open("IMAGES/levels.png")
bg_levels_size=bg_levels.resize((WINDOW_WIDTH,WINDOW_HEIGHT))
background_levels=ImageTk.PhotoImage(bg_levels_size)
#________ALL_LEVELS_bg__________
choose=Image.open("IMAGES/bg.png")
choose_size=choose.resize((WINDOW_WIDTH,WINDOW_HEIGHT))
levels_bg=ImageTk.PhotoImage(choose_size)
#______________HOME PAGE___________
def home():
    canvas.delete("all")
    canvas.create_image(0,0,image=bg,anchor="nw")
    #__________START_BTN_________
    canvas.create_image(650,410,image=levels,anchor="nw",tags="start")
    canvas.create_text(730,450,text="START",font=("Kavoon", 25, "bold"), fill="black",tags="start")
    #__________HELP_BTN_______
    canvas.create_image(650,500,image=levels,anchor="nw",tags="help")
    canvas.create_text(730,540,text="HELP",font=("Kavoon", 30, "bold"), fill="black",tags="help")
    #__________EXIT_BTN_______________
    canvas.create_image(650,590,image=levels,anchor="nw",tags="exit")
    canvas.create_text(730,630,text="EXIT",font=("Kavoon", 30, "bold"), fill="black",tags="exit")
#_______START_BUTTON_______
def start(event):
    alllevels()
#______EXIT_BUTTON_______
def exit(event):
    window.destroy()
#________BACKLEVEL_______
def backlevel(event):
    home()
#_______HEP_BTN__________
def help(event):
    canvas.create_image(1, 0, image=levels_bg, anchor="nw")
    canvas.create_image(400,150, image = instruct, anchor="nw")
    canvas.create_image(25, 10, image=back, anchor="nw", tags="back")
#________________KEY EVENTS_______________
canvas.tag_bind=("start","<Button-1>",start)
canvas.tag_bind=("help","<Button-1>",help)
canvas.tag_bind=("exit","<Button-1>",exit)
#========================= DISPLAY WINDOW =================
canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
window.mainloop()