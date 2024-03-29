import pylab
import numpy as np
import matplotlib.pyplot as plt
class Creation():
    def __init__(self, names, data, title):
        self.names = names
        self.data = data
        self.title = title
        #self.colors =["red","green","yellow","blue","purple","orange","brown","gray","white","black"]
        self.colors=['#2a1c0e','#472f17','#654321','#744d26',
                     '#83572b','#91602f','#a06a34','#af7439','#be7e3e']
    def getNames(self):
        return self.names
    def setNames(self, newnames):
        self.names = newnames
    def getData(self):
        return self.data
    def setData(self, newdata):
        self.data = newdata
    def getChartType(self):
        return self.chart_type
    def setChartType(self, newcharttype):
        self.chart_type = newcharttype
    def getTitle(self):
        return self.title
    def setTitle(self, newtitle):
        self.title = newtitle
    def buildPie(self):
        
        fig, ax = plt.subplots()
        ax.clear()
        fracs  = []
        total = sum(self.data)
        for entry in self.data:
            fracs.append(format(float(entry)/total*100,'.2f'))
        _, _, autotexts = plt.pie(fracs, labels=self.names, autopct='%1.1f%%', shadow=True, colors=self.colors)
        for autotext in autotexts:
            autotext.set_color('white')
        plt.title(self.title, bbox={'facecolor':'0.8', 'pad':5})
        plt.savefig("temp.png")
        plt.close(fig)
                                  
    def buildBar(self):
        width = 0.35
        
        x = np.arange(len(self.data))
        fig, ax = plt.subplots()
        ax.clear()
        #for x in range(len(self.names)):
        #    rects1 = ax.bar(x, self.data, width, color='r',)

        for z in range(len(self.data)):
            rect = ax.bar(z, self.data[z], width=0.35,
                            color=self.colors[z])
            self.autolabel(rect,ax)
        # add some text for labels, title and axes ticks
        ax.set_ylabel('Scores')
        ax.set_title('Scores by group and gender')
        ax.set_xticks(x)
        ax.set_xticklabels(self.names)
        ax.set_xlim(-width, len(self.data)+width)
        ax.set_ylim(0,(max(self.data)+3))
        ax.set_ylabel("Aantal keer")
        ax.set_xlabel("Persoon")
        xTickMarks = self.names
        xtickNames = ax.set_xticklabels(xTickMarks)
        plt.setp(xtickNames, rotation =45, fontsize=10)
        plt.title(self.title)
        plt.savefig("temp.png")
        plt.close(fig)
    def autolabel(self, rects, ax):
        # attach some text labels
        for rect in rects:
            height = rect.get_height()
            #print height, "HEIGHT"
            ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                    height,
                    ha='center', va='bottom')
            #print rect.get_x(),"X","\n"
            

