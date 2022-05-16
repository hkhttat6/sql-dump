import os
import re
# p=open(os.getcwd()+"\\2.html", encoding='utf-8').readlines()
# #bing
# rcp='"><h2><a href="'+'(.*?)'+'" h="'
# rc=re.findall(rcp , str(p) )
# for rc1 in rc:
#     open(os.getcwd()+"\\url list "+'google'+".txt" ,'a' ,encoding='utf-8').write(rc1 +'\n')
# # print(rc)
# # doukdoukgo
# rcp='<a rel="nofollow" class="result__a" href="'+'(.*?)'+'">'
# rc=re.findall(rcp , str(p) )
# for rc1 in rc:
#     open(os.getcwd()+"\\url list "+'duckduckgo'+".txt" ,'a' ,encoding='utf-8').write(rc1 +'\n')
# # print(rc)
# #google
# if True:
#     p=open(os.getcwd()+"\\2.html", encoding='utf-8').readlines()
#     for i in p:
#         try:
#             if '/url?q=' in i:
#                 rcp='"><a href="/url'+'(.*?)'+'sa='
#                 rc=re.findall(rcp , i )
#                 for rc1 in rc:
#                     print(rc1[3:-2])
#                                    
#         except:
#             pass
# p1=open(os.getcwd()+"\\bing.html" ,'r' ,encoding='utf-8').write(str(page)+'\n')
# rcp='"><h2><a href="'+'(.*?)'+'" h="'
# rc=re.findall(rcp , str(p) )
# print(rc)
# for rc1 in rc:
#     open(os.getcwd()+"\\url list "+'BING'+".txt" ,'a' ,encoding='utf-8').write(rc1 +'\n')
def reg1(i):
    
    rcp='http://'+'(.*?)'+'/'+'(.*?)'+'?'+'(.*?)'+'='
    rcp1='https://'+'(.*?)'+'/'+'(.*?)'+'?'+'(.*?)'+'='
    rc=re.findall(rcp , i )
    rc1=re.findall(rcp1 , i )
#     print(rc,rc1)
    bad=['google','youtube','facebook','instagram']
    
    if len(rc)>0 or len(rc1)>0 :
        
        for f in bad:
            if f in i:
                return False
        return True
    else:
        return False
# if True:
#     if True:
#         p=open(os.getcwd()+"\\duckduckgo.html", encoding='utf-8').readlines()
#         p1=open(os.getcwd()+"\\url list "+'duckduckgo'+".txt").readlines()
#         rcp='<a rel="nofollow" class="result__a" href="'+'(.*?)'+'">'
#         rc=re.findall(rcp , str(p) )
#         
#         for rc1 in rc:
#             print(rc1)
#             if reg1(rc1) and rc1 not in str(p1):
#                 print(rc1)
#                 open(os.getcwd()+"\\url list "+'duckduckgo'+".txt" ,'a' ,encoding='utf-8').write(rc1 +'\n')
#     
if True:
    if True:
        p=open(os.getcwd()+"\\g.html", encoding='utf-8').readlines()
        p1=open(os.getcwd()+"\\url list "+'google1'+".txt", encoding='utf-8').readlines()
        for i in p:
            try:
                if '/url?q=' in i:
                    rcp='"><a href="/url'+'(.*?)'+'sa='
                    rc=re.findall(rcp , i )
                    
                    
                    for rc1 in rc:
                        rc1=rc1[3:-1]
                        
                        if reg1(rc1) and rc1 not in str(p1):
                            print(rc1)
                            open(os.getcwd()+"\\url list "+'google1'+".txt" ,'a' ,encoding='utf-8').write(rc1 +'\n')         
            except:
                pass