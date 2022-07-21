import mysql.connector as conn
mydb = conn.connect(
  host="localhost",
  user="root",
  password="vikas@123"
)

cur=mydb.cursor()
cur.execute("use college")
cur.execute("show tables")
cur.fetchall()
cur.execute("select * from student")
myresult=cur.fetchall()
print(type(myresult))
print(myresult)
for x in myresult:
  print(x)