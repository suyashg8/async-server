import psycopg2 as pg

class DB:
  
  def __init__(self, db_name):
    self.db_name = db_name
    self.conn = None
  
  
  def get_conn(self):
    
    if not self.conn :
      self.conn = pg.connect(user='postgres',password='suyash',database=self.db_name)
    
    return self.conn
    
