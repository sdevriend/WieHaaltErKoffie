import wx
import pylab
from creation import Creation
class MyFrame(wx.Frame):
    """ Pie Chart Frame """
    def __init__(self):
        self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
        wx.Frame.__init__(self,None,-1)
        self.panel=wx.Panel(self,-1)
        """ Start Pie Chart Code"""
        # make a square figure and axes
        pylab.figure(1, figsize=(6,6))
        ax = pylab.axes([0.1, 0.1, 0.8, 0.8])
        names = ["Peter","John","James"]
        data = [12,15,8]
        title = "Are feet real?"
        circle = Creation("circle",names, data, title)
        circle.build()
        bar = Creation("bar", names, data, title)
        bar.build()
        # create an internal image
        image = wx.Bitmap("temp2.png")
        # show the image as static bitmap
        wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap("temp2.png"))
        perf_plot = 'temp2.png'
        self.Fit()
        """ End Pie Chart Code"""

            
class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True
app = MyApp(redirect=False)
app.MainLoop()
app.Destroy()
