from .db_c import CMysql

class Querys:
    def __init__(self) -> None:
        self.db = CMysql()
        self.db.connection()