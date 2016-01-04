from BakkieControlDatabase import BakkieControlDatabase

a = BakkieControlDatabase(True, True)


print "Doe hier je acties"
print "Voeg klaas toe."
a.addUser("Klaas")
a.addUser("Klaa")
a.addUser("Klaasje")
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
a.getPrijzenlijst()
print "Sluit daarna de db"
a.close()
