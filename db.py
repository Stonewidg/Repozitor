from sqlite3 import connect

class DB:
    def __init__(self, db_name) -> None:
        self.connection = connect(database=db_name)
        self.cur = self.connection.cursor()

    def add_data(self, name, email, phone):
        self.cur.execute('INSERT INTO form_data(?, ?, ?)', (name, email, phone))

db_con= DB('app_db.db')