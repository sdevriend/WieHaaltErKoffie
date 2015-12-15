"""
De class is gemaakt voor het beheren van de database. Er kunnen queries
geladen worden en naar toegestuurd worden door de gehele applicatie.
Om het database gedeelte eenvoudig te maken is het script in class vorm
gezet om alles eenvoudig te beheren.

Sebastiaan de Vriend 15-12-2015 Aanmaken script.
"""
import os
import sqlite3

class BakkieControlDatabase():
    def __init__(self, check=False):
        """
        Input:
            check: Boolean: Bij True wordt er gekeken of de database
                            beschikbaar is en zoniet dan wordt deze
                            aangemaakt.
    
        """
        self.db_filename = "Bakkie.db"
        if check:
            self.startup()
        self.startConnectionDatabase()
        
    
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