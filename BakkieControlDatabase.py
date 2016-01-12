"""
De class is gemaakt voor het beheren van de database. Er kunnen queries
geladen worden en naar toegestuurd worden door de gehele applicatie.
Om het database gedeelte eenvoudig te maken is het script in class vorm
gezet om alles eenvoudig te beheren.

Sebastiaan de Vriend 15-12-2015 Aanmaken script.
Sebastiaan de Vriend 04-01-2016 Documentatie en toevoegen features.
Sebastiaan de Vriend 05-01-2016 Features en documentatie.
"""
import os
import sqlite3
import datetime
import time



class BakkieControlDatabase():
    """
    Class documentatie voor BakkieControlDatabase.
    Het is aan te roepen door deze module te importeren.
    Voor een nieuwe database verwijder je eerst de oude
    Bakke.db en roepen
    je de module aan met check=True.
    Voor testdata gebruik je testdata=True.
    
    Voor een "Gebruikte" database kan je testdb.py runnen.
    Dit script handeld een aantal standaard procedures uit
    zoals het toevoegen en verwijderen van een gebruiker,
    het halen van een bestelling en het aanpassen van de prijzenlijst.
    
    Voorbeeld:
        db = BakkieControlDatabase()
        Zie documentatie init voor juiste opties.
    Handige modules:
    
        db.close()
        ALTIJD GEBRUIKEN ALS HET SCHERM WORDT AFGESLOTEN!
        
        db.getUsers()
        Lijst met gebruikers en daarbij hun id's.
        [(ID, Naam)]
        
        db.addUser(username)
        Voor het toevoegen van een nieuwe gebruiker.
        
        db.deleteUser(username)
        Voor het verwijderen van een bestaande gebruiker.
        
        db.getPrijzenlijst()
        Het verkrijgen van de producten en de behorende prijzen.
        [[ID, Naam, Prijs]]
        
        db.setPrijzenlijst(lijst)
        Methode om de prijzenlijst te updaten. Geeft hierbij de
        prijzenlijst van getPrijzenlijst me daarin de nieuwe
        bedragen.
        
        db.setBestelling(id, lijst)
        Hier kan je de bestelling naartoe sturen in het volgende formaat.
        id: gebruiker die koffie gaat halen.
        lijst: lijst met bestellingen. Elke bestelling ziet er als volgt uit:
        [userid, productid]
        
        queries voor Jesse:
        db.getFrequenties()
        db.getUserFreqs()
        db.getUserSchulden()
        db.getOpenstaand()
        
        
        Voor het ophalen van de schuldenlijst met daarbij namen en bedragen
        gebruik je het volgende:
        db.getSchulden(). Dit geeft de volgende lijst terug:
        [
        [EiserID, EiserNaam, MakerID, MakerNaam, Bedrag],
        [EiserID, EiserNaam, MakerID, MakerNaam, Bedrag]
        ]
        
        db.setSchulden(SchuldEiserID, SchuldmakerID)
        Voor het resetten van een schuld tussen schuldeiser en
        schuldmaker. Het bedrag komt hiermee op 0 euro.
        
        db.getLog()
        Voor het ophalen van het logfile. De functie geeft twee
        lijsten terug. De eerste lijst bevat de namen van de dagen
        die voorkomen in het log. De 2e lijst is het log zelf.
        Voor elke dag is een apparte lijst gemaakt met daarin een
        lijst voor elke log gebeurtenis met datum.
        log = [ #DAG [ [datum, bericht], [datum, bericht] ],
                #DAG [ [datum, bericht], [datum, bericht] ]]
    """
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
        self.cursor.execute('pragma foreign_keys=ON')
        self.connection.commit()
        
        
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
            sqlfile = open("BakkieControlDatabaseSQL.txt")
            sql = sqlfile.read()
            cursor.execute('pragma foreign_keys=ON')
            conn.commit()
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
        De functie haalt alle gebruikers op en plaatst deze in
        een lijst. Hoeft niet echt met lambda gesorteerd te worden,
        maar werkt wel.
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
        Als de user is aangemaakt, dan wordt er voor de user en de
        andere users een record toegevoegd aan de schulden tabel. Dit
        zorgt ervoor dat er altijd een 0 waarde beschikbaar is, en er
        hoeft niet gekeken worden of er een schuldenpaar aanwezig is...
        """
        self.cursor.execute('INSERT INTO Gebruiker (naam) VALUES(?)', (username,))
        self.connection.commit()
        bericht = "Gebruiker " + username + " is aangemaakt."
        self.__writelog(bericht)
        self.cursor.execute('SELECT ID FROM Gebruiker WHERE Naam = ? ;', (username,))
        gebruikerid = self.cursor.fetchall()[0][0]
        self.cursor.execute('SELECT ID FROM Gebruiker WHERE Naam != ? ;', (username,))
        gebruikers = self.cursor.fetchall()
        for user in gebruikers:
            self.cursor.execute('INSERT INTO Schulden (SchuldeiserID, SchuldmakerID, Bedrag) VALUES (?, ?, 0.00);', (gebruikerid, user[0],))
            self.cursor.execute('INSERT INTO Schulden (SchuldeiserID, SchuldmakerID, Bedrag) VALUES (?, ?, 0.00);', (user[0], gebruikerid,))
            self.connection.commit()
        
    def __writelog(self, bericht):
        """
        Input: 1
            bericht: str: Bericht die in de database geplaatst wordt.
        De functie maakt een epoch timestamp en haalt de miliseconde af
        en plaatst deze met het bericht in de log database.
        """
        tijd = int(time.time())
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
        """
        De functie haalt alles op uit de prijzenlijst tabel en zet
        alle rows om in tuples en plaatst deze in een lijst die
        vervolgens terug gegeven wordt.
        """
        self.cursor.execute('SELECT * FROM Prijzenlijst')
        rows = self.cursor.fetchall()
        prijzenlijst = []
        for row in rows:
            prijzenlijst.append([row[0], str(row[1]), float(row[2])])
        return prijzenlijst
    
    def setPrijzenlijst(self, newPrijs):
        """
        Input: 1
            newPrijs: Lijst: De nieuwe prijzenlijst.
        De functie haalt een kopielijst op van de prijzenlijst en
        loopt vervolgens door beide lijsten heen. Als er een
        verandering is, dan zijn de lijsten niet gelijk en wordt
        de prijzenlijst tabel geupdate met de nieuwe waarde.
        Vervolgens wordt er een bericht gemaakt en deze wordt
        doorgestuurd naar de logfunctie.
        """
        oudPrijs = self.getPrijzenlijst()
        for nPrijs, oudPrijs in zip(newPrijs, oudPrijs):
            if nPrijs != oudPrijs:
                self.cursor.execute('UPDATE Prijzenlijst SET Prijs = ? WHERE ID = ?;', (nPrijs[2], nPrijs[0],))
                self.connection.commit()
                bericht = "De prijs voor " + nPrijs[1] + " is veranderd van: " + str(oudPrijs[2]) + " naar: " + str(nPrijs[2])
                self.__writelog(bericht)
    def setBestelling(self, HaalID, Bestellingen):
        """
        Input: 2
            HaalID: Int: ID van de persoon die drankjes gaat halen.
            Bestellingen: Lijst met de volgende invoer.
            [[PersoonID, ProductID], [PersoonID, ProductID]]
        De functie haalt de namen van gebruikers en producten op en
        loopt door bestellingen. Bij elke bestelling wordt de juiste
        naam en de bestelling opgehaald. Daarvanuit worden er twee
        tabellen bijgewerkt. Als eerste wordt er een schuld toegevoegd
        bij de juiste gebruiker. En als tweede wordt er een bestelling
        toegevoegd aan de database. Daarna wordt er een bericht geschreven
        waarin staat wie er gehaald heeft en wat er precies gehaald is.
        Dit wordt doorgestuurd naar de logfunctie.
        """
        self.cursor.execute('SELECT Naam FROM Gebruiker WHERE ID = ?;', (str(HaalID)))
        haalNaam = self.cursor.fetchall()[0][0]
        for bestelling in Bestellingen:
            self.cursor.execute('SELECT Product, Prijs FROM Prijzenlijst WHERE ID = ?;', (str(bestelling[1])))
            producten = self.cursor.fetchall()[0]
            self.cursor.execute('SELECT Naam FROM Gebruiker WHERE ID = ?;', (str(bestelling[0])))
            bestelnaam = self.cursor.fetchall()[0][0]
            bericht = haalNaam + " heeft voor " + bestelnaam + " " + str(producten[0]) + " gehaald voor: " + str(producten[1]) + "."
            self.cursor.execute('UPDATE Schulden SET Bedrag=(Bedrag + ?) WHERE SchuldeiserID = ? AND SchuldmakerID = ?;', 
            (producten[1], str(HaalID), str(bestelling[0]), ))
            self.cursor.execute('INSERT INTO Bestelling (GehaaldID, VoorID, ProductID) VALUES (?, ?, ?);', (str(HaalID), str(bestelling[0]), str(bestelling[1]),))
            self.connection.commit()
            self.__writelog(bericht)
        
        
    def getFrequenties(self):
        """
        Functie queried de database en geeft een lijst terug.
        """
        self.cursor.execute('SELECT Prijzenlijst.Product, COUNT(Bestelling.ProductID) FROM Bestelling, Prijzenlijst WHERE Prijzenlijst.ID = Bestelling.ProductID GROUP BY ProductID;')
        freqs = []
        for data in self.cursor.fetchall():
            freqs.append([str(data[0]), data[1]])
        return freqs
    
    def getUserFreqs(self):
        """Query voor Jesse"""
        self.cursor.execute('SELECT Gebruiker.Naam, COUNT( Bestelling.GehaaldID ) FROM Gebruiker, Bestelling WHERE Gebruiker.ID = Bestelling.GehaaldID GROUP BY Gebruiker.Naam;')
        freqs = []
        for data in self.cursor.fetchall():
            freqs.append([str(data[0]), data[1]])
        return freqs
    
    def getUserSchulden(self):
        """Query voor Jesse"""
        self.cursor.execute('SELECT Gebruiker.Naam, sum(Schulden.Bedrag) FROM Gebruiker, Schulden WHERE Gebruiker.ID = Schulden.SchuldmakerID GROUP BY Gebruiker.Naam;')
        datalijst = []
        freqs = []
        for data in self.cursor.fetchall():
            freqs.append([str(data[0]), round(float(data[1]), 2)])
        return freqs
       
    def getOpenstaand(self):
        """Query voor Jesse"""
        self.cursor.execute('SELECT Gebruiker.Naam, SUM(Schulden.Bedrag) FROM Gebruiker, Schulden WHERE Gebruiker.ID = Schulden.SchuldeiserID GROUP BY Gebruiker.Naam;')
        freqs = []
        for data in self.cursor.fetchall():
            freqs.append([str(data[0]), round(float(data[1]), 2)])
        return freqs
        
    def getSchulden(self):
        """
        Functie haalt alle schulden op van de database in het
        volgende formaat:
        [
        [EiserID, EiserNaam, MakerID, MakerNaam, Bedrag],
        [EiserID, EiserNaam, MakerID, MakerNaam, Bedrag]
        ]
        """
        self.cursor.execute("""SELECT Schulden.SchuldeiserID AS Eiser, 
                               EI.Naam AS EiserNaam, 
                               Schulden.SchuldmakerID as Maker, 
                               Mak.Naam AS MakerNaam, Schulden.Bedrag from Schulden, 
                               Gebruiker AS EI, Gebruiker AS Mak 
                               WHERE Eiser = EI.ID AND Maker = Mak.ID  
                               ORDER BY EiserNaam, MakerNaam;""")
        schuldenlijst = []
        for row in self.cursor.fetchall():
            schuldenlijst.append([row[0], str(row[1]), row[2], str(row[3]), round(float(row[4]), 2)])
        return schuldenlijst
    
    def setSchulden(self, EiserID, MakerID, bedrag=0.0):
        """
        Input: 2
        EiserID: ID van de schuldeneiser.
        MakerID: ID van de schuldenmaker.
        bedrag: nieuw schuldbedrag.
        
        De functie lost de schulden op tussen de maker en de eiser en
        maakt een bericht op voor het logbestand.
        """
        self.cursor.execute('SELECT Naam FROM Gebruiker WHERE ID = ?;', (str(EiserID)))
        EiserNaam = self.cursor.fetchall()[0][0]
        self.cursor.execute('SELECT Naam FROM Gebruiker WHERE ID = ?;', (str(MakerID)))
        MakerNaam = self.cursor.fetchall()[0][0]
        
        self.cursor.execute("UPDATE Schulden SET Bedrag = ? WHERE SchuldeiserID = ? AND SchuldmakerID = ?;", (bedrag, str(EiserID), str(MakerID), ))
        self.connection.commit()
        bericht = MakerNaam + " lost de schulden in bij " + EiserNaam + "."
        self.__writelog(bericht)
    
    def getLog(self):
        """
        Functie maakt de tijd van nu aan, dat een string is, en een timestamp van nu.
        Daarna wordt een timestamp van precies 00:00 gemaakt van vandaag en wordt
        end aan de timestamp van nu gekoppeld en begin aan 00:00. Hiermee
        kunnen tijden uit de database gehaald worden per dag.
        Daarnaast worden de lijsten daynames voor de dagnamen en log gemaakt.
        In de loop worden alle logberichten per dag opgehaald. Als er
        logberichten zijn, dan wordt de dagnaam van de bijbehorende
        dag erbij geplaktin daynames en wordt er geloopt door de logberichten.
        en wordt de timestamp omgezet naar leesbaar en het logbericht
        toegevoegd als lijst. Aan het einde wordt de dag toegevoegd aan
        het logboek. 
        Daarna wordt end het begin van de dag en wordt begin de vorige dag.
        aan het einde wordt daynames en log terug gegeven.
        
        day = [dagnaam, dagnaam, dagnaam]
        log = [
        [ Dit is 1 dag[datum, bericht], [datum,bericht]],
        [ Dit is 1 dag[datum, bericht], [datum,bericht]]
        ]
        """
        today = datetime.date.today()
        now = time.time()
        prevDay = time.mktime(datetime.datetime.strptime(str(today), "%Y-%m-%d").timetuple())
        end = now
        begin = prevDay
        daynames = []
        log = []
        for x in range(1, 8):
            self.cursor.execute('SELECT Datum, Bericht FROM Log WHERE Datum > ? AND Datum < ?;', (begin, end, ))
            rows = self.cursor.fetchall()
            if len(rows) > 0:
                daynames.append(datetime.datetime.fromtimestamp(begin).strftime('%A'))
                daglog = []
                for row in rows:
                    rowtimestamp = datetime.datetime.fromtimestamp(row[0]).strftime('%Y-%m-%d %H:%M:%S')
                    rowbericht = str(row[1])
                    daglog.append([rowtimestamp, rowbericht])
                log.append(daglog)
            end = begin
            begin = begin - 86400 
        return daynames, log