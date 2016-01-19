
import wx

class VereffenScherm(wx.Panel):
    def __init__(self, parent, id, Gebruikers):
        """
        self.start()

        Als laatste zet deze methode de SetSizer naar self.box.
        """
        wx.Panel.__init__(self, parent, id, style=wx.SIMPLE_BORDER)
        self.startbox(Gebruikers)
        self.showbox()
        self.SetSizer(self.box)

  
    def startbox(self, gebruikers):
        self.Gebruikers = sorted(gebruikers)
        self.boxje = wx.BoxSizer(wx.HORIZONTAL)
        self.drop1 = wx.ComboBox(self, -1, choices=self.Gebruikers)
        self.drop2 = wx.ComboBox(self, -1, choices=self.Gebruikers)
        self.boxje.Add(wx.Panel(self, -1), 3, wx.EXPAND | wx.ALL)
        self.boxje.Add(self.drop1, 1)
        self.boxje.Add(wx.Panel(self, -1), 1, wx.EXPAND | wx.ALL)
        self.boxje.Add(self.drop2, 1)
        self.boxje.Add(wx.Panel(self, -1), 3, wx.EXPAND | wx.ALL)
        return self.boxje

    def showbox(self):
        self.box = wx.BoxSizer(wx.VERTICAL)
        self.Vereffenknop = wx.Button(self, -1, "Vereffen schuld!")
        self.box.Add(wx.Panel(self, -1), 3, wx.EXPAND | wx.ALL)
        tekst = wx.StaticText(self,-1, "\t\t         Schuldige:  \t\tSchuldeiser:")
        tekst.SetForegroundColour((255,255,255))
        self.box.Add(tekst, 1, wx.EXPAND | wx.ALL)
        self.box.Add(self.boxje, 1, wx.EXPAND, wx.ALL)
        self.box.Add(self.Vereffenknop, 1, wx.CENTRE)
        self.box.Add(wx.Panel(self, -1), 3, wx.EXPAND | wx.ALL)

        return self.box


class PopUpFrameVereffend(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="", size=(300, 150))
        panel = wx.Panel(self)
        self.Centre()
        text = wx.StaticText(panel, label="Schuld vereffend!",  pos=(100, 10))
        self.terug = wx.Button(panel, -1, "Oke",  pos=(100, 60), size=(100, 30))

"""
Hieronder staat de code die het scherm ook in deze file aan kan roepen,
en niet alleen in de main applicatie.
"""
if __name__ == "__main__":
    class Schermpje(wx.Frame):

        def __init__(self, parent, id, title):
            wx.Frame.__init__(self, parent, id, title, size=(450, 300))
            paneel = wx.Panel(self, id)
            paneel1 = VereffenScherm(paneel, id, ["Jeroen", "Sebastiaan", "Dwin", "Jesse", "Jolanda",
                      "Henk", "Jan"])
            boxje = wx.BoxSizer()
            boxje.Add(paneel1, 1, wx.EXPAND | wx.ALL, 2)
            paneel.SetSizer(boxje)
            self.Centre()
            self.Show(True)

    app = wx.App(False)
    Schermpje(None, -1, "Vereffen schuld")
    app.MainLoop()
