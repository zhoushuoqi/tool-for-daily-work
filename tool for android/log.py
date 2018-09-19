import os
import subprocess
import re
import datetime
def get_deviceid():
    cmd= 'adb devices'
    proc2 = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    deviceid_read = proc2.stdout.read()
    p = re.compile('(.*)\tdevice\r')
    deviceid = p.findall(deviceid_read)
    return deviceid



def pull():
    deviceid = get_deviceid()
    dict_list = {}
    print '---------------pull log-----------------\n'
    print 'No.  ------devices------'
    for i,j in enumerate(deviceid):
        print i+1,"     ",j
        dict_list[i+1] =j
    input_v = raw_input('\n\nwhich device you want catching log from (No.): ')
    print '----------------------------------------------------------------'
    deviceid2 = dict_list[int(input_v)]
    now_time = datetime.datetime.now()
    now_time =datetime.datetime.now().strftime('%Y%m%d_%H%M')
    create_folder = 'mkdir log_%s'%(now_time)
    os.system(create_folder)
    cmd = 'adb -s %s pull /data/tombstones log_%s'%(deviceid2,now_time)
    cmd2 = 'adb -s %s pull /data/misc/logd log_%s'%(deviceid2,now_time)
    os.system(cmd)
    os.system(cmd2)
    print '\n'+ deviceid2 +'---------Done!\n'
    print '----------------------------------------------------------------'

def clear():
    deviceid = get_deviceid()
    dict_list = {}
    print '---------------clear log------------------\n'
    print 'No.  ------devices------'
    for i,j in enumerate(deviceid):
        print i+1,"     ",j
        dict_list[i+1] =j
    input_v = raw_input('\n\nWhich deivce you want clear log from (No.): ')
    deviceid2 = dict_list[int(input_v)]
    cmd = 'adb -s %s shell rm -rf /data/misc/logd'%(deviceid2)
    cmd2 = 'adb -s %s shell rm -rf /data/tombstones'%(deviceid2)
    os.system(cmd)
    os.system(cmd2)
    print '\n'+ deviceid2 +'---------Done!\n'
    print '----------------------------------------------------------------'


def clear_all():
    deviceid = get_deviceid()
    for i in deviceid:
        cmd = 'adb -s %s shell rm -rf /data/misc/logd'%(i)
        cmd2 = 'adb -s %s shell rm -rf /data/tombstones'%(i)
        os.system(cmd)
        os.system(cmd2)
        print '---------Done!\n'
choice = ''
while choice != 'q':
    choice = raw_input("What would you like to do?\n1.pull log. \n2.clear log  \n3.clear all log \nInput: ")
    if choice == '1':
        pull()
    elif choice == '2':
        clear()
    elif choice == '3':
        clear_all()
    else:
        print("That is not a valid input.")