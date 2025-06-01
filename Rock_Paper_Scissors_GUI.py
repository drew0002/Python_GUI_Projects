from customtkinter import *
import random
def tohome(app):
    for i in app.winfo_children():
        i.destroy()
    mainf(app)
def reset(app):
    for i in app.winfo_children():
        i.destroy()
def exit(app):
    app.destroy()
def game(menu,app,promptfont,headerfont):
    reset(app)
    cpuchoice = ["🪨", "🗞️", "✂️"]
    userchoice = menu.get()
    cpuchoice = random.choice(cpuchoice)
    framesub=CTkFrame(master=app,fg_color="#B8AFE6")
    framesub.pack(expand=True,fill="both")
    framesub.tkraise()

    header= CTkLabel(master=framesub,text="Rock Paper Scissors!", font=headerfont)
    header.grid(row=0,column=1,padx=0, pady=(10, 0),sticky="n")
    symfont=CTkFont(size=40)
    labelsub1=CTkLabel(master=framesub,text="Your choice:",font=promptfont)
    labelsub1.grid(row=1,column=0,padx=(180,10),pady=(150,0),sticky='w')
    labelsub2 = CTkLabel(master=framesub, text=userchoice,font=symfont)
    labelsub2.grid(row=1,column=1,padx=(10,0),pady=(150,0),sticky='w')
    labelsub3=CTkLabel(master=framesub,text="vs",font=promptfont)
    labelsub3.grid(row=1,column=1,padx=(5,5),pady=(150,0),stick='n')
    labelsub4=CTkLabel(master=framesub,text="cpuchoice: ",font=promptfont)
    labelsub4.grid(row=1, column=2, padx=(0, 0), pady=(150, 0), stick='w')
    labelsub5 = CTkLabel(master=framesub, text=cpuchoice, font=symfont)
    labelsub5.grid(row=1, column=3, padx=(0, 10), pady=(150, 0), stick='w')
    labelsub6=CTkLabel(master=framesub,text='',font=promptfont)
    labelsub6.grid(row=2,column=1,padx=(10,10),pady=(100,0),sticky='n')
    subplayagain=CTkButton(master=framesub,text="Play again?",corner_radius=40,width=150,height=50,fg_color="orange",command=lambda:tohome(app))
    subplayagain.grid(row=3,column=1,padx=(10,10),pady=(100,0),sticky='n')
    subexit=CTkButton(master=framesub,text="Exit",corner_radius=40,width=150,height=50,fg_color="red",command=lambda:exit(app))
    subexit.grid(row=4,column=1,padx=(10,10),pady=(30,0),sticky='n')





    if(userchoice==cpuchoice):
        labelsub6.configure(text="draw :/")
    elif(userchoice=="🪨" and cpuchoice=="🗞️" or userchoice == "🗞️" and cpuchoice == "✂️" or userchoice == "✂️" and cpuchoice == "🪨"):
        labelsub6.configure(text="you lost..")
    elif (userchoice == "🪨" and cpuchoice == "✂️" or userchoice == "🗞️" and cpuchoice == "🪨" or userchoice == "✂️" and cpuchoice == "🗞️"):
        labelsub6.configure(text="Get in there..you won :D") # win


app=CTk()
def mainf(app):
    app.title("rock paper scissors")
    app.geometry("1900x1080")
    set_appearance_mode("dark")


    frame=CTkFrame(master=app,fg_color="#B8AFE6")
    frame.pack(expand=True,fill="both")

#header
    headerfont=CTkFont(family="Courier New",size=40,weight="bold")
    header=CTkLabel(master=frame,text="Rock Paper Scissors!",font=headerfont)
    header.pack(padx=100,pady=(10,0),side="top")

#entry prompt
    promptfont=CTkFont(family="Courier New",size=30,weight="bold")
    prompt=CTkLabel(master=frame,text="Enter your choice",font=promptfont)
    prompt.pack(padx=(70,0),pady=(100,0),side="top")

    #labelop=CTkLabel(master=frame,text="choose a choice",font=promptfont)
    #labelop.pack(padx=(700,0),pady=80,side="left")

#choice menu
    options=["🪨","🗞️","✂️"]
    menu=CTkOptionMenu(frame,values=options,corner_radius=30,height=50,width=200,fg_color="#FF8000",)
    menu.pack(padx=80,pady=(50,0),side="top")

#shoot button
    shootbutton=CTkButton(frame,text="Shoot!",corner_radius=40,width=150,height=50,command=lambda:game(menu,app,promptfont,headerfont))
    shootbutton.pack(padx=80,pady=(70,0),side="top")
#exit button
    exitbutton=CTkButton(master=frame,text="Exit",corner_radius=40,width=150,height=50,fg_color="red",command=lambda:exit(app))
    exitbutton.pack(side="top",padx=80,pady=(20,0))


    app.mainloop()

mainf(app)
