# from tkinter import *
# from tkinter.ttk import *
# from tkinter import ttk
# from PIL import ImageTk, Image
# import winsound

# def play_sound():
#     winsound.PlaySound('click.wav', winsound.SND_FILENAME)

# def open_new_window():
#     play_sound()  # Play the alert sound
#     new_window = Toplevel(root)
#     new_window.geometry('1920x1080')
#     new_window.title('New Window')
#     # Add your content to the new window...

# def close_window():
#     play_sound()  # Play the alert sound
#     root.destroy()

# root = Tk()
# root.geometry('1920x1080')
# bg = ImageTk.PhotoImage(file='IMAGES/bg_home.png')
# start=ImageTk.PhotoImage(file="IMAGES/start.png")
# my_label = Label(root, image=bg)
# my_label.place(x=0, y=0, relwidth=1, relheight=1)

# style = Style()
# style.configure('TButton', font=('calibri', 15, 'bold'), borderwidth='4')
# style.map('TButton', foreground=[('active', '!disabled', 'orange')],
#           background=[('active', 'green')])
# style.configure('TButton', background='orange')

# button_start = ttk.Button(root,image=start)
# button_start.place(x=600, y=325)

# button_menu = ttk.Button(root, text="Menu", command=play_sound)
# button_menu.place(x=600, y=375)

# button_close = ttk.Button(root, text="Close", command=close_window)
# button_close.place(x=600, y=425)

# style.configure('TButton', foreground='green')

# root.mainloop()
# ==============> Story <==================
# def story(event):
#     canvas.delete("all")
#     canvas.create_image(1, 0, image=game_story, anchor = 'nw')
#     canvas.create_image(20,20, image =button_exist, anchor = "nw",tags="backhome")
# # ---------------------------------------------------------------------------
# def back(event):
#     canvas.delete("all")
#     home()
# #=> CREATE GAME SHOW
# # ---------------------------------------------------------------------------
# def home():
#     canvas.create_image(1, 0, image=game_start, anchor='nw')
#     canvas.create_image(500,500,image=story_list, tags="story")
#     canvas.create_image(700,500, image=button_play, tags="startgame")
#     canvas.create_image(900,500,image=button_help, tags="help")
#     # winsound.PlaySound("sound/open.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)

# #=> ALLOW WINDOWS KEYS AND TAGES BIND
# # ---------------------------------------------------------------------------
# # root.bind("<w>", movePlayerUp)
# # root.bind("<s>", movePlayerDown)
# # root.bind("<Button-3>", createBullet)
# canvas.tag_bind("help","<Button-1>",introdution )
# canvas.tag_bind("story","<Button-1>", story)
# canvas.tag_bind("backhome","<Button-1>", back)
# canvas.tag_bind("startgame","<Button-1>", alllevels )
# canvas.tag_bind("level1-","<Button-1>", level01 )
# canvas.tag_bind("level2-","<Button-1>", level02 )
# canvas.tag_bind("level3-","<Button-1>", level03 )