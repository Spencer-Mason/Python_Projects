import sqlite3

#Creates a variable that is a shortcut to linking to the database
#And creates the database file if it doesn't exist
conn = sqlite3.connect('test2.db')

#Links to the database and creates a table
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName TEXT \
        )")
    conn.commit()

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

#Loops through the file list to find files that end with the '.txt' extention
for file in fileList:
    if file.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files (col_fileName) VALUES (?)", (file,))
            print(file)
conn.close()
