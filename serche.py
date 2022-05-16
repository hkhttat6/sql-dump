import re
import socket
import os
import time
from lib.core.common import getSafeExString
from lib.core.common import popValue
from lib.core.common import pushValue
from lib.core.common import readInput
from lib.core.common import urlencode
from lib.core.convert import getBytes
from lib.core.convert import getUnicode
from lib.core.data import conf
from lib.core.data import kb
from lib.core.data import logger
from lib.core.decorators import stackedmethod
from lib.core.enums import CUSTOM_LOGGING
from lib.core.enums import HTTP_HEADER
from lib.core.enums import REDIRECTION
from lib.core.exception import SqlmapBaseException
from lib.core.exception import SqlmapConnectionException
from lib.core.exception import SqlmapUserQuitException
from lib.core.settings import BING_REGEX
from lib.core.settings import DUCKDUCKGO_REGEX
from lib.core.settings import DUMMY_SEARCH_USER_AGENT
from lib.core.settings import GOOGLE_CONSENT_COOKIE
from lib.core.settings import GOOGLE_REGEX
from lib.core.settings import HTTP_ACCEPT_ENCODING_HEADER_VALUE
from lib.core.settings import UNICODE_ENCODING
from lib.request.basic import decodePage
from thirdparty.six.moves import http_client as _http_client
from thirdparty.six.moves import urllib as _urllib
from thirdparty.socks import socks
from fake_useragent import UserAgent
#<<<<<<<<< chesker list of site>>>>>>>>>>>>>>>>>
def ls():
    ##print(i)
    p1=open(os.getcwd()+"\\url list "+'google'+".txt", encoding='utf-8').readlines()
    site=[]
    for i in p1:
        rcp='://'+'(.*?)'+'/'+'(.*?)'+'?'+'(.*?)'+'='
        rcp1='://'+'(.*?)'+'/'+'(.*?)'+'?'+'(.*?)'+'='
        rc=re.findall(rcp , i )
        try:
            site.append(rc[0][0])
        except:
            pass
    return site
lsite=ls()
#<<<<<<<<< chesker the sql target>>>>>>>>>>>>>>>>>
def reg1(i):
    global lsite
    rcp='://'+'(.*?)'+'/'+'(.*?)'+'?'+'(.*?)'+'='
    rc=re.findall(rcp , i )
    bad=['google','youtube','facebook','instagram']
    if len(rc)>0 and  rc[0][0] not in lsite:
        for f in bad:
            if f in i:
                return False
        lsite.append(rc[0][0])
        return True
    else:
        return False
#<<<<<<<<< chesker the sql target>>>>>>>>>>>>>>>>>
def _search_google(dork):
    print(dork)
    if not dork:
        return None

    page = None
    data = None
    requestHeaders = {}
    responseHeaders = {}
    print(conf.httpHeaders)
    requestHeaders[HTTP_HEADER.USER_AGENT] = dict(conf.httpHeaders).get(HTTP_HEADER.USER_AGENT, DUMMY_SEARCH_USER_AGENT)
    print(requestHeaders[HTTP_HEADER.USER_AGENT])
    requestHeaders[HTTP_HEADER.ACCEPT_ENCODING] = HTTP_ACCEPT_ENCODING_HEADER_VALUE
    requestHeaders[HTTP_HEADER.COOKIE] = GOOGLE_CONSENT_COOKIE
    
    try:
        req = _urllib.request.Request("https://www.google.com/ncr", headers=requestHeaders)
        conn = _urllib.request.urlopen(req)
    except Exception as ex:
        errMsg = "unable to connect to Google ('%s')" % getSafeExString(ex)
        raise SqlmapConnectionException(errMsg)

    gpage = conf.googlePage if conf.googlePage > 1 else 1
    logger.info("using search result page #%d" % gpage)

    url = "https://www.google.com/search?"                                  # NOTE: if consent fails, try to use the "http://"
    url += "q=%s&" % urlencode(dork, convall=True)
    url += "num=100&hl=en&complete=0&safe=off&filter=0&btnG=Search"
    url += "&start=%d" % ((gpage - 1) * 100)

    try:
        req = _urllib.request.Request(url, headers=requestHeaders)
        conn = _urllib.request.urlopen(req)

        requestMsg = "HTTP request:\nGET %s" % url
        requestMsg += " %s" % _http_client.HTTPConnection._http_vsn_str
        logger.log(CUSTOM_LOGGING.TRAFFIC_OUT, requestMsg)

        page = conn.read()
        code = conn.code
        status = conn.msg
        responseHeaders = conn.info()

        responseMsg = "HTTP response (%s - %d):\n" % (status, code)

        if conf.verbose <= 4:
            responseMsg += getUnicode(responseHeaders, UNICODE_ENCODING)
        elif conf.verbose > 4:
            responseMsg += "%s\n%s\n" % (responseHeaders, page)

        logger.log(CUSTOM_LOGGING.TRAFFIC_IN, responseMsg)
    except _urllib.error.HTTPError as ex:
        try:
            page = ex.read()
            responseHeaders = ex.info()
        except Exception as _:
            warnMsg = "problem occurred while trying to get "
            warnMsg += "an error page information (%s)" % getSafeExString(_)
            logger.critical(warnMsg)
            return None
    except (_urllib.error.URLError, _http_client.error, socket.error, socket.timeout, socks.ProxyError):
        errMsg = "unable to connect to Google"
        raise SqlmapConnectionException(errMsg)

    page = decodePage(page, responseHeaders.get(HTTP_HEADER.CONTENT_ENCODING), responseHeaders.get(HTTP_HEADER.CONTENT_TYPE))

    page = getUnicode(page)  # Note: if upper function call fails (Issue #4202)
    open(os.getcwd()+"\\google.html" ,'w' ,encoding='utf-8').write(str(page)+'\n')
    if True:
        p=open(os.getcwd()+"\\google.html", encoding='utf-8').readlines()
        p1=open(os.getcwd()+"\\url list "+'google'+".txt", encoding='utf-8').readlines()
        for i in p:
            try:
                if '/url?q=' in i:
                    rcp='"><a href="/url'+'(.*?)'+'sa='
                    rc=re.findall(rcp , i )
                    for rc1 in rc:
                        rc1=rc1[3:-1]
                        if reg1(rc1) and rc1 not in str(p1):
                            ##print('her')
                        open(os.getcwd()+"\\url list "+'google'+".txt" ,'a' ,encoding='utf-8').write(rc1 +'\n')         
            except Exception as e:
                pass
    if True:
        warnMsg = "Google has detected 'unusual' traffic from "
        warnMsg += "used IP address disabling further searches"

        if conf.proxyList:
            raise SqlmapBaseException(warnMsg)
        else:
            logger.critical(warnMsg)
            
######################################################
##################<<bing>>############################
 def _search_bing(dork):
    print(dork)
    if not dork:
        return None
    page = None
    data = None
    requestHeaders = {}
    responseHeaders = {}
    requestHeaders[HTTP_HEADER.USER_AGENT] = dict(conf.httpHeaders).get(HTTP_HEADER.USER_AGENT, DUMMY_SEARCH_USER_AGENT)
    requestHeaders[HTTP_HEADER.ACCEPT_ENCODING] = HTTP_ACCEPT_ENCODING_HEADER_VALUE
    lpoi='/search?q='+dork+'&rdr=1&first=0&FORM=PQRE'
    ub=[]
    req = _urllib.request.Request(url, data=getBytes(data), headers=requestHeaders)
    conn = _urllib.request.urlopen(req)
    requestMsg = "HTTP request:\nGET %s" % url
    requestMsg += " %s" % _http_client.HTTPConnection._http_vsn_str
    logger.log(CUSTOM_LOGGING.TRAFFIC_OUT, requestMsg)
    page = conn.read()
    code = conn.code
                
    status = conn.msg
    responseHeaders = conn.info()
    page = decodePage(page, responseHeaders.get("Content-Encoding"), responseHeaders.get("Content-Type"))
    open(os.getcwd()+"\\"+"bing1.html" ,'w' ,encoding='utf-8').write(str(page)+'\n')
    rcp='" aria-label="Page'+'(.*?)'+'" href="'
    k=re.findall(rcp , str(page) )
    print(k)
    for i in k:
        rcp='" aria-label="Page'+i+'" href="'+'(.*?)'+'" h="'
        neurl=(re.findall(rcp , str(page) ))
        print(neurl)
        #             print(neurl[0])
        if neurl[0] not in ub and len(ub)<s and len(neurl[0])>10:
            ub.append(neurl[0])
def search(dork):
    pushValue(kb.choices.redirect)
    kb.choices.redirect = REDIRECTION.YES

    try:
        sert(dork)
    except SqlmapBaseException as ex:
        if conf.proxyList:
            logger.critical(getSafeExString(ex))

            warnMsg = "changing proxy"
            logger.warn(warnMsg)

            conf.proxy = None

            setHTTPHandlers()
            return sert(dork)
        else:
            raise
    finally:
        kb.choices.redirect = popValue()
def sert(dork):
    _search_bing(dork)
def setHTTPHandlers():  # Cross-referenced function
    raise NotImplementedError