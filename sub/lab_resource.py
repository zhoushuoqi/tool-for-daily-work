from Tkinter import *
import tkFileDialog
from tkMessageBox import *
import os
import paramiko


root = Tk() 
root.title("Shuoqi Tool")

def clear_function():
    txt_domains.configure(state='normal')
    txt_domains.delete(1.0,END)
    txt_domains.configure(state='disabled')

def run_function():
    c = var.get()
    if c == 1:
        path = '**confidential**'
        path_image = 'images-themeB'
    elif c == 2:
        path = '**confidential**'
        path_image = 'images'
    elif c == 3:
        path = '**confidential**'
        path_image = 'images'
    else:
        path = '**confidential**'
        path_image = 'images'

    def write(out):
        txt_domains.configure(state='normal')
        txt_domains.insert('end', out)
        txt_domains.configure(state='disabled')


    def serverConnect(node_ip):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())   
        ssh.connect(hostname=node_ip, port=22, username='**confidential**', password='**confidential**')
        return ssh

    node_num = int(e1.get())
    a = range(1,node_num+1)
    node_no = [i + 1 for i in a]
    for node in node_no:
        node_ip = '10.100.29.%d'%(node)
        try:
            ssh = serverConnect(node_ip)
            stdin, stdout, stderr = ssh.exec_command('ls **confidential**')
            stdin2, stdout2, stderr2 = ssh.exec_command('ls **confidential**/%s/%s'%(path,path_image))
            stdin3, stdout3, stderr3 = ssh.exec_command('ls **confidential**/%s/operations'%(path))
            stdin4, stdout4, stderr4 = ssh.exec_command('ls **confidential**')
            res_list_audio = stdout.readlines()
            res_list_image = stdout2.readlines()
            res_list_operation = stdout3.readlines()
            res_list_python = stdout4.readlines()
            #output =  'Node_%d\n'%(node-1),'audio:',len(res_list_audio),'image:',len(res_list_image),'operation:',len(res_list_operation),'python:',len(res_list_python),'\n'
            out = 'Node_%d:\nAudio:%s, Image:%s, Operation:%s, Python:%s \n'%(node-1,len(res_list_audio),len(res_list_image),len(res_list_operation),len(res_list_python))
            ssh.close()
            write(out)
            print out

        except Exception,IOError:
            info= 'Node_%d:\nError:%s. Ask Shuoqi for help! \n' %(node-1,IOError)
            write(info)
            print info







Label(root,text = 'Tool for check resource in lab ',fg='DarkViolet', font = "Chiller 25 bold").grid(row=0,columnspan=10,padx=5, pady=5)
Label(root,text = 'How many node in lab? ', font = "Verdana 10 bold").grid(row=1,column=3,columnspan=3,padx=5, pady=5)


e1 = Entry(root,width=20)
e1.grid(row=1,column=6,columnspan=2)


var = IntVar()
Radiobutton(root, text="GA 768P", variable=var, value=1,font = "Verdana 10 bold").grid(row=2,column=4,padx=5, pady=5)
Radiobutton(root, text="GA 1080P", variable=var, value=2,font = "Verdana 10 bold").grid(row=2,column=6,padx=5, pady=5)
Radiobutton(root, text="GB 768P", variable=var, value=3,font = "Verdana 10 bold").grid(row=3,column=4,padx=5, pady=5)
Radiobutton(root, text="GB 1080P", variable=var, value=4,font = "Verdana 10 bold").grid(row=3,column=6,padx=5, pady=5)


Button(root, text='Run', command=run_function,width=15,fg='yellow',bg='ForestGreen',font = "Verdana 12 bold").grid(row=4,column=4,padx=5, pady=5)
Button(root, text='Clear', command=clear_function,width=10,fg='yellow',bg='Crimson',font = "Verdana 12 bold").grid(row=4,column=6,padx=5, pady=5)
Button(root, text='Quit', command=root.quit,width=9,fg='black',bg='LightGrey',font = "Verdana 12 bold").grid(row=4,column=8,padx=5, pady=5)



txt_domains = Text(root,height=20,width=60)
txt_domains.grid(row =5,columnspan=10,rowspan=7,padx=5, pady=5)
scr_domains = Scrollbar(root,orient='vertical')
scr_domains.grid(row=5,column=10,sticky=S+N,rowspan=7)
txt_domains.config(yscrollcommand=scr_domains.set)
scr_domains.config(command=txt_domains.yview)

#text = Text(root,width=60,height=20,bg='Lavender',bd=5,state='disabled')
#text.grid(row =5,columnspan=10,rowspan=7)

Label(root, text="Copyright 2018 by Shuoqi Zhou",fg = "BlueViolet",font = "Verdana 10 bold").grid(columnspan=10,sticky=S)

root.mainloop()
