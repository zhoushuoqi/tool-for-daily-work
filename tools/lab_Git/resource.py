import os
import paramiko


     
#choose = raw_input(' 1. GA 768 \n 2. GA 1080 \n 3. GB 768 \n 4. GB 1080 \n Any other press for quit:\n Input: ')


def serverConnect(node_ip):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())   
    ssh.connect(hostname=node_ip, port=22, username='mats', password='cienet')
    return ssh
#ssh = serverConnect()
#stdin, stdout, stderr = ssh.exec_command('ls /cygdrive/c/Users/mats/MATS')
#res_list = stdout.readlines()
#print res_list
#print stdout.read()
#ssh.close()

def fun2(path,path_image):

    a = range(1,16)
    node_no = [i + 1 for i in a]
    for node in node_no:
        node_ip = '10.100.29.%d'%(node)
        try:
            ssh = serverConnect(node_ip)
            stdin, stdout, stderr = ssh.exec_command('ls /cygdrive/c/gitdata/info3/my20-Intel-768P/audio')
            stdin2, stdout2, stderr2 = ssh.exec_command('ls /cygdrive/c/gitdata/info3/%s/%s'%(path,path_image))
            stdin3, stdout3, stderr3 = ssh.exec_command('ls /cygdrive/c/gitdata/info3/%s/operations'%(path))
            stdin4, stdout4, stderr4 = ssh.exec_command('ls /cygdrive/c/Users/mats/MATS/python')
            res_list_audio = stdout.readlines()
            res_list_image = stdout2.readlines()
            res_list_operation = stdout3.readlines()
            res_list_python = stdout4.readlines()
            output =  'Node_%d'%(node-1),'audio:',len(res_list_audio),'image:',len(res_list_image),'operation:',len(res_list_operation),'python:',len(res_list_python)
            ssh.close()
            print output
        except:
            output =  'Node_%d might not online'%(node-1)
            print output




