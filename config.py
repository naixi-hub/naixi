"""
Name :config.py
Author: Zhouzhegyang
Contect: 课堂案例
Time: 2020/6/12 9:25
DESC: 项目配置文件，提供开发模式和生产模式两种配置
"""
import redis
class Config():

    SECRET_KEY= "aferedreaxxxretrgaee9802212)"  #加密字符串！确保生产tocken令牌特别复杂！ CSRF安全机制开启后，在页面的cookie中设置一个随机CSRF_Tocken值！
    # 数据库配置
    SQLALCHEMY_DATABASE_URI ="mysql://root:123456@127.0.0.1:3306/info02"
    SQLALCHEMY_TRACK_MODIFICATIONS = True


    # session配置,sesion存储交给redis数据库实现 [IP和端口常量]
    REDIS_HOST= "127.0.0.1"
    REDIS_PORT = 6379

    SESSION_TYPE="redis"  # 指定项目中session使用redis库存储
    SESION_REDIS= redis.StrictRedis(host=REDIS_HOST,port=REDIS_PORT) # 创建redis对象
    SESSION_USE_SIGNER= True # 对缓存中session_id标记进行隐藏
    PERMANENT_SESSION_LIFETIME = 86400 # sesion数据的有效期，单位是s. 3600*24 =86400一天


class DevelopmentConfig(Config):
    '''开发模式配置信息,该数据库'''
    DEBUG = True


class ProductionmentConfig(Config):
    '''生产模式的配置'''
    pass

# 工厂模块式: 作用生产不同类的! 传递不同参数,可以调用不同类!
config_map={
    "develop":DevelopmentConfig, #开发时的配置,使用的是DevelopmentConfig类
    "product":ProductionmentConfig
}






