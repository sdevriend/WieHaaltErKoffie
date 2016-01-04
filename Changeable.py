#!/usr/bin/env python
# -*- coding: CP1252 -*-

import wx
import pylab
from creation import Creation

import gettext



class Stats(wx.Frame):
    def __init__(self, *args, **kwds):
        self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
        # begin wxGlade: Stats.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.radio_box_1 = wx.RadioBox(self, wx.ID_ANY, _("radio_box_1"), choices=[_("Bar"), _("Circle")], majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        self.radio_box_1.Bind(wx.EVT_RADIOBOX, self.onChange)
        sel = self.radio_box_1.GetSelection()
        print self.radio_box_1.GetString(sel)
        
        self.panel = wx.Panel(self, wx.ID_ANY)
        """ Start Pie Chart Code"""
        # make a square figure and axes
        pylab.figure(1, figsize=(6,6))
        ax = pylab.axes([0.1, 0.1, 0.8, 0.8])
        names = ["Peter","John","James","Mark","Bart","Jude","Andrew","Simon"]
        data = [12,15,8,3,18,23,9,12]
        title = "Placeholder title"
        self.circle = Creation("circle",names, data, title)
        self.bar = Creation("bar", names, data, title)
        self.bar.build()
        self.showGraph()
        perf_plot = 'temp.png'
        self.Fit()
        self.__set_properties()
        self.__do_layout()
        # end wxGlade
    def showGraph(self):
        image = wx.Bitmap("temp.png")
        wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap("temp.png"))
    def onChange(self, event):
        graphtype = self.radio_box_1.GetString(self.radio_box_1.GetSelection())
        
        if graphtype == "Circle":
            
            self.circle.build()
        elif graphtype == "Bar":
            self.bar.build()
        self.showGraph()
    def __set_properties(self):

        self.SetTitle(_("Changeable stats"))
        self.radio_box_1.SetSelection(0)
     

    def __do_layout(self):

        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(self.radio_box_1, 0, wx.EXPAND, 0)
        sizer_2.Add(self.panel, 2, wx.EXPAND, 1)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()

# end of class Stats
if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name

    app = wx.App(0)
    wx.InitAllImageHandlers()
    frame_1 = Stats(None, wx.ID_ANY, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()
