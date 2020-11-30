import matplotlib.pyplot as plt
import matplotlib.animation as animation    #This is the module that will allow us to animate the figure 
from matplotlib import style
import csv
style.use('fivethirtyeight')

fig = plt.figure()    #In order to modify the figure, we need to reference it, so we'll store it to the variable called "fig"
ax1 = fig.add_subplot(1,1,1)   #defining subplot as "ax1"

def animate(i):    #animation function
        x = []
        y = []

        with open('samplefile.csv','r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            for row in plots:
                x.append(int(row[0]))
                y.append(int(row[1]))
                ax1.clear()
                ax1.plot(x, y)
                plt.xlabel('No. of samples')     #label for x-axis
                plt.ylabel('RPM variation')     #label for y-axis
                plt.title('Graph')
        


ani = animation.FuncAnimation(fig, animate, interval = 1000)     #animating the graph every "1000" milliseconds

plt.show()     # showing the plot
