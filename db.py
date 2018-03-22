import psycopg2 as pg
import asyncio
import asyncpg

class DB:
  
  def __init__(self, db_name):
    self.db_name = db_name
    self.conn = None
  
  
  async def get_conn(self):
    
    if not self.conn :
      self.conn = await asyncpg.connect(user='postgres',password='suyash',database=self.db_name)
    return self.conn

    
