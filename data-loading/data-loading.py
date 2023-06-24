import pandas as pd

class DataModel:
    magAvgList = []
    edaAvgList = []
    tempAvgList = []
    movementList = []
    stepsList = []
    restList = []
    wristList = []

class DataLoading:

    def __init__(self, subject, dateStart, dateEnd):
        self.subject = subject
        self.dateStart = dateStart
        self.dateEnd = dateEnd

    def get_data_frame(subject):
        if (subject == '310'):
            print('Reading 1st')
            sub_310_18 = pd.read_csv(r'https://raw.githubusercontent.com/ParkerHarpool/Data.Visualization/main/data-pandas/310-01-18.csv')
            print('Modifying 1st')
            sub_310_18 = sub_310_18[sub_310_18['Datetime (UTC)'] >= '2020-01-18T00:00:00Z']
            sub_310_18 = sub_310_18[sub_310_18['Datetime (UTC)'] <= '2020-01-18T23:59:00Z']

            print('Reading 2nd')
            sub_310_19 = pd.read_csv(r'https://raw.githubusercontent.com/ParkerHarpool/Data.Visualization/main/data-pandas/310-01-19.csv')
            sub_310_19 = sub_310_19[sub_310_19['Datetime (UTC)'] >= '2020-01-19T00:00:00Z']
            sub_310_19 = sub_310_19[sub_310_19['Datetime (UTC)'] <= '2020-01-19T23:59:00Z']

            print('Reading 3rd')
            sub_310_20 = pd.read_csv(r'https://raw.githubusercontent.com/ParkerHarpool/Data.Visualization/main/data-pandas/310-01-20.csv')
            sub_310_20 = sub_310_20[sub_310_20['Datetime (UTC)'] >= '2020-01-20T00:00:00Z']
            sub_310_20 = sub_310_20[sub_310_20['Datetime (UTC)'] <= '2020-01-20T23:59:00Z']

            print('Reading 4th')
            sub_310_21 = pd.read_csv(r'https://raw.githubusercontent.com/ParkerHarpool/Data.Visualization/main/data-pandas/310-01-21.csv')
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

    def load_data(subject, dateStart, dateEnd, magAvgCheck, 
                         edaAvgCheck, tempAvgCheck, movementCheck, 
                         stepsCheck, restCheck, wristCheck):
        df = DataLoading.get_data_frame(subject)
        dfStart = df[df['Datetime (UTC)'] >= dateStart]
        dfEnd = df[df['Datetime (UTC)'] <= dateEnd]
        dfMerge = pd.merge(dfStart, dfEnd, how='inner')
        print(dfMerge.head(3))
        print(dfMerge.tail(3))

        model = DataModel()
        if (magAvgCheck):
            model.magAvgList = list(dfMerge['Acc magnitude avg'])
            print(model.magAvgList)
        if (edaAvgCheck):
            model.edaAvgList = list(dfMerge['Eda avg'])
            print(model.edaAvgList)
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



sub = '310'
x = '2020-01-18T02:00:00Z'
y = '2020-01-20T03:00:00Z'
x1 = 0
x2 = 0
x3 = 0
x4 = 1
x5 = 1
x6 = 0
x7 = 0
test_model = DataLoading.load_data(sub, x, y, x1, x2, x3, x4, x5, x6, x7)