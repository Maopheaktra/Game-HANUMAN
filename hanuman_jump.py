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
    canvas.create_image(570,570,image=exit,anchor="nw",tags="exit")
home()
player=ImageTk.PhotoImage(file="IMAGES/player.png")
bg_game = ImageTk.PhotoImage(file="IMAGES/bg_game.jpg")
wall1_game = ImageTk.PhotoImage(file="IMAGES/wall1.png")
wall2_game = ImageTk.PhotoImage(file="IMAGES/wall2.png")
wall3_game = ImageTk.PhotoImage(file="IMAGES/wall3.png")
kill_game = ImageTk.PhotoImage(file="IMAGES/kill1.png")
kill1_game = ImageTk.PhotoImage(file="IMAGES/kill2.png")
stone_game =ImageTk.PhotoImage(file ="IMAGES/stone.png")
win_game =ImageTk.PhotoImage(file ="IMAGES/winer.png")
god_game =ImageTk.PhotoImage(file ="IMAGES/god.png")
winer1_game =ImageTk.PhotoImage(file ="IMAGES/winer1.png")
winer2_game =ImageTk.PhotoImage(file ="IMAGES/player.png")
winer3_game =ImageTk.PhotoImage(file ="IMAGES/snake.png")
banana_game =ImageTk.PhotoImage(file ="IMAGES/banana.png")
banana1_game =ImageTk.PhotoImage(file ="IMAGES/banana1.png")
dragon_game =ImageTk.PhotoImage(file ="IMAGES/dragon.png")


#===============BG-LEVEL-2=============
l2=Image.open("IMAGES/bg_game.jpg")
l2_size=l2.resize((WINDOW_WIDTH,WINDOW_HEIGHT))
bg_l2=ImageTk.PhotoImage(l2_size)

l3=Image.open("IMAGES/wall1.png")
l3_size = l3.resize((200,110))
bg_l3 = ImageTk.PhotoImage(l3_size)

l4=Image.open("IMAGES/wall2.png")
l4_size = l4.resize((220,100))
bg_l4 = ImageTk.PhotoImage(l4_size)

l5=Image.open("IMAGES/wall3.png")
l5_size = l5.resize((250,100))
bg_l5 = ImageTk.PhotoImage(l5_size)

l6=Image.open("IMAGES/kill1.png")
l6_size = l6.resize((100,60))
bg_l6 = ImageTk.PhotoImage(l6_size)

l7=Image.open("IMAGES/kill2.png")
l7_size = l7.resize((180,100))
bg_l7 = ImageTk.PhotoImage(l7_size)

l8=Image.open("IMAGES/stone.png")
l8_size = l8.resize((370,60))
bg_l8 = ImageTk.PhotoImage(l8_size)

l9=Image.open("IMAGES/winer.png")
l9_size = l9.resize((250,300))
bg_l9 = ImageTk.PhotoImage(l9_size)

l10=Image.open("IMAGES/god.png")
l10_size = l10.resize((100,80))
bg_l10 = ImageTk.PhotoImage(l10_size)

l11=Image.open("IMAGES/winer1.png")
l11_size = l11.resize((90,70))
bg_l11 = ImageTk.PhotoImage(l11_size)

l12=Image.open("IMAGES/player.png")
l12_size = l12.resize((90,70))
bg_l12 = ImageTk.PhotoImage(l12_size)

l13=Image.open("IMAGES/snake.png")
l13_size = l13.resize((100,80))
bg_l13 = ImageTk.PhotoImage(l13_size)

l14=Image.open("IMAGES/banana.png")
l14_size = l14.resize((190,130))
bg_l14 = ImageTk.PhotoImage(l14_size)

l15=Image.open("IMAGES/banana1.png")
l15_size = l15.resize((60,30))
bg_l15 = ImageTk.PhotoImage(l15_size)

l16=Image.open("IMAGES/dragon.png")
l16_size = l16.resize((150,90))
bg_l16 = ImageTk.PhotoImage(l16_size)
#______________HOME PAGE___________
# def home():
#     canvas.create_image(0,0,image=bg,anchor="nw")
#     canvas.create_image(600,410,image=start,anchor="nw",tags="start")
#     canvas.create_image(590,500,image=help,anchor="nw",tags="help")
#     canvas.create_image(570,570,image=exit,anchor="nw",tags="exit")
# home()
#__________LEVEL-2___________
def level_2():
    canvas.create_image(1,0,image = bg_l2, anchor = "nw")
    canvas.create_image(300,350, image= bg_l3, anchor = "nw",tags="PLATFORM")
    canvas.create_image(150,440, image= bg_l3, anchor = "nw",tags="PLATFORM")
    canvas.create_image(370,320, image= bg_l6, anchor = "nw",tags="PLATFORM")
    canvas.create_image(700,400, image= bg_l4, anchor = "nw",tags="PLATFORM")
    canvas.create_image(800,400, image= bg_l4, anchor = "nw",tags="PLATFORM")
    canvas.create_image(970,520, image= bg_l5, anchor = "nw",tags="PLATFORM")
    canvas.create_image(400,500, image= bg_l4, anchor = "nw",tags="PLATFORM")
    canvas.create_image(460,250, image= bg_l5, anchor = "nw",tags="PLATFORM")
    canvas.create_image(660,250, image= bg_l5, anchor = "nw",tags="PLATFORM")
    canvas.create_image(1040,450, image= bg_l7, anchor = "nw",tags="PLATFORM")
    canvas.create_image(480,190, image= bg_l10, anchor = "nw",tags="PLATFORM")

    canvas.create_image(1700,400, image= bg_l4, anchor = "nw",tags="PLATFORM")
    canvas.create_image(1600,500, image= bg_l4, anchor = "nw",tags="PLATFORM")
    canvas.create_image(1500,600, image= bg_l4, anchor = "nw",tags="PLATFORM")
    canvas.create_image(1330,410, image= bg_l4, anchor = "nw",tags="PLATFORM")
    

    canvas.create_image(1100,300, image= bg_l5, anchor = "nw",tags="PLATFORM")


    canvas.create_image(600,220, image= bg_l15, anchor = "nw",tags="PLATFORM")
    canvas.create_image(640,220, image= bg_l15, anchor = "nw",tags="PLATFORM")
    canvas.create_image(660,220, image= bg_l15, anchor = "nw",tags="PLATFORM")
    canvas.create_image(690,220, image= bg_l15, anchor = "nw",tags="PLATFORM")

    canvas.create_image(180,410, image= bg_l15, anchor = "nw",tags="PLATFORM")
    canvas.create_image(220,410, image= bg_l15, anchor = "nw",tags="PLATFORM")
    canvas.create_image(260,410, image= bg_l15, anchor = "nw",tags="PLATFORM")
    canvas.create_image(270,410, image= bg_l15, anchor = "nw",tags="PLATFORM")

    canvas.create_image(410,470, image= bg_l15, anchor = "nw",tags="PLATFORM")
    canvas.create_image(450,470, image= bg_l15, anchor = "nw",tags="PLATFORM")
    canvas.create_image(480,470, image= bg_l15, anchor = "nw",tags="PLATFORM")
    canvas.create_image(500,470, image= bg_l15, anchor = "nw",tags="PLATFORM")

    canvas.create_image(720,370, image= bg_l15, anchor = "nw",tags="PLATFORM")
    canvas.create_image(760,370, image= bg_l15, anchor = "nw",tags="PLATFORM")
    canvas.create_image(790,370, image= bg_l15, anchor = "nw",tags="PLATFORM")
    canvas.create_image(810,370, image= bg_l15, anchor = "nw",tags="PLATFORM")

    canvas.create_image(1150,280, image= bg_l15, anchor = "nw",tags="PLATFORM")
    canvas.create_image(1200,280, image= bg_l15, anchor = "nw",tags="PLATFORM")
    canvas.create_image(1240,280, image= bg_l15, anchor = "nw",tags="PLATFORM")
    canvas.create_image(1290,280, image= bg_l15, anchor = "nw",tags="PLATFORM")

    canvas.create_image(1350,380, image= bg_l15, anchor = "nw",tags="PLATFORM")
    canvas.create_image(1400,380, image= bg_l15, anchor = "nw",tags="PLATFORM")
    canvas.create_image(1440,380, image= bg_l15, anchor = "nw",tags="PLATFORM")
    canvas.create_image(1490,380, image= bg_l15, anchor = "nw",tags="PLATFORM")

    

# __________grass_______________________________________

    canvas.create_image(0,694, image= bg_l8, anchor = "nw",tags="PLATFORM")
    canvas.create_image(100,694, image= bg_l8, anchor = "nw",tags="PLATFORM")
    canvas.create_image(200,694, image= bg_l8, anchor = "nw",tags="PLATFORM")
    canvas.create_image(300,694, image= bg_l8, anchor = "nw",tags="PLATFORM")
    canvas.create_image(400,694, image= bg_l8, anchor = "nw",tags="PLATFORM")
    canvas.create_image(700,694, image= bg_l8, anchor = "nw",tags="PLATFORM")
    canvas.create_image(800,694, image= bg_l8, anchor = "nw",tags="PLATFORM")
    canvas.create_image(900,694, image= bg_l8, anchor = "nw",tags="PLATFORM")
    canvas.create_image(1000,694, image= bg_l8, anchor = "nw",tags="PLATFORM")
    canvas.create_image(1050,694, image= bg_l8, anchor = "nw",tags="PLATFORM")
    canvas.create_image(1050,694, image= bg_l8, anchor = "nw",tags="PLATFORM")
    canvas.create_image(1000,694, image= bg_l8, anchor = "nw",tags="PLATFORM")
    canvas.create_image(1000,694, image= bg_l8, anchor = "nw",tags="PLATFORM")
    canvas.create_image(1070,694, image= bg_l8, anchor = "nw",tags="PLATFORM")
    canvas.create_image(1370,694, image= bg_l8, anchor = "nw",tags="PLATFORM")
    canvas.create_image(1670,694, image= bg_l8, anchor = "nw",tags="PLATFORM")
    canvas.create_image(1970,694, image= bg_l8, anchor = "nw",tags="PLATFORM")
    canvas.create_image(1970,694, image= bg_l8, anchor = "nw",tags="PLATFORM")
    canvas.create_image(370,694, image= bg_l8, anchor = "nw",tags="PLATFORM")
    
    

    canvas.create_image(0,640, image= bg_l12, anchor = "nw",tags="PLATFORM")
    canvas.create_image(600,630, image= bg_l13, anchor = "nw",tags="PLATFORM")
    canvas.create_image(400,630, image= bg_l13, anchor = "nw",tags="PLATFORM")
    canvas.create_image(900,630, image= bg_l13, anchor = "nw",tags="PLATFORM")
    canvas.create_image(1000,630, image= bg_l13, anchor = "nw",tags="PLATFORM")
    canvas.create_image(800,630, image= bg_l13, anchor = "nw",tags="PLATFORM")
    canvas.create_image(750,150, image= bg_l14, anchor = "nw",tags="PLATFORM")

    canvas.create_image(830,350, image= bg_l16, anchor = "nw",tags="PLATFORM")

# ====================win place++++++++++++

    canvas.create_image(1740,130, image= bg_l9, anchor = "nw",tags="PLATFORM")
    canvas.create_image(1820,280, image= bg_l11, anchor = "nw",tags="PLATFORM")
#________________KEY EVENTS_______________
canvas.tag_bind=("start","<Button-1>",start)
canvas.tag_bind=("help","<Button-1>",help)
canvas.tag_bind=("exit","<Button-1>",exit)
#========================= DISPLAY WINDOW =================
canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
window.mainloop()