"""
Name :demo.py
Author: Zhouzhegyang
Contect: 课堂案例
Time: 2020/6/12 10:32
DESC:测试案例，写日志
"""
from flask import  current_app,jsonify  # 全局对象表示当前应用
from  . import  api

@api.route('/index')
def index():
    current_app.logger.error('测试：Error信息...,都会被写到log文件中')
    current_app.logger.warn('测试:worn信息...')
    current_app.logger.debug('测试:debug信息...')
    current_app.logger.info('测试:info信息普通信息,...')

    # ORM操作数据库！
    restult = {'errno':"OK",'errormsg':'写入日志成功'}
    return jsonify(restult)
