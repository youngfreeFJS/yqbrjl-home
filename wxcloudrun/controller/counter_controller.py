"""Counter controller - Counter 控制器。"""

from flask import Blueprint, jsonify
from wxcloudrun.service.counter_service import CounterService

# 创建蓝图
counter_bp = Blueprint("counter", __name__, url_prefix="/counter")


@counter_bp.route("/count", methods=["GET"])
def get_count():
    """获取当前计数值的接口。"""
    try:
        count = CounterService.get_current_count()
        return jsonify({"count": count}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@counter_bp.route("/count/increment", methods=["POST"])
def increment_count():
    """增加计数值的接口。"""
    try:
        new_count = CounterService.increment_counter()
        return jsonify({"count": new_count}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
