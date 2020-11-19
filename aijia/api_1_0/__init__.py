"""
Name :.py
Author: Zhouzhegyang
Contect: 课堂案例
Time: 2020/6/12 9:47
DESC: 接口v1蓝图，引入各种模块！
 1个蓝图对象---》包含N个模块
"""
from flask import  Blueprint
api = Blueprint("api_1_0",__name__) # 创建蓝图和Flask创建app一样

# 导入蓝图中的各种模块/view逻辑方法
#from . import  users,shoppingcart,demo,verify_code
from . import  demo,users


