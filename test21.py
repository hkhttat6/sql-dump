import os
import re
dorklist=open(os.getcwd()+"\\dork.txt", encoding='utf-8').readlines()
for dork in dorklist:
    dork=dork.split(',')[0]
    try:
        l=['login','siginup','password','email','You Plan','Username','cart','shop new','Shopping','checkout','Credit/Debit Card','cvv','cvc','paypal','My Balance','Wallet']
        for k in l :
            dork1='inurl:"%s"' % dork
            dork1+=',intext:"%s"' % k
            #print(dork1)
            #print(k)
            open(os.getcwd()+"\\dork hot"+".txt" ,'a' ,encoding='utf-8').write(dork1 +'\n')
            dork1=''
    except:
        pass
for dork in dorklist:
    try:
        dork=dork.split(',')[0]
        
        dork='?'+dork.split('?')[1]
        
        l=['login','siginup','password','email','You Plan','Username','cart','shop new','Shopping','checkout','Credit/Debit Card','cvv','cvc','paypal','My Balance','Wallet']
        for k in l :
            dork1='inurl:"%s"' % dork
            dork1+=',intext:"%s"' % k
            #print(dork1)
            #print(k)
            open(os.getcwd()+"\\dork hot1"+".txt" ,'a' ,encoding='utf-8').write(dork1 +'\n')
            dork1=''
    except:
        pass

