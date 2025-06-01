import random
from customtkinter import *
from module1task3 import nums
from module3task3 import char
from module2task3 import spechar


app=CTk()
app.geometry("1900x1080")
app.title("Password generator")
screenwidth=app.winfo_screenwidth()
screenheight=app.winfo_screenheight()
set_appearance_mode("dark")
def tbclear():
    textbox.delete(0,"end")
def gen():
    charnum=textbox.get()
    if charnum.isdigit():
        textbox.delete(0,'end')
        for i in range(int(charnum)):
            arrchoice = random.choice(mainset)
            characters =''+ str(random.choice(arrchoice))
            textbox.insert(0, characters)
    else:
        textbox.delete(0,"end")
        textbox.insert(0,"please Enter a number!")
        textbox.after(2000,tbclear)
def clear():
    textbox.delete(0,"end")


mainset=[nums,spechar,char]



heading=CTkLabel(master=app,text="Password generator",font=("Arial",29,"bold"))
heading.pack(padx=500,pady=50)
entryfont=CTkFont(size=22,family="Arial",weight="bold")

textbox=CTkEntry(app,placeholder_text="number of characters",width=300,height=60,fg_color="white",
                 text_color="black",corner_radius=40,font=entryfont)
textbox.pack(padx=100,pady=(10,50))

buttonfont=CTkFont(size=17,family="Arial",weight="bold")
generatebutton=CTkButton(width=200,height=40,master=app,text="generate",font=buttonfont,corner_radius=40,fg_color="teal",command=lambda : gen())
generatebutton.pack(padx=100,pady=10)
exitbutton=CTkButton(width=200,height=40,master=app,text="Exit",font=buttonfont,corner_radius=40,fg_color="red",command=lambda : exit(None))
buttonclear=CTkButton(width=200,height=40,master=app,text="clear",font=buttonfont,corner_radius=40,fg_color="orange",command=lambda : clear())
buttonclear.pack(padx=100,pady=10)
exitbutton.pack(padx=100,pady=10)




app.mainloop()
