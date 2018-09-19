import os
import subprocess
import re
import pandas as pd



def get_deviceid():
    cmd= 'adb devices'
    proc2 = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    deviceid_read = proc2.stdout.read()
    p = re.compile('(.*)\tdevice\r')
    deviceid = p.findall(deviceid_read)
    return deviceid_read,deviceid

def get_imei(deviceid):
    cmd = 'adb -s %s shell service call iphonesubinfo 1'%(deviceid)
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    output = proc.stdout.read()
    p = re.compile("'(.*)'")
    p2 = p.findall(output)
    p3 =  ' '.join(p2)
    p4 = p3.replace('. ','')
    p5 = p4.replace('.','')
    #output =  'IMEI: %s'%(p5)
    return p5[:15]

def get_version(deviceid):
    cmd = 'adb -s %s shell getprop ro.build.version.release'%(deviceid)
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    version = proc.stdout.read()
    p = re.compile('(.*)\r\r')
    version = p.findall(version)
    return version[0]

def get_buildversion(deviceid):
    cmd = 'adb -s %s shell getprop  ro.product.swversion'%(deviceid)
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    build = proc.stdout.read()
    p = re.compile('(.*)\r\r')
    build = p.findall(build)
    return build[0]

def get_bluetooth(deviceid):
    cmd = 'adb -s %s shell dumpsys bluetooth_manager'%(deviceid)
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    build = proc.stdout.read()
    p = re.compile('CONNECTED (.*)\r\r')
    bluetooth = p.findall(build)
    return bluetooth[0]


adb_devices,deviceid = get_deviceid()
print adb_devices
print '----------------------------------------------'
tot = []
for i in deviceid:
    deviceid = i
    imei = get_imei(i)
    version = get_version(i)
    build = get_buildversion(i)
    lst = [deviceid,imei,version,build]
    tot.append(lst)
    print i+'     Done'
    print deviceid,imei,version,build
df = pd.DataFrame(tot,columns=['Serial number', 'IMEI', 'Android version', 'Build number'])
writer = pd.ExcelWriter('output.xlsx')
df.to_excel(writer,'Sheet1',index=False)
writer.save()
print '----------------------------------------------'
print 'Total %s device(s)'%(len(tot))+'            Done!'
    