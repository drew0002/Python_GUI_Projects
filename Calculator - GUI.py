from tkinter import *
from tkinter import font as tkf

window=Tk()
window.title("Calculator")
window.geometry("284x270")
frame1=Frame(window,width=320,height=65,bg="#47c7fc")

entrybox= Entry(frame1, width=50, font=("Arial", 14),highlightthickness=3,highlightcolor="white")
entrybox.pack(padx=10,pady=10,fill="both",expand="True")

canvas=Canvas(window,width=320,height=235)
frame1.pack(fill="both",expand="true")
canvas.pack()

entrybox.focus_set()

def wipe():
    entrybox.delete(0,"end")

def erase():
    entrybox.delete(0,"end")

def entry(event=None):
    input = entrybox.get()
    try:
        value=eval(input)
        entrybox.delete(0,"end")
        entrybox.insert(0,str(value))
    except:
        entrybox.delete(0,"end")
        entrybox.insert(0, "Error!")
        window.after(2000,wipe)

def getval(a):
    entrybox.insert("end",a)

buttonfont=tkf.Font(family="Kozuka Gothic Pr6N B",size=9,weight="bold")

#button 1
number1=Button(canvas,text="1",width=7,height=3,bg="#808080",font=buttonfont,command=lambda:getval(1))
#button 2
number2=Button(canvas,text="2",width=7,height=3,bg="#808080",font=buttonfont,command=lambda:getval(2))
#button 3
number3=Button(canvas,text="3",width=7,height=3,bg="#808080",command=lambda:getval(3),font=buttonfont)
#button 4
number4=Button(canvas,text="4",width=7,height=3,bg="#808080",command=lambda:getval(4),font=buttonfont)
#button 5
number5=Button(canvas,text="5",width=7,height=3,bg="#808080",command=lambda:getval(5),font=buttonfont)
#button 6
number6=Button(canvas,text="6",width=7,height=3,bg="#808080",command=lambda:getval(6),font=buttonfont)
#button 7
number7=Button(canvas,text="7",width=7,height=3,bg="#808080",command=lambda:getval(7),font=buttonfont)
#button 8
number8=Button(canvas,text="8",width=7,height=3,bg="#808080",command=lambda:getval(8),font=buttonfont)
#button 9
number9=Button(canvas,text="9",width=7,height=3,bg="#808080",command=lambda:getval(9),font=buttonfont)
#button 0
number0=Button(canvas,text="0",width=7,height=3,bg="#FF8000",command=lambda:getval(0),font=buttonfont)
#button.
numberdec=Button(canvas,text=".",width=7,height=3,bg="#FF8000",command=lambda:getval('.'),font=buttonfont)
#button-
numbermin=Button(canvas,text="-",width=7,height=3,bg="#FF8000",command=lambda:getval('-'),font=buttonfont)
#button=
numbereq=Button(canvas,text="=",width=7,height=3,bg="red",command=lambda:entry(),font=buttonfont)
#button/
numberdiv=Button(canvas,text="/",width=7,height=3,bg="#FF8000",command=lambda:getval('/'),font=buttonfont)
#buttonx
numbermul=Button(canvas,text="X",width=7,height=3,bg="#FF8000",command=lambda:getval('*'),font=buttonfont)
#nuttonplu
numberplu=Button(canvas,text="+",width=7,height=3,bg="#FF8000",command=lambda:getval('+'),font=buttonfont)
#clear
clearbut=Button(canvas,text="c",height=200,width=6,font=buttonfont,bg="#41424C",command=erase)



#packing the buttons
#button 1
canvas.create_window(0,0,window=number1,anchor="nw")
#button 2
canvas.create_window(87,0,window=number2,anchor="n")
#button 3
canvas.create_window(175,0,window=number3,anchor="ne")
#button 4
canvas.create_window(0,83,window=number4,anchor="w")
#button 5
canvas.create_window(87,83,window=number5,anchor="center")
# button 6
canvas.create_window(175,83,window=number6,anchor="e")
# button 7
canvas.create_window(0,166,window=number7,anchor="sw")
#button 8
canvas.create_window(87,166,window=number8,anchor="s")
#button 9
canvas.create_window(175,166,window=number9,anchor="se")
# button 0
canvas.create_window(0,221,window=number0,anchor="sw")
# button .
canvas.create_window(87,221,window=numberdec,anchor="s")
#button -
canvas.create_window(145,221,window=numbermin,anchor="s")
#button =
canvas.create_window(203,221,window=numbereq,anchor="s")
#button/
canvas.create_window(233,166,window=numberdiv,anchor="se")
#buttonX
canvas.create_window(233,83,window=numbermul,anchor="e")
#button+
canvas.create_window(233,0,window=numberplu,anchor="ne")
#clear
canvas.create_window(284,100,window=clearbut,anchor="e")


window.bind("<Return>",entry)







window.mainloop()
