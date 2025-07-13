import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,6,5,6,71,2,3,4,5,6,7,8,9,10])
y = np.array([0,256,4,5,6,7,54,7,8,9,10,11,12,13])

plt.plot(x,y,)
plt.show()
# plt.savefig('plot.png')  # Save the plot as a PNG file

ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()

# matplotlib markers 
plt.plot(ypoints, marker = 'o')
plt.show()

# make each point with circle marker
plt.plot(ypoints, 'o:r')
plt.show()

# marker size 
plt.plot(ypoints, marker = 'o', markersize = 20)
plt.show()



# set the edge color of the marker
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'red')
plt.show()

# marker face color
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'red', mfc = 'yellow')


# Set the color of both the edge and the face to red:
print("Setting both edge and face color to red")
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'red', mfc = 'red')
plt.show()

# use dotted line style
print("Using dotted line style")
plt.plot(ypoints, ls = 'dotted')
plt.title('Dotted Line Style')
plt.show()

# use dashed line style
print("Using dashed line style")    
plt.plot(ypoints, ls = 'dashed')
plt.title('Dashed Line Style')  
plt.show()

# shortest syntax for line style
print("Using shortest syntax for line style")
plt.plot(ypoints, ls = ':')


# set the line color to red
print("Setting line color to red")
plt.plot(ypoints, color = 'red')
plt.title('Line Color Red')
plt.show()


# Labels for plot
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
print("Setting labels for the plot")
plt.plot(x, y)

plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show()

# Set the title of the plot

print("Setting title for the plot")
plt.plot(x, y)
font1 = {'family':'serif','color':'blue','weight':'normal','size':12}
font2 = {'family':'serif','color':'blue','weight':'bold','size':16}
plt.title("Calories Burned vs. Average Pulse", fontdict = font2)    
plt.xlabel("Average Pulse", fontdict = font1)
plt.ylabel("Calorie Burnage", fontdict = font1)
plt.show()


# add grid to the plot
print("Addint the grid to the plot")
plt.plot(x, y)
font1 = {'family':'serif','color':'blue','weight':'normal','size':12}
font2 = {'family':'serif','color':'blue','weight':'bold','size':16}
plt.title("Calories Burned vs. Average Pulse", fontdict = font2)    
plt.xlabel("Average Pulse", fontdict = font1)
plt.ylabel("Calorie Burnage", fontdict = font1)
plt.grid()
plt.show()

#show grid on only x-axis
print("Showing grid on only x-axis")    
plt.plot(x, y)
font1 = {'family':'serif','color':'blue','weight':'normal','size':12}
font2 = {'family':'serif','color':'blue','weight':'bold','size':16}
plt.title("Calories Burned vs. Average Pulse", fontdict = font2)    
plt.xlabel("Average Pulse", fontdict = font1)
plt.ylabel("Calorie Burnage", fontdict = font1)
plt.grid(axis='x')
plt.show()


