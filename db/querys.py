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
    
    def insertOrder(self, salesmen, date_order, cliente_clienteid):
        try:
            query = """
                        INSERT INTO `order`(salesmen, date_order, cliente_idcliente) VALUES(%s, %s, %s)
                    """
            values = (salesmen, date_order, cliente_clienteid)
            self.db.execute_query(query, values)
            self.db.close_connection()
            
        except:
            print('error')
    
    def selectOrder(self):
        query = """
                    SELECT idorder FROM `order` ORDER BY idorder LIMIT 1
                """
        idOrder= self.db.execute_query(query)
        self.db.close_connection()
        return idOrder[0]
    
    def insertDetailOrder(self, moto, modelo, description, original_generic, img, state, abono, order_idorder):
        try:
            query = """
                        INSERT INTO detail_order(moto, modelo, description, original_generic, img, state, abono, order_idorder) VALUES(%s, %s, %s, %s, %s, %s, %s,%s)
                    """
            values = (moto, modelo, description, original_generic, img, state, abono, order_idorder)
            self.db.execute_query(query, values)
            self.db.close_connection()
        except:
            print('error')
            