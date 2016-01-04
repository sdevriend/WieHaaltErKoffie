# Refferentie:
# http://www.cs.colorado.edu/~kena/classes/5448/s11/presentations/pearse.pdf

import wx

import numpy 
import matplotlib

import matplotlib.pyplot as plt

from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas

class TestFrame(wx.Frame):

    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title,size=(500,600))

        self.create_main_panel()    
        self.draw_figure()

    def create_main_panel(self):
        self.panel = wx.Panel(self)
        #wx.StaticText(self.panel,-1,"This is static text",(500,500))
        self.data = [0, 0, 1, 3, 5]
        self.names= ["Jesse", "Sebastiaan", "Jeroen", "Jolanda", "Dwin"]
        self.textbox = wx.TextCtrl(self.panel,pos=(100,430),size=(300,-1),style=wx.TE_PROCESS_ENTER)
        self.textbox.SetValue(' '.join(map(str, self.data)))
        #print self.textbox.GetValue()
        self.namebox = wx.TextCtrl(self.panel,pos=(100,480),size=(300,-1),style=wx.TE_PROCESS_ENTER)
        self.namebox.SetValue(' '.join(map(str, self.names)))
        #self.typebox = wx.Te
        self.Bind(wx.EVT_TEXT_ENTER, self.on_text_enter, self.namebox)
        self.Bind(wx.EVT_TEXT_ENTER, self.on_text_enter, self.textbox)
        self.radio1 = wx.RadioButton(self.panel, -1, " Radio 1 ",style = wx.RB_GROUP)
        self.radio2 = wx.RadioButton(self.panel, -1," Radio 2 ",style = wx.RB_GROUP)
        self.radio3 = wx.RadioButton(self.panel, -1," Radio 3",style = wx.RB_GROUP)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.radio1, 0, wx.ALL, 5)
        sizer.Add(self.radio2, 0, wx.ALL, 5)
        sizer.Add(self.radio3, 0, wx.ALL, 5)
        self.panel.SetSizer(sizer)
        button=wx.Button(self.panel,label="Draw",pos=(10,430))
        self.Bind(wx.EVT_BUTTON, self.on_draw_button, button)
        self.dpi = 100
        self.fig = Figure((5.0, 4.0), dpi=self.dpi)
        self.canvas = FigureCanvas(self.panel, -1, self.fig)
        self.axes = self.fig.add_subplot(111)

    def on_text_enter(self, event):
        self.draw_figure()

    def draw_figure(self):
        colors =["red","green","yellow","blue","purple","orange","brown","gray","white","black"]
        str = self.textbox.GetValue()
        str2 = self.namebox.GetValue()
        users = str2.split(" ")
        self.data = map(int, str.split())
        #print 'self.data', self.data
        #self.figure = matplotlib.figure.Figure((5.0, 4.0))
        #self.axes = self.figure.add_subplot(111)
        x = numpy.arange(len(self.data))
        y = self.data
        self.axes.clear()  
        for z in range(len(self.data)):
                self.axes.bar(z, self.data[z], width=0.35,
                                color=colors[z])
       
        width = 0.35
        #self.axes.bar(x,y,width=1.0,bottom=0,color='Green',alpha=0.65,label='Legend')

        self.axes.set_xlim(-width,len(self.data)+width)
        self.axes.set_ylim(0,(max(self.data)+1))
        self.axes.set_ylabel('Aantal keren gehaald')
        self.axes.set_title('Aantal keren gehaald per persoon')
        xTickMarks = users
        self.axes.set_xticks(x)
        xtickNames = self.axes.set_xticklabels(xTickMarks)
        plt.setp(xtickNames, rotation=45, fontsize=10)        
        self.canvas.draw()

    def on_draw_button(self, event):
        self.draw_figure()

if __name__ == "__main__":
    app=wx.App()
    frame=TestFrame(None,"First bargraph test")
    frame.Show()
    app.MainLoop()
