import mysql.connector
connection =    mysql.connector.connect(host="localhost",
                                        user="root",
                                      password = "admin",
                                        database= "officesalary"  )
cursor = connection.cursor()
query =""" CREATE Table  EMP_sal(emp_id INT auto_increment PRIMARY KEY, EMP_salary INT , bouns INT) """
cursor.execute(query)
cursor.execute(query)
try:
     cursor.execute(query)
except Exception as e:
     print(e)
data =[(10000, 1200),
       (13000, 1400),
       (10000, 1200),
       (13000, 1400),
       (10000, 1200),
       (13000, 1400),]
insertdataquery= """""INSERT INTO EMP_sal(EMP_salary,bouns),VALUES(%s,%s)"""
cursor.executemany(insertdataquery, data)
connection .commit()
print(f"{cursor.rowcount},rowcount")