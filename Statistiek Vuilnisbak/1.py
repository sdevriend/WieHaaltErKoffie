import pylab
import numpy as np
import matplotlib.pyplot as plt
class Creation():
    def __init__(self, chart_type, names, data, title):
        self.chart_type = chart_type
        self.names = names
        self.data = data
        self.title = title
        self.colors =["red","green","yellow","blue","purple","orange","brown","gray","white","black"]
            
    def build(self):
        if self.chart_type == "circle":
            fracs  = []
            total = sum(self.data)
            for entry in self.data:
                fracs.append(format(float(entry)/total*100,'.2f'))
            pylab.pie(fracs, labels=self.names, autopct='%1.1f%%', shadow=True)
            pylab.title(self.title, bbox={'facecolor':'0.8', 'pad':5})
            pylab.savefig("temp2.png")

        elif self.chart_type == "bar":
            width = 0.35
          
            x = np.arange(len(self.data))
            fig, ax = plt.subplots()
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
            ax.set_ylim(0,(max(self.data)+1))
            ax.set_ylabel('title')
            ax.set_xlabel(self.title)
            xTickMarks = self.names
            xtickNames = ax.set_xticklabels(xTickMarks)
            plt.setp(xtickNames, rotation =45, fontsize=10)
            
            plt.savefig("foo2.png")
    def autolabel(self, rects, ax):
        # attach some text labels
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                    '%d' % int(height),
                    ha='center', va='bottom')
            
creator = Creation("bar", ['John','Peter','James'], [1,2,3], "Hoe vaak haalt wie koffie?")
creator.build()

