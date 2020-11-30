#Plotting simple graph from .csv / .txt file and included a button


import matplotlib.pyplot as plt
import matplotlib.animation as animation    #This is the module that will allow us to animate the figure 
from matplotlib import style
import csv
from matplotlib.widgets import Button

style.use('fivethirtyeight')

fig = plt.figure(200)    #In order to modify the figure, we need to reference it, so we'll store it to the variable called "fig"
ax1 = fig.add_subplot(1,1,1)   #defining subplot as "ax1"


def animate(i):    #animation function
        x = []
        y = []

        with open('samplefile.csv','r') as csvfile:       #opening .csv file and reading it
            plots = csv.reader(csvfile, delimiter=',')
            for row in plots:
                x.append(int(row[0]))    #selected row 0 of .csv file for x-axis
                y.append(int(row[1]))     #selected row 1 of .csv file for x-axis
                ax1.clear()                 #clearing prev plot
                ax1.plot(x, y)          #ploting

                ax1.set_xlabel('No. of Samples')    
                ax1.set_ylabel('RPM Variation')
                ax1.set_title('Graph')
                

#adding button (from here)
def _yes(event):
    print("yolo")       

axcut = plt.axes([0.9, 0.0, 0.07, 0.075])   #defining button with dimensions "(x_position, y_position, length, width)"
bcut = Button(axcut, 'Set', color='red', hovercolor='green')     # text for button, colour
bcut.on_clicked(_yes)  #when button is clicked then call "_yes" function

#adding button (to here)


ani = animation.FuncAnimation(fig, animate, interval = 1000)     #animating the graph every "1000" milliseconds

plt.show()     # showing the plot

