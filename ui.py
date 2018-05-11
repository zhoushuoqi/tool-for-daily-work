# -*- coding:UTF-8 -*-
from Tkinter import *
import tkMessageBox
import sys
import os
import Tkinter

  

def quit():    
    #quit = tkMessageBox.askokcancel('Shuoqi Zhou','wana quit?')
    #if quit == True:
    root.destroy()



def report_check():   
    os.system('python ./sub/check_report.py')

def node_assignment():   
    os.system('python ./sub/node_assignment.py')

def lab_resource():   
    os.system('python ./sub/lab_resource.py')



root = Tk() 
root.title("Shuoqi Tool") 
Label(root,text = 'Tool for Cienet Auto Lab', font = "Chiller 25 bold").grid(row=0,columnspan=5,padx=5, pady=5)  
Label(root,text = 'Tool 1', font = "Gabriola 15 bold").grid(row=1,column=0)
Button(root, text='check report', command=report_check, width=15, height=2, font = "Verdana 10 ").grid(row=1,column=1,sticky=W+E+N+S,padx=5, pady=5)
Label(root,text = 'Tool 2', font = "Gabriola 15 bold").grid(row=2,column=0)
Button(root, text='node_assignment', command=node_assignment, width=15, height=2, font = "Verdana 10 ").grid(row=2,column=1,sticky=W+E+N+S,padx=5, pady=5)
Label(root,text = 'Tool 3', font = "Gabriola 15 bold").grid(row=3,column=0)
Button(root, text='lab_resource', command=lab_resource, width=15, height=2, font = "Verdana 10 ").grid(row=3,column=1,sticky=W+E+N+S,padx=5, pady=5)
#Button(root, text='Quit', command=quit).grid(row=10, column=2)


photo=PhotoImage(file="logo.gif", width=150, height=150)
label=Label(image=photo)
label.image=photo
label.grid(row=1,column=3,rowspan=3,sticky=W+E+N+S, padx=5, pady=5)


Label(root, text="Copyright 2018 by Shuoqi Zhou",fg = "BlueViolet",font = "Verdana 10 bold").grid(columnspan=5,sticky=S)

root.mainloop()
