#________________________IMPORT FILES______________________
import tkinter as tk
from PIL import ImageTk, Image
#_________________________CONSTANTS________________________
WINDOW_WIDTH=1420
WINDOW_HEIGHT=800
#_____________________GLOBAL____________
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
bg_home=Image.open("IMAGES/bg_home.png")
bg_size=bg_home.resize((WINDOW_WIDTH,WINDOW_HEIGHT))
bg=ImageTk.PhotoImage(bg_size)
canvas.create_image(0,0,image=bg,anchor="nw")

start_button=Image.open("IMAGES/start_button.png")
start_button_size=start_button.resize((150,150))
start=ImageTk.PhotoImage(start_button_size)
canvas.create_image(600,300,image=start,anchor="nw",tags="start")
# bg_default=PhotoImage(file="IMAGES/bg_home.png")
#______________HOME PAGE___________

window.mainloop()