import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling


insert_sql_query = """INSERT INTO laptop (id, name, price) VALUES (4, 'Hp TrueVision HD', 75000) """

def getDBConnection():
    try:
        dbConnection_List=[]
        if len(dbConnection_List) > 0:
            return dbConnection_List[0]
        
        coonection_pool = pooling.MySQLConnectionPool(pool_name="testPool", pool_size=5,
                                    host="localhost", database="testDB", autocommit=True, user="root", password="admin")
        
        
        #conn = mysql.connector.connect(host="localhost", database="testDB", autocommit=True, user="root", password="admin")
        #dbConnection_List.append(conn)
        return coonection_pool
    except Error as e:
        print("Error during databaser execution", e)
    except Exception as ex:
        print("Exception in db Execution", ex)
    
try:
    dbConn = getDBConnection().get_connection()
    mysqlcursor = dbConn.cursor()
    
    dbConn.start_transaction()
    mysqlcursor.execute(insert_sql_query)
    #dbConn.commit()
    dbConn.rollback()
    
    mysqlcursor.execute("SELECT * FROM laptop")
    dbRecords = mysqlcursor.fetchall()
    
    for row in dbRecords:
        print(row)
    
except Error as e:
    print("Error during databaser execution", e)
except Exception as ex:
    print("Exception in db Execution", ex)
finally:
    if dbConn.is_connected():
        mysqlcursor.close()
        dbConn.close()    
