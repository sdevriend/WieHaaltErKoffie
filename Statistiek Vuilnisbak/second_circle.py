import wx
import pylab
class MyFrame(wx.Frame):
    """ Pie Chart Frame """
    def __init__(self):
        wx.Frame.__init__(self,None,-1)
        self.panel=wx.Panel(self,-1)
        '''
        """ Start Pie Chart Code"""
        # make a square figure and axes
        pylab.figure(1, figsize=(6,6))
        ax = pylab.axes([0.1, 0.1, 0.8, 0.8])
        image = wx.Bitmap("test.png")
         #show the image as static bitmap
        wx.StaticBitmap(self, wx.ID_ANY, image)
        perf_plot = 'test.png'
        self.Fit()
        """ End Pie Chart Code"""
        '''
        make_graph(("Jesse","Sebastiaan"),[45,65])
        
def make_graph(users, data):
    labels = "Jesse","Sebastiaan"
    ax = pylab.axes([0.1, 0.1, 0.8, 0.8])
    pylab.pie(data, labels=labels, autopct='%1.1f%%', shadow=True)
    pylab.title('Raining Hogs and Dogs', bbox={'facecolor':'0.8', 'pad':5})
    #plt.show()
    pylab.savefig("temp.png")



if __name__ == "__main__":
    app=wx.App()
    frame=MyFrame()
    app.MainLoop()
