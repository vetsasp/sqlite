import sys


class SQL:
    def __init__(self, path: str):
        self.path = path 

    def run(self, cmd: str):
        # print("running", cmd)    # DEBUG 
        with open(self.path, "rb") as db:
            try:    # skip header and fail if invalid file type 
                self.skip_header(db) 
            except Exception as e:
                print(f"Error: {e}")
                exit(65)

            self.runCmd(cmd, db)

    def runCmd(self, cmd: str, db):
        commands = {
            ".dbinfo": self.dbinfo
        }
        if cmd in commands:
            commands[cmd](db)
        else:
            print(f"Invalid command: {cmd}")

    def dbinfo(self, db):
        self.pageSize(db)
        self.tableCount(db)

    def pageSize(self, db):
        sz = int.from_bytes(db.read(2), byteorder="big")
        print(f"database page size: {sz}")

    def tableCount(self, db):
        table_count = sum(line.count(b"CREATE TABLE") for line in db)
        print(f"number of tables: {table_count}")

    def skip_header(self, db):
        # db.seek(16)
        head = db.read(16)
        if head != b'SQLite format 3\x00':
            raise ValueError("Not a valid SQLite 3 database file.")