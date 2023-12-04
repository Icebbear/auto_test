# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test_57
# FileName:      test_pytest_func.py
# Author:       xxxxxxx
# Datetime:     2023/11/3 9:36
# Description:
# 
# ---------------------------------------------------------------------------
import base64
import random
import pytest
import requests
import allure

"""
    pytest装饰器：
        1：@pytest.fixture(scope="指定自定义固件的级别", autouse=False, params=可迭代类型)：实现自定义固件
        2：@pytest.mark.parametrize("字符串", 可迭代类型): 实现用例的参数化
        
        3: 下载插件，插件为：pytest-dependency, 下载方式为：pip install pytest-dependency
            插件：pytest-dependency的功能为实现用例之间的依赖。
            使用流程：
                先使用装饰器@pytest.mark.dependency()标记依赖的用例
                再使用装饰器@pytest.mark.dependency(depends=["用例的名称"])管理依赖的用例，也可以标记用例被后面的用例依赖
                
        4: @pytest.mark.标签名：功能给用例打上标签，在终端运行的时候，使用的命令为：pytest -vs 用例py文件 -m="标签名"
        
        5: @pytest.mark.run(order=num): num为整形，数字越小越先执行。但是需要下载插件，插件为：pip install pytest-ordering
        
        
        6：@pytest.mark.usefixtures("自定义固件名称")：实现自定义固件的调用
        
        7: @pytest.mark.skip(reason="无条件跳过"): 让用例无条件跳过
        
        8: @pytest.mark.skipif(bool, reason="有条件跳过")：如果bool表达式为True，用例有条件跳过
        
        9：@pytest.mark.xfail(reason="预期失败")
"""


dict1 = {}


@allure.epic("BPM_流程测试")
@allure.feature("认证接口和维度管理流程")
class Test01:

    def setup_class(self):
        login_url = "http://120.46.172.186:8080/auth"
        # 配置登录数据
        login_data = {"username": "admin", "password": base64.b64encode("123456".encode()).decode()}
        self.bpm_sess = requests.sessions.Session()
        self.token = self.bpm_sess.post(login_url, json=login_data).json().get("token")
        self.bpm_sess.headers.update({"Authorization": "Bearer "+self.token})

    @allure.story("登录")
    @pytest.mark.dependency()
    def test1(self):
        print("用例1")
        # 实现登录，获取服务器返回的token
        login_url = "http://120.46.172.186:8080/auth"
        # 配置登录数据
        login_data = {"username": "admin", "password": base64.b64encode("123456".encode()).decode()}
        res = self.bpm_sess.post(url=login_url, json=login_data)
        print(res.text)
        assert "超级管理员" == res.json().get("username")

    @allure.story("添加维度")
    @pytest.mark.dependency(depends=["Test01::test1"])
    def test2(self):
        print("添加维度用例")
        add_dem_url = "http://120.46.172.186:8080/api/demension/v1/dem/addDem"
        add_dem_data = {
                "code": "addDem"+str(random.randrange(100, 999)),
                "description": "addDem",
                "isDefault": 0,
                "name": "addDem"
            }

        res = self.bpm_sess.request(method="post", url=add_dem_url, json=add_dem_data)
        print(res.text)
        assert "添加维度成功" in res.text

    @pytest.mark.dependency(depends=["Test01::test1", "Test01::test2"])
    def test3(self):
        print("用例3")



'''
@pytest.mark.run(order=4)
@pytest.mark.p1
def test1():
    print("用例1")


@pytest.mark.dependency(depends=["test4"])
@pytest.mark.run(order=2)
@pytest.mark.p0
def test2():
    print("用例2")


@pytest.mark.run(order=3)
@pytest.mark.p0
def test3():
    print("用例3")


@pytest.mark.dependency()
@pytest.mark.run(order=1)
@pytest.mark.p1
def test4():
    print("用例4")
    assert 1 == 2
'''

'''
def test1():
    print("用例1")


@pytest.mark.skip(reason="无条件跳过")
def test2():
    print("用例2")


@pytest.mark.skipif(1 == 2, reason="无条件跳过")
def test3():
    print("用例2")


@pytest.mark.xfail(reason="预期失败")
def test4():
    print("预期失败")
    assert 1 == 3
'''


if __name__ == '__main__':
    pytest.main()