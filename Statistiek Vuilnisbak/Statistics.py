class Statistics():
    def __init__(self, stat):
        self.stat = "self."+str(stat)+"()"
        print self.stat
        eval(self.stat)
    def Test(self):
        print "testertje"
statistiek = Statistics("Test")
