import sys
from app.sql import SQL

# from dataclasses import dataclass

# import sqlparse - available if you need it!

database_file_path = sys.argv[1]
command = sys.argv[2]

sql = SQL(database_file_path)

sql.run(command)