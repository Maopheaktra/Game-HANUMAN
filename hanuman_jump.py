#________________________IMPORT______________________
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import font
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
window.attributes('-fullscreen',True)
window.title("HANUMAN JUMP")
frame=tk.Frame(window,width=WINDOW_WIDTH,height=WINDOW_HEIGHT)
canvas=tk.Canvas(frame,width=WINDOW_WIDTH,height=WINDOW_HEIGHT)

#____________IMPORT IMAGES____________
bg=ImageTk.PhotoImage(file="IMAGES/bg_home.png")
player=ImageTk.PhotoImage(file="IMAGES/player.png")
levels=ImageTk.PhotoImage(file="IMAGES/levels.png")
back=ImageTk.PhotoImage(file="IMAGES/back.png")
level_3=ImageTk.PhotoImage(file="IMAGES/level-3.png")
stone=ImageTk.PhotoImage(file="IMAGES/stone.png")
small_stone=ImageTk.PhotoImage(file="IMAGES/small_stone.png")
thorn=ImageTk.PhotoImage(file="IMAGES/thorns.png")
levelsremove=ImageTk.PhotoImage(file="IMAGES/remove.png")
#__________REMOVE________
level_file=Image.open("IMAGES/remove.png")
level_file_size=level_file.resize((50,50))
levelsremove=ImageTk.PhotoImage(level_file_size)
#___________THORN__________
thorn_file=Image.open("IMAGES/thorns.png")
thorn_file_size=thorn_file.resize((70,50))
thorn=ImageTk.PhotoImage(thorn_file_size)
#__________Tiger__________
tiger_file=Image.open("IMAGES/tiger.png")
tiger_file_size=tiger_file.resize((150,100))
tiger=ImageTk.PhotoImage(tiger_file_size)
#______________GRASS__________
grasses=Image.open("IMAGES/grass.png")
grasses_size=grasses.resize((300,200))
grass_level3=ImageTk.PhotoImage(grasses_size)
#____________Level-3_____________
l3=Image.open("IMAGES/level-3.png")
l3_size=l3.resize((WINDOW_WIDTH,WINDOW_HEIGHT))
level_3=ImageTk.PhotoImage(l3_size)
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
def remove(event):
    alllevels()
#_______HEP_BTN__________
def help(event):
    canvas.create_image(1, 0, image=levels_bg, anchor="nw")
    canvas.create_image(400,150, image = instruct, anchor="nw")
    canvas.create_image(25, 10, image=back, anchor="nw", tags="back")
# _____________________LEVELS BUTTON______________________
def alllevels():
    canvas.delete("all")
    canvas.create_image(0,0,image=levels_bg,anchor="nw")
    canvas.create_text(700,200,text="CHOOSE LEVELS",font=("Kavoon", 50, "bold"), fill="black",tags="levels")
    #_______________LEVEL-1_______________
    canvas.create_image(650,410,image=levels,anchor="nw",tags="level1")
    canvas.create_text(725,445,text="LEVEL1",font=("Kavoon", 20, "bold"), fill="black",tags="level1")
    #__________________LEVEL-2______________
    canvas.create_image(650,500,image=levels,anchor="nw",tags="level2")
    canvas.create_text(725,535,text="LEVEL2",font=("Kavoon", 20, "bold"), fill="black",tags="level2")
    #______________LEVEL-3__________
    canvas.create_image(650,590,image=levels,anchor="nw",tags="level3")
    canvas.create_text(725,625,text="LEVEL3",font=("Kavoon", 20, "bold"), fill="black",tags="level3")
    #___________BACK_HOME___________
    canvas.create_image(10,10,image=back,anchor="nw",tags="back")
#________________LEVEL-3__________________
def level3(event):
    canvas.delete("all")
    global playerx
    canvas.create_image(0,0,image=level_3,anchor="nw")
    #_____________ground__________________
    canvas.create_image(0,650,image=grass_level3,anchor="nw",tags="grass")
    canvas.create_image(290,650,image=grass_level3,anchor="nw",tags="grass")
    canvas.create_image(580,650,image=grass_level3,anchor="nw",tags="grass")
    canvas.create_image(870,650,image=grass_level3,anchor="nw",tags="grass")
    canvas.create_image(1070,650,image=grass_level3,anchor="nw",tags="grass")
    #____________Stone______________-
    canvas.create_image(130,490,image=stone,anchor="nw",tags="stone")
    canvas.create_image(420,300,image=stone,anchor="nw",tags="stone")
    canvas.create_image(940,500,image=stone,anchor="nw",tags="stone")
    canvas.create_image(740,200,image=small_stone,anchor="nw",tags="stone")
    canvas.create_image(840,400,image=small_stone,anchor="nw",tags="stone")
    canvas.create_image(1250,350,image=small_stone,anchor="nw",tags="stone")
    #______________Tiger__________________
    canvas.create_image(320,430,image=tiger,anchor="nw",tags="tiger")
    #______________Thorns____________________
    canvas.create_image(600,280,image=thorn,anchor="nw",tags="thorn")
    canvas.create_image(650,280,image=thorn,anchor="nw",tags="thorn")
    canvas.create_image(700,280,image=thorn,anchor="nw",tags="thorn")
    canvas.create_image(780,170,image=thorn,anchor="nw",tags="thorn")
    canvas.create_image(1000,480,image=thorn,anchor="nw",tags="thorn")
    #___________BACK TO ALL LEVEL_____________
    canvas.create_image(10,10,image=levelsremove,anchor="nw",tags="remove")

#__________________KEY EVENTS______________________
canvas.tag_bind("start","<Button-1>", start)
canvas.tag_bind("exit","<Button-1>", exit)
canvas.tag_bind("help","<Button-1>", help)
canvas.tag_bind("back","<Button-1>", backlevel)
canvas.tag_bind("level3","<Button-1>",level3)
canvas.tag_bind("remove","<Button-1>",remove)
home()
#========================= DISPLAY WINDOW =================
canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
window.mainloop()