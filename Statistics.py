#importing tkinter
from tkinter import *

#creating the Statistics class
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

    #calculateInt method that allows a dataList and a type to be passed into it
    def calculateInt(self, dataList, type):

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

    #trying to create the table that the Statistic data will be viewed in
    def __init__(self):
        for i in range(total_rows):
            for j in range(columns):
                self.e = Entry(root, width =30, fg = 'white',
                               font=('Times',18,'Normal'))
                self.e.grid(row=i, column=j)
                self.e.insert(END, list[i][j])


#trying to add the StatisticList variables to a list
list = [('magAvg', 1, 1, 1, 1, 1, 1),
       ('edaAvg', 2, 2, 2, 2, 2, 2),
       ('tempAvg', 3, 3, 3, 3, 3, 3),
       ('movement', 4, 4, 4, 4, 4, 4),
       ('steps', 5, 5, 5, 5, 5, 5,),
       ('rest', 6, 6, 6, 6, 6, 6,)]

total_rows = len(list)
columns = len(list[0])

root = Tk()
t = StatisticsList(root)
root.mainloop()