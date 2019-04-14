from pathlib import Path
from database.migrations import *

db_path = os.path.join(os.getenv("STORAGE_PATH"), 'ds.db')

if Path(db_path).is_file():
    IssueInfo.drop_table()
    IssueInfo.create_table()
else:
    print('file ds.db not exist.')
