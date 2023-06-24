class DataModel(object):
    magAvgList = []
    edaAvgList = []
    tempAvgList = []
    movementList = []
    stepsList = []
    restList = []
    wristList = []

    def __init__(self, magAvgList, edaAvgList, tempAvgList, 
                 movementList, stepsList, restList, wristList):
        self.magAvgList = magAvgList
        self.edaAvgList = edaAvgList
        self.tempAvgList = tempAvgList
        self.movementList = movementList
        self.stepsList = stepsList
        self.restList = restList
        self.wristList = wristList