import sqlite3

#connect to sqlite3
connection = sqlite3.connect("student.db")

##create a cursor object to insert record,create table

cursor=connection.cursor()

#create table

table_info = """
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT);
"""

cursor.execute(table_info)

# insert record
cursor.execute("""insert into student values('DIPESH','DATA SCIENCE','A',80)""")
cursor.execute("""insert into student values('SHUBHAM','DATA SCIENCE','B',95)""")
cursor.execute("""insert into student values('OM','DATA ANALYSIS','A',86)""")
cursor.execute("""insert into student values('JOHN','DEVOPS','A',35)""")
cursor.execute("""insert into student values('SOHAM','DEVPOS','A',50)""")

#Display all records

print("inserted all records")
data=cursor.execute("""select * from student""")

for row in data:
    print(row)

#close connection

connection.commit()
connection.close()
