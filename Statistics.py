#importing tkinter
from tkinter import *

#creating the Statistics class
from tkinter import ttk


class Statistics:

    #creating constructor for Statistics class
    #allows for points, mean, sd, min, max, and median values to be assigned
    def __init__(self, points, mean, sd, min, max, median):
        self.points = points
        self.mean = mean
        self.sd = sd
        self.min = min
        self.max = max
        self.median = median


#calculateFloat method that allows a dataList and a type to be passed into it
def calculateFloat(dataList, type):
        value = 0.0
        if type == 'mean':
            for entry in dataList:
                sum = sum + entry
            value = sum/dataList.__sizeof__()
        if type == 'sd':
            for entry in dataList:
                sum = sum + entry
            avg = sum/dataList.__sizeof__
            for entry in dataList:
                sub = (entry-avg) ** 2
                subSum = sub + subSum
            div = subSum/(dataList.__sizeof__ - 1)
            sd = div ** 0.5
            value = sd
        if type == 'min':
            value = dataList.min
        if type == 'max':
            value = dataList.max
        if type == 'median':
            dataList.sort
            point = dataList.__sizeof__/2
            value = dataList(point)
        else:
            print("Invalid type")
        return value

dataList = (1,2,3,4,5,6)
calculateFloat(dataList, min)
#calculateInt method that allows a dataList and a type to be passed into it
def calculateInt(dataList, type):
    value = 0
    if type == 'points':
        value = dataList.__sizeof__
    else:
        print("Invalid type")
    return value


#creating the StatisticsList class
class StatisticsList:

    #creating Statistics objects for each needed variable
    #passing in dummy data for each object's respective points, mean, sd, min, max and median values
    magAvg = Statistics(1.044551,0.9662190,1.053038,1.078198,1.078063,1.079643)
    edaAvg = Statistics(0.568742,0.857908,1.103204,1.221607,1.355337,1.598131)
    tempAvg = Statistics(28.112500,28.254328,28.992183,29.232367,29.4212,29.588217)
    movement = Statistics(0,0,0,17,20,53)
    steps = Statistics(0,0,0,47,0,0)
    rest = Statistics(0,0,0,0,0,0)

    #calculateStats method that allows a dataModel to be passed into it
    def calculateStats(self, dataModel):
        self.dataModel = dataModel


magAvg = Statistics(1.044551,0.9662190,1.053038,1.078198,1.078063,1.079643)
edaAvg = Statistics(0.568742,0.857908,1.103204,1.221607,1.355337,1.598131)
tempAvg = Statistics(28.112500,28.254328,28.992183,29.232367,29.4212,29.588217)
movement = Statistics(0,0,0,17,20,53)
steps = Statistics(0,0,0,47,0,0)
rest = Statistics(0,0,0,0,0,0)

ws = Tk()
ws.title('Data Statistics')
ws.geometry('650x180')
ws['bg'] = '#FFFFFF'

stats_frame = Frame(ws)
stats_frame.pack()

chart = ttk.Treeview(stats_frame)

chart['columns'] = ('Acc magnitude avg', 'Eda avg', 'Temp avg', 'Movement',
                    'Steps', 'Rest')

chart.column("#0", width = 0, stretch = NO)
chart.column("Acc magnitude avg", anchor = CENTER, width = 100)
chart.column("Eda avg", anchor = CENTER, width = 100)
chart.column("Temp avg", anchor = CENTER, width = 100)
chart.column("Movement", anchor = CENTER, width = 100)
chart.column("Steps", anchor = CENTER, width = 100)
chart.column("Rest", anchor = CENTER, width = 100)

chart.heading("#0", text = "", anchor = CENTER)
chart.heading("Acc magnitude avg", text = "Acc magnitude avg", anchor = CENTER)
chart.heading("Eda avg", text = "Eda avg", anchor = CENTER)
chart.heading("Temp avg", text = "Temp avg", anchor = CENTER)
chart.heading("Movement", text = "Movement", anchor = CENTER)
chart.heading("Steps", text = "Steps", anchor = CENTER)
chart.heading("Rest", text = "Rest", anchor = CENTER)

chart.insert(parent = '', index = 'end', iid = 0, text = '',
             values = (magAvg.points, edaAvg.points, tempAvg.points,
                       movement.points, steps.points, rest.points))
chart.insert(parent = '', index = 'end', iid = 1, text = '',
             values = (magAvg.mean, edaAvg.mean, tempAvg.mean,
                       movement.mean, steps.mean, rest.mean))
chart.insert(parent = '', index = 'end', iid = 2, text = '',
             values = (magAvg.sd, edaAvg.sd, tempAvg.sd,
                       movement.sd, steps.sd, rest.sd))
chart.insert(parent = '', index = 'end', iid = 3, text = '',
             values = (magAvg.min, edaAvg.min, tempAvg.min,
                       movement.min, steps.min, rest.min))
chart.insert(parent = '', index = 'end', iid = 4, text = '',
             values = (magAvg.max, edaAvg.max, tempAvg.max,
                       movement.max, steps.max, rest.max))
chart.insert(parent = '', index = 'end', iid = 5, text = '',
             values = (magAvg.median, edaAvg.median, tempAvg.median,
                       movement.median, steps.median, rest.median))

chart.pack()

ws.mainloop()

