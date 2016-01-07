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
        titeltje.SetForegroundColour((255,191,0))
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

        drinken = [(1, "Boffie", "1.20"), (2, "Thee", "1.00"), (3, "Bier", "1.50"), (4, "Wijn", "1.70")]
        
        self.sw = wx.ScrolledWindow(paneel, -1, pos=(15, 100), size=(600, 180))

        txtKoffieTijd = "Lijst met dranken tijdens koffietijd:"
        stTxtKoffieTijd = wx.StaticText (self.sw, -1, txtKoffieTijd, pos = (15, 5))
  
        self.txtKoffie = self.prijzen[0][1]
        self.stTxtKoffie = wx.StaticText(self.sw, -1, self.txtKoffie, pos = (15, 35))
        self.txtCtrlKoffie = wx.TextCtrl(self.sw, -1, value=(str(self.prijzen[0][2])) ,pos=(150, 30))
        self.txtCtrlKoffie.SetEditable(False)

        self.txtThee = self.prijzen[1][1]
        self.stTxtThee = wx.StaticText (self.sw, -1, self.txtThee, pos = (15, 65))
        self.txtCtrlThee = wx.TextCtrl(self.sw, -1, value=(str(self.prijzen[1][2])),pos=(150, 60))
        self.txtCtrlThee.SetEditable(False)

        txtBierTijd = "Lijst met extra dranken na koffietijd:"
        stTxtBierTijd = wx.StaticText (self.sw, -1, txtBierTijd, pos = (15, 95))

        self.txtBier = drinken[2][1]
        self.stTxtBier = wx.StaticText (self.sw, -1, self.txtBier, pos = (15, 125))
        self.txtCtrlBier = wx.TextCtrl(self.sw, -1, value=(drinken[2][2]),pos=(150, 120))
        self.txtCtrlBier.SetEditable(False)

        self.txtWijn = drinken[3][1]
        self.stTxtWijn = wx.StaticText (self.sw, -1, self.txtWijn, pos = (15, 155))
        self.txtCtrlWijn = wx.TextCtrl(self.sw, -1, value=(drinken[3][2]),pos=(150, 150))
        self.txtCtrlWijn.SetEditable(False)
        
        
        self.sw.SetScrollbars(0,20,0,40)
      
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