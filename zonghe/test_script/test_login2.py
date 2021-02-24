import pytest

from zonghe.baw import Member
from zonghe.caw import DataRead, MySqlOp, Check


@pytest.fixture(params=DataRead.read_yaml(r"test_data\login.yaml"))
def login_data(request):
    return request.param

def test_login(login_data,db_info,baserequest,url):
    #注册用户
    print("注册数据",login_data['regdata'])
    # 初始化环境：避免环境中已有本次测试用到的数据
    # MySqlOp.delete_user(db_info, login_data['data']['mobilephone'])
    r = Member.register(baserequest, url, login_data['regdata'])
    #登录
    print("登录数据",login_data['logindata'])
    r = Member.login(baserequest, url, login_data['logindata'])
    #检查结果
    # assert r.json()['code'] == login_data['expect']['code']
    # assert r.json()['status'] == login_data['expect']['status']
    # assert r.json()['msg'] == login_data['expect']['msg']
    Check.equal(r.json(), login_data['expect'], 'code,status,msg')
    #删除注册用户
    MySqlOp.delete_user(db_info, login_data['regdata']['mobilephone'])



