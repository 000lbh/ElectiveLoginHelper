import getpass
import json
from urllib import request,parse

header=('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36')
username=input('用户名（学号）：')
password=getpass.getpass(prompt='密码（不显示）：')
loginData=parse.urlencode([
    ('appid','syllabus'),
    ('userName',username),
    ('password',password),
    ('randCode',''),
    ('smsCode',''),
    ('otpCode',''),
    ('redirUrl','http://elective.pku.edu.cn:80/elective2008/ssoLogin.do')])
print('IAAA登录中')
req=request.Request('https://iaaa.pku.edu.cn/iaaa/oauthlogin.do')#IAAA登录
req.add_header(*header)
with request.urlopen(req,data=loginData.encode('utf-8')) as iaaa:
    pagedata=iaaa.read()
logonData=json.loads(pagedata.decode('utf-8'))
try:
    token=logonData['token']
    print('请用以下链接登录IAAA')
    print('http://elective.pku.edu.cn:80/elective2008/ssoLogin.do'+'?token='+token)
except Exception:
    print('Error!')
input()