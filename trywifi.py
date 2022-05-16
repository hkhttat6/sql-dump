from usp.tree import sitemap_tree_for_homepage
import requests
import re
import os
import socket
from bs4 import BeautifulSoup
from thirdparty.six.moves import urllib as _urllib
from fake_useragent import UserAgent
from time import sleep
from lib.core.enums import HTTP_HEADER
from subprocess import Popen , PIPE
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# for i in range(1000000):
#     try:
#         s.connect(('192.168.4.1',i))
#         s.close()
#         s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     except:
#         pass
dork='"'+os.getcwd()+"\\dork hot1.txt"+'@1@'+"1"+'"'
print(dork)

k='python  sqlmap.py -g '+dork
print(k)#,shell=True , stdout=PIPE
cmd=Popen(k,shell=True , stdout=PIPE).communicate()
dorklist=open(os.getcwd()+"\\url list google33.txt", encoding='utf-8').readlines()
for i in dorklist:
    print(i)
    page = None
    data = None
    requestHeaders = {}
    responseHeaders = {}
    requestHeaders[HTTP_HEADER.USER_AGENT] = UserAgent().random
    try:
        req = _urllib.request.Request(i, headers=requestHeaders)
        conn = _urllib.request.urlopen(req)
        page = conn.read()
        s=re.findall('"description" content="(.*?)"',str(page))
        for i in s:
            open(os.getcwd()+"\\url list "+'google77'+".txt" ,'a' ,encoding='utf-8').write(i +'\n')
    except:
        pass