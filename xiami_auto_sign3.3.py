# -*- coding: utf-8 -*-  
''''' 
Created on 2013-10-03 
 
@author: 
'''  
import urllib,sys,http.cookiejar
  
class LoginXiami:  
    login_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4'}  
    signin_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 Safari/537.31', 'X-Requested-With':'XMLHttpRequest', 'Content-Length':'0', 'Origin':'http://www.xiami.com', 'Referer':'http://www.xiami.com/'}  
    email = ''  
    password = ''  
    cookie = None  
    cookieFile = './cookie.dat'  
  
    def __init__(self, email, pwd):  
        self.email = email  
        self.password = pwd
        self.cookie = http.cookiejar.LWPCookieJar()  
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cookie))  
        urllib.request.install_opener(opener)  
          
    def login(self):  
        postdata = {'email':self.email, 'password':self.password, 'done':'http://www.xiami.com', 'submit':'%E7%99%BB+%E5%BD%95'}  
        postdata = urllib.parse.urlencode(postdata)
        print(postdata)
        print('Logining...')
        req = urllib.request.Request(url='http://www.xiami.com/member/login', data=postdata.encode('utf-8'), headers=self.login_header)  
        result = urllib.request.urlopen(req).read()
        self.cookie.save(self.cookieFile)  
        result = str(result) 
        if 'Email 或者密码错误' in result:  
            print('Login failed due to Email or Password error...') 
            sys.exit()  
        else :  
            print('Login successfully!')
    

   
    def signIn(self):  
        postdata = {}  
        postdata = urllib.parse.urlencode(postdata)
        print('signing...')
        req = urllib.request.Request(url='http://www.xiami.com/task/signin', data=postdata.encode('utf-8'), headers=self.signin_header)  
        content_stream = urllib.request.urlopen(req)
        result = content_stream.read()
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
    user = LoginXiami('test002@163.com', 'password')  
    user.login()  
    user.signIn()  
