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
bg_levels=Image.open("IMAGES/bg.png")
bg_levels_size=bg_levels.resize((800,WINDOW_HEIGHT))
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

# test 


def alllevels():
    canvas.delete("all")
    global player_id
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
    canvas.create_image(0,670,image = road, anchor = "nw", tags="PLATFORM")
    canvas.create_image(300,670,image = road, anchor = "nw", tags="PLATFORM")
    canvas.create_image(600,670,image = road, anchor = "nw", tags="PLATFORM")
    canvas.create_image(900,670,image = road, anchor = "nw", tags="PLATFORM")
    canvas.create_image(1200,670,image = road, anchor = "nw",tags="PLATFORM")
    canvas.create_image(1500,670,image = road, anchor = "nw",tags="PLATFORM")
    canvas.create_image(1800,670,image = road, anchor = "nw",tags="PLATFORM")
    canvas.create_image(180, 640,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(200, 640,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(220, 640,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(240, 640,image = banana, anchor = "nw",tags="banana")

    canvas.create_image(300, 440,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(320, 440,image = banana, anchor = "nw",tags="banana")

    canvas.create_image(530, 290,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(550, 290,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(570, 290,image = banana, anchor = "nw",tags="banana")

    canvas.create_image(490, 640,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(530, 640,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(570, 640,image = banana, anchor = "nw",tags="banana")

    canvas.create_image(800,640,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(820,640,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(840, 640,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(860, 640,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(880, 640,image = banana, anchor = "nw",tags="banana")

    canvas.create_image(700, 170,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(730, 170,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(760, 170,image = banana, anchor = "nw",tags="banana")

    canvas.create_image(880, 210,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(910, 210,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(940, 210,image = banana, anchor = "nw",tags="banana")

    canvas.create_image(1080, 350,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(1110, 350,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(1140, 350,image = banana, anchor = "nw",tags="banana")

    canvas.create_image(800,640,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(820,640,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(840, 640,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(860, 640,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(880, 640,image = banana, anchor = "nw",tags="banana")

    canvas.create_image(1040,490,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(1060, 490,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(1080, 490,image = banana, anchor = "nw",tags="banana")

    canvas.create_image(1240,300,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(1260, 300,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(1280, 300,image = banana, anchor = "nw",tags="banana")

    canvas.create_image(1440,640,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(1470, 640,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(1500, 640,image = banana, anchor = "nw",tags="banana")

    canvas.create_image(1440,640,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(1470, 640,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(1500, 640,image = banana, anchor = "nw",tags="banana")

    canvas.create_image(1760,640,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(1790, 640,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(1820, 640,image = banana, anchor = "nw",tags="banana")

    canvas.create_image(1760,640,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(1790, 640,image = banana, anchor = "nw",tags="banana")
    canvas.create_image(1820, 640,image = banana, anchor = "nw",tags="banana")

    canvas.create_image(250, 430,image = stone1, anchor = "nw",tags="PLATFORM")
    canvas.create_image(480, 280,image = stone1, anchor = "nw",tags="PLATFORM")
    canvas.create_image(850, 200,image = stone1, anchor = "nw",tags="PLATFORM")
    canvas.create_image(1000, 480,image = stone1, anchor = "nw",tags="PLATFORM")
    canvas.create_image(1200, 300,image = stone1, anchor = "nw",tags="PLATFORM")

    canvas.create_image(650, 620,image = enemy, anchor = "nw",tags="platform") 
    canvas.create_image(1200, 620,image = enemy, anchor = "nw",tags="platform") 
    canvas.create_image(1600, 620,image = enemy, anchor = "nw",tags="platform") 

    canvas.create_rectangle(0,780,3800,800,fill="black",tags="PLATFORM")
    
    
    player_file = Image.open("IMAGES/player.png")
    player_size = player_file.resize((10, 10))
    player = ImageTk.PhotoImage(player_size)
    player_id=canvas.create_image(100,0,image=player)

    #_____________APSARA WIN PLACE_________________
    canvas.create_image(1880, 570,image = apsora, anchor = "nw",tags="PLATFORM") 
    canvas.create_image(10,10,image=levelsremove,anchor="nw",tags="remove")
    scroll_background()
    gravity()
#________________LEVEL-3_________________
def level3(event):
    canvas.delete("all")
    global player_id
    global bg_l1_label1,bg_l1_label2
    
    bg_l1_label1=canvas.create_image(0,0,image=level_3,anchor="nw")
    bg_l1_label2=canvas.create_image(WINDOW_WIDTH,0,image=level_3,anchor="nw")
    #_____________ground__________________
    canvas.create_image(0,590,image=grass_level3,anchor="nw",tags="PLATFORM")
    canvas.create_image(290,590,image=grass_level3,anchor="nw",tags="PLATFORM")
    canvas.create_image(580,590,image=grass_level3,anchor="nw",tags="PLATFORM")
    canvas.create_image(870,590,image=grass_level3,anchor="nw",tags="PLATFORM")
    canvas.create_image(1070,590,image=grass_level3,anchor="nw",tags="PLATFORM")
    canvas.create_image(1270,590,image=grass_level3,anchor="nw",tags="PLATFORM")
    canvas.create_image(1470,590,image=grass_level3,anchor="nw",tags="PLATFORM")
    canvas.create_image(1760,590,image=grass_level3,anchor="nw",tags="PLATFORM")
    #____________Stone______________-
    canvas.create_image(130,490,image=stone,anchor="nw",tags="PLATFORM")
    canvas.create_image(420,300,image=stone,anchor="nw",tags="PLATFORM")
    canvas.create_image(940,500,image=stone,anchor="nw",tags="PLATFORM")
    canvas.create_image(740,200,image=small_stone,anchor="nw",tags="PLATFORM")
    canvas.create_image(840,400,image=small_stone,anchor="nw",tags="PLATFORM")
    canvas.create_image(1250,350,image=small_stone,anchor="nw",tags="PLATFORM")
    #______________Tiger__________________
    canvas.create_image(320,430,image=tiger,anchor="nw",tags="tiger")
    #______________Thorns____________________
    canvas.create_image(600,280,image=thorn,anchor="nw",tags="thorn")
    canvas.create_image(650,280,image=thorn,anchor="nw",tags="thorn")
    canvas.create_image(700,280,image=thorn,anchor="nw",tags="thorn")
    canvas.create_image(780,170,image=thorn,anchor="nw",tags="thorn")
    canvas.create_image(1000,480,image=thorn,anchor="nw",tags="thorn")
    player_file = Image.open("IMAGES/player.png")
    player_size = player_file.resize((10, 10))
    player = ImageTk.PhotoImage(player_size)
    player_id=canvas.create_image(100,0,image=player)
    #___________BACK TO ALL LEVEL_____________
    canvas.create_image(10,10,image=levelsremove,anchor="nw",tags="remove")
    scroll_background()
    gravity()
# # ------------- Functions ---------------------
def check_movement(dx=0, dy=0, checkGround=False):
    # global scroll_background
    coord = canvas.coords(player_id)
    platforms = canvas.find_withtag("PLATFORM")
    if coord[0] + dx -15 < 0 or coord[0]+player.width() + dx > WINDOW_WIDTH:
        return False
    if checkGround:
        overlap = canvas.find_overlapping(coord[0]+player.width(), coord[1], coord[0] + dx+ 50 , coord[1]+ dy + 15)
    else:
        overlap = canvas.find_overlapping(coord[0]+dx, coord[1]+dy, coord[0] - player.width(), coord[1] - player.height())
    print(overlap)
    for platform in platforms:
        if platform in overlap:
            return False
    return True

def jump(force):
    if force > 0:
        if check_movement(0, -force):
            canvas.move(player_id, 0, -force)
            window.after(TIMED_LOOP, jump, force-1)

def start_move(event):
    if event.keysym not in keyPressed:
        keyPressed.append(event.keysym)
        if len(keyPressed) == 1:
            move()
def eat_banana():
    coord = canvas.coords(player_id)
    bananas = canvas.find_withtag("banana")
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + player.width(),coord[1] + player.height())
    for bn in bananas:
        if bn in overlap:
            return bn
    return 0

def playSound():
    mixer.init() #Initialzing pyamge mixer
    mixer.music.load('SOUND/sound.mp3') #Loading Music File
    mixer.music.play() #Playing Music with Pygame
    time.sleep(0.2)
    mixer.music.stop()



def move():
    if not keyPressed == []:
        x = 0
        if "Left" in keyPressed:
            canvas.itemconfigure(player_id,image=player)
            x -= SPEED
        if "Right" in keyPressed:
            canvas.itemconfigure(player_id,image=player)
            x += SPEED
        if "space" in keyPressed and not check_movement(0, GRAVITY_FORCE, True):
            jump(JUMP_FORCE)
        if check_movement(x):
            canvas.move(player_id, x, 0)
        window.after(TIMED_LOOP, move)

    banana_id = eat_banana()
    if banana_id > 0:
        coord = canvas.coords(banana_id)
        canvas.delete(banana_id)
        playSound()

def gravity():
    if check_movement(0, GRAVITY_FORCE, False):
        canvas.move(player_id, 0, GRAVITY_FORCE)
    window.after(TIMED_LOOP, gravity)

def stop_move(event):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
    global keyPressed
    if event.keysym in keyPressed:
        keyPressed.remove(event.keysym)

window.bind("<Key>", start_move)
window.bind("<KeyRelease>", stop_move)
#__________________KEY EVENTS______________________
canvas.tag_bind("start","<Button-1>", start)
canvas.tag_bind("exit","<Button-1>", exit)
canvas.tag_bind("help","<Button-1>", help)
canvas.tag_bind("back","<Button-1>", backlevel)
canvas.tag_bind("level3","<Button-1>",level3)
canvas.tag_bind("level1","<Button-1>",level1)
canvas.tag_bind("remove","<Button-1>",remove)
home()
#========================= DISPLAY WINDOW =================
canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
window.mainloop()