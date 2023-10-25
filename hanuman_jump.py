#________________________IMPORT______________________
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import font
from pygame import mixer
import time
#============================ CONSTANTS ============================

WINDOW_WIDTH=2000
WINDOW_HEIGHT=800
GRAVITY_FORCE = 9
JUMP_FORCE = 30
SPEED = 9
TIMED_LOOP = 10


#============================ VARIABLES ============================

keyPressed = []

#============================ GLOBAL ============================
score=0

#________________MAIN WINDOW________________
window=tk.Tk()
window.geometry(str(WINDOW_WIDTH)+ "x" + str(WINDOW_HEIGHT))
window.attributes('-fullscreen',True)
window.title("HANUMAN JUMP")
window.attributes('-fullscreen',True)
frame=tk.Frame(window,width=WINDOW_WIDTH,height=WINDOW_HEIGHT)
canvas=tk.Canvas(frame,width=WINDOW_WIDTH,height=WINDOW_HEIGHT)
frame.pack()
canvas=tk.Canvas(frame,width=WINDOW_WIDTH,height=WINDOW_HEIGHT,scrollregion=(0,0,2000,800))
canvas.pack()

#scrollbar
scrollbar_bottom = tk.Scrollbar(window, orient='horizontal', command=canvas.xview)
canvas.configure(xscrollcommand=scrollbar_bottom.set)
scrollbar_bottom.place(relx=0, rely=1, relwidth=1, anchor='sw')

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
player=ImageTk.PhotoImage(file="IMAGES/player.png")

wall1_game = ImageTk.PhotoImage(file="IMAGES/wall1.png")
wall2_game = ImageTk.PhotoImage(file="IMAGES/wall2.png")
wall3_game = ImageTk.PhotoImage(file="IMAGES/wall3.png")
kill_game = ImageTk.PhotoImage(file="IMAGES/kill1.png")
kill1_game = ImageTk.PhotoImage(file="IMAGES/kill2.png")
god_game =ImageTk.PhotoImage(file ="IMAGES/god.png")
winer1_game =ImageTk.PhotoImage(file ="IMAGES/winer1.png")
winer2_game =ImageTk.PhotoImage(file ="IMAGES/player.png")
winer3_game =ImageTk.PhotoImage(file ="IMAGES/snake.png")
banana_game =ImageTk.PhotoImage(file ="IMAGES/banana.png")
banana1_game =ImageTk.PhotoImage(file ="IMAGES/banana1.png")
dragon_game =ImageTk.PhotoImage(file ="IMAGES/dragon.png")
#======win place=====
winer_file=Image.open("IMAGES/winer.png")
winer_file_size=winer_file.resize((50,100))
win_game =ImageTk.PhotoImage(winer_file_size)
#=========BACKGROUND MENU=========
bg_game_file=Image.open("IMAGES/bg_game.jpg")
bg_game_file_size=bg_game_file.resize((WINDOW_WIDTH,WINDOW_HEIGHT))
bg_game=ImageTk.PhotoImage(bg_game_file_size)
#=======STONE LEVEL3==========
stone_file=Image.open("IMAGES/stone.png")
stone_file_size=stone_file.resize((100,30))
stone_game =ImageTk.PhotoImage(stone_file_size)
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

l14=Image.open("IMAGES/banana-tree.png")
l14_size = l14.resize((190,130))
bg_l14 = ImageTk.PhotoImage(l14_size)

l15=Image.open("IMAGES/banana1.png")
l15_size = l15.resize((60,30))
bg_l15 = ImageTk.PhotoImage(l15_size)

l16=Image.open("IMAGES/dragon.png")
l16_size = l16.resize((150,90))
bg_l16 = ImageTk.PhotoImage(l16_size)
# _____________________Bird_____________________________
bird1_file = Image.open("IMAGES/bird1.gif")
bird1_size = bird1_file.resize((150, 100))
bird1 = ImageTk.PhotoImage(bird1_size)
bird=canvas.create_image(640, 250,image = bird1, anchor = "nw",tags="PLATFORM") 
apsora_file = Image.open("IMAGES/apsora_winner.png")
apsora_size = apsora_file.resize((150, 150))
apsora = ImageTk.PhotoImage(apsora_size)

enemy_file = Image.open("IMAGES/enemy.png")
enemy_size = enemy_file.resize((100, 80))
enemy = ImageTk.PhotoImage(enemy_size)
#____________________Road___________________________
road_file = Image.open("IMAGES/road1.png")
road_size = road_file.resize((320, 50))
road = ImageTk.PhotoImage(road_size)
#____________________Banana____________________________
banana_file = Image.open("IMAGES/banana.png")
banana_size = banana_file.resize((50, 30))
banana = ImageTk.PhotoImage(banana_size)
#______________BG-LEVEL-1______________
bg_l1_file=Image.open("IMAGES/bg_l1.png")
bg_l1_file_size=bg_l1_file.resize((WINDOW_WIDTH,WINDOW_HEIGHT))
bg_l1=ImageTk.PhotoImage(bg_l1_file_size)
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
#____________________stone________________________________
stone1_file = Image.open("IMAGES/stone1.png")
stone1_size = stone1_file.resize((180, 130))
stone1 = ImageTk.PhotoImage(stone1_size)
#______________GRASS__________
grasses=Image.open("IMAGES/grass.png")
grasses_size=grasses.resize((300,200))
grass_level3=ImageTk.PhotoImage(grasses_size)
#____________Level-3_____________
l3=Image.open("IMAGES/level-3.png")
l3_size=l3.resize((WINDOW_WIDTH,WINDOW_HEIGHT))
level_3=ImageTk.PhotoImage(l3_size)
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
 #___________________Player_________________________________

def scroll_background():
    canvas.move(bg_l1_label1,-1,0)
    canvas.move(bg_l1_label2,-1,0)
    if canvas.coords(bg_l1_label1)[0]<-WINDOW_WIDTH:
        canvas.coords(bg_l1_label1,WINDOW_WIDTH,0)
    elif canvas.coords(bg_l1_label2)[0]<-WINDOW_WIDTH:
        canvas.coords(bg_l1_label2,WINDOW_WIDTH,0)
    canvas.after(5,scroll_background)
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
    #_______________LEVEL-1_______________
def level1(event):
    canvas.delete("all")
    global player_id
    global bg_l1_label1,bg_l1_label2
    bg_l1_label1=canvas.create_image(0,0,image=bg_l1, anchor="nw")
    bg_l1_label2=canvas.create_image(WINDOW_WIDTH,0,image=bg_l1, anchor="nw")
    canvas.create_image(0,700,image = road, anchor = "nw", tags="PLATFORM")
    canvas.create_image(300,700,image = road, anchor = "nw", tags="PLATFORM")
    canvas.create_image(600,700,image = road, anchor = "nw", tags="PLATFORM")
    canvas.create_image(900,700,image = road, anchor = "nw", tags="PLATFORM")
    canvas.create_image(1200,700,image = road, anchor = "nw",tags="PLATFORM")
    canvas.create_image(1500,700,image = road, anchor = "nw",tags="PLATFORM")
    canvas.create_image(1800,700,image = road, anchor = "nw",tags="PLATFORM")
    canvas.create_image(180, 700,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(200, 700,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(220, 700,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(240, 700,image = banana, anchor = "nw",tags="banana")

    canvas.create_image(300, 440,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(320, 440,image = banana, anchor = "nw",tags="banana")

    canvas.create_image(530, 290,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(550, 290,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(570, 290,image = banana, anchor = "nw",tags="banana")

    canvas.create_image(490, 700,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(530, 700,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(570, 700,image = banana, anchor = "nw",tags="banana")

    canvas.create_image(800,700,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(820,700,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(840, 700,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(860, 700,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(880, 700,image = banana, anchor = "nw",tags="banana")

    canvas.create_image(700, 170,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(730, 170,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(760, 170,image = banana, anchor = "nw",tags="banana")

    canvas.create_image(880, 210,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(910, 210,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(940, 210,image = banana, anchor = "nw",tags="banana")

    canvas.create_image(1080, 350,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(1110, 350,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(1140, 350,image = banana, anchor = "nw",tags="banana")

    canvas.create_image(800,700,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(820,700,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(840, 700,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(860, 700,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(880, 700,image = banana, anchor = "nw",tags="banana")

    canvas.create_image(1040,490,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(1060, 490,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(1080, 490,image = banana, anchor = "nw",tags="banana")

    canvas.create_image(1240,300,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(1260, 300,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(1280, 300,image = banana, anchor = "nw",tags="banana")

    canvas.create_image(1440,700,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(1470, 700,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(1500, 700,image = banana, anchor = "nw",tags="banana")

    canvas.create_image(1440,640,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(1470, 640,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(1500, 640,image = banana, anchor = "nw",tags="banana")

    canvas.create_image(1760,700,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(1790, 700,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(1820, 700,image = banana, anchor = "nw",tags="banana")

    canvas.create_image(1760,640,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(1790, 640,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(1820, 640,image = banana, anchor = "nw",tags="banana")

    canvas.create_image(250, 430,image = stone1, anchor = "nw",tags="PLATFORM")
    canvas.create_image(480, 280,image = stone1, anchor = "nw",tags="PLATFORM")
    canvas.create_image(850, 200,image = stone1, anchor = "nw",tags="PLATFORM")
    canvas.create_image(1000, 480,image = stone1, anchor = "nw",tags="PLATFORM")
    canvas.create_image(1200, 300,image = stone1, anchor = "nw",tags="PLATFORM")

    canvas.create_image(650, 650,image = enemy, anchor = "nw",tags="platform") 
    canvas.create_image(1200, 650,image = enemy, anchor = "nw",tags="platform") 
    canvas.create_image(1600, 650,image = enemy, anchor = "nw",tags="platform") 
    player_file = Image.open("IMAGES/player.png")
    player_size = player_file.resize((10, 10))
    player = ImageTk.PhotoImage(player_size)
    player_id=canvas.create_image(50,0,image=player)
    # char_file = Image.open("IMAGES/player.png")
    # char_size = char_file.resize((10,10))
    # char = ImageTk.PhotoImage(char_size)
    #_____________APSARA WIN PLACE_________________
    canvas.create_image(1880, 570,image = apsora, anchor = "nw",tags="PLATFORM") 
    canvas.create_image(10,10,image=levelsremove,anchor="nw",tags="remove")
    scroll_background()
    # gravity()
#__________LEVEL-2___________
def level2(event):
    canvas.delete("all")
    global player_id
    global bg_l1_label1,bg_l1_label2
    bg_l1_label1=canvas.create_image(1,0,image = bg_l2, anchor = "nw")
    bg_l1_label2=canvas.create_image(WINDOW_WIDTH,0,image = bg_l2, anchor = "nw")
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
    canvas.create_image(750,155, image= bg_l14, anchor = "nw",tags="PLATFORM")

    canvas.create_image(830,350, image= bg_l16, anchor = "nw",tags="PLATFORM")

# ====================win place++++++++++++

    canvas.create_image(1740,130, image= bg_l9, anchor = "nw",tags="PLATFORM")
    canvas.create_image(1820,280, image= bg_l11, anchor = "nw",tags="PLATFORM")
    #___________BACK TO ALL LEVEL_____________
    canvas.create_image(10,10,image=levelsremove,anchor="nw",tags="remove")
    scroll_background()
#________________LEVEL-3__________________
def level3(event):
    canvas.delete("all")
    # global player_id
    global bg_l1_label1,bg_l1_label2
    bg_l1_label1=canvas.create_image(0,0,image=level_3,anchor="nw")
    bg_l1_label2=canvas.create_image(WINDOW_WIDTH,0,image=level_3,anchor="nw")
    #_____________ground__________________
    canvas.create_image(0,650,image=grass_level3,anchor="nw",tags="PLATFORM")
    canvas.create_image(290,650,image=grass_level3,anchor="nw",tags="PLATFORM")
    canvas.create_image(580,650,image=grass_level3,anchor="nw",tags="PLATFORM")
    canvas.create_image(870,650,image=grass_level3,anchor="nw",tags="PLATFORM")
    canvas.create_image(1160,650,image=grass_level3,anchor="nw",tags="PLATFORM")
    canvas.create_image(1450,650,image=grass_level3,anchor="nw",tags="PLATFORM")
    canvas.create_image(1740,650,image=grass_level3,anchor="nw",tags="PLATFORM")
 
    #____________Stone______________-
    canvas.create_image(130,490,image=stone,anchor="nw",tags="stone")
    canvas.create_image(420,300,image=stone,anchor="nw",tags="stone")
    canvas.create_image(940,500,image=stone,anchor="nw",tags="stone")
    canvas.create_image(740,200,image=small_stone,anchor="nw",tags="stone")
    canvas.create_image(840,400,image=small_stone,anchor="nw",tags="stone")
    canvas.create_image(1450,350,image=small_stone,anchor="nw",tags="stone")
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
    scroll_background()
# # ------------- Functions ---------------------
def check_movement(dx=0, dy=0, checkGround=False):
    coord = canvas.coords(player_id)
    platforms = canvas.find_withtag("PLATFORM")
    if coord[0] + dx < 0 or coord[0]+player.width() + dx > WINDOW_WIDTH:
        return False
    if checkGround:
        overlap = canvas.find_overlapping(coord[0]+player.width(), coord[1], coord[0]+ player.width() , coord[1]+player.height() + dy)
    else:
        overlap = canvas.find_overlapping(coord[0]+dx, coord[1]+dy, coord[0]+dx, coord[1]+ player.width())
    for platform in platforms:
        if platform in overlap:
            return False
    return True

def move():
    global score
    if not keyPressed == []:
        x = 0
        if "Left" in keyPressed:
            x -= SPEED
        if "Right" in keyPressed:
            x += SPEED
        if "space" in keyPressed and not check_movement(0, GRAVITY_FORCE, True):
            jump(JUMP_FORCE)
        if check_movement(x):
            canvas.move(player_id, x, 0)
        window.after(TIMED_LOOP, move)
# ==============>MOVE-BALL <================== 
#____JUMP THE PLAYER____________
def jump(force):
    if force > 0:
        if check_movement(0, -force):
            canvas.move(player, 0, -force)
            window.after(TIMED_LOOP, jump, force-1)
# ==============>GRAVITY <==================        
def gravity():
    if check_movement(0, GRAVITY_FORCE, True):
        canvas.move(player_id, 0, GRAVITY_FORCE)
    window.after(TIMED_LOOP, gravity)
#_______START MOVE THE CHARACTER______
def start_move(event):
    if event.keysym not in keyPressed:
        keyPressed.append(event.keysym)
        if len(keyPressed) == 1:
            move()
def stop_move(event):
    global keyPressed
    if event.keysym in keyPressed:
        keyPressed.remove(event.keysym)
gravity()
window.bind("<Key>", start_move)
window.bind("<KeyRelease>", stop_move)
#__________________KEY EVENTS______________________
canvas.tag_bind("start","<Button-1>", start)
canvas.tag_bind("exit","<Button-1>", exit)
canvas.tag_bind("help","<Button-1>", help)
canvas.tag_bind("back","<Button-1>", backlevel)
canvas.tag_bind("level3","<Button-1>",level3)
canvas.tag_bind("level1","<Button-1>",level1)
canvas.tag_bind("level2","<Button-1>",level2)
canvas.tag_bind("remove","<Button-1>",remove)
home()
# #========================= DISPLAY WINDOW =================
canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
window.mainloop()