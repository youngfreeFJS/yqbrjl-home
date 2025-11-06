"""计数器控制器模块。

定义 /api/v1/counter/ 路由下的业务处理逻辑。
"""
import logging
from flask import Blueprint, request
from wxcloudrun.response import make_succ_response, make_err_response
from wxcloudrun.dao.counter_dao import CounterDao, CountersModel

logger = logging.getLogger('log')

# 创建蓝图，URL 前缀为 /api/v1/counter
counter_bp = Blueprint('counter', __name__, url_prefix='/api/v1/counter')


class CounterController:
    """计数器业务控制器。"""

    @staticmethod
    @counter_bp.route('/get', methods=['GET'])
    def get_count():
        """获取当前计数值。

        Returns:
            Response: 包含 count 字段的成功响应。
        """
        counter_instance: CountersModel = CounterDao.query_counter_by_id(1)
        return make_succ_response({'count': counter_instance.count,
                                   'counter': counter_instance.to_dict()})

    @staticmethod
    @counter_bp.route('/update', methods=['POST'])
    def update_count():
        """更新计数值。

        请求体应包含: {"count": int, "type": str add|sub|mul|div}

        Returns:
            Response: 更新结果。
        """
        try:
            data = request.get_json()
            count = data.get('count')
            update_type = data.get('type')
            logger.info("update_count count=%s, type=%s", count, update_type)
            counter_instance: CountersModel = CounterDao.update_counter_by_id(1, count, update_type)

            return make_succ_response({'updated_count': counter_instance.count,
                                       'counter': counter_instance.to_dict()})
        except Exception as e:
            return make_err_response(f"更新失败: {str(e)}")
