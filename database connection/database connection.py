                # Mysql connection
# mysql kan hman dawn chuan connector kan install phawt angai a ni.
# pip install mysql-connector   hmang hian kan install ang.


import mysql.connector  # mysql connector kan import


mydb = mysql.connector.connect(host='localhost', user='hpa', passwd='hpahpa')  # mysql database kan connect.

mycursor = mydb.cursor()  # cursor() hmang hian database ah kan insert, execute leh fetch engkim kha kan ti thei a ni.

mycursor.execute('show databases')  # database kan show dawn a ni.

for i in mycursor:
    print(i)

    # kan table kha kan show duh chuan mysql database kan connect naah khian "database" hming kha kan dah ve ang.
mydb1 = mysql.connector.connect(host='localhost', user='hpa', passwd='hpahpa', database='hpa')

mycur = mydb1.cursor()

mycur.execute('select * from student')  # "mycur" ah hian a in store vek dawn a ni.

print('table kan show ang')
# for i in mycur:  # hei "mycur" a mi kan print hi.
#     print(i)


     # mycur a mi kha 'result' ah kan dah anga chuan a print theih tho dawn a ni.
result = mycur.fetchall()  # fetchall a nih chuan a vaiin
# result = mycur.fetchone()  # fetchone hi chuan a row a kha a print ang
# result = mycur.fetchmany(1)  # hei pawh hian a row a tho kha a ni.
for i in result:
    print(i)