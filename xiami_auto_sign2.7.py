# -*- coding: cp936 -*-  
''''' 
Created on 2012-11-15 
 
@author:  
'''  
import urllib, urllib2, cookielib, sys,base64
  
class LoginXiami:  
    login_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4'}  
    signin_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 Safari/537.31', 'X-Requested-With':'XMLHttpRequest', 'Content-Length':'0', 'Origin':'http://www.xiami.com', 'Referer':'http://www.xiami.com/'}  
    email = ''  
    password = ''  
    cookie = None  
    cookieFile = './cookie.dat'  
  
    def __init__(self, email, pwd):  
        self.email = email  
        self.password = base64.decodestring(pwd)
        self.cookie = cookielib.LWPCookieJar()  
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))  
        urllib2.install_opener(opener)  
          
    def login(self):  
        postdata = {'email':self.email, 'password':self.password, 'done':'http://www.xiami.com', 'submit':'%E7%99%BB+%E5%BD%95'}  
        postdata = urllib.urlencode(postdata)
        print(postdata)
        print('Logining...')  
        req = urllib2.Request(url='http://www.xiami.com/member/login', data=postdata, headers=self.login_header)  
        result = urllib2.urlopen(req).read()  
        self.cookie.save(self.cookieFile)  
        result = str(result)
        #.decode('utf-8').encode('gbk')  
        if 'Email �����������' in result:  
            print('Login failed due to Email or Password error...') 
            sys.exit()  
        else :  
            print('Login successfully!')  
        
    def signIn(self):  
        postdata = {}  
        postdata = urllib.urlencode(postdata)
        print('signing...')
        req = urllib2.Request(url='http://www.xiami.com/task/signin', data=postdata, headers=self.signin_header)  
        #my_req = str(req, encoding="utf-8")
        #print type(req)
        content_stream = urllib2.urlopen(req)
        
        result = content_stream.read()
        
        #result = str(result).decode('utf-8').encode('gbk')  
        self.cookie.save(self.cookieFile)  
        try:  
            result = int(result)  
        except ValueError:  
            print('signing failed...')
            sys.exit()  
        except:  
            print('signing failed due to unknown reasons ...')
            sys.exit()  
        print('signing successfully!') 
        print(self.email,'have signed', result, 'days continuously...')
       
              
  
if __name__ == '__main__':  
    user = LoginXiami('test001@163.com', 'MbixMDB2MCY=')  
    user.login()  
    user.signIn()  