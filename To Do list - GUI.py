from tkinter import *
window=Tk()
window.geometry("520x450")
window.title("TO DO list")

#frame banner
framebanner=Frame(window,bg="#3E3E3E",width=450,height=80)
framebanner.pack(fill="both",side="top")

frameintersection = Frame(framebanner, bg="#694C56", width=70, height=80)


#frame margin
framemargin=Frame(window,bg="#000000",width=70,height=450)
framemargin.pack(fill="both",side="left")




#frame1
frame1=Frame(window,bg="#C0C0C0",width=400,height=450)
frame1.pack(fill="both",expand=True)


#label1(present in frame 1)
label1=Label(master=framebanner,text="To DO list",font=('Alice', 20, "bold"),bg="#3E3E3E",fg="white")
label1.pack(pady="5",padx="10")

#canvas1
canvas1= Canvas(frame1, bg="#C0C0C0", width=400, height=450, highlightthickness=0)
canvas1.pack(fill="both", expand=True, side="left", padx=100, pady=50)



#label2
label2=Label(canvas1,text="To DO list:",font=('Alice', 15),bg="#C0C0C0",fg="black")
text1=Entry(master=canvas1,width=30)
text1.insert(END,string="Enter a task!")

#Inserting data
def insert():
    temp=text1.get()
    if(temp !="" and temp !="Enter a task!"):
        listbox.insert("end",temp)
    text1.delete(0,"end")


#deleting data
def delete():
    selected_index=listbox.curselection()
    if selected_index:
        for i in selected_index:
            listbox.delete(i)
    else:
        listbox.delete("end")
#exit the app
def exitapp():
    window.destroy()



#Insert data button
button1=Button(width="10",height="1",text="Add task",command=insert)
button1.bind("<Return>",lambda event:insert())


#Delete data button
button2=Button(width="10",height="1",text="Delete",command=delete)

#Exit button
button3=Button(width="10",height="1",text="Exit app",command=exitapp)



#canvas1 anchoring
canvas1.create_window(20,100,window=text1,anchor="nw")
canvas1.create_window(70,50,window=label2,anchor="n")
canvas1.create_window(63,150,window=button1,anchor="center")
canvas1.create_window(63,200,window=button2,anchor="center")
canvas1.create_window(63,250,window=button3,anchor="center")

#canvas2
canvas2= Canvas(frame1, bg="#C0C0C0", width=300, height=350, highlightthickness=0)
canvas2.pack(fill="both",side="right",padx=(0,300),pady=50)

#label 3
label3=Label(text="Tasks",font=("Alice",20),bg="#C0C0C0",fg="black")
#list box in canvas2
listbox=Listbox(canvas2,width=60,height=20)
canvas2.create_window(200,250,window=listbox)
canvas2.create_window(50,50,window=label3, anchor='n')



window.mainloop()
