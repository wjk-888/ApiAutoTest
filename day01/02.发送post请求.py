import requests

#表单格式的数据：content-type：www-x-urlencoded，使用data传参
#登录接口
# url="http://jy001:8081/futureloan/mvc/api/member/login"
# cs={"mobilephone":"18112345678","pwd":"123456"}
# r=requests.post(url,data=cs)
# print(r.text)
# assert r.json()['msg']=="登录成功"

# url="http://jy001:8081/futureloan/mvc/api/member/register"
# cs={
# "mobilephone":"18012345678",
#     "pwd":"123456",
#     "regname":"requests_test"
# }
# r=requests.post(url,data=cs)
# print(r.text)
# rjson=r.json()
# assert rjson['status']==0
# assert rjson['code']=='20110'
# assert rjson['msg']=="手机号码已被注册"

#json格式的数据：content-type：application/json，使用json传参
#具体使用data还是json传参，崖看接口是怎么定义的
#httpbin.org 是一个测试网站，不管发送什么类型发数据，这个接口将发送的请求，封装成json格式的返回
# url="http://www.httpbin.org/post"
# cs={"monilepjone":18012345678,"pwd":"123456"}
# r=requests.post(url,data=cs)
# print("data传参===",r.text)
# r=requests.post(url,json=cs)
# print("json传参===",r.text)

#租车系统，添加车辆
url="http://192.168.150.70:8089/carRental/car/addCar.action"
#接口文档中对接口描述不清晰
#通过界面操作接口对应的功能，抓包（Fiddler、浏览器的F12）看
cs={
    "carnumber":112,
    "cartype":112,
    "color":112,
    "carimg":"image/defaultcarimage.jpg",
    "description":"2020新车",
    "price":200000,
    "rentprice":1000,
    "deposit":500,
    "isrenting":1
}
#使用接口添加的车辆，中文字符乱码，但是用界面添加的车辆，不会有乱码
#分别抓脚本的包与界面的包，对比差异。界面设置了charset=UTF-8，但是脚本未设置导致
head={
    "Content=Type":"application/x-www-form-urlencoded;charset=UTF-8",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
}
#Fiddler抓脚本的包，设置代理
proxy={
    "http":"http://127.0.0.1:8888",#http协议，使用这个代理
    "https":"http://127.0.0.1:8888"#https协议，使用这个代理
}
r=requests.post(url,data=cs,headers=head,proxies=proxy)
print(r.text)
