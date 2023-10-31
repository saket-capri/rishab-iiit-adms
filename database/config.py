import mysql.connector
db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="db2325Rish@bh"
)
# print(db_connection)

import pymysql
pymysql.install_as_MySQLdb()