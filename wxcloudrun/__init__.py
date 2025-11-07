"""Flask 应用入口。"""

import os
from flask import Flask
from wxcloudrun.config import config
from wxcloudrun.extensions import db
from wxcloudrun.controller.counter_controller import counter_bp


def create_app():
    """创建并配置 Flask 应用。"""
    app_instance: Flask = Flask(__name__, instance_relative_config=True)
    app_instance.config['DEBUG'] = config.DEBUG
    app_instance.config.from_object('config')

    # 初始化数据库连接池
    db.init_app(app_instance)

    # 注册蓝图
    app_instance.register_blueprint(counter_bp)

    return app_instance


if __name__ == "__main__":
    app = create_app()
