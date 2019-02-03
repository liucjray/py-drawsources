from database.migrations import *

# for db in ['k3.db', 'ssc.db', 'n115.db', 'pk10.db', 'klsf.db']:
#     deferred_db.init(os.getenv("STORAGE_PATH") + db)
#     deferred_db.drop_tables([IssueInfo])
#     deferred_db.create_tables([IssueInfo])

for db in ['ds.db']:
    deferred_db.drop_tables([IssueInfo])
    deferred_db.create_tables([IssueInfo])
