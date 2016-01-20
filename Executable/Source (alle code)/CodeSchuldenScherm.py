import wx
import sys
import os
import Schuldenscherm
import VereffenSchuld
from BakkieControlDatabase import BakkieControlDatabase



class SchuldenSchermCode(wx.Frame):

    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(750, 600))
        self.db = BakkieControlDatabase()
        self.SchuldStartfunctie()
        
    def SchuldStartfunctie(self):
        users = self.db.getUsers()
        self.Gebruikers = [x[1] for x in users]
        self.IDs = {}
        for x in users:
            self.IDs[x[1]] = x[0]
        self.HergroepeerSchuld()
        self.schuldige = "1"
        self.schuldeiser = "1"
        self.SchuldStartfunctie2()
        
    def SchuldStartfunctie2(self):
	#Bouwt het scherm
        self.db.setSchulden(1, 3, 6.34) #Verwijder!
        self.db.setSchulden(2, 4, 1.32) #Verwijder!
        self.SchuldSetpanel()
        self.SchuldStartscherm()
        self.Schuldbuttonevents()

    def HergroepeerSchuld(self):
	#Filtert de IDs uit de schulden lijst van de database (self.schulden)
	# Filtert de namen uit de schuldenlijst van de database (self.SchuldByID)
        Schuld = self.db.getSchulden()
        self.schulden = []
        self.SchuldByID = []
        for x in Schuld:
            temp = [x[1], x[3], x[4]]
            temp2 = [x[0], x[2], x[4]]
            self.schulden.append(temp)
            self.SchuldByID.append(temp2)

    def SchuldSetpanel(self):
	#Aanroepen schermen
        self.paneel = wx.Panel(self, -1)
        self.Schuldpaneel = Schuldenscherm.Schuldenscherm1(self.paneel, -1, self.Gebruikers,
                                                      self.schulden)
        self.Vereffenpaneel = VereffenSchuld.VereffenScherm(self.paneel, -1, self.Gebruikers)
        self.frame = VereffenSchuld.PopUpFrameVereffend()
        
    def SchuldStartscherm(self):
        self.boxje = wx.BoxSizer(wx.VERTICAL)
        self.boxje.Add(self.Schuldpaneel, 1, wx.EXPAND)
        self.boxje.Add(self.Vereffenpaneel, 1, wx.EXPAND)
        self.Schuldpanelhide(self.Schuldpaneel, (750, 600))
        self.paneel.SetSizer(self.boxje)
        self.Centre()
        self.Show(True)
           
    def Schuldpanelhide(self, zie, bh):
	#Hide overbodige panelen.
	#zie = paneel welke te zien is
	#bh = breedte x hoogte
        self.Schuldpaneel.Hide()
        self.Vereffenpaneel.Hide()
        self.frame.Hide()
        zie.Show()
        self.SetSize(bh)
        self.Centre()
        self.Refresh()

    def Schuldbuttonevents(self):
	#Bindt de buttons
        self.Schuldpaneel.Terug.Bind(wx.EVT_BUTTON, self.SchuldTerugButton)
        self.Schuldpaneel.Schuldknop.Bind(wx.EVT_BUTTON, self.SchuldButton)
        self.Vereffenpaneel.Vereffenknop.Bind(wx.EVT_BUTTON, self.VereffenButton)
        self.Vereffenpaneel.drop1.Bind(wx.EVT_COMBOBOX, self.SchuldDropButton1)
        self.Vereffenpaneel.drop2.Bind(wx.EVT_COMBOBOX, self.SchuldDropButton2)
        self.frame.terug.Bind(wx.EVT_BUTTON, self.SchuldTerugButton)

    def SchuldTerugButton(self, event):
        #Code voor scherm terug vanaf schuldenscherm, moet naar menuscherm
        "voer hier code in om terug te gaan naar het menuscherm"

    def SchuldButton(self, event):
	#Start het vereffenschuld scherm op
        self.Schuldpanelhide(self.Vereffenpaneel, (450, 300))
        
    def VereffenButton(self, event):
	#Vereffend schuld tussen twee gebruikers
        if self.schuldige == self.schuldeiser or self.schuldige == "1" or self.schuldeiser == "1":
            pass
        else:
            SchuldigeID = self.IDs[self.schuldige] #Haalt ID op
            SchuldEiserID = self.IDs[self.schuldeiser] #Haalt ID op
            for x in self.SchuldByID:
                if x[0] == SchuldigeID and x[1] == SchuldEiserID:
                    Check1 = x[2] # schuld te vereffenen 
                if x[1] == SchuldigeID and x[0] == SchuldEiserID:
                    Check2 = x[2] # schuld andersom te vereffenen
            if float(Check1) > float(Check2):
                self.db.setSchulden(SchuldEiserID, SchuldigeID)
                self.db.setSchulden(SchuldigeID, SchuldEiserID)# reset beiden naar 0
            if float(Check2) > float(Check1):
                self.db.setSchulden(SchuldEiserID, SchuldigeID) #reset laagste schuld naar 0
                self.db.setSchulden(SchuldigeID, SchuldEiserID, float(Check2 - Check1))                
            self.Schuldpanelhide(self.frame, (300, 150))

    def SchuldDropButton1(self, event):
        self.schuldige = self.Vereffenpaneel.drop1.GetValue() #Haalt naam schuldige op

    def SchuldDropButton2(self, event):
        self.schuldeiser = self.Vereffenpaneel.drop2.GetValue() #Haalt naam schuldeiser op
        


app = wx.App(False)
SchuldenSchermCode(None, -1, "Schuldenscherm")
app.MainLoop()
