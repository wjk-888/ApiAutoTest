class TestRegister:
    def test_001(self):
        print("注册用例1")
    def test_002(self,db):#类里面，首次调用db的地方执行前置
        print("注册用例2")
    def test_003(self):
        print("注册用例3")#类里所有用例执行完，执行后置