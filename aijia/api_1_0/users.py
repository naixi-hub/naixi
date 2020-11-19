"""
Name :demo.py
Author: Zhouzhegyang
Contect: 课堂案例
Time: 2020/6/12 10:32
DESC:测试案例，写日志
"""
from flask import  current_app  ,jsonify,request,session# 全局对象表示当前应用
from  . import  api
from aijia.utils.response_code import RET # 状态码工具类
from aijia import redis_store,db,constants #导入redis对象,数据库对象,常量
import  re
from aijia.models import  User
# 非查询返回结果return jsonify(errno=RET.OK, errmsg="OK")
# 查询返回结果return jsonify(errno=RET.OK, errmsg="OK", data={"house_id": house.id})
# 地址: api/v1.0/login
@api.route('/login',methods=['POST'])
def login():
    # 1. 获取表单数据
    mobile = request.form.get('mobile')
    password = request.form.get('password')
    print(mobile,password)
    # 2. 验证参数是否完整
    if not all([mobile,password]):
        return jsonify(errno=RET.PARAMERR, errmsg='用户名密码不完整')
    #4. 格式验证
    if not  re.match(r'1[3456789]\d{9}',mobile):
        return jsonify(errno=RET.PARAMERR, errmsg='手机号格式错误')

    # 登陆
    try:
        user = User.query.filter_by(mobile=mobile,password_hash=password).first()
        #print(f'真实名字:{user.real_name}')
    except Exception as e:
        current_app.logger.error(e) #日志
    # 登陆失败,错误次数+1
    user_ip =request.remote_addr

    # 判断登陆次数
    try:
        access_num = redis_store.get('access_num_%s'%user_ip)
    except Exception as  e:
        current_app.logger.error(e)  # 日志
    if access_num is not None and int(access_num) > constants.LOGIN_ERROR_MAX_TIMES:
        return jsonify(errno=RET.DATAERR, errmsg='登陆次数多,10分钟后重试')


    #print(f'访问者IP:{user_ip}')
    if user is None:
        # 访问次数+1   access_num_127.0.0.1
        access_num = redis_store.incr('access_num_%s'%user_ip)
        redis_store.expire('access_num_%s'%user_ip,constants.LOGIN_ERROR_MAX_TIMES) # 有效期10分钟
        return jsonify(errno=RET.DATAERR, errmsg='手机号或密码错误')
    session['name'] = user.name
    session['mobile'] = user.mobile
    session['id'] = user.id
    return jsonify(errno=RET.OK, errmsg='登陆成功')


@api.route('/register',methods=['POST'])
def register():
    # 获取参数
    mobile = request.form.get('mobile')
    password = request.form.get('password')
    # 判断完整性
    if not all([mobile, password]):
        return jsonify(errno=RET.PARAMERR, errmsg='用户名密码不完整')
    # 写入数据库

    return jsonify(errno=RET.OK, errmsg='注册成功')

