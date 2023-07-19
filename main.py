import tkinter as tk
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from tkcalendar import DateEntry
import statistics as st
import pandas as pd
from datetime import datetime, timedelta
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
    localDates = []

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
            sub_310_18 = pd.read_csv("310-01-18.csv")
            print('Modifying 1st')
            sub_310_18 = sub_310_18[sub_310_18['Datetime (UTC)'] >= '2020-01-18T00:00:00Z']
            sub_310_18 = sub_310_18[sub_310_18['Datetime (UTC)'] <= '2020-01-18T23:59:00Z']

            print('Reading 2nd')
            sub_310_19 = pd.read_csv("310-01-19.csv")
            sub_310_19 = sub_310_19[sub_310_19['Datetime (UTC)'] >= '2020-01-19T00:00:00Z']
            sub_310_19 = sub_310_19[sub_310_19['Datetime (UTC)'] <= '2020-01-19T23:59:00Z']

            print('Reading 3rd')
            sub_310_20 = pd.read_csv("310-01-20.csv")
            sub_310_20 = sub_310_20[sub_310_20['Datetime (UTC)'] >= '2020-01-20T00:00:00Z']
            sub_310_20 = sub_310_20[sub_310_20['Datetime (UTC)'] <= '2020-01-20T23:59:00Z']

            print('Reading 4th')
            sub_310_21 = pd.read_csv("310-01-21.csv")
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
            sub_311_18 = pd.read_csv("311-01-18.csv")
            sub_311_18 = sub_311_18[sub_311_18['Datetime (UTC)'] >= '2020-01-18T00:00:00Z']
            sub_311_18 = sub_311_18[sub_311_18['Datetime (UTC)'] <= '2020-01-18T23:59:00Z']

            sub_311_19 = pd.read_csv("311-01-19.csv")
            sub_311_19 = sub_311_19[sub_311_19['Datetime (UTC)'] >= '2020-01-19T00:00:00Z']
            sub_311_19 = sub_311_19[sub_311_19['Datetime (UTC)'] <= '2020-01-19T23:59:00Z']

            sub_311 = pd.merge(sub_311_18, sub_311_19, how='outer')
            print(sub_311.head(5))
            print(sub_311.tail(5))

            return sub_311

        if (subject == '312'):
            print('Reading 1st')
            sub_312_18 = pd.read_csv("312-01-18.csv")
            print('Modifying 1st')
            sub_312_18 = sub_312_18[sub_312_18['Datetime (UTC)'] >= '2020-01-18T00:00:00Z']
            sub_312_18 = sub_312_18[sub_312_18['Datetime (UTC)'] <= '2020-01-18T23:59:00Z']

            print('Reading 2nd')
            sub_312_19 = pd.read_csv("312-01-19.csv")
            sub_312_19 = sub_312_19[sub_312_19['Datetime (UTC)'] >= '2020-01-19T00:00:00Z']
            sub_312_19 = sub_312_19[sub_312_19['Datetime (UTC)'] <= '2020-01-19T23:59:00Z']

            print('Reading 3rd')
            sub_312_20 = pd.read_csv("312-01-20.csv")
            sub_312_20 = sub_312_20[sub_312_20['Datetime (UTC)'] >= '2020-01-20T00:00:00Z']
            sub_312_20 = sub_312_20[sub_312_20['Datetime (UTC)'] <= '2020-01-20T23:59:00Z']

            print('Reading 4th')
            sub_312_21 = pd.read_csv("312-01-21.csv")
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
        model.localDates = []
        for date in model.dates:
             utcDate = datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
             estDate = utcDate - timedelta(hours=5, minutes=0)
             finalDate = estDate.strftime("%Y-%m-%dT%H:%M:%SZ")
             model.localDates.append(finalDate)
        print(model.localDates)

        if (magAvgCheck == '1'):
            model.magAvgList = list(dfMerge['Acc magnitude avg'])
            print(model.magAvgList)
        if (edaAvgCheck == '1'):
            model.edaAvgList = list(dfMerge['Eda avg'])
            print(model.edaAvgList)
        if (tempAvgCheck == '1'):
            model.tempAvgList = list(dfMerge['Temp avg'])
            print(model.tempAvgList)
        if (movementCheck == '1'):
            model.movementList = list(dfMerge['Movement intensity'])
            print(model.movementList)
        if (stepsCheck == '1'):
            model.stepsList = list(dfMerge['Steps count'])
            print(model.stepsList)
        if (restCheck == '1'):
            model.restList = list(dfMerge['Rest'])
            print(model.restList)
        if (wristCheck == '1'):
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

magAvg = Statistics(0,0,0,0,0,0)
edaAvg = Statistics(0,0,0,0,0,0)
tempAvg = Statistics(0,0,0,0,0,0)
movement = Statistics(0,0,0,0,0,0)
steps = Statistics(0,0,0,0,0,0)
rest = Statistics(0,0,0,0,0,0)

def createStats():
    global magAvg
    global edaAvg
    global tempAvg
    global movement
    global steps
    global rest

    magAvg = Statistics(0,0,0,0,0,0)
    edaAvg = Statistics(0,0,0,0,0,0)
    tempAvg = Statistics(0,0,0,0,0,0)
    movement = Statistics(0,0,0,0,0,0)
    steps = Statistics(0,0,0,0,0,0)
    rest = Statistics(0,0,0,0,0,0)

    if (test_model.magAvgList):
        magAvg = Statistics.calculateFloat(test_model.magAvgList)
    if (test_model.edaAvgList):
        edaAvg = Statistics.calculateFloat(test_model.edaAvgList)
    if (test_model.tempAvgList):
        tempAvg = Statistics.calculateFloat(test_model.tempAvgList)
    if (test_model.movementList):
        movement = Statistics.calculateFloat(test_model.movementList)
    if (test_model.stepsList):
        steps = Statistics.calculateFloat(test_model.stepsList)
    if (test_model.restList):
        rest = Statistics.calculateFloat(test_model.restList)

#The graph label font doesnt want to change, so the graph should be viewed
#in the maximized frame to allow the view of the xLabels.
def createGraph():
        global test_model
        dates: list
        i: int = 1
        localTime = checkboxes.checkbox_vars[7].get()

        if (localTime == '1'):
             dates = test_model.localDates
        else:
             dates = test_model.dates

        if (len(test_model.magAvgList) > 0):
                plt.figure(i)
                i += 1

                if (graph_choice.checkbox_vars[0].get() == '1'):
                    plt.bar(dates, test_model.magAvgList, color=(0.2, 0.4, 0.6, 0.6))
                else:
                    plt.plot(dates, test_model.magAvgList, color=(0.2, 0.4, 0.6, 0.6))

                ticks = np.arange(0, len(dates)-1, math.floor(len(dates)*.05))
                ticksValues = [dates[ticks[0]], dates[ticks[1]],
                        dates[ticks[2]], dates[ticks[3]], dates[ticks[4]], dates[ticks[5]],
                        dates[ticks[6]], dates[ticks[7]], dates[ticks[8]], dates[ticks[9]],
                        dates[ticks[10]], dates[ticks[11]], dates[ticks[12]], dates[ticks[13]],
                        dates[ticks[14]], dates[ticks[15]], dates[ticks[16]], dates[ticks[17]],
                        dates[ticks[18]], dates[ticks[19]], dates[ticks[20]]]
                labels: list = []
                for x in ticksValues:
                    date_format = "%Y-%m-%dT%H:%M:%SZ"

                    y = datetime.strptime(x, date_format)
                    z = y.strftime("Jan %d, %H:%M")
                    labels.append(z)
                    
                plt.xticks(ticks, labels, rotation=60, ha='right')
                plt.tight_layout()
                plt.title('Mag Avg')

        if (len(test_model.edaAvgList) > 0):
                plt.figure(i)
                i += 1

                if (graph_choice.checkbox_vars[1].get() == '1'):
                    plt.bar(dates, test_model.edaAvgList, color=(0.2, 0.4, 0.6, 0.6))
                else:
                    plt.plot(dates, test_model.edaAvgList, color=(0.2, 0.4, 0.6, 0.6))

                ticks = np.arange(0, len(dates)-1, math.floor(len(dates)*.05))
                ticksValues = [dates[ticks[0]], dates[ticks[1]],
                        dates[ticks[2]], dates[ticks[3]], dates[ticks[4]], dates[ticks[5]],
                        dates[ticks[6]], dates[ticks[7]], dates[ticks[8]], dates[ticks[9]],
                        dates[ticks[10]], dates[ticks[11]], dates[ticks[12]], dates[ticks[13]],
                        dates[ticks[14]], dates[ticks[15]], dates[ticks[16]], dates[ticks[17]],
                        dates[ticks[18]], dates[ticks[19]], dates[ticks[20]]]
                labels: list = []
                for x in ticksValues:
                    date_format = "%Y-%m-%dT%H:%M:%SZ"

                    y = datetime.strptime(x, date_format)
                    z = y.strftime("Jan %d, %H:%M")
                    labels.append(z)

                plt.xticks(ticks, labels, rotation=60, ha='right')
                plt.tight_layout()
                plt.title('EDA Avg')

        if (len(test_model.tempAvgList) > 0):
                plt.figure(i)
                i += 1
                
                if (graph_choice.checkbox_vars[2].get() == '1'):
                    plt.bar(dates, test_model.tempAvgList, color=(0.2, 0.4, 0.6, 0.6))
                else:
                    plt.plot(dates, test_model.tempAvgList, color=(0.2, 0.4, 0.6, 0.6))

                ticks = np.arange(0, len(dates)-1, math.floor(len(dates)*.05))
                ticksValues = [dates[ticks[0]], dates[ticks[1]],
                        dates[ticks[2]], dates[ticks[3]], dates[ticks[4]], dates[ticks[5]],
                        dates[ticks[6]], dates[ticks[7]], dates[ticks[8]], dates[ticks[9]],
                        dates[ticks[10]], dates[ticks[11]], dates[ticks[12]], dates[ticks[13]],
                        dates[ticks[14]], dates[ticks[15]], dates[ticks[16]], dates[ticks[17]],
                        dates[ticks[18]], dates[ticks[19]], dates[ticks[20]]]
                labels: list = []
                for x in ticksValues:
                    date_format = "%Y-%m-%dT%H:%M:%SZ"

                    y = datetime.strptime(x, date_format)
                    z = y.strftime("Jan %d, %H:%M")
                    labels.append(z)

                plt.xticks(ticks, labels, rotation=60, ha='right')
                plt.tight_layout()
                plt.title('Temp Avg')

        if (len(test_model.movementList) > 0):
                plt.figure(i)
                i += 1
                
                if (graph_choice.checkbox_vars[3].get() == '1'):
                    plt.bar(dates, test_model.movementList, color=(0.2, 0.4, 0.6, 0.6))
                else:
                    plt.plot(dates, test_model.movementList, color=(0.2, 0.4, 0.6, 0.6))

                ticks = np.arange(0, len(dates)-1, math.floor(len(dates)*.05))
                ticksValues = [dates[ticks[0]], dates[ticks[1]],
                        dates[ticks[2]], dates[ticks[3]], dates[ticks[4]], dates[ticks[5]],
                        dates[ticks[6]], dates[ticks[7]], dates[ticks[8]], dates[ticks[9]],
                        dates[ticks[10]], dates[ticks[11]], dates[ticks[12]], dates[ticks[13]],
                        dates[ticks[14]], dates[ticks[15]], dates[ticks[16]], dates[ticks[17]],
                        dates[ticks[18]], dates[ticks[19]], dates[ticks[20]]]
                labels: list = []
                for x in ticksValues:
                    date_format = "%Y-%m-%dT%H:%M:%SZ"

                    y = datetime.strptime(x, date_format)
                    z = y.strftime("Jan %d, %H:%M")
                    labels.append(z)

                plt.xticks(ticks, labels, rotation=60, ha='right')
                plt.tight_layout()
                plt.title('Movement Intensity')

        if (len(test_model.stepsList) > 0):
                plt.figure(i)
                i += 1
                
                if (graph_choice.checkbox_vars[4].get() == '1'):
                    plt.bar(dates, test_model.stepsList, color=(0.2, 0.4, 0.6, 0.6))
                else:
                    plt.plot(dates, test_model.stepsList, color=(0.2, 0.4, 0.6, 0.6))

                ticks = np.arange(0, len(dates)-1, math.floor(len(dates)*.05))
                ticksValues = [dates[ticks[0]], dates[ticks[1]],
                        dates[ticks[2]], dates[ticks[3]], dates[ticks[4]], dates[ticks[5]],
                        dates[ticks[6]], dates[ticks[7]], dates[ticks[8]], dates[ticks[9]],
                        dates[ticks[10]], dates[ticks[11]], dates[ticks[12]], dates[ticks[13]],
                        dates[ticks[14]], dates[ticks[15]], dates[ticks[16]], dates[ticks[17]],
                        dates[ticks[18]], dates[ticks[19]], dates[ticks[20]]]
                labels: list = []
                for x in ticksValues:
                    date_format = "%Y-%m-%dT%H:%M:%SZ"

                    y = datetime.strptime(x, date_format)
                    z = y.strftime("Jan %d, %H:%M")
                    labels.append(z)

                plt.xticks(ticks, labels, rotation=60, ha='right')
                plt.tight_layout()
                plt.title('Steps Count')

        if (len(test_model.restList) > 0):
                plt.figure(i)
                i += 1
                
                if (graph_choice.checkbox_vars[5].get() == '1'):
                    plt.bar(dates, test_model.restList, color=(0.2, 0.4, 0.6, 0.6))
                else:
                    plt.plot(dates, test_model.restList, color=(0.2, 0.4, 0.6, 0.6))

                ticks = np.arange(0, len(dates)-1, math.floor(len(dates)*.05))
                ticksValues = [dates[ticks[0]], dates[ticks[1]],
                        dates[ticks[2]], dates[ticks[3]], dates[ticks[4]], dates[ticks[5]],
                        dates[ticks[6]], dates[ticks[7]], dates[ticks[8]], dates[ticks[9]],
                        dates[ticks[10]], dates[ticks[11]], dates[ticks[12]], dates[ticks[13]],
                        dates[ticks[14]], dates[ticks[15]], dates[ticks[16]], dates[ticks[17]],
                        dates[ticks[18]], dates[ticks[19]], dates[ticks[20]]]
                labels: list = []
                for x in ticksValues:
                    date_format = "%Y-%m-%dT%H:%M:%SZ"

                    y = datetime.strptime(x, date_format)
                    z = y.strftime("Jan %d, %H:%M")
                    labels.append(z)

                plt.xticks(ticks, labels, rotation=60, ha='right')
                plt.tight_layout()
                plt.title('Rest')

        if (len(test_model.wristList) > 0):
                plt.figure(i)
                i += 1
                
                if (graph_choice.checkbox_vars[6].get() == '1'):
                    plt.bar(dates, test_model.wristList, color=(0.2, 0.4, 0.6, 0.6))
                else:
                    plt.plot(dates, test_model.wristList, color=(0.2, 0.4, 0.6, 0.6))

                ticks = np.arange(0, len(dates)-1, math.floor(len(dates)*.05))
                ticksValues = [dates[ticks[0]], dates[ticks[1]],
                        dates[ticks[2]], dates[ticks[3]], dates[ticks[4]], dates[ticks[5]],
                        dates[ticks[6]], dates[ticks[7]], dates[ticks[8]], dates[ticks[9]],
                        dates[ticks[10]], dates[ticks[11]], dates[ticks[12]], dates[ticks[13]],
                        dates[ticks[14]], dates[ticks[15]], dates[ticks[16]], dates[ticks[17]],
                        dates[ticks[18]], dates[ticks[19]], dates[ticks[20]]]
                labels: list = []
                for x in ticksValues:
                    date_format = "%Y-%m-%dT%H:%M:%SZ"

                    y = datetime.strptime(x, date_format)
                    z = y.strftime("Jan %d, %H:%M")
                    labels.append(z)

                plt.xticks(ticks, labels, rotation=60, ha='right')
                plt.tight_layout()
                plt.title('On Wrist')
        
        plt.show()

root = Tk()
root.geometry("1060x1000")
root.title("Data Visualization")
root['background'] = '#dcdad5'

# Use the 'clam' ttk theme which looks more modern than the default theme
style = ttk.Style(root)
style.theme_use('clam')

# Apply styles to specific widget types
style.configure("TLabel", foreground="black", background="white", padding=10, font=('Helvetica', 11))
style.configure("TCombobox", padding=5, font=('Helvetica', 11))
style.configure("TButton", foreground="black", background="#008CBA", padding=10, font=('Helvetica', 11), borderwidth=0)

data_loader = Frame(root)
data_loader.grid(column=0, row=0)
data_loader['background'] = '#dcdad5'

checkboxes = Frame(root)
checkboxes.grid(column=1, row=0)
checkboxes['background'] = '#dcdad5'

graph_choice = Frame(root)
graph_choice.grid(column=2, row=0)
graph_choice['background'] = '#dcdad5'

stats_frame = Frame(root)
stats_frame.grid(column=0, row=1, columnspan=3)

data_loader.participant_var = tk.StringVar()
data_loader.start_date_var = tk.StringVar()
data_loader.end_date_var = tk.StringVar()

ttk.Label(checkboxes, text="Choose Data:", style="TLabel").grid(column=0, row=0, padx=20, pady=10)
checkboxes.checkbox_vars = [tk.StringVar() for _ in range(8)]
checkboxes.checkbox_labels = ["Acc magnitude avg", "Eda avg", "Temp avg", "Movement intensity", "Steps count", "Rest", "On Wrist", "Convert to Local?"]

ttk.Label(graph_choice, text="Choose Graph:", style="TLabel").grid(column=0, row=0, padx=20, pady=10)
graph_choice.checkbox_vars = [tk.StringVar() for _ in range(7)]
graph_choice.checkbox_labels = ["MagAvg Bar Chart?", "EdaAvg Bar Chart?", "Temp Bar Chart?", "Movement Bar Chart?", "Steps Bar Chart?", "Rest Bar Chart?", "OnWrist Chart?"]

ttk.Label(data_loader, text="Participant:", style="TLabel").grid(column=0, row=0, padx=20, pady=10)
data_loader.participant_combobox = ttk.Combobox(data_loader, textvariable=data_loader.participant_var, style="TCombobox")
data_loader.participant_combobox['values'] = ['310','311','312']
data_loader.participant_combobox.grid(column=1, row=0, sticky='w')

ttk.Label(data_loader, text="Start Date:", style="TLabel").grid(column=0, row=1, padx=20, pady=10)
data_loader.start_date_entry = DateEntry(data_loader, textvariable=data_loader.start_date_var)
data_loader.start_date_entry.grid(column=1, row=1, sticky='w')

ttk.Label(data_loader, text="Start Time:", style="TLabel").grid(column=0, row=2, padx=20, pady=10)
data_loader.start_time_entry = TimeCombobox(data_loader)
data_loader.start_time_entry.grid(column=1, row=2, sticky='w')

ttk.Label(data_loader, text="End Date:", style="TLabel").grid(column=0, row=3, padx=20, pady=10)
data_loader.end_date_entry = DateEntry(data_loader, textvariable=data_loader.end_date_var)
data_loader.end_date_entry.grid(column=1, row=3, sticky='w')

ttk.Label(data_loader, text="End Time:", style="TLabel").grid(column=0, row=4, padx=20, pady=10)
data_loader.end_time_entry = TimeCombobox(data_loader)
data_loader.end_time_entry.grid(column=1, row=4, sticky='w')

for i, label in enumerate(checkboxes.checkbox_labels):
    ttk.Checkbutton(checkboxes, text=label, variable=checkboxes.checkbox_vars[i]).grid(column=1, row=i, sticky='e', padx=20, pady=10)

for i, label in enumerate(graph_choice.checkbox_labels):
    ttk.Checkbutton(graph_choice, text=label, variable=graph_choice.checkbox_vars[i]).grid(column=1, row=i, sticky='e', padx=20, pady=10)

data_loader.confirm_button = ttk.Button(data_loader, text="Confirm", command=lambda: confirm(), style="TButton")
data_loader.confirm_button.grid(column=1, row=5, pady=20)

def confirm():
        global test_model
        participant = data_loader.participant_var.get()
        start_date = data_loader.start_date_var.get()
        start_time = data_loader.start_time_entry.get()
        end_date = data_loader.end_date_var.get()
        end_time = data_loader.end_time_entry.get()
        mag_avg = checkboxes.checkbox_vars[0].get()
        eda_avg = checkboxes.checkbox_vars[1].get()
        temp_avg = checkboxes.checkbox_vars[2].get()
        movement = checkboxes.checkbox_vars[3].get()
        steps = checkboxes.checkbox_vars[4].get()
        rest = checkboxes.checkbox_vars[5].get()
        wrist = checkboxes.checkbox_vars[6].get()

        # Perform additional validations as needed
        print({
            "participant": participant,
            "start_date": start_date,
            "start_time": start_time,
            "end_date": end_date,
            "end_time": end_time
        })
        
        test_model = DataLoading.load_data(participant, start_date, start_time, end_date,  
                                        end_time, mag_avg, eda_avg, temp_avg, 
                                        movement, steps, rest, wrist)
        createStats()   
        

chart = ttk.Treeview(stats_frame)

chart['columns'] = ('Stats', 'Acc magnitude avg', 'Eda avg', 'Temp avg', 'Movement',
                    'Steps', 'Rest')

chart.column("#0", width = 0, stretch = NO)
chart.column("Stats", anchor=CENTER, width=150)
chart.column("Acc magnitude avg", anchor = CENTER, width = 150)
chart.column("Eda avg", anchor = CENTER, width = 150)
chart.column("Temp avg", anchor = CENTER, width = 150)
chart.column("Movement", anchor = CENTER, width = 150)
chart.column("Steps", anchor = CENTER, width = 150)
chart.column("Rest", anchor = CENTER, width = 150)

chart.heading("#0", text = "", anchor = CENTER)
chart.heading("Stats", text = "Stats", anchor = CENTER)
chart.heading("Acc magnitude avg", text = "Acc magnitude avg", anchor = CENTER)
chart.heading("Eda avg", text = "Eda avg", anchor = CENTER)
chart.heading("Temp avg", text = "Temp avg", anchor = CENTER)
chart.heading("Movement", text = "Movement", anchor = CENTER)
chart.heading("Steps", text = "Steps", anchor = CENTER)
chart.heading("Rest", text = "Rest", anchor = CENTER)

chart.insert(parent = '', index = 'end', iid = 0, text = '',
             values = ("Points", magAvg.points, edaAvg.points, tempAvg.points,
                       movement.points, steps.points, rest.points))
chart.insert(parent = '', index = 'end', iid = 1, text = '',
             values = ("Mean", magAvg.mean, edaAvg.mean, tempAvg.mean,
                       movement.mean, steps.mean, rest.mean))
chart.insert(parent = '', index = 'end', iid = 2, text = '',
             values = ("SD", magAvg.sd, edaAvg.sd, tempAvg.sd,
                       movement.sd, steps.sd, rest.sd))
chart.insert(parent = '', index = 'end', iid = 3, text = '',
             values = ("Min", magAvg.min, edaAvg.min, tempAvg.min,
                       movement.min, steps.min, rest.min))
chart.insert(parent = '', index = 'end', iid = 4, text = '',
             values = ("Max", magAvg.max, edaAvg.max, tempAvg.max,
                       movement.max, steps.max, rest.max))
chart.insert(parent = '', index = 'end', iid = 5, text = '',
             values = ("Median", magAvg.median, edaAvg.median, tempAvg.median,
                       movement.median, steps.median, rest.median))

def updateStats():
    chart.delete(*chart.get_children())
    chart.insert(parent = '', index = 'end', iid = 0, text = '',
             values = ("Points", magAvg.points, edaAvg.points, tempAvg.points,
                       movement.points, steps.points, rest.points))
    chart.insert(parent = '', index = 'end', iid = 1, text = '',
             values = ("Mean", magAvg.mean, edaAvg.mean, tempAvg.mean,
                       movement.mean, steps.mean, rest.mean))
    chart.insert(parent = '', index = 'end', iid = 2, text = '',
             values = ("SD", magAvg.sd, edaAvg.sd, tempAvg.sd,
                       movement.sd, steps.sd, rest.sd))
    chart.insert(parent = '', index = 'end', iid = 3, text = '',
             values = ("Min", magAvg.min, edaAvg.min, tempAvg.min,
                       movement.min, steps.min, rest.min))
    chart.insert(parent = '', index = 'end', iid = 4, text = '',
             values = ("Max", magAvg.max, edaAvg.max, tempAvg.max,
                       movement.max, steps.max, rest.max))
    chart.insert(parent = '', index = 'end', iid = 5, text = '',
             values = ("Median", magAvg.median, edaAvg.median, tempAvg.median,
                       movement.median, steps.median, rest.median))

    root.after(1000, updateStats)

chart.grid(column=0, row=1, columnspan=3)

b = ttk.Button(data_loader, text="Create Graphs", style="TButton", command=lambda: createGraph()).grid(column=2, row=5)

root.after(1000, updateStats)
root.mainloop()