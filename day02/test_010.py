import random
import requests
import pytest

#生成用户名
cs=[
    {"data":{"mobilephone":1811233456,"pwd":"123456"},
     "expect":{"status":0,"code":"20109","data":None,"msg":"手机号码格式不正确"}},
    {"data":{"mobilephone":181123345611,"pwd":"123456"},
     "expect":{"status":0,"code":"20109","data":None,"msg":"手机号码格式不正确"}},
    {"data":{"mobilephone":18012345678,"pwd":"1234"},
     "expect":{"status":0,"code":"20108","data":None,"msg":"密码长度必须为6~18"}}
]

@pytest.fixture(params=cs)
def register_data(request):#固定写法
    return request.param#固定写法

def register(data):
    url="http://jy001:8081/futureloan/mvc/api/member/register?"
    r=requests.post(url,data=data)
    return r

#数据驱动的测试模型
#test_register测试脚本/测试逻辑，测试数据与测试逻辑分离，相同逻辑的数据放到一起，实现一个脚本即可
#数据可以放到csv、xml、yaml......去维护
def test_register(register_data):
    print(f"测试结果:{register_data['data']}")
    print(f"预期结果：{register_data['expect']}")
    r=register(register_data['data'])
    print(f"实际结果：{r.text}")
    assert r.json()['status']==register_data['expect']['status']
    assert r.json()['code']==register_data['expect']['code']
    assert r.json()['msg'] == register_data['expect']['msg']








# #测试用例
# def test_login(get_login_data):
#     print(f"测试登录功能，登录的数据为：username:{},pwd:{}")
#
# #练习：fixture+requests，优化金融项目注册接口的脚本
#
# def test_register_001():
#     url=f"http://jy001:8081/futureloan/mvc/api/member/register?"
#     r=requests.get(url)
#     rjson=r.json()
#     assert rjson['status']==0
#     assert rjson['code']=="20109"
#     assert rjson['msg']=="手机号码格式不正确"
#     print("用例1验证完成")
#
# def test_register_002():
#     url=f"http://jy001:8081/futureloan/mvc/api/member/register?mobilephone={}&pwd={}"
#     r = requests.get(url)
#     rjson = r.json()
#     assert rjson['status'] == 0
#     assert rjson['code'] == "20109"
#     assert rjson['msg'] == "手机号码格式不正确"
#     print("用例2验证完成")
#
# def test_register_003():
#     url=f"http://jy001:8081/futureloan/mvc/api/member/register?mobilephone={}&pwd={}"
#     r = requests.get(url)
#     rjson = r.json()
#     assert rjson['status'] == 0
#     assert rjson['code'] == "20108"
#     assert rjson['msg'] == "密码长度必须为6~18"
#     print("用例3验证完成")
#     # print("密码不足5位")



