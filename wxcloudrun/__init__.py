"""主应用入口模块。

初始化 Flask 应用、数据库连接，并注册所有蓝图路由。
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
from wxcloudrun.router import register_blueprint_to_app
import config


# 因MySQLDB不支持Python3，使用pymysql扩展库代替MySQLDB库
pymysql.install_as_MySQLdb()

# 初始化web应用
app = Flask(__name__, instance_relative_config=True)
app.config['DEBUG'] = config.DEBUG

# 设定数据库链接
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{config.username}:{config.password}@{config.db_address}/flask_demo'

# 初始化DB操作对象
db = SQLAlchemy(app)

# 加载配置
app.config.from_object('config')

# 注册蓝图
register_blueprint_to_app(app)
