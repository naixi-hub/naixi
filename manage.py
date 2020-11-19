"""
Name :manage.py
Author: Zhouzhegyang
Contect: 课堂案例
Time: 2020/6/12 9:25
DESC: 项目启动文件,创建应用，数据库迁移！
"""
from aijia import  models
from aijia import  create_app,db
from flask_script import  Manager  # Flas扩展命令包！ 扩展app.run(参数...)
from flask_migrate import  Migrate,MigrateCommand # 数据库迁移模块中迁移对象和迁移命令对象
#1.  创建应用
#app = Flask(__name__) # 默认创建，数据库配置，日志配置，csrf等功能不能加入！
app = create_app("develop")
manage = Manager(app) # 扩展app.run()命令
Migrate(app,db)
manage.add_command("db",MigrateCommand) # 给app扩展 数据库迁移相关指令！

if __name__ == '__main__':
    #app.run(debug=True) #默认的启动应用  【不能传数据库迁移指定】
    manage.run()
