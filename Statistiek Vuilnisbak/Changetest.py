#!/usr/bin/env python
# -*- coding: CP1252 -*-


import wx

import gettext


import pylab
from creation import Creation
import os


class Stats(wx.Frame):
    def __init__(self, *args, **kwds):
        if os.path.isfile("temp.png"):
            os.remove("temp.png")
            print "BESTAAT"
        self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        
        self.radio_box_1 = wx.RadioBox(self, wx.ID_ANY, _("radio_box_1"), choices=[_("Bar"), _("Circle")], majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        
        pylab.figure(1, figsize=(6,6))
        
        ax = pylab.axes([0.1, 0.1, 0.8, 0.8])

        names = ["Dwin"]
        #names = ["Peter","John","James","Mark","Bart","Jude","Andrew","Simon"]
        self.data = [5]
        title = "Placeholder title"
        self.graph = Creation(names, self.data, title)
        #self.graph.buildBar()
        
        perf_plot = 'temp.png'

        self.list_box_3 = wx.ListBox(self, wx.ID_ANY, choices=[_("Iedereen"),_("Jan"), _("Joost"),
                                                               _("Klaas-Peter IV"), _("Kees-Jan"), _("Dwin")],
                                                                 style=wx.LB_MULTIPLE)
        self.list_box_2 = wx.ListBox(self, wx.ID_ANY, choices=[_("Grootste klootviool"), _("Homo"), _("Wie lijkt het meest op Dwin"), _("Wie is Kees-Jan")])
        self.radio_box_1.Bind(wx.EVT_RADIOBOX, self.onChange)
        self.list_box_2.Bind(wx.EVT_LISTBOX, self.onUpdateData)
        self.list_box_3.Bind(wx.EVT_LISTBOX, self.onUpdateNames)
        sel = self.radio_box_1.GetSelection()
        print self.radio_box_1.GetString(sel)
        self.__set_properties()
        self.onUpdateNames(wx.EVT_LISTBOX)
        self.onUpdateData(wx.EVT_LISTBOX)
        
        self.__do_layout()
    def onUpdateNames(self, event):
  
        selected = self.list_box_3.GetSelections()
        
        if selected[0] == 0:
            print "IEDEREEN"
            
            for name in range(self.list_box_3.GetCount()):
                self.list_box_3.Select(name)
                
                print name
            selected = self.list_box_3.GetSelections()[1:]   
        newnames = []
        data = [1,2,3,4,5,6]
        
        
        for selection in selected:
            newnames.append(str(self.list_box_3.GetString(selection)))
        #print newnames
        self.graph.setNames(newnames)
        #print self.graph.getNames()
        self.graph.setData(data[:len(newnames)])
        #self.__do_layout()
        self.onChange(wx.EVT_RADIOBOX)
    def onUpdateData(self, event):
        stat = self.list_box_2.GetSelection()
        #print stat
        if stat == 0:
            newdata = [1,2,3,4,5,6]
        elif stat == 1:
            newdata = [6,5,4,3,2,1]
        elif stat == 2:
            newdata = [12,10,8,6,13,1]
        elif stat == 3:
            newdata = [7,23,1,17,5,6]
        self.graph.setData(newdata[:len(self.graph.getNames())])
        self.graph.setTitle(str(self.list_box_2.GetString(stat)))
        print self.graph.getData()
        self.onChange(wx.EVT_RADIOBOX)
    def onChange(self, event):
        graphtype = self.radio_box_1.GetString(self.radio_box_1.GetSelection())
        
        if graphtype == "Circle":
            self.graph.buildPie()
        elif graphtype == "Bar":
            self.graph.buildBar()
            
        self.__do_layout()
    def __set_properties(self):

        self.SetTitle(_("frame_1"))
        self.SetSize((900, 675))
        self.radio_box_1.SetSelection(0)
        self.list_box_3.SetSelection(0)
        self.list_box_2.SetSelection(0)

    
    def __do_layout(self):

        self.image = wx.Image("temp.png")
        self.image.Rescale(666,500)
        image2 = wx.Bitmap(self.image)
        self.bitmap_1 = wx.StaticBitmap(self, wx.ID_ANY, image2)
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(self.radio_box_1, 0, wx.EXPAND, 0)
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
