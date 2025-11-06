"""计数器数据访问对象模块。

提供对 CountersModel 的数据库查询与更新操作封装。
"""

import logging
from typing import Optional
from sqlalchemy.exc import OperationalError
from wxcloudrun import db
from wxcloudrun.model.counter_model import CountersModel

logger = logging.getLogger('log')


class CounterDao:
    """计数器数据访问对象（DAO），封装数据库操作逻辑。"""

    @staticmethod
    def query_counter_by_id(counter_id: int) -> Optional[CountersModel]:
        """根据 ID 查询计数器实体。

        Args:
            counter_id (int): 计数器的唯一标识。

        Returns:
            CountersModel | None: 查询到的实体，未找到则返回 None。
        """
        try:
            return CountersModel.query.filter(CountersModel.id == counter_id).first()
        except OperationalError as e:
            logger.error("query_counter_by_id failed: %s", e)
            return None

    @staticmethod
    def update_counter_by_id(counter_id: int, count: int, update_type: str) -> Optional[CountersModel]:
        """根据 ID 更新计数器实体。

        支持加、减、乘、除四种操作类型。

        Args:
            counter_id (int): 计数器的唯一标识。
            count (int): 操作数值。
            update_type (str): 更新类型，必须为 'add'、'sub'、'mul' 或 'div'。

        Returns:
            bool: 更新成功返回 True，否则返回 False。
        """
        counter = CountersModel.query.get(counter_id)

        valid_types = {'add', 'sub', 'mul', 'div'}
        if update_type not in valid_types:
            logger.error("Invalid update_type: %s", update_type)
            return counter

        if update_type == 'div' and count == 0:
            logger.error("Division by zero in update_counter_by_id")
            return counter

        try:

            if counter is None:
                logger.warning("Counter with id=%s not found for update", counter_id)
                return counter

            if update_type == 'add':
                counter.count += count
            elif update_type == 'sub':
                counter.count -= count
            elif update_type == 'mul':
                counter.count *= count
            elif update_type == 'div':
                counter.count = 0 if count == 0 else int(counter.count / count)

            db.session.commit()
            return counter
        except OperationalError as e:
            logger.error("update_counter_by_id failed: %s", e)
            db.session.rollback()
            return counter
