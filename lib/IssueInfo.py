from peewee import *
from lib import *

db = SqliteDatabase("C:\\B2B\\drawsources\\storages\\ds.db")


class BaseModel(Model):
    class Meta:
        database = db


class IssueInfo(BaseModel):
    # 號源
    resource = CharField()
    # 類型
    type = CharField()
    # 區域
    area = CharField()
    # 獎期
    issue = CharField()
    # 號碼
    code = CharField()
    # 附加資訊
    info = TextField(null=True)
    # 建立時間
    created_at = DateTimeField()

    class Meta:
        # 唯一索引
        indexes = (
            (('resource', 'type', 'area', 'issue'), True),
        )
