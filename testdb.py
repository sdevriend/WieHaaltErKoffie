from BakkieControlDatabase import BakkieControlDatabase

a = BakkieControlDatabase(True, True)


print "Doe hier je acties"
print "Voeg klaas toe."
a.addUser("Klaas")

print "Show users: "
users = a.getUsers()
print users
print "--------"
print "Verwijder Klaas"
a.deleteUser("Klaas")
users = a.getUsers()
print users
print "--------------"
print "Prijzenlijst:"
prijzen = a.getPrijzenlijst()
print prijzen
prijzen[0][2] = 5.65
a.setPrijzenlijst(prijzen)
prijzen = a.getPrijzenlijst()
print prijzen
print "Sebastiaan heeft voor Jesse een koffie gehaald en voor Dwin een Theetje."
a.setBestelling(1, [[2, 1], [3,2]])
print "Jesse haalt nu cappuchino voor iedereen!"
a.setBestelling(2, [[1, 3], [3,3], [4,3], [5,3]]) 
print "Sluit daarna de db"
#a.cursor.execute('INSERT INTO Schulden (SchuldeiserID, SchuldmakerID, Bedrag) VALUES (1, 2, 5);')
#a.cursor.execute('SELECT Prijzenlijst.Product, COUNT(Bestelling.ProductID) FROM Bestelling, Prijzenlijst WHERE Prijzenlijst.ID = Bestelling.ProductID GROUP BY ProductID;')
#print a.cursor.fetchall()
a.getFrequenties()
a.getUserFreqs()
a.getUserSchulden()
a.getOpenstaand()
a.close()
