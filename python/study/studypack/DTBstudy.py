from configparser import Error
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="DTBCode3075",
  database = "testbase"
)

mycursor = mydb.cursor()

#    mycursor.execute("create database testbase")
mycursor.execute('show databases')
for x in mycursor:
    print(x)

#   mycursor.execute('create table testtable (
# id INT AUTO_INCREMENT PRIMARY KEY,
# name varchar(255),address varchar(255))')
'''column name is -- id --'''
mycursor.execute("show tables")
for x in mycursor:
    print(x)


#    mycursor.execute("alter table testtable add column id INT AUTO_INCREMENT PRIMARY KEY")


sqlcmd = 'INSERT INTO testtable ( name , address ) VALUES ( %s , %s )'
val = (' Morning_Star' , 'HL&MS_HR' )

try:
    mycursor.execute(sqlcmd , val)
except Error:
    print('Error')    

mydb.commit()

mycursor.execute( "SELECT * FROM testtable")
result = mycursor.fetchall()
for i in result :
    print(i)