'''Kết nối CSDL'''
from pymysql import connect, cursors, Error
import game as ga
from datetime import datetime
from datetime import date
config = {
  'host': 'localhost',
  'user': 'root',
  'password': '',
  'database': 'game_card',
  }
cnx = connect(**config)
def get_lanchoigannhat():
    sql="SELECT MAX(route) as lancho FROM `logs` "
    cur = cnx.cursor()
    cur.execute(sql)
    for i in cur:
        print(i[0])
        result= i[0]
    return result
get_lanchoigannhat()





