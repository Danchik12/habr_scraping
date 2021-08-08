#loading  libraries
import pandas as pd         
import numpy as np
from tkinter import *
import webbrowser
import random
from tkinter import ttk
#loading  data.csv
index=["post_name","post_link"]   # Column names
csd=pd.read_csv("data.csv",names=index,header=None,sep=",",engine="python")
dates=pd.DataFrame(csd)
def rand(event):             #random article
    link=random.choice(dates["post_link"])
    webbrowser.open(link)
def select(event):              #select article
    value=box.get(box.curselection())
    indexed=dates.index[dates.post_name==value].tolist()
    link=dates.post_link[dates.index[indexed]].tolist()
    webbrowser.open(link[0])
root=Tk()
root.geometry("450x500")
root.title("Статьи Habr")
root.iconbitmap('icone.ico')

    
    
      
    

scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT,fill=Y)
scroll=Scrollbar(root,orient='horizontal')

box=Listbox(root,width=50,height=50,font=24, yscrollcommand = scrollbar.set,xscrollcommand=scroll.set)
for i in dates["post_name"]:
    box.insert(0,i)
    
but=Button(root,text="читать рандомную статью",font=12)
but.bind("<Button-1>",rand)
box.bind("<Double-Button-1>",select)
scrollbar.config( command = box.yview )
scroll.config(command=box.xview)
but.pack(side=BOTTOM)
scroll.pack(side=BOTTOM,fill=X)
box.pack(side=BOTTOM)











root.mainloop()

