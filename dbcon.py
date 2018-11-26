import pymysql

conn = pymysql.connect(host ="localhost",user = "root", password = "", db ="my_python" )

mycursor = conn.cursor()

mycursor.execute(""""CREATE TABLE names

    (
    id int primary key,
    name varchar(50)
    )

    """)

conn.commit()
conn.close()