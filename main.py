import tkinter as tk
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from tkcalendar import DateEntry
import statistics as st
import pandas as pd
from datetime import datetime
import numpy as np
import math

class DataModel:
    magAvgList = []
    edaAvgList = []
    tempAvgList = []
    movementList = []
    stepsList = []
    restList = []
    wristList = []
    dates = []

    def __init__(self):
        return None

test_model = DataModel()

class DataLoading:

    def __init__(self, subject, dateStart, dateEnd):
        self.subject = subject
        self.dateStart = dateStart
        self.dateEnd = dateEnd

    def get_data_frame(subject):
        if (subject == '310'):
            print('Reading 1st')
            sub_310_18 = pd.read_csv(r'https://raw.githubusercontent.com/ParkerHarpool/Data.Visualization/test-branch/csv-files/310-01-18.csv')
            print('Modifying 1st')
            sub_310_18 = sub_310_18[sub_310_18['Datetime (UTC)'] >= '2020-01-18T00:00:00Z']
            sub_310_18 = sub_310_18[sub_310_18['Datetime (UTC)'] <= '2020-01-18T23:59:00Z']

            print('Reading 2nd')
            sub_310_19 = pd.read_csv(r'https://raw.githubusercontent.com/ParkerHarpool/Data.Visualization/test-branch/csv-files/310-01-19.csv')
            sub_310_19 = sub_310_19[sub_310_19['Datetime (UTC)'] >= '2020-01-19T00:00:00Z']
            sub_310_19 = sub_310_19[sub_310_19['Datetime (UTC)'] <= '2020-01-19T23:59:00Z']

            print('Reading 3rd')
            sub_310_20 = pd.read_csv(r'https://raw.githubusercontent.com/ParkerHarpool/Data.Visualization/test-branch/csv-files/310-01-20.csv')
            sub_310_20 = sub_310_20[sub_310_20['Datetime (UTC)'] >= '2020-01-20T00:00:00Z']
            sub_310_20 = sub_310_20[sub_310_20['Datetime (UTC)'] <= '2020-01-20T23:59:00Z']

            print('Reading 4th')
            sub_310_21 = pd.read_csv(r'https://raw.githubusercontent.com/ParkerHarpool/Data.Visualization/test-branch/csv-files/310-01-21.csv')
            sub_310_21 = sub_310_21[sub_310_21['Datetime (UTC)'] >= '2020-01-21T00:00:00Z']
            sub_310_21 = sub_310_21[sub_310_21['Datetime (UTC)'] <= '2020-01-21T23:59:00Z']

            print('1st Merge')
            sub_310_1819 = pd.merge(sub_310_18, sub_310_19, how='outer')
            print('2nd Merge')
            sub_310_2021 = pd.merge(sub_310_20, sub_310_21, how='outer')
            print('Final Merge')
            sub_310 = pd.merge(sub_310_1819, sub_310_2021, how='outer')

            print(sub_310.head(5))
            print(sub_310.tail(5))

            return sub_310
        
        if (subject == '311'):
            sub_311_18 = pd.read_csv(r'https://raw.githubusercontent.com/ParkerHarpool/Data.Visualization/test-branch/csv-files/311-01-18.csv')
            sub_311_18 = sub_311_18[sub_311_18['Datetime (UTC)'] >= '2020-01-18T00:00:00Z']
            sub_311_18 = sub_311_18[sub_311_18['Datetime (UTC)'] <= '2020-01-18T23:59:00Z']

            sub_311_19 = pd.read_csv(r'https://raw.githubusercontent.com/ParkerHarpool/Data.Visualization/test-branch/csv-files/311-01-19.csv')
            sub_311_19 = sub_311_19[sub_311_19['Datetime (UTC)'] >= '2020-01-19T00:00:00Z']
            sub_311_19 = sub_311_19[sub_311_19['Datetime (UTC)'] <= '2020-01-19T23:59:00Z']

            sub_311 = pd.merge(sub_311_18, sub_311_19, how='outer')
            print(sub_311.head(5))
            print(sub_311.tail(5))

            return sub_311

        if (subject == '312'):
            print('Reading 1st')
            sub_312_18 = pd.read_csv(r'https://raw.githubusercontent.com/ParkerHarpool/Data.Visualization/main/data-pandas/312-01-18.csv')
            print('Modifying 1st')
            sub_312_18 = sub_312_18[sub_312_18['Datetime (UTC)'] >= '2020-01-18T00:00:00Z']
            sub_312_18 = sub_312_18[sub_312_18['Datetime (UTC)'] <= '2020-01-18T23:59:00Z']

            print('Reading 2nd')
            sub_312_19 = pd.read_csv(r'https://raw.githubusercontent.com/ParkerHarpool/Data.Visualization/main/data-pandas/312-01-19.csv')
            sub_312_19 = sub_312_19[sub_312_19['Datetime (UTC)'] >= '2020-01-19T00:00:00Z']
            sub_312_19 = sub_312_19[sub_312_19['Datetime (UTC)'] <= '2020-01-19T23:59:00Z']

            print('Reading 3rd')
            sub_312_20 = pd.read_csv(r'https://raw.githubusercontent.com/ParkerHarpool/Data.Visualization/main/data-pandas/312-01-20.csv')
            sub_312_20 = sub_312_20[sub_312_20['Datetime (UTC)'] >= '2020-01-20T00:00:00Z']
            sub_312_20 = sub_312_20[sub_312_20['Datetime (UTC)'] <= '2020-01-20T23:59:00Z']

            print('Reading 4th')
            sub_312_21 = pd.read_csv(r'https://raw.githubusercontent.com/ParkerHarpool/Data.Visualization/main/data-pandas/312-01-21.csv')
            sub_312_21 = sub_312_21[sub_312_21['Datetime (UTC)'] >= '2020-01-21T00:00:00Z']
            sub_312_21 = sub_312_21[sub_312_21['Datetime (UTC)'] <= '2020-01-21T23:59:00Z']

            print('1st Merge')
            sub_312_1819 = pd.merge(sub_312_18, sub_312_19, how='outer')
            print('2nd Merge')
            sub_312_2021 = pd.merge(sub_312_20, sub_312_21, how='outer')
            print('Final Merge')
            sub_312 = pd.merge(sub_312_1819, sub_312_2021, how='outer')

            print(sub_312.head(5))
            print(sub_312.tail(5))

            return sub_312

        if (subject == '311'):
            sub_311_18 = pd.read_csv(r'https://raw.githubusercontent.com/ParkerHarpool/Data.Visualization/main/data-pandas/311-01-18.csv')
            sub_311_18 = sub_311_18[sub_311_18['Datetime (UTC)'] >= '2020-01-18T00:00:00Z']
            sub_311_18 = sub_311_18[sub_311_18['Datetime (UTC)'] <= '2020-01-18T23:59:00Z']

            sub_311_19 = pd.read_csv(r'https://raw.githubusercontent.com/ParkerHarpool/Data.Visualization/main/data-pandas/311-01-19.csv')
            sub_311_19 = sub_311_19[sub_311_19['Datetime (UTC)'] >= '2020-01-19T00:00:00Z']
            sub_311_19 = sub_311_19[sub_311_19['Datetime (UTC)'] <= '2020-01-19T23:59:00Z']

            sub_311 = pd.merge(sub_311_18, sub_311_19, how='outer')
            print(sub_311.head(5))
            print(sub_311.tail(5))

            return sub_311

        if (subject == '312'):
            print('Reading 1st')
            sub_312_18 = pd.read_csv(r'https://raw.githubusercontent.com/ParkerHarpool/Data.Visualization/main/data-pandas/312-01-18.csv')
            print('Modifying 1st')
            sub_312_18 = sub_312_18[sub_312_18['Datetime (UTC)'] >= '2020-01-18T00:00:00Z']
            sub_312_18 = sub_312_18[sub_312_18['Datetime (UTC)'] <= '2020-01-18T23:59:00Z']

            print('Reading 2nd')
            sub_312_19 = pd.read_csv(r'https://raw.githubusercontent.com/ParkerHarpool/Data.Visualization/main/data-pandas/312-01-19.csv')
            sub_312_19 = sub_312_19[sub_312_19['Datetime (UTC)'] >= '2020-01-19T00:00:00Z']
            sub_312_19 = sub_312_19[sub_312_19['Datetime (UTC)'] <= '2020-01-19T23:59:00Z']

            print('Reading 3rd')
            sub_312_20 = pd.read_csv(r'https://raw.githubusercontent.com/ParkerHarpool/Data.Visualization/main/data-pandas/312-01-20.csv')
            sub_312_20 = sub_312_20[sub_312_20['Datetime (UTC)'] >= '2020-01-20T00:00:00Z']
            sub_312_20 = sub_312_20[sub_312_20['Datetime (UTC)'] <= '2020-01-20T23:59:00Z']

            print('Reading 4th')
            sub_312_21 = pd.read_csv(r'https://raw.githubusercontent.com/ParkerHarpool/Data.Visualization/main/data-pandas/312-01-21.csv')
            sub_312_21 = sub_312_21[sub_312_21['Datetime (UTC)'] >= '2020-01-21T00:00:00Z']
            sub_312_21 = sub_312_21[sub_312_21['Datetime (UTC)'] <= '2020-01-21T23:59:00Z']

            print('1st Merge')
            sub_312_1819 = pd.merge(sub_312_18, sub_312_19, how='outer')
            print('2nd Merge')
            sub_312_2021 = pd.merge(sub_312_20, sub_312_21, how='outer')
            print('Final Merge')
            sub_312 = pd.merge(sub_312_1819, sub_312_2021, how='outer')

            print(sub_312.head(5))
            print(sub_312.tail(5))

            return sub_312

    def load_data(subject, dateStart, dateStartTime, dateEnd, dateEndTime, magAvgCheck, 
                         edaAvgCheck, tempAvgCheck, movementCheck, 
                         stepsCheck, restCheck, wristCheck):
        df = DataLoading.get_data_frame(subject)

        time_data_start = dateStart + " " + dateStartTime
        time_data_end = dateEnd + " " + dateEndTime
        date_format = "%m/%d/%y %H:%M"

        start = datetime.strptime(time_data_start, date_format)
        end = datetime.strptime(time_data_end, date_format)

        startDate = start.strftime("%Y-%m-%dT%H:%M:%SZ")
        endDate = end.strftime("%Y-%m-%dT%H:%M:%SZ")

        print(startDate)
        print(endDate)

        dfStart = df[df['Datetime (UTC)'] >= startDate]
        dfEnd = df[df['Datetime (UTC)'] <= endDate]
        dfMerge = pd.merge(dfStart, dfEnd, how='inner')
        print(dfMerge.head(3))
        print(dfMerge.tail(3))

        model = DataModel()
        model.dates = list(dfMerge['Datetime (UTC)'])
        if (magAvgCheck):
            model.magAvgList = list(dfMerge['Acc magnitude avg'])
            #print(model.magAvgList)
        if (edaAvgCheck):
            model.edaAvgList = list(dfMerge['Eda avg'])
            #print(model.edaAvgList)
        if (tempAvgCheck):
            model.tempAvgList = list(dfMerge['Temp avg'])
            print(model.tempAvgList)
        if (movementCheck):
            model.movementList = list(dfMerge['Movement intensity'])
            print(model.movementList)
        if (stepsCheck):
            model.stepsList = list(dfMerge['Steps count'])
            print(model.stepsList)
        if (restCheck):
            model.restList = list(dfMerge['Rest'])
            print(model.restList)
        if (wristCheck):
            model.wristList = list(dfMerge['On Wrist'])
            print(model.wristList)
        
        print(len(model.magAvgList))
        return model

class TimeCombobox(ttk.Combobox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self['values'] = [f"{str(hour).zfill(2)}:{str(minute).zfill(2)}" for hour in range(24) for minute in range(0, 60, 15)]
        self.current(0)

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
    def calculateFloat(dataList):
        dataList = dataList

        points = len(dataList)
        maxValue = max(dataList)
        minValue = min(dataList)
        mean = sum(dataList)/len(dataList)
        median = st.median(dataList)
        sd = st.stdev(dataList)

        return Statistics(points, mean, sd, minValue, maxValue, median)

    #calculateInt method that allows a dataList and a type to be passed into it
    #def calculateInt(self, dataList, type):

magAvg = Statistics(2,1,1,1,1,1)
edaAvg = Statistics(1,1,1,1,1,1)
tempAvg = Statistics(1,1,1,1,1,1)
movement = Statistics(1,1,1,1,1,1)
steps = Statistics(1,1,1,1,1,1)
rest = Statistics(1,1,1,1,1,1)

def createStats():
    global magAvg
    global edaAvg
    global tempAvg
    global movement
    global steps
    global rest

    magAvg = Statistics.calculateFloat(test_model.magAvgList)
    edaAvg = Statistics.calculateFloat(test_model.edaAvgList)
    tempAvg = Statistics.calculateFloat(test_model.tempAvgList)
    movement = Statistics.calculateFloat(test_model.movementList)
    steps = Statistics.calculateFloat(test_model.stepsList)
    rest = Statistics.calculateFloat(test_model.restList)

stepsGraph = [200, 150, 321, 723, 632, 100, 180, 132, 123, 502]
dates = ["Jan 1st, 2023", "Jan 2nd, 2023", "Jan 3rd, 2023", "Jan 4th, 2023", 
         "Jan 5th, 2023", "Jan 6th, 2023", "Jan 7th, 2023", "Jan 8th, 2023",
           "Jan 9th, 2023", "Jan 10th, 2023"]


#The graph label font doesnt want to change, so the graph should be viewed
#in the maximized frame to allow the view of the xLabels.
def createGraph():
        global test_model

        plt.subplot(311)
        plt.plot(test_model.dates, test_model.magAvgList, color=(0.2, 0.4, 0.6, 0.6))
        ticks = np.arange(0, len(test_model.dates)-1, math.floor(len(test_model.dates)*.24))
        ticksValues = [test_model.dates[ticks[0]], test_model.dates[ticks[1]],
                  test_model.dates[ticks[2]], test_model.dates[ticks[3]], test_model.dates[ticks[4]]]
        labels: list = []
        for x in ticksValues:
            date_format = "%Y-%m-%dT%H:%M:%SZ"

            y = datetime.strptime(x, date_format)
            z = y.strftime("Jan %d, %H:%M")
            labels.append(z)
            
        plt.xticks(ticks, labels)
        plt.title('Mag Avg')

        plt.subplot(312)
        plt.plot(test_model.dates, test_model.edaAvgList, color=(0.2, 0.4, 0.6, 0.6))
        ticks = np.arange(0, len(test_model.dates)-1, math.floor(len(test_model.dates)*.24))
        ticksValues = [test_model.dates[ticks[0]], test_model.dates[ticks[1]],
                  test_model.dates[ticks[2]], test_model.dates[ticks[3]], test_model.dates[ticks[4]]]
        labels: list = []
        for x in ticksValues:
            date_format = "%Y-%m-%dT%H:%M:%SZ"

            y = datetime.strptime(x, date_format)
            z = y.strftime("Jan %d, %H:%M")
            labels.append(z)

        plt.xticks(ticks, labels)
        plt.title('EDA Avg')

        plt.subplot(313)
        plt.plot(test_model.dates, test_model.tempAvgList, color=(0.2, 0.4, 0.6, 0.6))
        ticks = np.arange(0, len(test_model.dates)-1, math.floor(len(test_model.dates)*.24))
        ticksValues = [test_model.dates[ticks[0]], test_model.dates[ticks[1]],
                  test_model.dates[ticks[2]], test_model.dates[ticks[3]], test_model.dates[ticks[4]]]
        labels: list = []
        for x in ticksValues:
            date_format = "%Y-%m-%dT%H:%M:%SZ"

            y = datetime.strptime(x, date_format)
            z = y.strftime("Jan %d, %H:%M")
            labels.append(z)

        plt.xticks(ticks, labels)
        plt.title('Temp Avg')

        plt.subplots_adjust(hspace=0.5)
    
        plt.show()

root = Tk()
root.geometry("1000x1000")

data_loader = Frame(root)
data_loader.pack()

stats_frame = Frame(root)
stats_frame.pack(side = BOTTOM)

graphs = Frame(root)
graphs.pack()

data_loader.participant_var = tk.StringVar()
data_loader.start_date_var = tk.StringVar()
data_loader.end_date_var = tk.StringVar()

ttk.Label(data_loader, text="Participant:").grid(column=0, row=0, padx=20, pady=10)
data_loader.participant_combobox = ttk.Combobox(data_loader, textvariable=data_loader.participant_var)
data_loader.participant_combobox['values'] = ['310','311','312']
data_loader.participant_combobox.grid(column=1, row=0, sticky='w')

ttk.Label(data_loader, text="Start Date:").grid(column=0, row=1, padx=20, pady=10)
data_loader.start_date_entry = DateEntry(data_loader, textvariable=data_loader.start_date_var)
data_loader.start_date_entry.grid(column=1, row=1, sticky='w')

ttk.Label(data_loader, text="Start Time:").grid(column=0, row=2, padx=20, pady=10)
data_loader.start_time_entry = TimeCombobox(data_loader)
data_loader.start_time_entry.grid(column=1, row=2, sticky='w')

ttk.Label(data_loader, text="End Date:").grid(column=0, row=3, padx=20, pady=10)
data_loader.end_date_entry = DateEntry(data_loader, textvariable=data_loader.end_date_var)
data_loader.end_date_entry.grid(column=1, row=3, sticky='w')

ttk.Label(data_loader, text="End Time:").grid(column=0, row=4, padx=20, pady=10)
data_loader.end_time_entry = TimeCombobox(data_loader)
data_loader.end_time_entry.grid(column=1, row=4, sticky='w')

data_loader.confirm_button = ttk.Button(data_loader, text="Confirm", command=lambda: confirm())
data_loader.confirm_button.grid(column=1, row=5, pady=20)

def confirm():
        global test_model
        participant = data_loader.participant_var.get()
        start_date = data_loader.start_date_var.get()
        start_time = data_loader.start_time_entry.get()
        end_date = data_loader.end_date_var.get()
        end_time = data_loader.end_time_entry.get()

        # Perform additional validations as needed
        print({
            "participant": participant,
            "start_date": start_date,
            "start_time": start_time,
            "end_date": end_date,
            "end_time": end_time
        })
        test_model = DataLoading.load_data(participant, start_date, start_time, end_date,  
                                        end_time, 1,1,1,1,1,1,1)
        createStats()   
        

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

def updateStats():
    chart.delete(*chart.get_children())
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

    root.after(1000, updateStats)

chart.pack()

b = Button(graphs, text="Create Graph", command=lambda: createGraph())
b.pack()

root.after(1000, updateStats)
root.mainloop()