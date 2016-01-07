"""
Dwin Grashof      s1082225
De aanroeper

"""

from welkomstscherm_1 import Welkomstscherm
from menuscherm_1 import Menuscherm
from BeheerScherm import Beheerscherm
from PrijzenlijstScherm import Prijzenlijstscherm
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
        self.SetBackgroundColour((46,24,0))
        self.welkom(self)
        self.SetSizer(self.boxje)
        self.Centre()
        self.Show()

    def welkom(self, event):
        """ 
        """
        self.db = BakkieControlDatabase()
        prijzen = self.db.getPrijzenlijst()
        self.welkompaneel = Welkomstscherm(self, -1)
        self.menupaneel = Menuscherm(self)
        self.beheerpaneel = Beheerscherm(self)
        self.prijzenlijstpaneel = Prijzenlijstscherm(self, prijzen)
        self.gebruikerspaneel = Gebruikersscherm(self)
        self.logpaneel = Logscherm(self)
        self.menupaneel.Hide()
        self.beheerpaneel.Hide()
        self.prijzenlijstpaneel.Hide()
        self.gebruikerspaneel.Hide()
        self.logpaneel.Hide()
        self.boxje.Add(self.welkompaneel, 1, wx.EXPAND | wx.ALL)
        self.welkompaneel.koffie_knop.Bind(wx.EVT_BUTTON, self.naarMenu)
        self.welkompaneel.bier_knop.Bind(wx.EVT_BUTTON, self.naarMenu)

    def naarMenu(self, event):
        """
        """
        self.menupaneel = Menuscherm(self) #Balngrijk
        try:
            self.boxje.Add(self.menupaneel, 1, wx.EXPAND | wx.ALL) #probeert het paneel toe te voegen
            self.welkompaneel.Hide()    #Daarna wordt het welkomstscherm verborgen
        except wx._core.PyAssertionError: #De error die optreed
            pass
        self.beheerpaneel.Hide() #Hide alle schermen die een terugknop hebben naar dit scherm
        self.menupaneel.Show()
        self.SetSize((700, 440))
        self.SetSizer(self.boxje)
        self.Centre()
        self.boxje.Layout()

        self.menupaneel.new.Bind(wx.EVT_BUTTON, self.beheer)

    def beheer(self, event):
        """
        """
        self.beheerpaneel = Beheerscherm(self) #Balngrijk
        try:
            self.boxje.Add(self.beheerpaneel, 1, wx.EXPAND | wx.ALL)
            self.menupaneel.Hide()
        except wx._core.PyAssertionError:
            pass
        self.menupaneel.Hide()
        self.prijzenlijstpaneel.Hide()
        self.gebruikerspaneel.Hide()
        self.logpaneel.Hide()
        self.beheerpaneel.Show()
        self.SetSize((700, 440))
        self.SetSizer(self.boxje)
        self.Centre()
        self.boxje.Layout()

        self.beheerpaneel.terug.Bind(wx.EVT_BUTTON, self.naarMenu)
        self.beheerpaneel.pri.Bind(wx.EVT_BUTTON, self.prijzenlijstscherm)
        self.beheerpaneel.geb.Bind(wx.EVT_BUTTON, self.gebruikersscherm)
        self.beheerpaneel.log.Bind(wx.EVT_BUTTON, self.logScherm)

    def prijzenlijstscherm(self, event):
        """
        """
        self.db = BakkieControlDatabase()
        prijzen = self.db.getPrijzenlijst()
        print prijzen
        self.prijzenlijstpaneel = Prijzenlijstscherm(self, prijzen)
        self.boxje.Add(self.prijzenlijstpaneel, 1, wx.EXPAND | wx.ALL)
        self.beheerpaneel.Hide()
        self.prijzenlijstpaneel.Show()
        self.SetSize((700, 440))
        self.SetSizer(self.boxje)
        self.Centre()
        self.boxje.Layout()

        self.prijzenlijstpaneel.terug.Bind(wx.EVT_BUTTON, self.beheer)
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
        self.prijzenlijstpaneel.txtCtrlKoffie.SetEditable(False)
        self.prijzenlijstpaneel.txtCtrlThee.SetEditable(False)
        self.prijzenlijstpaneel.txtCtrlCapp.SetEditable(False)
        self.prijzenlijstpaneel.txtCtrlFris.SetEditable(False)
        self.prijzenlijstpaneel.txtCtrlBier.SetEditable(False)
        self.prijzenlijstpaneel.txtCtrlWijn.SetEditable(False)

    def gebruikersscherm(self, event):
        """
        """
        self.gebruikerspaneel = Gebruikersscherm(self)
        self.boxje.Add(self.gebruikerspaneel, 1, wx.EXPAND | wx.ALL)
        self.beheerpaneel.Hide()
        self.gebruikerspaneel.Show()
        self.SetSize((700, 440))
        self.SetSizer(self.boxje)
        self.Centre()
        self.boxje.Layout()

        self.gebruikerspaneel.terug.Bind(wx.EVT_BUTTON, self.beheer)
        self.gebruikerspaneel.toe.Bind(wx.EVT_BUTTON, self.showPopUpToe)
        self.gebruikerspaneel.ver.Bind(wx.wx.EVT_BUTTON, self.gebruikerVerwijderen)

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
        self.gebruikerspaneel.LCGebruikers.DeleteItem(long(geselecteerd))
        self.frameVer.Close()

    def closePopUpVer(self, event):
        self.frameVer.Close()

    def logScherm(self, event):
        self.logpaneel = Logscherm(self)
        self.boxje.Add(self.logpaneel, 1, wx.EXPAND | wx.ALL)
        self.beheerpaneel.Hide()
        self.logpaneel.Show()
        self.SetSize((700, 440))
        self.SetSizer(self.boxje)
        self.Centre()
        self.boxje.Layout()

        self.logpaneel.terug.Bind(wx.EVT_BUTTON, self.beheer)

    def onStop(self, event):
        """ Als onStop als event van een knop wordt gebonden sluit het
        scherm.
        """
        self.Close()

    

# de klasse schermpje wordt aangeroepen
if __name__ == "__main__":
    app = wx.App()
    Schermpje(None, -1, "Bakkie")
    app.MainLoop()
