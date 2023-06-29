import matplotlib.pyplot as plt

steps = [200, 150, 321, 723, 632, 100, 180, 132, 123, 502]
dates = ["Jan 1st, 2023", "Jan 2nd, 2023", "Jan 3rd, 2023", "Jan 4th, 2023", 
         "Jan 5th, 2023", "Jan 6th, 2023", "Jan 7th, 2023", "Jan 8th, 2023",
           "Jan 9th, 2023", "Jan 10th, 2023"]


#The graph label font doesnt want to change, so the graph should be viewed
#in the maximized frame to allow the view of the xLabels.
def createGraph(varX, varY, xLabel, yLabel, type):
    if(type == "Bar"):
        plt.bar(varX, varY, color=(0.2, 0.4, 0.6, 0.6))
    elif(type == "Line"):
        plt.plot(varX, varY, color=(0.2, 0.4, 0.6, 0.6))
    
    plt.title(type+ ' Graph')
    plt.xlabel(xLabel, fontsize=1)
    plt.ylabel(yLabel)
    plt.show()  
    

if __name__ == "__main__":
    createGraph(dates, steps, "Date", "Steps", "Line")


