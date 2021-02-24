'''
pytest命名约束
1.文件用test_开头
2.类用Test开头
3.函数或方法用test_开头
'''
import requests
def test_register_001():
    url="http://jy001:8081/futureloan/mvc/api/member/register?mobilephone=1801234567&pwd=123456"
    r=requests.get(url)
    rjson=r.json()
    assert rjson['status']==0
    assert rjson['code']=="20109"
    assert rjson['msg']=="手机号码格式不正确"
    print("用例1验证完成")

def test_register_002():
    url = "http://jy001:8081/futureloan/mvc/api/member/register?mobilephone=1&pwd=123456"
    r = requests.get(url)
    rjson = r.json()
    assert rjson['status'] == 0
    assert rjson['code'] == "20109"
    assert rjson['msg'] == "手机号码格式不正确"
    print("用例2验证完成")

def test_register_003():
    url = "http://jy001:8081/futureloan/mvc/api/member/register?mobilephone=1801234567&pwd=1234"
    r = requests.get(url)
    rjson = r.json()
    assert rjson['status'] == 0
    assert rjson['code'] == "20108"
    assert rjson['msg'] == "密码长度必须为6~18"
    print("用例3验证完成")
    # print("密码不足5位")


