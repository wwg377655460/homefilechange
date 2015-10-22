#coding:utf-8
#!/usr/bin/env python
 
 
from threading import Timer
import time
import os
import shutil

url2 = "C:\Users\WSDevotion\Desktop";
url = "/Users/wsdevotion/Desktop";
 
def getchangfile(list_num):
	for lis in list_num:
		if lis not in listfile1:
			print url2+os.path.sep+lis
			if os.path.isfile(url2+os.path.sep+lis):
				# fp = open(url+lis,"r")
				# fp1 = open("/Users/wsdevotion","w")
				shutil.copy(url2+os.path.sep+lis,"C://") 


def delayrun():
	
    listfile=os.listdir(url)
    if(len(listfile1)!=len(listfile)):
    	getchangfile(listfile)
    	global listfile1
    	listfile1 = listfile

    else:
    	print "22"
   


timer_interval=1
global url2
listfile1=os.listdir(url2);
t=Timer(timer_interval,delayrun)
t.start()
while True:
    time.sleep(2)
    delayrun()