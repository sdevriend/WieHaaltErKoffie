#!/usr/bin/env python
# -*- coding: CP1252 -*-


import wx

import gettext

import shutil
import time
import pylab
from creation import Creation
import os
from BakkieControlDatabase import BakkieControlDatabase

class Stats(wx.Frame):
    def __init__(self, *args, **kwds):
        if os.path.isfile("temp.png"):
            os.remove("temp.png")
            #print "BESTAAT"
        self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.savebutton = wx.Button(self, wx.ID_ANY, "Opslaan")
        self.backbutton = wx.Button(self, wx.ID_ANY, "Terug")
        self.backbutton.Bind(wx.EVT_BUTTON, self.onBack)
        self.savebutton.Bind(wx.EVT_BUTTON, self.onSave)
        self.radio_box_1 = wx.RadioBox(self, wx.ID_ANY, _("Soort grafiek"), choices=[_("Bar"), _("Circle")], majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        
        pylab.figure(1, figsize=(6,6))
        
        ax = pylab.axes([0.1, 0.1, 0.8, 0.8])

        
        #names = ["Peter","John","James","Mark","Bart","Jude","Andrew","Simon"]
        self.data = [0]
        names= [""]
        title = "Placeholder title"
        self.graph = Creation(names, self.data, title)
        #self.graph.buildBar()
        
        perf_plot = 'temp.png'
        names = self.getNames()
        self.list_box_3 = wx.ListBox(self, wx.ID_ANY, choices=names,
                                                                 style=wx.LB_MULTIPLE)
        self.list_box_2 = wx.ListBox(self, wx.ID_ANY, choices=[_("Wie haalt het vaakst?"), _("Wie is de grootste wanbetaler?"),
                                                               _("Welke dranken worden het meest gehaald?"), _("Wie geeft het gulst?")])
        self.radio_box_1.Bind(wx.EVT_RADIOBOX, self.onChange)
        self.list_box_2.Bind(wx.EVT_LISTBOX, self.onUpdateData)
        self.list_box_3.Bind(wx.EVT_LISTBOX, self.onUpdateNames)
        sel = self.radio_box_1.GetSelection()
        ##print self.radio_box_1.GetString(sel)
        self.__set_properties()
        self.onUpdateNames(wx.EVT_LISTBOX)
        self.onUpdateData(wx.EVT_LISTBOX)
        
        self.__do_layout()
    def onSave(self, event):
        newname = str(time.strftime("%y_%m_%d_%H_%M_%S"))
        newname+=".png"
        shutil.copy("temp.png",newname)
    def onBack(self, event):
        pass
    def getNames(self):
        self.db = BakkieControlDatabase()
        namelist = self.db.getUsers()
        ##print namelist
        newnames = ['iedereen']
        for tup in namelist:
            newnames.append(tup[1])
        return newnames
    def onUpdateNames(self, event):
        self.updateNames()
        
        self.onUpdateData(wx.EVT_LISTBOX)
        
        
        self.onChange(wx.EVT_RADIOBOX)
    def updateNames(self):
        selected = self.list_box_3.GetSelections()
        
        if selected[0] == 0:
            ##print "IEDEREEN"
            
            for name in range(self.list_box_3.GetCount()):
                self.list_box_3.Select(name)
                
                ##print name
            selected = self.list_box_3.GetSelections()[1:]   
        newnames = []
        
        
        for selection in selected:
            newnames.append(str(self.list_box_3.GetString(selection)))
        ##print newnames
        self.graph.setNames(newnames)
        ##print self.graph.getNames()
        data = self.graph.getData()
        self.graph.setData(data[:len(newnames)])
        #self.__do_layout()
    def onUpdateData(self, event):
        self.updateNames()
        stat = self.list_box_2.GetSelection()
        names = self.graph.getNames()
        ##print stat
        if stat == 0:
            freqs = self.db.getUserFreqs()
            
            data_names = []
            data_nums= []
            newdata = []
            for tup in freqs:
                data_names.append(tup[0])
                data_nums.append(tup[1])
            ##print data_names , "D_N"
            
            newdata = []
            for name in names:
                if name in data_names:
                    namenum = data_names.index(name)
                    newdata.append(data_nums[namenum])
                else:
                    newdata.append(0)
                
                    
                
        elif stat == 1:
            debt = self.db.getUserSchulden()
            #print debt
            data_names = []
            data_nums = []
            newdata = []
            for tup in debt:
                data_names.append(tup[0])
                data_nums.append(tup[1])
            for name in names:
                if name in data_names:
                    namenum = data_names.index(name)
                    newdata.append(data_nums[namenum])
                else:
                    newdata.append(0)
        elif stat == 2:
            
            freqs = self.db.getFrequenties()
            data_drinks = []
            data_nums = []
            newdata = []
            for tup in freqs:
                data_drinks.append(tup[0])
                data_nums.append(tup[1])
            
            self.graph.setNames(data_drinks)
            newdata = data_nums
        elif stat == 3:
            loan = self.db.getOpenstaand()
            #print loan
            data_names = []
            data_nums = []
            newdata = []
            for tup in loan:
                data_names.append(tup[0])
                data_nums.append(tup[1])
            for name in names:
                if name in data_names:
                    namenum = data_names.index(name)
                    newdata.append(data_nums[namenum])
                else:
                    newdata.append(0)
        #print self.graph.getData(),"ervoor"
        self.graph.setData(newdata)
        
        self.graph.setTitle(str(self.list_box_2.GetString(stat)))
        #print self.graph.getData(),"erna"
        self.onChange(wx.EVT_RADIOBOX)
    def onChange(self, event):
        graphtype = self.radio_box_1.GetString(self.radio_box_1.GetSelection())
        
        if graphtype == "Circle":
            self.graph.buildPie()
        elif graphtype == "Bar":
            self.graph.buildBar()
            
        self.__do_layout()
    def __set_properties(self):

        self.SetTitle(_("Statistieken"))
        self.SetSize((900, 675))
        self.radio_box_1.SetSelection(0)
        self.list_box_3.SetSelection(0)
        self.list_box_2.SetSelection(0)

    
    def __do_layout(self):

        self.image = wx.Image("temp.png")
        self.image.Rescale(666,500)
        image2 = wx.Bitmap(self.image)
        self.bitmap_1 = wx.StaticBitmap(self, wx.ID_ANY, image2)
        sizer_1 = wx.BoxSizer(wx.VERTICAL) #sizers
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL) # list boxes1
        sizer_2 = wx.BoxSizer(wx.VERTICAL) #Radiobox, bitmap
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL) # Radiobox, buttons
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL) #Butons
        sizer_4.Add(self.radio_box_1, 2, wx.EXPAND, 0)
        sizer_4.Add(sizer_5, 1, wx.EXPAND, 0)
        sizer_5.Add(self.backbutton, 1, wx.EXPAND, 0)
        sizer_5.Add(self.savebutton, 1, wx.EXPAND, 0)
        sizer_2.Add(sizer_4, 1, wx.EXPAND, 0)
        sizer_2.Add(self.bitmap_1, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        sizer_3.Add(self.list_box_3, 1, wx.EXPAND, 0)
        sizer_3.Add(self.list_box_2, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_3, 1, wx.EXPAND, 0)
        
        self.SetSizer(sizer_1)
        
        self.Layout()
   

if __name__ == "__main__":
    gettext.install("app") 

    app = wx.App(0)
    wx.InitAllImageHandlers()
    frame_1 = Stats(None, wx.ID_ANY, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()
