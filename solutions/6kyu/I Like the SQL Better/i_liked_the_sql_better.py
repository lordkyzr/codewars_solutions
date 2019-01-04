import sqlite3
conn = sqlite3.connect('/tmp/movies.db')
cursor = conn.cursor()

cursor.execute('CREATE TABLE MOVIES (Name text, Year int, Rating int)')
cursor.execute('INSERT INTO MOVIES (Name,Year,Rating) VALUES ("Rise of the Planet of the Apes",2011,77)')
cursor.execute('INSERT INTO MOVIES (Name,Year,Rating) VALUES ("Dawn of the Planet of the Apes",2014,91)')
cursor.execute('INSERT INTO MOVIES (Name,Year,Rating) VALUES ("Alien",1979,97)')
cursor.execute('INSERT INTO MOVIES (Name,Year,Rating) VALUES ("Aliens",1986,98)')
cursor.execute('INSERT INTO MOVIES (Name,Year,Rating) VALUES ("Mad Max",1979,95)')
cursor.execute('INSERT INTO MOVIES (Name,Year,Rating) VALUES ("Mad Max 2: The Road Warrior",1981,100)')
conn.commit()
conn.close()