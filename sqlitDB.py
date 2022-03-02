import sqlite3

dbConn = sqlite3.Connection("firstDB.db")
c = dbConn.cursor()
#c.execute("CREATE TABLE task(id integer, name text, priority integer);")
#c.execute("INSERT INTO task VALUES (1, 'First task', 1)")
#dbConn.commit()

tasks =[(2, 'second task', 10),
        (3, 'next task', 5),
        (4, 'Fourth task', 2)]
#input as list
#c.executemany("INSERT INTO task (id, name, priority) VALUES (?,?,?)", tasks)
#dbConn.commit()

c.execute("UPDATE task SET name=? where id =?", ("My first task", 2))
dbConn.commit()

#fetchall() / fetchmany() / fetchone()
c.execute("Select * from task")

#row = c.fetchone()
#print("First record=",row)
#print("---"*10)

noofrows = c.fetchmany(3)
for row in noofrows:
    print(row)

#rows = c.fetchall()
#print(rows)
#for row in rows:
#    print(row)

