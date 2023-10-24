#________________________IMPORT______________________
import tkinter as tk
from PIL import ImageTk, Image
from pygame import mixer
import time
#============================ CONSTANTS ============================

WINDOW_WIDTH=2000
WINDOW_HEIGHT=800
GRAVITY_FORCE = 9
JUMP_FORCE = 30
SPEED = 7
TIMED_LOOP = 10

#============================ VARIABLES ============================

keyPressed = []

#============================ GLOBAL ============================
score=0

#________________MAIN WINDOW________________
window=tk.Tk()
window.geometry(str(WINDOW_WIDTH)+ "x" + str(WINDOW_HEIGHT))
window.title("HANUMAN JUMP")
window.attributes('-fullscreen',True)
frame=tk.Frame(window,width=WINDOW_WIDTH,height=WINDOW_HEIGHT)
frame.pack()
canvas=tk.Canvas(frame,width=WINDOW_WIDTH,height=WINDOW_HEIGHT,scrollregion=(0,0,2000,800))
canvas.pack()

#scrollbar
scrollbar_bottom = tk.Scrollbar(window, orient='horizontal', command=canvas.xview)
canvas.configure(xscrollcommand=scrollbar_bottom.set)
scrollbar_bottom.place(relx=0, rely=1, relwidth=1, anchor='sw')

#____________IMPORT IMAGES____________
bg=ImageTk.PhotoImage(file="IMAGES/bg_home.png")
start=ImageTk.PhotoImage(file="IMAGES/start.png")
help=ImageTk.PhotoImage(file="IMAGES/help.png")
exit=ImageTk.PhotoImage(file="IMAGES/exit.png")
player=ImageTk.PhotoImage(file="IMAGES/player.png")

bg_l1_file=Image.open("IMAGES/bg_l1.png")
bg_l1_file_size=bg_l1_file.resize((WINDOW_WIDTH,WINDOW_HEIGHT))
bg_l1=ImageTk.PhotoImage(bg_l1_file_size)
bg_l1_label1=canvas.create_image(0,0,image=bg_l1, anchor="nw")
bg_l1_label2=canvas.create_image(WINDOW_WIDTH,0,image=bg_l1, anchor="nw")
# canvas.create_image(600,350,image=bg_l1)
# canvas.create_image(1950,350,image=bg_l1)
# canvas.create_image(3300,350,image=bg_l1)

# ______________HOME PAGE___________
# def home():
#     canvas.create_image(0,0,image=bg,anchor="nw")
#     canvas.create_image(600,410,image=start,anchor="nw",tags="start")
#     canvas.create_image(590,500,image=help,anchor="nw",tags="help")
#     canvas.create_image(570,570,image=exit,anchor="nw",tags="exit")
# home()
def scroll_bg_img():
    canvas.move(bg_l1_label1,-1,0)
    canvas.move(bg_l1_label2,-1,0)

    if canvas.coords(bg_l1_label1)[0]<-2000:
        canvas.coords(bg_l1_label1,2000,0)
    elif canvas.coords(bg_l1_label2)[0]<-2000:
        canvas.coords(bg_l1_label2,2000,0)
    canvas.after(5,scroll_bg_img)
scroll_bg_img()
#_______________LEVEL-1_______________
def level1(event):
    canvas.delete("all")
    global player
    global bg_l1_label1
    global bg_l1_label2
#____________________Road___________________________
road_file = Image.open("IMAGES/road1.png")
road_size = road_file.resize((320, 50))
road = ImageTk.PhotoImage(road_size)
canvas.create_image(0, 670,image = road, anchor = "nw", tags="PLATFORM")
canvas.create_image(300, 670,image = road, anchor = "nw", tags="PLATFORM")
canvas.create_image(600, 670,image = road, anchor = "nw", tags="PLATFORM")
canvas.create_image(900, 670,image = road, anchor = "nw", tags="PLATFORM")
canvas.create_image(1200, 670,image = road, anchor = "nw",tags="PLATFORM")
canvas.create_image(1500, 670,image = road, anchor = "nw",tags="PLATFORM")
canvas.create_image(1800, 670,image = road, anchor = "nw",tags="PLATFORM")
#____________________Banana____________________________
banana_file = Image.open("IMAGES/banana.png")
banana_size = banana_file.resize((50, 30))
banana = ImageTk.PhotoImage(banana_size)
banana_id=canvas.create_image(180, 650,image = banana, anchor = "nw",tags="banana")
banana_id=canvas.create_image(200, 650,image = banana, anchor = "nw",tags="banana")
banana_id=canvas.create_image(220, 650,image = banana, anchor = "nw",tags="banana")
banana_id=canvas.create_image(240, 650,image = banana, anchor = "nw",tags="banana")

banana_id=canvas.create_image(300, 440,image = banana, anchor = "nw",tags="banana")
banana_id=canvas.create_image(320, 440,image = banana, anchor = "nw",tags="banana")

banana_id=canvas.create_image(530, 290,image = banana, anchor = "nw",tags="banana")
banana_id=canvas.create_image(550, 290,image = banana, anchor = "nw",tags="banana")
banana_id=canvas.create_image(570, 290,image = banana, anchor = "nw",tags="banana")

banana_id=canvas.create_image(490, 650,image = banana, anchor = "nw",tags="banana")
banana_id=canvas.create_image(530, 650,image = banana, anchor = "nw",tags="banana")
banana_id=canvas.create_image(570, 650,image = banana, anchor = "nw",tags="banana")

banana_id=canvas.create_image(800,650,image = banana, anchor = "nw",tags="banana")
banana_id=canvas.create_image(820,650,image = banana, anchor = "nw",tags="banana")
banana_id=canvas.create_image(840, 650,image = banana, anchor = "nw",tags="banana")
banana_id=canvas.create_image(860, 650,image = banana, anchor = "nw",tags="banana")
banana_id=canvas.create_image(880, 650,image = banana, anchor = "nw",tags="banana")

banana_id=canvas.create_image(700, 170,image = banana, anchor = "nw",tags="banana")
banana_id=canvas.create_image(730, 170,image = banana, anchor = "nw",tags="banana")
banana_id=canvas.create_image(760, 170,image = banana, anchor = "nw",tags="banana")

banana_id=canvas.create_image(880, 210,image = banana, anchor = "nw",tags="banana")
banana_id=canvas.create_image(910, 210,image = banana, anchor = "nw",tags="banana")
banana_id=canvas.create_image(940, 210,image = banana, anchor = "nw",tags="banana")

banana_id=canvas.create_image(1080, 350,image = banana, anchor = "nw",tags="banana")
banana_id=canvas.create_image(1110, 350,image = banana, anchor = "nw",tags="banana")
banana_id=canvas.create_image(1140, 350,image = banana, anchor = "nw",tags="banana")

banana_id=canvas.create_image(800,650,image = banana, anchor = "nw",tags="banana")
banana_id=canvas.create_image(820,650,image = banana, anchor = "nw",tags="banana")
banana_id=canvas.create_image(840, 650,image = banana, anchor = "nw",tags="banana")
banana_id=canvas.create_image(860, 650,image = banana, anchor = "nw",tags="banana")
banana_id=canvas.create_image(880, 650,image = banana, anchor = "nw",tags="banana")

banana_id=canvas.create_image(1040,490,image = banana, anchor = "nw",tags="banana")
banana_id=canvas.create_image(1060, 490,image = banana, anchor = "nw",tags="banana")
banana_id=canvas.create_image(1080, 490,image = banana, anchor = "nw",tags="banana")

# banana_id=canvas.create_image(1080,650,image = banana, anchor = "nw",tags="banana")
# banana_id=canvas.create_image(1100, 650,image = banana, anchor = "nw",tags="banana")
# banana_id=canvas.create_image(1120, 650,image = banana, anchor = "nw",tags="banana")

banana_id=canvas.create_image(1240,300,image = banana, anchor = "nw",tags="banana")
banana_id=canvas.create_image(1260, 300,image = banana, anchor = "nw",tags="banana")
banana_id=canvas.create_image(1280, 300,image = banana, anchor = "nw",tags="banana")

banana_id=canvas.create_image(1440,360,image = banana, anchor = "nw",tags="banana")
banana_id=canvas.create_image(1460, 360,image = banana, anchor = "nw",tags="banana")
banana_id=canvas.create_image(1480, 360,image = banana, anchor = "nw",tags="banana")

# banana_id=canvas.create_image(1400,360,image = banana, anchor = "nw",tags="banana")
# banana_id=canvas.create_image(1420, 360,image = banana, anchor = "nw",tags="banana")
# banana_id=canvas.create_image(1440, 360,image = banana, anchor = "nw",tags="banana")
# banana_id=canvas.create_image(1460, 360,image = banana, anchor = "nw",tags="banana")
#___________________Thorns________________________________
# thorn_file = Image.open("IMAGES/thorns.png")
# thorn_size = thorn_file.resize((150, 80))
# thorn = ImageTk.PhotoImage(thorn_size)
# canvas.create_image(1180, 620,image = thorn, anchor = "nw",tags="PLATFORM")
#____________________stone________________________________
stone1_file = Image.open("IMAGES/stone1.png")
stone1_size = stone1_file.resize((180, 130))
stone1 = ImageTk.PhotoImage(stone1_size)
# stone2_file = Image.open("IMAGES/stone2.png")
# stone2_size = stone2_file.resize((250, 150))
# stone2 = ImageTk.PhotoImage(stone2_size)
# stone3_file = Image.open("IMAGES/stone3.png")
# stone3_size = stone3_file.resize((250, 150))
# stone3 = ImageTk.PhotoImage(stone3_size)
canvas.create_image(250, 430,image = stone1, anchor = "nw",tags="PLATFORM")
canvas.create_image(480, 280,image = stone1, anchor = "nw",tags="PLATFORM")
canvas.create_image(850, 200,image = stone1, anchor = "nw",tags="PLATFORM")
canvas.create_image(1000, 480,image = stone1, anchor = "nw",tags="PLATFORM")
canvas.create_image(1200, 300,image = stone1, anchor = "nw",tags="PLATFORM")
canvas.create_image(1400, 350,image = stone1, anchor = "nw",tags="PLATFORM")
# _____________________Bird_____________________________
bird1_file = Image.open("IMAGES/bird1.gif")
bird1_size = bird1_file.resize((150, 100))
bird1 = ImageTk.PhotoImage(bird1_size)
bird=canvas.create_image(640, 250,image = bird1, anchor = "nw",tags="PLATFORM") 

enemy_file = Image.open("IMAGES/enemy.png")
enemy_size = enemy_file.resize((100, 80))
enemy = ImageTk.PhotoImage(enemy_size)
canvas.create_image(650, 605,image = enemy, anchor = "nw",tags="PLATFORM") 
canvas.create_image(1200, 605,image = enemy, anchor = "nw",tags="PLATFORM") 
canvas.create_image(1800, 605,image = enemy, anchor = "nw",tags="PLATFORM") 

#___________________Player_________________________________
player_file = Image.open("IMAGES/player.png")
player_size = player_file.resize((70, 70))
player = ImageTk.PhotoImage(player_size)

play_id=canvas.create_image(50, 0,image = player)

char_file = Image.open("IMAGES/player.png")
char_size = char_file.resize((70,70))
char = ImageTk.PhotoImage(char_size)

score_file = Image.open("IMAGES/banana.png")
score_size = score_file.resize((50,50))
score = ImageTk.PhotoImage(score_size)


# ------------- Functions ---------------------

def check_movement(dx=0, dy=0, checkGround=False):
    global scroll_bg_img
    coord = canvas.coords(play_id)
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
            canvas.move(play_id, 0, -force)
            window.after(TIMED_LOOP, jump, force-1)

def start_move(event):
    if event.keysym not in keyPressed:
        keyPressed.append(event.keysym)
        if len(keyPressed) == 1:
            move()
def eat_banana():
    coord = canvas.coords(play_id)
    bananas = canvas.find_withtag("banana")
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + player.width(),coord[1] + player.height())
    for bn in bananas:
        if bn in overlap:
            return bn
    return 0
def meet_bird():
    coord = canvas.coords(play_id)
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
            # canvas.itemconfigure(player,image=charL)
            x -= SPEED
        if "Right" in keyPressed:
            canvas.itemconfigure(play_id,image=char)
            x += SPEED
        if "space" in keyPressed and not check_movement(0, GRAVITY_FORCE, True):
            jump(JUMP_FORCE)
        if check_movement(x):
            canvas.move(play_id, x, 0)
        window.after(TIMED_LOOP, move)

    banana_id = eat_banana()
    if banana_id > 0:
        coord = canvas.coords(banana_id)
        canvas.delete(banana_id)
        playSound()

def gravity():
    if check_movement(0, GRAVITY_FORCE, True):
        canvas.move(play_id, 0, GRAVITY_FORCE)
    window.after(TIMED_LOOP, gravity)

def stop_move(event):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
    global keyPressed
    if event.keysym in keyPressed:
        keyPressed.remove(event.keysym)

gravity()

window.bind("<Key>", start_move)
window.bind("<KeyRelease>", stop_move)
# #________________KEY EVENTS_______________
canvas.tag_bind=("start","<Button-1>",start)
canvas.tag_bind=("help","<Button-1>",help)
canvas.tag_bind=("exit","<Button-1>",exit)
# #========================= DISPLAY WINDOW =================
# canvas.pack(expand=True, fill="both")
# frame.pack(expand=True, fill="both")
window.mainloop()