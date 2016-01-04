import wx
import pylab
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
        labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
        fracs = [15,30,45, 10]
        explode=(0, 0.05, 0, 0)
        pylab.pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
        pylab.title('Raining Hogs and Dogs', bbox={'facecolor':'0.8', 'pad':5})
        #plt.show()
        pylab.savefig("test.png")
        # create an internal image
        image = wx.Bitmap("test.png")
        # show the image as static bitmap
        wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap("test.png"))
        perf_plot = 'test.png'
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
