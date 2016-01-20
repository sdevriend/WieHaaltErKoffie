"""
Jeroen Kuivenhoven      s1084216
De aanroeper

"""

from welkomstscherm_1 import Welkomstscherm
from menuscherm_1 import Menuscherm
from Instellingen_drinken_halen_1 import In_dr_ha_1_scherm
from Bestelling_drinken_halen_1 import Be_dr_ha_1_scherm
from Bestelling_drinken_halen_1 import PopUpFrame
#from Statistiekscherm import Stats
import Schuldenscherm
import VereffenSchuld
from BeheerScherm import Beheerscherm
from PrijzenlijstScherm import Prijzenlijstscherm
from StaticPrijzenlijstScherm import StaticPrijzenlijstscherm
from GebruikersScherm import Gebruikersscherm
from GebruikersScherm import PopUpFrameToe
from GebruikersScherm import PopUpFrameVer
from LogScherm import Logscherm
from BakkieControlDatabase import BakkieControlDatabase

import wx
import random


class Schermpje(wx.Frame):
    def __init__(self, parent, id, title):
        """ 
        """
        wx.Frame.__init__(self, parent, id, 'Bakkie', style=wx.SYSTEM_MENU |
                          wx.CAPTION | wx.CLIP_CHILDREN, size=(1000, 750))
        self.boxje = wx.BoxSizer()
        #self.SetBackgroundColour((46,24,0))
        self.SetBackgroundColour((92,48,0))
        self.welkom()
        self.SetSizer(self.boxje)
        self.Centre()
        self.Show()

    def welkom(self):
        """ 
        """
        self.db = BakkieControlDatabase()
        self.prijzen = self.db.getPrijzenlijst()
        self.users = self.db.getUsers()
        
        self.welkompaneel = Welkomstscherm(self, -1)
        self.menupaneel = Menuscherm(self, -1)
        self.menupaneel.Hide()
        self.boxje.Add(self.welkompaneel, 1, wx.EXPAND | wx.ALL)
        self.welkompaneel.koffie_knop.Bind(wx.EVT_BUTTON, lambda evt : self.naarMenu(evt, "koffie"))
        self.welkompaneel.bier_knop.Bind(wx.EVT_BUTTON, lambda evt : self.naarMenu(evt, "bier"))

    def bier(self, event):
        self.SetBackgroundColour((255,255,20))

    def koffie(self, event):
        self.SetBackgroundColour((46,24,0))

    def naarWelkom(self, event):
        self.menupaneel.Hide()
        self.welkompaneel.Hide()
        self.welkompaneel = Welkomstscherm(self, -1)
        self.menupaneel = Menuscherm(self, -1)
        try:
            self.boxje.Add(self.welkompaneel, 1, wx.EXPAND | wx.ALL)
            self.menupaneel.Hide()
        except wx._core.PyAssertionError:
            pass
        #self.menupaneel.Hide()
        #self.boxje.Add(self.welkompaneel, 1, wx.EXPAND | wx.ALL)
        self.welkompaneel.koffie_knop.Bind(wx.EVT_BUTTON, lambda evt : self.naarMenu(evt, "koffie"))
        #self.welkompaneel.koffie_knop.Bind(wx.EVT_BUTTON, self.koffie)
        self.welkompaneel.bier_knop.Bind(wx.EVT_BUTTON, lambda evt : self.naarMenu(evt, "bier"))
        #self.welkompaneel.bier_knop.Bind(wx.EVT_BUTTON, self.bier)
        self.SetSize((1000, 750))
        self.SetSizer(self.boxje)
        self.Centre()
        self.boxje.Layout()

    def naarMenu(self, event, tijd):
        """
        """
        self.tijd = tijd
        try:
            self.drinken_1_paneel.Hide()
            self.bestelling_paneel.Hide()
            self.frame1.Hide()
        except AttributeError:
            pass
        try:
            self.beheerpaneel.Hide()
        except AttributeError:
            pass
        
        self.menupaneel = Menuscherm(self, -1)
        
        try:
            self.boxje.Add(self.menupaneel, 1, wx.EXPAND | wx.ALL)
            self.welkompaneel.Hide()
        except wx._core.PyAssertionError:
            pass
        self.menupaneel.Show()
        self.menupaneel.stop_knop.Bind(wx.EVT_BUTTON, self.onStop)
        self.menupaneel.terug_knop.Bind(wx.EVT_BUTTON, self.naarWelkom)
        self.menupaneel.drinken_halen_knop.Bind(wx.EVT_BUTTON, lambda evt : self.naarIn_dr_ha_1(evt, tijd))
        self.menupaneel.schulden_knop.Bind(wx.EVT_BUTTON, lambda evt : self.SchuldStartfunctie(evt, tijd))
        self.menupaneel.beheer_knop.Bind(wx.EVT_BUTTON, lambda evt : self.beheer(evt, tijd))
        #self.menupaneel.statistiek_knop.Bind(wx.EVT_BUTTON, lambda evt : self.naarStatistiek(evt, tijd))
        self.SetSize((850, 550))
        self.SetSizer(self.boxje)
        self.Centre()
        self.boxje.Layout()

    def naarIn_dr_ha_1(self, event, tijd):
        self.users = self.db.getUsers()
        self.drinken_1_paneel = In_dr_ha_1_scherm(self, -1, self.users)
        try:
            self.bestelling_paneel.Hide()
        except AttributeError:
            pass
        try:
            self.boxje.Add(self.drinken_1_paneel, 1, wx.EXPAND | wx.ALL)
            self.menupaneel.Hide()
        except wx._core.PyAssertionError:
            pass
        #self.drinken_1_paneel.Update()
        self.drinken_1_paneel.Show()
        #self.drinken_1_paneel.drinken_halen_knop.Bind(wx.EVT_RADIOBUTTON, self.naam)
        self.drinken_1_paneel.stop_knop.Bind(wx.EVT_BUTTON, self.onStop)
        self.drinken_1_paneel.terug_knop.Bind(wx.EVT_BUTTON, lambda evt : self.naarMenu(evt, tijd))
        self.drinken_1_paneel.random_knop.Bind(wx.EVT_BUTTON, lambda evt : self.naarBestelling(evt, tijd))
        self.drinken_1_paneel.hoogste_s_knop.Bind(wx.EVT_BUTTON, lambda evt : self.naarBestelling(evt, tijd))
        
        self.SetSize((950, 550))
        self.SetSizer(self.boxje)
        self.Centre()
        self.boxje.Layout()

        
    def naarBestelling(self, event, tijd):
        dezewillen = self.drinken_1_paneel.bestellers
        if len(dezewillen) > 0:
            self.bestelling_paneel = Be_dr_ha_1_scherm(self, -1, dezewillen, self.prijzen, tijd)
            try:
                self.boxje.Add(self.bestelling_paneel, 1, wx.EXPAND | wx.ALL)
                self.drinken_1_paneel.Hide()
            except wx._core.PyAssertionError:
                pass
            try:
                self.Staticprijzenlijstpaneel.Hide()
            except AttributeError:
                pass
            self.bestelling_paneel.Show()
            #self.drinken_1_paneel.drinken_halen_knop.Bind(wx.EVT_RADIOBUTTON, self.naam)
            self.bestelling_paneel.prijzenkaart_knop.Bind(wx.EVT_BUTTON, self.naarStaticLijst)
            self.bestelling_paneel.doorgaan_knop.Bind(wx.EVT_BUTTON, lambda evt : self.naarPopUp(evt, tijd))
            self.bestelling_paneel.terug_knop.Bind(wx.EVT_BUTTON, lambda evt : self.naarIn_dr_ha_1(evt, tijd))

            self.SetSize((800, 700))
            self.SetSizer(self.boxje)
            self.Centre()
            self.boxje.Layout()

    def naarStaticLijst(self, event):
        self.db = BakkieControlDatabase()
        prijzen = self.db.getPrijzenlijst()
        self.Staticprijzenlijstpaneel = StaticPrijzenlijstscherm(self, prijzen, self.tijd)
        self.Staticprijzenlijstpaneel.terug.Bind(wx.EVT_BUTTON, lambda evt : self.naarBestelling(evt, self.tijd))
        self.boxje.Add(self.Staticprijzenlijstpaneel, 1, wx.EXPAND | wx.ALL)
        self.bestelling_paneel.Hide()
        self.Staticprijzenlijstpaneel.Show()
        self.SetSize((700, 440))
        self.SetSizer(self.boxje)
        self.Centre()
        self.boxje.Layout()

        
    def naarPopUp(self, event, tijd):
        self.frame1 = PopUpFrame()
        self.frame1.Show()
        self.frame1.ok.Bind(wx.EVT_BUTTON, lambda evt : self.naarMenu(evt, tijd))

    def SchuldStartfunctie(self, event, tijd):
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
        self.Schuldpaneel = Schuldenscherm.Schuldenscherm1(self, -1, self.Gebruikers,
                                                      self.schulden)
        self.Vereffenpaneel = VereffenSchuld.VereffenScherm(self, -1, self.Gebruikers)
        self.frame = VereffenSchuld.PopUpFrameVereffend()
        
    def SchuldStartscherm(self):
        self.boxje.Add(self.Schuldpaneel, 1, wx.EXPAND | wx.ALL)
        self.boxje.Add(self.Vereffenpaneel, 1, wx.EXPAND | wx.ALL)
        self.Schuldpanelhide(self.Schuldpaneel, (750, 600))
        self.SetSizer(self.boxje)
        self.Centre()
        self.Show(True)
           
    def Schuldpanelhide(self, zie, bh):
	#Hide overbodige panelen.
	#zie = paneel welke te zien is
	#bh = breedte x hoogte
        self.menupaneel.Hide()
        self.Schuldpaneel.Hide()
        self.Vereffenpaneel.Hide()
        self.frame.Hide()
        zie.Show()
        self.SetSize(bh)
        self.Centre()
        self.Layout()

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
        self.Schuldpanelhide(self.menupaneel, (850, 550))

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

    """
    def naarStatistiek(self, event, tijd):
        
        self.statspaneel = Stats(self, wx.ID_ANY, "")
        self.statspaneel.Centre()
       
     
        self.statspaneel.Show()
    """

    

    def beheer(self, event, tijd):
        """
        """
        self.beheerpaneel = Beheerscherm(self) #Balngrijk
        try:
            self.menupaneel.Hide()
        except AttributeError:
            pass
        try:
            self.prijzenlijstpaneel.Hide()
        except AttributeError:
            pass
        try:
            self.gebruikerspaneel.Hide()
        except AttributeError:
            pass
        try:
            self.logpaneel.Hide()
        except AttributeError:
            pass
        try:
            self.boxje.Add(self.beheerpaneel, 1, wx.EXPAND | wx.ALL)
            self.menupaneel.Hide()
        except wx._core.PyAssertionError:
            pass
        self.beheerpaneel.Show()
        self.SetSize((700, 440))
        self.SetSizer(self.boxje)
        self.Centre()
        self.boxje.Layout()

        self.beheerpaneel.terug.Bind(wx.EVT_BUTTON, lambda evt : self.naarMenu(evt, tijd))
        self.beheerpaneel.pri.Bind(wx.EVT_BUTTON, lambda evt : self.prijzenlijstscherm(evt, tijd))
        self.beheerpaneel.geb.Bind(wx.EVT_BUTTON, lambda evt : self.gebruikersscherm(evt, tijd))
        self.beheerpaneel.log.Bind(wx.EVT_BUTTON, lambda evt : self.logScherm(evt, tijd))

    def prijzenlijstscherm(self, event, tijd):
        """
        """
        self.db = BakkieControlDatabase()
        prijzen = self.db.getPrijzenlijst()
        self.prijzenlijstpaneel = Prijzenlijstscherm(self, prijzen)
        self.boxje.Add(self.prijzenlijstpaneel, 1, wx.EXPAND | wx.ALL)
        self.beheerpaneel.Hide()
        self.prijzenlijstpaneel.Show()
        self.SetSize((700, 440))
        self.SetSizer(self.boxje)
        self.Centre()
        self.boxje.Layout()

        self.prijzenlijstpaneel.terug.Bind(wx.EVT_BUTTON, lambda evt : self.beheer(evt, tijd))
        self.prijzenlijstpaneel.bew.Bind(wx.EVT_BUTTON, self.bewerken)
        self.prijzenlijstpaneel.ops.Bind(wx.EVT_BUTTON, self.opslaan)

    def bewerken(self, event):
        self.prijzenlijstpaneel.txtCtrlKoffie.SetEditable(True)
        self.prijzenlijstpaneel.txtCtrlThee.SetEditable(True)
        self.prijzenlijstpaneel.txtCtrlCapp.SetEditable(True)
        self.prijzenlijstpaneel.txtCtrlFris.SetEditable(True)
        self.prijzenlijstpaneel.txtCtrlBier.SetEditable(True)
        self.prijzenlijstpaneel.txtCtrlWijn.SetEditable(True)

    def opslaan(self, event):
        self.db = BakkieControlDatabase()
        prijzen = self.db.getPrijzenlijst()
        HetZelfde = 0

        prijzenlijst= []
        
        self.prijzenlijstpaneel.txtCtrlKoffie.SetEditable(False)
        newKoffie = self.prijzenlijstpaneel.txtCtrlKoffie.GetLineText(0)
        if any(c.isalpha() for c in newKoffie):
            prijzenlijst.append((1, "Koffie", self.db.getPrijzenlijst()[0][2]))
            self.prijzenlijstpaneel.txtCtrlKoffie.SetValue(str(self.db.getPrijzenlijst()[0][2]))
            HetZelfde += 1
        else:
            prijzenlijst.append((1, "Koffie", float(newKoffie)))
            if str(newKoffie) == str(prijzen[0][2]):
                HetZelfde += 1
        
        self.prijzenlijstpaneel.txtCtrlThee.SetEditable(False)
        newThee = self.prijzenlijstpaneel.txtCtrlThee.GetLineText(0)
        if any(c.isalpha() for c in newThee):
            prijzenlijst.append((2, "Thee", self.db.getPrijzenlijst()[1][2]))
            self.prijzenlijstpaneel.txtCtrlThee.SetValue(str(self.db.getPrijzenlijst()[1][2]))
            HetZelfde += 1
        else:
            prijzenlijst.append((2, "Thee", float(newThee)))
            if str(newThee) == str(prijzen[1][2]):
                HetZelfde += 1
            
        self.prijzenlijstpaneel.txtCtrlCapp.SetEditable(False)
        newCapp = self.prijzenlijstpaneel.txtCtrlCapp.GetLineText(0)
        if any(c.isalpha() for c in newCapp):
            prijzenlijst.append((3, "Cappuccino", self.db.getPrijzenlijst()[2][2]))
            self.prijzenlijstpaneel.txtCtrlCapp.SetValue(str(self.db.getPrijzenlijst()[2][2]))
            HetZelfde += 1
        else:
            prijzenlijst.append((3, "Cappuccino", float(newCapp)))
            if str(newCapp) == str(prijzen[2][2]):
                HetZelfde += 1
        
        self.prijzenlijstpaneel.txtCtrlFris.SetEditable(False)
        newFris = self.prijzenlijstpaneel.txtCtrlFris.GetLineText(0)
        if any(c.isalpha() for c in newFris):
            prijzenlijst.append((4, "Fris", self.db.getPrijzenlijst()[3][2]))
            self.prijzenlijstpaneel.txtCtrlFris.SetValue(str(self.db.getPrijzenlijst()[3][2]))
            HetZelfde += 1
        else:
            prijzenlijst.append((4, "Fris", float(newFris)))
            if str(newFris) == str(prijzen[3][2]):
                HetZelfde += 1
            
        self.prijzenlijstpaneel.txtCtrlBier.SetEditable(False)
        newBier = self.prijzenlijstpaneel.txtCtrlBier.GetLineText(0)
        if any(c.isalpha() for c in newBier):
            prijzenlijst.append((5, "Bier", self.db.getPrijzenlijst()[4][2]))
            self.prijzenlijstpaneel.txtCtrlBier.SetValue(str(self.db.getPrijzenlijst()[4][2]))
            HetZelfde += 1
        else:
            prijzenlijst.append((5, "Bier", float(newBier)))
            if str(newBier) == str(prijzen[4][2]):
                HetZelfde += 1
        
        self.prijzenlijstpaneel.txtCtrlWijn.SetEditable(False)
        newWijn = self.prijzenlijstpaneel.txtCtrlWijn.GetLineText(0)
        if any(c.isalpha() for c in newWijn):
            prijzenlijst.append((6, "Wijn", self.db.getPrijzenlijst()[5][2]))
            self.prijzenlijstpaneel.txtCtrlWijn.SetValue(str(self.db.getPrijzenlijst()[5][2]))
            HetZelfde += 1
        else:
            prijzenlijst.append((6, "Wijn", float(newWijn)))
            if str(newWijn) == str(prijzen[5][2]):
                HetZelfde += 1

        if HetZelfde != 6:
            self.db.setPrijzenlijst(prijzenlijst)

    def gebruikersscherm(self, event, tijd):
        """
        """
        self.db = BakkieControlDatabase()
        users = self.db.getUsers()
        self.gebruikerspaneel = Gebruikersscherm(self, users)
        self.boxje.Add(self.gebruikerspaneel, 1, wx.EXPAND | wx.ALL)
        self.beheerpaneel.Hide()
        self.gebruikerspaneel.Show()
        self.SetSize((700, 440))
        self.SetSizer(self.boxje)
        self.Centre()
        self.boxje.Layout()

        self.gebruikerspaneel.terug.Bind(wx.EVT_BUTTON, lambda evt : self.beheer(evt, tijd))
        self.gebruikerspaneel.toe.Bind(wx.EVT_BUTTON, self.showPopUpToe)
        self.gebruikerspaneel.ver.Bind(wx.EVT_BUTTON, self.gebruikerVerwijderen)

    def showPopUpToe(self, event):
        self.frameToe = PopUpFrameToe()
        self.frameToe.Show()

        self.frameToe.cancel.Bind(wx.EVT_BUTTON, self.closePopUpToe)
        self.frameToe.opslaan.Bind(wx.EVT_BUTTON, self.gebruikerOpslaan)

    def closePopUpToe(self, event):
        self.frameToe.Close()

    def gebruikerOpslaan(self, event):
        naam = self.frameToe.txtCtrlNaam.GetValue()
        if len(str(naam)) == 0:
            pass
        else:
            index = self.gebruikerspaneel.LCGebruikers.GetItemCount()
            self.gebruikerspaneel.LCGebruikers.InsertStringItem(index+1, naam)
            self.db.addUser(naam)
            self.frameToe.Close()

    def gebruikerVerwijderen(self, event):
        geselecteerd =  self.gebruikerspaneel.LCGebruikers.GetFirstSelected()
        if geselecteerd == -1:
            pass
        else:
            self.showPopUpVer()
            #self.gebruikerspaneel.LCGebruikers.DeleteItem(long(geselecteerd))

    def showPopUpVer(self):
        self.frameVer = PopUpFrameVer()
        self.frameVer.Show()

        self.frameVer.nee.Bind(wx.EVT_BUTTON, self.closePopUpVer)
        self.frameVer.ja.Bind(wx.EVT_BUTTON, self.verwijderenGebruiker)

    def verwijderenGebruiker(self, event):
        geselecteerd =  self.gebruikerspaneel.LCGebruikers.GetFirstSelected()
        naam = self.gebruikerspaneel.LCGebruikers.GetItemText(geselecteerd, 0)
        self.gebruikerspaneel.LCGebruikers.DeleteItem(long(geselecteerd))
        self.db.deleteUser(naam)
        self.frameVer.Close()

    def closePopUpVer(self, event):
        self.frameVer.Close()

    def logScherm(self, event, tijd):
        self.db = BakkieControlDatabase()
        days, log = self.db.getLog()
        #print log
        self.logpaneel = Logscherm(self, days, log)
        self.boxje.Add(self.logpaneel, 1, wx.EXPAND | wx.ALL)
        self.beheerpaneel.Hide()
        self.logpaneel.Show()
        self.SetSize((700, 440))
        self.SetSizer(self.boxje)
        self.Centre()
        self.boxje.Layout()

        self.logpaneel.terug.Bind(wx.EVT_BUTTON, lambda evt : self.beheer(evt, tijd))
        self.logpaneel.CBDatum.Bind(wx.EVT_COMBOBOX, self.nieuweLog)

    def nieuweLog(self, event):
        dag = self.logpaneel.CBDatum.GetValue()
        self.db = BakkieControlDatabase()
        days, log = self.db.getLog()
        for item in log:
            if str(item[0][0][0:10]) == str(dag):
                index = log.index(item)
                self.logpaneel.list.ClearAll()
                self.logpaneel.list.InsertColumn(0,"Datum", width=130)
                self.logpaneel.list.InsertColumn(1,"Geberurtenis",  width=wx.LIST_AUTOSIZE_USEHEADER)
                try:
                    for a in log[index]:
                        pos = self.logpaneel.list.InsertStringItem(0,str(a[0]))
                        self.logpaneel.list.SetStringItem(pos,1,str(a[1]))
                except:
                    pass
    
    def onStop(self, event):
        """ 
        """
        self.Destroy()

    

# de klasse schermpje wordt aangeroepen
if __name__ == "__main__":
    app = wx.App()
    Schermpje(None, -1, "Bakkie")
    app.MainLoop()
