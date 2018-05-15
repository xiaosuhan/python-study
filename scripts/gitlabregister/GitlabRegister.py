# -*- coding: utf-8 -*-
__Author__ = "suhan"
__Date__ = '2018/05/14/20:46'

"""
用户注册gitlab和发送邮件给用户
"""

import requests
import random
import string

url = 'http://gitlab.wuxingdev.cn'
token = 'zsm44PTux_r65p5rbTBG'

#登录
#gl = gitlab.Gitlab(url,private_token='token')
CreateUserUrl = "%s/api/v3/users" %url

#输入需要创建的用户信息，密码是随机生成的
name = input("请输入中文用户名:")
email = input("请输入邮箱地址:")
username = email.strip().split("@guanaitong.com")[0]
password = "".join(random.sample(['A','b','5','D','e','7','g','h','2','j','q'], 8))

print("name:%s\nemail:%s\nusername:%s\npassword:%s\n" %(name,email,username,password))

UserData = {'email':email,'username':username,'name':name,'password':password,'private_token':token}
response = requests.post(CreateUserUrl, data = UserData)

print("response.status_code%s\n:" %response.status_code)

if response.status_code == 201:
    print("创建成功")
    email2 = "han.su@guanaitong.com"
    data2 = {'tos':email2,'subject':"Gitlab密码",'content':password}
    EmailUrl = "https://notice.ops.gat/sender/mail/"
    SendEmailResponse = requests.post(EmailUrl,data = data2)
else:
    print("创建失败，请确认邮箱和用户名是否已存在")




#xurl = "%s/api/v3/projects?private_token=%s" %(url,token)
# x = requests.get(xurl)
# print(x)
# #两种都可以
# content = x.json()
# content2 = x.text
# print(content)
