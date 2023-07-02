#importing tkinter
from tkinter import *

#creating the Statistics class
from tkinter import ttk

import matplotlib.pyplot as plt

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
    def calculateFloat(self, dataList, type):
        self.dataList = dataList
        self.type = type

    #calculateInt method that allows a dataList and a type to be passed into it
    #def calculateInt(self, dataList, type):

#creating the StatisticsList class
class StatisticsList:

    #creating Statistics objects for each needed variable
    #passing in dummy data for each object's respective points, mean, sd, min, max and median values
    magAvg = Statistics(1,1,1,1,1,1)
    edaAvg = Statistics(2,2,2,2,2,2)
    tempAvg = Statistics(3,3,3,3,3,3)
    movement = Statistics(4,4,4,4,4,4)
    steps = Statistics(5,5,5,5,5,5)
    rest = Statistics(6,6,6,6,6,6)

    #calculateStats method that allows a dataModel to be passed into it
    def calculateStats(self, dataModel):
        self.dataModel = dataModel


magAvg = Statistics(1,1,1,1,1,1)
edaAvg = Statistics(2,2,2,2,2,2)
tempAvg = Statistics(3,3,3,3,3,3)
movement = Statistics(4,4,4,4,4,4)
steps = Statistics(5,5,5,5,5,5)
rest = Statistics(6,6,6,6,6,6)

stepsGraph = [200, 150, 321, 723, 632, 100, 180, 132, 123, 502]
dates = ["Jan 1st, 2023", "Jan 2nd, 2023", "Jan 3rd, 2023", "Jan 4th, 2023", 
         "Jan 5th, 2023", "Jan 6th, 2023", "Jan 7th, 2023", "Jan 8th, 2023",
           "Jan 9th, 2023", "Jan 10th, 2023"]


#The graph label font doesnt want to change, so the graph should be viewed
#in the maximized frame to allow the view of the xLabels.
def createGraph(varX, varY, xLabel, yLabel, type):
    if(type == "Bar"):
        plt.bar(varX, varY, color=(0.2, 0.4, 0.6, 0.6))
    elif(type == "Line"):
        plt.subplot(varX, varY, color=(0.2, 0.4, 0.6, 0.6))
        plt.subplot(varX, varY, color=(0.2, 0.4, 0.6, 0.6))
    
    plt.title(type+ ' Graph')
    plt.xlabel(xLabel, fontsize=1)
    plt.ylabel(yLabel)
    plt.show()

root = Tk()
root.geometry("1000x1000")

stats_frame = Frame(root)
stats_frame.pack(side = BOTTOM)

graphs = Frame(root)
graphs.pack(side = RIGHT)

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

b = Button(graphs, text="Create Graph", command=lambda: createGraph(dates, stepsGraph, "Date", "Steps", "Line"))
b.pack()

root.mainloop()