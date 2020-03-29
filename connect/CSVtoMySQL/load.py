import csv
import mysql.connector
import re

#Establish connection to MYSQL
conn = mysql.connector.connect(host = '127.0.0.1',
user = 'root', passwd = 'password', db = 'mysql')
#Use the Right Table
curr = conn.cursor()
curr.execute("USE dndscraping")
#Test if Table is found
curr.execute("SELECT * FROM linkstable")
print(curr.fetchone())


with open('output.csv') as csvfile:
    csv_data = csv.reader(csvfile)
    if csv_data == None:
        print("None csv recognized")
    else:
        print("CSV read")
    for row in csv_data:

        curr.execute('INSERT INTO linkstable(link, \
            newReference)' \
            'VALUES("%s", "%s")',
            row)
#close the connection to the database.
conn.commit()
curr.close()
print("Done")
