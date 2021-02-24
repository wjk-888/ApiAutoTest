import requests

#接口路径
url="http://www.httpbin.org/post"
#本地存在的文件
file="d:/test.png"
#rb二进制只读的方式打开
with open(file,mode='rb') as f:
    # {'name':file-tuple}
    # ('filename',fileobj,'content_type')
    cs={"filename":(file,f,"image/png")}
    r=requests.post(url,files=cs)
    print(r.text)

#http://127.0.0.1:8089/carRental/file/uploadFile.action
#上传图片
#添加车，使用刚上传的图片
#租车系统上传图片
url="http://192.168.150.70:8089/carRental/file/uploadFile.action"
file="d:/test.png"
with open(file,mode='rb') as f:
    cs={"mf":(file,f ,"image/png")}
    r = requests.post(url, files=cs)
    print(r.text)
    uploadPath=r.json()['data']['src']


url="http://192.168.150.70:8089/carRental/car/addCar.action"
cs={
"carnumber":1128,
    "cartype":112,
    "color":112,
    "carimg":uploadPath,
    "description":"2020新车",
    "price":200000,
    "rentprice":1000,
    "deposit":500,
    "isrenting":1
}
head={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
r=requests.post(url,data=cs,headers=head)
print(r.text)




