class Standings():

    def __init__(self,regId):
        self.regId = regId
        self.winTally = 0
        self.matchTally = 0
        self.lossTally = 0
        self.drawTally = 0

    def tallyWin():
    	self.winTally = self.winTally + 1
    	self.matchTally = self.matchTally + 1

    def tallyLoss():
    	self.lossTally = self.lossTally + 1
    	self.matchTally = self.matchTally + 1

    def tallyDraw():
    	self.drawTally = selfDrawTally + 1
    	self.matchTally = self.matchTally + 1
