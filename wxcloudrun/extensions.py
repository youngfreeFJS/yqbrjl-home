"""集中管理应用扩展。"""

import mysql.connector.pooling
from wxcloudrun.config import USERNAME, PASSWORD, DB_ADDRESS, DATABASE


class Database:
    """数据库连接池管理器。"""

    def __init__(self):
        self.pool = None

    def init_app(self, app):
        """初始化数据库连接池。"""
        db_host_port = DB_ADDRESS.split(":")
        db_config = {
            "host": db_host_port[0],
            "port": int(db_host_port[1]) if len(db_host_port) > 1 else 3306,
            "database": DATABASE,
            "user": USERNAME,
            "password": PASSWORD,
            "pool_name": "mypool",
            "pool_size": 5,
            "autocommit": True,
        }
        try:
            self.pool = mysql.connector.pooling.MySQLConnectionPool(**db_config)
            app.logger.info("数据库连接池初始化成功")
        except Exception as e:
            app.logger.error("数据库连接池初始化失败: %s", e)
            raise

    def get_connection(self):
        """从连接池获取连接。"""
        return self.pool.get_connection()


# 全局数据库实例
db = Database()
