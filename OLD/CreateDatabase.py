import os
import sqlite3

db_filename = "KoffieDB"
#schema_filename = "KoffieDB_Schema.sql"
db_exist = os.path.exists(db_filename)
if not db_exist:
    print "Database wordt aangemaakt."
    conn = sqlite3.connect(db_filename)
    
    print 'Creating schema'
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE Gebruiker (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, naam text not null)''')
    cursor.execute('''CREATE TABLE Prijzenlijst (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, product text not null, prijs real not null)''')
    cursor.execute('''CREATE TABLE Log (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, datum numeric not null, bericht text not null)''')
    cursor.execute('''CREATE TABLE Schulden (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, SchuldeiserID INTEGER NOT NULL, 
    SchuldmakerID INTEGER NOT NULL, Bedrag REAL NOT NULL, FOREIGN KEY(SchuldeiserID) REFERENCES Gebruiker(ID),
    FOREIGN KEY(SchuldmakerID) REFERENCES Gebruiker(ID)
    )''')
    conn.commit()
    cursor.execute("INSERT INTO Gebruiker (naam) VALUES ('Sebastiaan')")
    cursor.execute("INSERT INTO Gebruiker (naam) VALUES ('Jesse')")
    cursor.execute("INSERT INTO Gebruiker (naam) VALUES ('Dwin')")
    cursor.execute("INSERT INTO Gebruiker (naam) VALUES ('Jolanda')")
    cursor.execute("INSERT INTO Gebruiker (naam) VALUES ('Jeroen')")
    cursor.execute("INSERT INTO Prijzenlijst (product, prijs) VALUES ('Koffie', '1,25')")
    conn.commit()
else:
    pass
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    cursor.execute("""SELECT * From Gebruiker""")
    for row in cursor.fetchall():
        print row
