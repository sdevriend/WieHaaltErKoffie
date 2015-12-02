import os
import sqlite3

db_filename = "KoffieDB"
schema_filename = "KoffieDB_Schema.sql"
db_exist = os.path.exists(db_filename)
if not db_exist:
    print "Database wordt aangemaakt."
    conn = sqlite3.connect(db_filename)
    
    print 'Creating schema'
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE Persoon (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, naam text not null)''')
    conn.commit()
    cursor.execute("INSERT INTO Persoon (naam) VALUES ('Sebastiaan')")
    cursor.execute("INSERT INTO Persoon (naam) VALUES ('Jesse')")
    cursor.execute("INSERT INTO Persoon (naam) VALUES ('Dwin')")
    cursor.execute("INSERT INTO Persoon (naam) VALUES ('Jolanda')")
    cursor.execute("INSERT INTO Persoon (naam) VALUES ('Jeroen')")
    conn.commit()
else:
    pass
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    cursor.execute("""SELECT * From Persoon""")
    for row in cursor.fetchall():
        print row
