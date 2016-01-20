"""
Jeroen Kuivenhoven      s1084216

"""

import wx


class Prijzenlijstscherm(wx.Panel):
    def __init__(self, parent, prijzen):
        """ 
        """
        self.prijzen = prijzen
        wx.Panel.__init__(self, parent)
        titelpaneel = wx.Panel(self)
        self.teksten(titelpaneel)
        self.menubuttons(titelpaneel)
        self.scroll(titelpaneel)
        self.navigatiebuttons()
        boxje = self.boxen(titelpaneel)
        self.eindbox = wx.BoxSizer()
        self.eindbox.Add(boxje, 1, wx.EXPAND | wx.ALL)
        self.SetSizer(self.eindbox)

    def teksten(self, paneel):
        """ 
        """
        titeltje = wx.StaticText(paneel, -1, "Prijzenlijst",
                                 pos=(10, 10), size=(295, -1),
                                 style=wx.ALIGN_LEFT)
        titeltje.SetForegroundColour((232,144,30))
        titeltje.SetFont(wx.Font(40, wx.DECORATIVE, wx.NORMAL, wx.NORMAL))

    def menubuttons(self, paneel):
        """ 
        """
        self.bew = wx.Button(paneel, -1,'Bewerken', pos=(15, 290), size=(250, 30))
        self.ops = wx.Button(paneel, -1,'Opslaan', pos=(280, 290), size=(250, 30))
        self.terug = wx.Button(paneel, -1,'Terug', pos=(10, 330), size=(200, 60))

    def scroll(self, paneel):
        """
        """
        self.sw = wx.ScrolledWindow(paneel, -1, pos=(15, 100), size=(600, 180))

        txtKoffieTijd = "Lijst met dranken tijdens koffietijd:"
        self.stTxtKoffieTijd = wx.StaticText (self.sw, -1, txtKoffieTijd, pos = (15, 5))
        self.stTxtKoffieTijd.SetForegroundColour((255,255,255))
  
        self.txtKoffie = self.prijzen[0][1]
        self.stTxtKoffie = wx.StaticText(self.sw, -1, self.txtKoffie, pos = (15, 35))
        self.stTxtKoffie.SetForegroundColour((255,255,255))
        self.txtCtrlKoffie = wx.TextCtrl(self.sw, -1, value=(str(self.prijzen[0][2])) ,pos=(150, 30))
        self.txtCtrlKoffie.SetEditable(False)

        self.txtThee = self.prijzen[1][1]
        self.stTxtThee = wx.StaticText (self.sw, -1, self.txtThee, pos = (15, 65))
        self.stTxtThee.SetForegroundColour((255,255,255))
        self.txtCtrlThee = wx.TextCtrl(self.sw, -1, value=(str(self.prijzen[1][2])),pos=(150, 60))
        self.txtCtrlThee.SetEditable(False)

        self.txtCapp = self.prijzen[2][1]
        self.stTxtCapp = wx.StaticText (self.sw, -1, self.txtCapp, pos = (15, 95))
        self.stTxtCapp.SetForegroundColour((255,255,255))
        self.txtCtrlCapp = wx.TextCtrl(self.sw, -1, value=(str(self.prijzen[2][2])),pos=(150, 90))
        self.txtCtrlCapp.SetEditable(False)

        txtBierTijd = "Lijst met extra dranken na koffietijd:"
        self.stTxtBierTijd = wx.StaticText (self.sw, -1, txtBierTijd, pos = (15, 125))
        self.stTxtBierTijd .SetForegroundColour((255,255,255))

        self.txtFris = self.prijzen[3][1]
        self.stTxtFris = wx.StaticText (self.sw, -1, self.txtFris, pos = (15, 155))
        self.stTxtFris.SetForegroundColour((255,255,255))
        self.txtCtrlFris = wx.TextCtrl(self.sw, -1, value=(str(self.prijzen[3][2])),pos=(150, 150))
        self.txtCtrlFris.SetEditable(False)
        
        self.txtBier = self.prijzen[4][1]
        self.stTxtBier = wx.StaticText (self.sw, -1, self.txtBier, pos = (15, 185))
        self.stTxtBier.SetForegroundColour((255,255,255))
        self.txtCtrlBier = wx.TextCtrl(self.sw, -1, value=(str(self.prijzen[4][2])),pos=(150, 180))
        self.txtCtrlBier.SetEditable(False)

        self.txtWijn = self.prijzen[5][1]
        self.stTxtWijn = wx.StaticText (self.sw, -1, self.txtWijn, pos = (15, 215))
        self.stTxtWijn.SetForegroundColour((255,255,255))
        self.txtCtrlWijn = wx.TextCtrl(self.sw, -1, value=(str(self.prijzen[5][2])),pos=(150, 210))
        self.txtCtrlWijn.SetEditable(False)
        
        
        self.sw.SetScrollbars(0,20,0,15)
      
    def navigatiebuttons(self):
        """
        """
        self.terug_knop = wx.Button(self, -1, ("Terug"))

    def boxen(self, paneel):
        """ 
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.new, 0, wx.CENTER, wx.TOP, 30)
        vbox.Add((1, 1), 2)
        vbox.Add(self.ren, 0, wx.CENTER,wx.TOP, 30)
        vbox.Add((1, 1), 2)
        vbox.Add(self.dlt, 0, wx.CENTER,wx.TOP, 30)
        vbox.Add((1, 1), 2)
        vbox.Add(self.clr, 0, wx.CENTER,wx.TOP, 30)
        vbox.Add((1, 1), 2)
        """
        
        boxje = wx.BoxSizer(wx.VERTICAL)
        boxje.Add(paneel, 1, wx.EXPAND | wx.ALL)
        
        #boxje.Add(vbox, 8, wx.EXPAND | wx.ALL)
        return boxje
