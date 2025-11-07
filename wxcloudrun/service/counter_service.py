"""业务逻辑层 - Counter 服务。"""

from wxcloudrun.dao.counter_dao import CounterDAO


class CounterService:
    """Counter 业务逻辑服务。"""

    @staticmethod
    def get_current_count():
        """获取当前计数值。"""
        return CounterDAO.get_count()

    @staticmethod
    def increment_counter():
        """增加计数值并返回新值。"""
        return CounterDAO.increment_count()
