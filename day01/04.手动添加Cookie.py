'''
Cookie 用来识别用户
'''

import requests

#没有登录时调用，返回跳转到登录页面
url="https://www.bagevent.com/account/dashboard"
r=requests.get(url)
print(r.text)

#发送请求时，带上cookie信息
head={
    "Cookie":'_ga=GA1.2.1116096681.1611732732; _gid=GA1.2.1482125451.1611732732; JSESSIONID=FF5F85F7AFC86BDA6C96DA6180AB0211; BAGSESSIONID=c1d4f44e-2d8c-4858-86f2-e9ef7ed9a51c; BAG_EVENT_TOKEN_=02de735f68204d51009e7edda78e58c13a3fcdd1; BAG_EVENT_CK_KEY_="2780487875@qq.com"; BAG_EVENT_CK_TOKEN_=2440f5d17af838308ba4b390db81af38; _gat=1'
}
r=requests.get(url,headers=head)
print(r.text)
assert "<title>百格活动 - 账户总览</title>" in r.text

'''
缺点：
1.cookie会失效，失效后需要重新获取
2.登录后的每个接口，需要带着cookie
'''


