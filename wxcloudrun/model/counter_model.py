"""计数器数据模型模块。

定义 Counters 表结构，支持创建时间和更新时间自动维护。
"""

from datetime import datetime
from sqlalchemy import Column, Integer, TIMESTAMP
from wxcloudrun import db


class CountersModel(db.Model):
    """计数器表模型，用于存储计数值及其时间戳。"""

    __tablename__ = 'Counters'

    id = Column(Integer, primary_key=True)
    count = Column(Integer, default=1)
    created_at = Column(
        'createdAt',
        TIMESTAMP,
        nullable=False,
        default=datetime.utcnow
    )
    updated_at = Column(
        'updatedAt',
        TIMESTAMP,
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    # 创建一个 to_dict 方法
    def to_dict(self):
        """将模型转换为字典。"""
        return {
            'id': self.id,
            'count': self.count,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
