import sqlite3

#connect to SQLite, connects to datebase file or creates it.
connection = sqlite3.connect('emaildb.sqlite')
#Send and receive SQL commands through cursor
cursor= connection.cursor()
#Sends command removes the table only if the table exists (to start fresh)
#otherwise, it just ignores the statement and does nothing.
cursor.execute('DROP TABLE IF EXISTS Counts');
#Sends command to create table, pass fields and type in parathenses
cursor.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')
#Prompts user to input a file name
filename = input('Enter file name:')
#Error handling
if (len(filename) < 1): filename = 'nbox-short.txt'
#File handler, allows us to read the content of the File
filehandler = open(filename)
#Loop across every line in the file
for line in filehandler:
    #if line doesnt start by From: skip line and continue Loop
    if not line.startswith('From: '): continue
    #Split the line into a list of strings to retrieve email
    list = line.split()
    email = list[1]
    # This line is not retrieving data. It's 'connecting' to the database row
    # It is dangerous to put strings into SQL.
    # the ? is a placeholder, it's meant to not allow SQL injections
    cursor.execute('SELECT count FROM Counts WHERE email = ?', (email,))
    #row is the information we get from the database. If no records, row = None
    row = cursor.fetchone()
    if row is None:
        #if email isnt in the database, insert email and add 1 to count.
        cursor.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', (email,))
    else:
        #if email is in the database, add +1 to count.
        cursor.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
    #commit is the command to "commit" the changes. Forces to disk, can be slow, avoid committing in loops.
    connection.commit()

#command to select the emails and counts order them by descing order, only retrieve 10.
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

#execute command and loop across all the rows
for row in cursor.execute(sqlstra):
    #str() fonction converts the specified value into a string
    print(str(row[0]), row[1])

cursor.close()
