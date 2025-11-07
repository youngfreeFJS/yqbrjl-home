"""应用配置模块。"""
import os

# 是否开启debug模式
DEBUG = True

# 读取数据库环境变量
USERNAME = os.environ.get("MYSQL_USERNAME", 'root')
PASSWORD = os.environ.get("MYSQL_PASSWORD", 'root')
DB_ADDRESS = os.environ.get("MYSQL_ADDRESS", '127.0.0.1:3306')
DATABASE = "flask_demo"

CHARSET = "utf8mb4"
