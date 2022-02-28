#Types of Database
#RDS - mysql, SQLite, PostgreSQL, ms sqlserver, Oracle, DB2
#DocumentDB - mangoDB

#How to connect mysql from python?

#from sqlite3 import connect


#mysql connector python - pip install -U mysql-connector-python 
#or
#pymysql - pip install -U pymysql

import mysql.connector
from mysql.connector import Error

createTable_sql_query="""CREATE TABLE laptop (id int, Name char(10), price float, primary key(id))"""

show_table_sql_query="""SHOW TABLES"""

def getDBConnection():
    try:
        dbConnection_List=[]
        if len(dbConnection_List) > 0:
            return dbConnection_List[0]
        conn = mysql.connector.connect(host="localhost", database="testDB", user="root", password="admin")
        dbConnection_List.append(conn)
        return conn
    except Error as e:
        print("Error during databaser execution", e)
    except Exception as ex:
        print("Exception in db Execution", ex)
    
try:
    dbConn = getDBConnection()
    mysqlcursor = dbConn.cursor()
    #mysqlcursor.execute("CREATE DATABASE testDB")
    mysqlcursor.execute("SHOW DATABASES")
    for dbName in mysqlcursor:
        print("Database Name =", dbName)

    mysqlcursor.execute("USE testDB")

    mysqlcursor.execute(createTable_sql_query)
    mysqlcursor.execute(show_table_sql_query)

    for tableName in mysqlcursor:
        print("Table Name =", dbName)
except Error as e:
    print("Error during databaser execution", e)
except Exception as ex:
    print("Exception in db Execution", ex)
finally:
    if dbConn.is_connected():
        mysqlcursor.close()
        dbConn.close()    
