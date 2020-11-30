import matplotlib.pyplot as plt
import matplotlib.animation as animation    #This is the module that will allow us to animate the figure 
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()    #In order to modify the figure, we need to reference it, so we'll store it to the variable called "fig"
ax1 = fig.add_subplot(1,1,1)   #defining subplot as "ax1"

def animate(i):    #animation function
        graph_data = open('samplefile.csv','r').read()      #opening the "examplefile.txt" file, 
        lines = graph_data.split('\n')                          #split by comma, into xs and ys, which we'll plot
        print('lines = ',lines)
        xs = []
        ys = []
        for line in lines:        
                if len(line) > 1:
                        x, y = line.split(',')
                        xs.append(x)
                        ys.append(y)
        ax1.clear()
        ax1.plot(xs, ys)
        plt.xlabel('No. of samples')     #label for x-axis
        plt.ylabel('RPM variation')     #label for y-axis
        plt.title('Graph')
        


ani = animation.FuncAnimation(fig, animate, interval = 1000)     #animating the graph every "1000" milliseconds

plt.show()     # showing the plot

