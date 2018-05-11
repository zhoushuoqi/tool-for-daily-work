from Tkinter import *
sys.path.insert(0, './tools/python')
from tool_new import *
import tkFileDialog
from tkMessageBox import *

def selectFile():
    fpath_ = tkFileDialog.askopenfilename(title='open file',filetypes=[('Excel','*.xls *.xlsx'),('All Files','*')])
    fpath.set(fpath_)

def covert_file():
    try:
        if e1.get():
            filepath =e1.get()
            covert(filepath)
            showinfo(title='Success', message='Finish!')
        else:
            showinfo(title='ERRROR', message='mandatory data missing')
        

    except (IOError ,ZeroDivisionError),e:
        showerror(title='ERROR', message= e)
        showerror(title='ERROR', message= 'Something wrong! Ask ShuoQI for help!')

def run_function():
    c = var.get()
    if c == 1:
        try:
            checkpre()
            text.configure(state='normal')
            text.delete(1.0,END)
            text.insert('end', 'Output path: ./Ztool/tools/python/result/check_error.csv')
            text.configure(state='disabled')
            showinfo(title='Success', message='Finish!')
        except Exception,IOError:
            info= 'Error:%s. Ask Shuoqi for help!' %(IOError)
            showerror(title='ERRROR', message=info) 
    elif c == 2:
        try:
            check()
            text.configure(state='normal')
            text.delete(1.0,END)
            text.insert('end', 'Output path: ./Ztool/tools/python/result/result.csv')
            text.configure(state='disabled')
            showinfo(title='Success', message='Finish!')
        except Exception,IOError:
            info= 'Error:%s. Ask Shuoqi for help!' %(IOError)
            showerror(title='ERRROR', message=info) 
    elif c == 3:
        try:
            count()
            text.configure(state='normal')
            text.delete(1.0,END)
            text.insert('end', 'Output path: ./Ztool/tools/python/result/count.csv')
            text.configure(state='disabled')
            showinfo(title='Success', message='Finish!')
        except Exception,IOError:
            info= 'Error:%s. Ask Shuoqi for help!' %(IOError)
            showerror(title='ERRROR', message=info) 
    elif c == 4:
        try:
            df = count2() 
            text.configure(state='normal')
            text.delete(1.0,END)          
            text.insert('end', 'Output path: ./Ztool/tools/python/result/count2.csv')
            text.configure(state='disabled')
            showinfo(title='Success', message='Finish!')
        except Exception,IOError:
            info= 'Error:%s. Ask Shuoqi for help!' %(IOError)
            showerror(title='ERRROR', message=info) 
    else:
        try:
            len = count3() 
            text.configure(state='normal')
            text.delete(1.0,END)
            text.insert('end', 'Total use %d cases'%(len))
            text.configure(state='disabled')
            showinfo(title='Success', message='Finish!')
        except Exception,IOError:
            info= 'Error:%s. Ask Shuoqi for help!' %(IOError)
            showerror(title='ERRROR', message=info) 
master = Tk()
master.title("Shuoqi Tool")   

fpath =  StringVar()
Label(master, text="File path: ",font = "Verdana 10 bold").grid(row=1,column=0)

e1 = Entry(master,width=60,textvariable = fpath)
e1.grid(row=1, column=1)

var = IntVar()

Label(master,text = 'Tool for node assignment in lab ',fg='DarkViolet', font = "Chiller 25 bold").grid(row=0,columnspan=10,padx=5, pady=5)
Radiobutton(master, text="Check error", variable=var, value=1,font = "Verdana 10 bold").grid(row=2,sticky=W,padx=20, pady=5)
Radiobutton(master, text="Node assignment", variable=var, value=2,font = "Verdana 10 bold").grid(row=3,sticky=W,padx=20, pady=5)
Radiobutton(master, text="Node performance", variable=var, value=3,font = "Verdana 10 bold").grid(row=4,sticky=W,padx=20, pady=5)
Radiobutton(master, text="Precode case count", variable=var, value=4,font = "Verdana 10 bold").grid(row=5,sticky=W,padx=20, pady=5)
Radiobutton(master, text="Sum of cases", variable=var, value=5,font = "Verdana 10 bold").grid(row=6,sticky=W,padx=20, pady=5)



Button(master, text='Run', command=run_function,width=15,fg='yellow',bg='ForestGreen',font = "Verdana 12 bold").grid(row=7)
Button(master, text='Quit', command=master.quit,width=9,fg='black',bg='LightGrey',font = "Verdana 12 bold").grid(row=8)
Button(master, text = "...", command = selectFile,width=6).grid(row =1, column = 2)
Button(master, text = "Covert", command = covert_file,width=6,bg='ForestGreen',fg='yellow',font = "Verdana 10 bold").grid(row =1, column = 3)
text = Text(master,width=50,height=20,bg='Lavender',bd=5,state='disabled')
text.grid(row =2, column = 1,rowspan=7)

#text.configure(state='normal')
#text.insert('end', 'Some Text')
#text.configure(state='disabled')

Label(master, text="Copyright 2018 by Shuoqi Zhou",fg = "BlueViolet",font = "Verdana 10 bold").grid(row =10, column = 1)
mainloop( )