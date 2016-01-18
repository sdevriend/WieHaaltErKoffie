# -*- coding: cp1252 -*-
"""
Jolanda Essens              Bin3a               s1082795
Dit programma is op 03-01-2016 geschreven.
Op 12-6-2014 is deze klasse gedocumenteerd.

Eerst wordt wx geimporteerd
"""
import wx

class Schuldenscherm1(wx.Panel):
    def __init__(self, parent, id, namen, schulden):
        """
        In deze methode slaat de welkomsttekst op.
        De volgende methodes worden aangeroepen:

        self.button()
        self.start()

        Als laatste zet deze methode de SetSizer naar self.box.
        """
        wx.Panel.__init__(self, parent, id, style=wx.SIMPLE_BORDER)
        self.schulden = schulden
        self.button()
        self.VerkrijgInformatie(namen)
        self.start(len(self.namen))
        self.SetSizer(self.box)

    def VerkrijgInformatie(self, namen):
        self.coordinaten = {}
        self.namen = sorted(namen)
        self.omgevormd = {}
        for x in range(0, len(self.namen)):
            self.coordinaten[self.namen[x]]=str(x+2)
        for x in self.schulden:
            temp=str("("+self.coordinaten[x[0]]+", "+self.coordinaten[x[1]]+")")
            self.omgevormd[temp]= str(x[2])
        for x in range(2, len(self.namen)+2):
            for y in range(2, len(self.namen)+2):
                         temp1=str("("+str(x)+", "+str(y)+")")
                         temp2=str("("+str(y)+", "+str(x)+")")
                         if temp1 == temp2:
                             self.omgevormd[temp1] = ""
                         else:
                             self.TryExcept(temp1, temp2)

    def TryExcept(self, temp1, temp2):
         try:
             if temp1 in self.omgevormd.keys() and temp2 not in self.omgevormd.keys():
                  self.omgevormd[temp1]=str("-€"+str(self.omgevormd[temp1]).replace('.',','))
             elif float(self.omgevormd[temp1]) > float(self.omgevormd[temp2]):
                 self.omgevormd[temp1]=str("-€"+str(float(self.omgevormd[temp1])-
                                                    float(self.omgevormd[temp2])).replace('.',','))
                 self.omgevormd[temp2]="€0,00"
             elif float(self.omgevormd[temp2]) > float(self.omgevormd[temp1]):
                 self.omgevormd[temp2]=str("-€"+str(float(self.omgevormd[temp2])-
                                                    float(self.omgevormd[temp1])).replace('.',','))
                 self.omgevormd[temp1]="€0,00"
             if self.omgevormd[temp1] == "0.0":
                 self.omgevormd[temp1]="€0,00"
             if self.omgevormd[temp2] == "0.0":
                 self.omgevormd[temp2]="€0,00"
         except KeyError:
             pass
         except ValueError:
             pass          
      
    def button(self):
        """
        In deze methode worden er twee knoppen aangemaakt, en
        vervolgens toegevoegd aan een box. Na het toevoegen van
        de knoppen, wordt self.kbox gereturned.
        """
        self.Terug = wx.Button(self, -1, "Terug")
        self.kbox = wx.BoxSizer()
        self.kbox.Add(self.Terug, 1, wx.EXPAND | wx.ALL)
        self.kbox.Add(wx.Panel(self, -1), 3, wx.EXPAND | wx.ALL)
        return self.kbox

    def tablebox(self, aantalcol, aantalrow, tekst, midden):

        self.column=0
        self.table = wx.BoxSizer()
        if aantalrow == midden:
            self.table.Add(wx.StaticText(self, -1, "Schuldeiser"), 2,
                           wx.CENTRE | wx.ALL)
        else:
            self.table.Add(wx.Panel(self, -1), 2, wx.CENTRE | wx.ALL)
        for x in range(0, aantalcol+1):
            if type(tekst) is list:
                if x == 0:
                    self.table.Add(wx.Panel(self, -1, style=wx.NO_BORDER), 1,
                                   wx.EXPAND | wx.ALL)
                else:
                    self.table.Add(wx.StaticText(self, -1, str(tekst[x-1]),
                        style=wx.SIMPLE_BORDER), 1, wx.EXPAND | wx.ALL)
            else:                    
                self.tablebox2(x, aantalcol, aantalrow, tekst)
        self.table.Add(wx.Panel(self, -1), 2, wx.EXPAND | wx.ALL)
        return self.table

    def tablebox2(self, x, aantalcol, aantalrow, tekst):
        if x == 0:
           self.column +=1
           self.table.Add(wx.StaticText(self, -1, str("\n"+tekst),
                          style=wx.SIMPLE_BORDER), 1, wx.EXPAND | wx.ALL)
        else:
           self.column += 1
           rowcolum=("("+str(self.column)+", "+str(aantalrow)+")")
           try:
               tekst = wx.StaticText(self, -1, str(self.omgevormd[rowcolum]),
                                     style=wx.SIMPLE_BORDER)
               if str(self.omgevormd[rowcolum]) != "€0,00":
                   tekst.SetForegroundColour((191,0,0))
               self.table.Add(tekst, 1, wx.EXPAND | wx.ALL)
           except KeyError:
               self.table.Add(wx.StaticText(self, -1, str("€0,00"),
               style=wx.SIMPLE_BORDER), 1, wx.EXPAND | wx.ALL)

   
    def start(self, aantal):
        """
        Deze methode voegt alle elementen samen tot één box.
        self.box wordt gereturned.
        """
        self.Schuldknop = wx.Button(self, -1, "Vereffen schuld")
        self.box = wx.BoxSizer(wx.VERTICAL)
        self.box.Add(wx.StaticText(self, -1, "Schuldmaker"), 1, wx.CENTRE | wx.ALL)
        for x in range(0, aantal+1):
            if x == 0:
                self.box.Add(self.tablebox(aantal, (x+1), self.namen, int((aantal+1)/2)),
                             1, wx.EXPAND | wx.ALL)
            else:
                self.box.Add(self.tablebox(aantal, (x+1), self.namen[x-1], int((aantal+1)/2)),
                             1, wx.EXPAND | wx.ALL)
        self.box.Add(self.Schuldknop, 1, wx.ALL | wx.CENTRE)
        self.box.Add(wx.Panel(self, -1), 1, wx.EXPAND | wx.ALL)
        self.box.Add(self.kbox, 1, wx.EXPAND)
        return self.box



"""
Hieronder staat de code die het scherm ook in deze file aan kan roepen,
en niet alleen in de main applicatie.
"""
if __name__ == "__main__":
    class Schermpje(wx.Frame):

        def __init__(self, parent, id, title):
            wx.Frame.__init__(self, parent, id, title, size=(750, 600))
            paneel = wx.Panel(self, id)
            paneel1 = Schuldenscherm1(paneel, id, ["Jeroen", "Sebastiaan", "Dwin", "Jesse", "Jolanda",
                      "Henk", "Jan"], [["Henk", "Jan", "3.01"],["Jan", "Henk", "2.99"]])
            boxje = wx.BoxSizer()
            boxje.Add(paneel1, 1, wx.EXPAND | wx.ALL, 2)
            paneel.SetSizer(boxje)
            self.Centre()
            self.Show(True)

    app = wx.App(False)
    Schermpje(None, -1, "Schuldenscherm")
    app.MainLoop()
