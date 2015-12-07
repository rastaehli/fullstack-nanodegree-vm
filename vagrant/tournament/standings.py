class Standings():

    def __init__(self,regId, name):
        self.regId = regId
        self.name = name
        self.winTally = 0
        self.matchTally = 0
        self.lossTally = 0
        self.drawTally = 0

    def tallyWin(self):
    	self.winTally = self.winTally + 1
    	self.matchTally = self.matchTally + 1

    def tallyLoss(self):
    	self.lossTally = self.lossTally + 1
    	self.matchTally = self.matchTally + 1

    def tallyDraw(self):
    	self.drawTally = selfDrawTally + 1
    	self.matchTally = self.matchTally + 1
