from .db_c import CMysql

class Querys:
    def __init__(self) -> None:
        self.db = CMysql()
        self.db.connection()
        
    def insertCliente(self, name, phone):
        query = """
                    INSERT INTO cliente(name, phone) VALUES(%s, %s)
                """
        values = (name, phone)
        self.db.execute_query(query, values)
        self.db.close_connection()
        
    def selectCliente(self):
        query = """
                    SELECT idcliente FROM cliente ORDER BY idcliente LIMIT 1
                """
        idCliente = self.db.execute_query(query)
        self.db.close_connection()
        return idCliente[0]
    
    def insertOrder(self, salesmen, date_order, state, abono, cliente_clienteid):
        query = """
                    INSERT INTO order(salesmen, date_order, state, abono, cliente_clienteid) VALUES(%s, %s, %s, %s, %s)
                """
        values = (salesmen, date_order, state, abono, cliente_clienteid)
        self.db.execute_query(query, values)
        self.db.close_connection()