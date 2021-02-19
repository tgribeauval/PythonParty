import sqlite3
import re

connection = sqlite3.connect('orgdb.sqlite')
cursor= connection.cursor()

cursor.execute('DROP TABLE IF EXISTS Counts');
cursor.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

filename = input('Enter file name:')

filehandler = open(filename)

for line in filehandler:
    if not line.startswith('From: '): continue
    org = line.rstrip().split()[1].split('@')[1]

    cursor.execute('SELECT count FROM counts WHERE org = ?', (org,))
    row = cursor.fetchone()
    if row is None:
        cursor.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
    else:
        cursor.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))

connection.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cursor.execute(sqlstr):

    print(str(row[0]), row[1])

cursor.close()
