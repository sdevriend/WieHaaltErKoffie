"""
Jeroen Kuivenhoven      s1084216

"""

import wx


class Gebruikersscherm(wx.Panel):
    def __init__(self, parent, users):
        """ 
        """
        self.users = users
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
        titeltje = wx.StaticText(paneel, -1, "Gebruikers",
                                 pos=(10, 10), size=(295, -1),
                                 style=wx.ALIGN_LEFT)
        titeltje.SetForegroundColour((232,144,30))
        titeltje.SetFont(wx.Font(40, wx.DECORATIVE, wx.NORMAL, wx.NORMAL))

    def menubuttons(self, paneel):
        """ 
        """
        self.toe = wx.Button(paneel, -1,'Gebruiker toevoegen', pos=(15, 290), size=(250, 30))
        self.ver = wx.Button(paneel, -1,'Gebruiker verwijderen', pos=(280, 290), size=(250, 30))
        self.terug = wx.Button(paneel, -1,'Terug', pos=(10, 330), size=(200, 60))

    def scroll(self, paneel):

        Gebruikers = [(1, "Jesse"), (2, "Jeroen"), (3, "Sebastiaan"), (4, "Jolanda"), (5, "Dwin")]
        
        self.txtGebruikers = "De huidige gebruikers zijn:"
        self.stTxtGebruikers = wx.StaticText (paneel, -1, self.txtGebruikers, pos = (15, 80))
        self.stTxtGebruikers.SetForegroundColour((255,255,255))
        
        self.sw = wx.ScrolledWindow(paneel, -1, pos=(15, 100), size=(150, 180))

        self.LCGebruikers = wx.ListCtrl(self.sw, -1, pos=(0, 0), size=(600, 400), style = wx.LC_REPORT | wx.LC_NO_HEADER)
        self.LCGebruikers.SetBackgroundColour((46,24,0))
        self.LCGebruikers.SetTextColour((255,255,255))

        self.LCGebruikers.InsertColumn(0, "Gebruikers")
        self.LCGebruikers.Arrange()

        index = 1
        for item in self.users:
            self.LCGebruikers.InsertStringItem(index, item[1])
            index += 1

        self.sw.SetScrollbars(0,20,0,13)
        
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

class PopUpFrameToe(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Second Frame", size=(350, 150))
        panel = wx.Panel(self)
        self.SetBackgroundColour((46,24,0))
        self.Centre()
        self.txttoe = wx.StaticText(panel, label="Wat is de naam van de gebruiker?", pos = (15, 10))
        self.txttoe.SetForegroundColour((255,255,255))
        self.txtCtrlNaam = wx.TextCtrl(panel, -1, pos=(15, 30))
        self.cancel = wx.Button(panel, -1,'Cancel', pos=(15, 60), size=(100, 30))
        self.opslaan = wx.Button(panel, -1,'Opslaan', pos=(125, 60), size=(100, 30))

class PopUpFrameVer(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Second Frame", size=(250, 100))
        panel = wx.Panel(self)
        self.SetBackgroundColour((46,24,0))
        self.Centre()
        self.txtver = wx.StaticText(panel, label="Weet U het zeker?", pos = (15, 10))
        self.txtver.SetForegroundColour((255,255,255))
        self.ja = wx.Button(panel, -1,'Ja', pos=(15, 30), size=(100, 30))
        self.nee = wx.Button(panel, -1,'Nee', pos=(125, 30), size=(100, 30))
