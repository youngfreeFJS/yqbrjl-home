"""数据访问对象层 - Counter DAO。"""

from flask import current_app
from wxcloudrun.extensions import db


class CounterDAO:
    """Counter 数据访问对象。"""

    @staticmethod
    def get_count():
        """获取当前计数值。"""
        connection = None
        cursor = None
        try:
            connection = db.get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT value FROM counter WHERE id = 1")
            result = cursor.fetchone()
            return result[0] if result else 0
        except Exception as e:
            current_app.logger.error("查询计数失败: %s", e)
            raise
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    @staticmethod
    def increment_count():
        """增加计数值并返回新值。"""
        connection = None
        cursor = None
        try:
            connection = db.get_connection()
            cursor = connection.cursor()
            # 初始化计数器（如果不存在）
            cursor.execute(
                "INSERT INTO counter (id, value) VALUES (1, 0) "
                "ON DUPLICATE KEY UPDATE value = value"
            )
            # 增加计数
            cursor.execute(
                "UPDATE counter SET value = value + 1 WHERE id = 1"
            )
            cursor.execute("SELECT value FROM counter WHERE id = 1")
            result = cursor.fetchone()
            return result[0] if result else 1
        except Exception as e:
            current_app.logger.error("增加计数失败: %s", e)
            raise
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
