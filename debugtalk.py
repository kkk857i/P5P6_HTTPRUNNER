
import os

# os.environ['http_proxy']='hppt://127.0.0.1:8888' #密码写后面
# os.environ['http_proxy']='hppt://127.0.0.1:8888'

def get_value():
    return "newderam_p5p6"

def setup_test_step():
    print("测试步骤开始")
def teardown_test_step():
    print("测试步骤结束")
def setup_test_case(content):
    print("测试用例[%s]执行开始"%content )
def teardown_test_case(content):
    print("测试用例[%s]执行结束"%content )

def get_conditions():
    return 1   #非0 非空，逻辑表达式成立等都为真

# def setup_test_case(content):
#     print("测试用例[%s]执行开始"%content)
# def teardow_test_case(content):
#     print("测试用例[%s]执行结束"%content)

#参数化
def get_params():
    return ['newdream','火车票','汽车票']
def git_params():
    pass

if __name__=='__main__':
    print(get_value())
