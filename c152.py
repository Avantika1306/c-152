# -*- coding: utf-8 -*-
from tkinter import *

root=Tk()
root.title("multidimensional arrays")
root.geometry("500x500")
label_1=Label(root)
label_1.place(relx=0.5,rely=0.4,anchor=CENTER)
array_1d=["ayana","ridhi","jungkook","mishka"]
print(array_1d[2])
array_2d=[["ayana","A"],["ridhi","B"],["jungkook","A"],["mishka","A"]]
print(array_2d[1][1])
array_3d=[[["ayana","A","excellent"],["ridhi","B","can do better"],["jungkook","A","awesome"],["mishka","A","good job"]]]
print(array_3d[0][1][2])

def show_report():
    label_1["text"]=array_3d[0][0][0]+ " got grade "+ array_3d[0][0][1]+" and she is doing "+array_3d[0][0][2]    
button_1=Button(root,text="show report",command=show_report)
button_1.place(relx=0.5,rely=0.3,anchor=CENTER)
root.mainloop()
