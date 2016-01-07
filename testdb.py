from BakkieControlDatabase import BakkieControlDatabase

a = BakkieControlDatabase(True, True)


print "Doe hier je acties"
print "Voeg klaas toe."
a.addUser("Klaas")
a.addUser("Kwawawalaa")
a.addUser("Kldsadsasadaasje")
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
print "Sluit daarna de db"
#a.cursor.execute('INSERT INTO Schulden (SchuldeiserID, SchuldmakerID, Bedrag) VALUES (1, 2, 5);')
a.cursor.execute('SELECT Gebruiker.Naam, Schulden.Bedrag FROM Gebruiker, Schulden WHERE Gebruiker.ID = Schulden.SchuldmakerID;')
print a.cursor.fetchall()
a.close()
