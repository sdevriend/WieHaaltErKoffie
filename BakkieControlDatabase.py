"""
De class is gemaakt voor het beheren van de database. Er kunnen queries
geladen worden en naar toegestuurd worden door de gehele applicatie.
Om het database gedeelte eenvoudig te maken is het script in class vorm
gezet om alles eenvoudig te beheren.

Sebastiaan de Vriend 15-12-2015 Aanmaken script.
Sebastiaan de Vriend 04-01-2016 Documentatie en toevoegen features.
"""
import os
import sqlite3
from datetime import datetime
from time import time


class BakkieControlDatabase():
    def __init__(self, check=False, testdata=False):
        """
        Input:
            check: Boolean: Bij True wordt er gekeken of de database
                            beschikbaar is en zoniet dan wordt deze
                            aangemaakt.
            testdata: Boolean: Bij True wordt er testdata ingevoerd.
                               Aan te raden is om dit op True te
                               zetten bij eerste keer startup van de
                               applicatie.
        """
        self.db_filename = "Bakkie.db"
        if check:
            self.startup()
        self.startConnectionDatabase() #  Hierna datainvoeren.
        if testdata:
            self.addTestData()
        
        
        
    
    def startConnectionDatabase(self):
        """
        De functie maakt verbinding met de Bakkie database en slaat een
        connection op samen met een cursor in self variabelen omdat 
        deze vaak gebruikt worden.
        """
        self.connection = sqlite3.connect(self.db_filename)
        self.cursor = self.connection.cursor()
        
        
    def startup(self):
        """
        De functie kijkt of de database filename bestaat in de huidige
        directory. Als dit niet zo is, dan wordt de database aangemaakt 
        en wordt er uit de huidige directory de sql file gepakt die bij
        Bakkie.db hoort. Daarna wordt de file gelezen en uitgevoerd
        door de cursor. Daarna wordt het bestand gesloten, de transactie
        voltooid en de database wordt gesloten. Er is nu een lege 
        database aangemaakt voor de applicatie.    
        """
        db_exist = os.path.exists(self.db_filename)
        if not db_exist:
            conn = sqlite3.connect(self.db_filename)
            cursor = conn.cursor()
            sqlfile = open("Bakkie.txt")
            sql = sqlfile.read()
            cursor.executescript(sql)
            sqlfile.close()
            conn.commit()
            conn.close()
    
    def close(self):
        """
        De functie sluit de connectie met de database.
        """
        self.connection.commit()
        self.connection.close()

    def getUsers(self):
        """
        De functie haalt alle gebruikers op en plaatst deze 
        """
        self.cursor.execute('SELECT * FROM Gebruiker')
        rows = self.cursor.fetchall()
        users = []
        for row in rows:
            users.append((row[0], str(row[1])))
        users.sort(key=lambda x: x[1])
        return users
    
    def addTestData(self):
        """
        De functie kijkt of er al data in de database zit. Als er geen
        data in de gebruikersdatabase zit, dan wordt er testdata
        queries ingeladen en deze worden vervolgens in de database
        geplaatst. Na het schrijven van de data, wordt de transactie
        voltooid.
        """
        self.cursor.execute('SELECT * FROM Gebruiker')
        testusers = ["Sebastiaan", "Jesse", "Dwin", "Jolanda", "Jeroen"]
        if len(self.cursor.fetchall()) == 0:
            map(self.addUser, testusers)
            #sqlfile = open("testdata.txt")
            #sql = sqlfile.read()
            #self.cursor.executescript(sql)
            #sqlfile.close()
            #self.connection.commit()
            # Is voor echte testdata.

    def addUser(self, username):
        """
        Input: 1
            username: String: Gebruikersnaam van nieuwe gebruiker.
        Het script voegd de nieuwe gebruiker toe aan de database en
        commit de transactie. Daarna wordt de username in een bericht
        geplaatst en deze wordt doorgestuurd naar de writelog functie.
        """
        self.cursor.execute('INSERT INTO Gebruiker (naam) VALUES(?)', (username,))
        self.connection.commit()
        bericht = "Gebruiker " + username + " is aangemaakt."
        self.__writelog(bericht)
        
    def __writelog(self, bericht):
        """
        Input: 1
            bericht: str: Bericht die in de database geplaatst wordt.
        De functie maakt een epoch timestamp en haalt de miliseconde af
        en plaatst deze met het bericht in de log database.
        """
        tijd = int(time())
        self.cursor.execute('INSERT INTO Log (Datum, Bericht) VALUES(?, ?)', (tijd, bericht, ))
        self.connection.commit()
    
    def deleteUser(self, username):
        """
        Input: 1 
            username: str: Gebruikersnaam die verwijderd kan worden uit
                           de database.
        De functie verwijderd uit de database de gebruiker. en commit
        daarna de transactie. Vervolgens wordt er een bericht
        aangemaakt en doorgestuurd naar writelog.
        """
        self.cursor.execute('DELETE FROM Gebruiker WHERE Naam = ?', (username,)) # mogelijk cascade onderzoeken!
        self.connection.commit()
        bericht = "Gebruiker" + username + " is verwijderd."
        self.__writelog(bericht)
    
    def getPrijzenlijst(self):
        self.cursor.execute('SELECT * FROM Prijzenlijst')
        rows = self.cursor.fetchall()
        for row in rows:
            print row