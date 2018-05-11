from Tkinter import *
sys.path.insert(0, './tools/report_check')
from tool import *
import tkFileDialog
from tkMessageBox import *

def show_entry_fields():
    try:
        if e1.get():
            if e2.get():
                logpath =e1.get()
                filepath =e2.get()
                covert(filepath)
                check_report(logpath)
                showinfo(title='Success', message='Finish!')
        else:
            showinfo(title='ERRROR', message='mandatory data missing')
        

    except Exception,IOError:
        info= 'Error:%s. Ask Shuoqi for help!' %(IOError)
        #info=info[1]
        showerror(title='ERRROR', message=info) 
        



def selectPath():
    path_ = tkFileDialog.askdirectory()
    path.set(path_)

def selectFile():
    fpath_ = tkFileDialog.askopenfilename(title='open file',filetypes=[('Excel','*.xls *.xlsx'),('All Files','*')])
    fpath.set(fpath_)


master = Tk()
master.title("Shuoqi Tool")   
path = StringVar()
fpath =  StringVar()
Label(master, text="Report path: ").grid(row=1)
Label(master, text="Log path: ").grid(row=2)

e1 = Entry(master,width=50,textvariable = path)
e2 = Entry(master,width=50,textvariable = fpath)



e1.grid(row=2, column=1)
e2.grid(row=1, column=1)

Label(master,text = 'Tool for check report in lab ',fg='DarkViolet', font = "Chiller 25 bold").grid(row=0,columnspan=10,padx=5, pady=5)
Button(master, text='Run', command=show_entry_fields,width=20,fg='yellow',bg='ForestGreen',font = "Futura 12 bold").grid(row=4, column=1)
Button(master, text='Quit', command=master.quit,width=6,fg='black',bg='LightGrey',font = "Verdana 10 bold").grid(row=4, column=2)
Button(master, text = "...", command = selectFile,width=6).grid(row =1, column = 2)
Button(master, text = "...", command = selectPath,width=6).grid(row =2, column = 2)
Label(master, text="Copyright 2018 by Shuoqi Zhou",fg = "BlueViolet",font = "Verdana 10 bold").grid(row =5, column = 1)
mainloop( )