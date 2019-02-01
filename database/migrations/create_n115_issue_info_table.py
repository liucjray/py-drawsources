from database.migrations import *

deferred_db.init(os.getenv("STORAGE_PATH") + 'n115.db')

deferred_db.drop_tables([IssueInfo])

deferred_db.create_tables([IssueInfo])
