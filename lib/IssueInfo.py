from peewee import *

deferred_db = SqliteDatabase(None, autocommit=False)


class IssueInfo(Model):
    # 號源
    resource = CharField()
    # 獎期
    issue = CharField()
    # 號碼
    code = CharField()
    # 建立時間
    created_at = DateTimeField()

    class Meta:
        database = deferred_db
