"""应用路由注册模块。

负责将所有蓝图注册到 Flask 应用实例。
"""

from wxcloudrun.controller.counter_controller import counter_bp


def register_blueprint_to_app(app):
    """注册所有蓝图到 Flask 应用。

    Args:
        app (Flask): Flask 应用实例。
    """
    # Counter controller.
    app.register_blueprint(counter_bp)
