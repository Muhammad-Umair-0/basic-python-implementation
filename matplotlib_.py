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

# subplots
#plot 1:
print("Creating subplots")
plt.figure(figsize=(10, 5)) 
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)

plt.show()


# plot 6 subplots
x= np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.axis('off')
plt.subplot(2, 3, 1)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(x,y)
plt.show()

def plot_six_subplots():
    x1 = np.array([0, 1, 2, 3])
    y1 = np.array([3, 8, 1, 10])
    x2 = np.array([0, 1, 2, 3])
    y2 = np.array([10, 20, 30, 40])

    for i in range(1, 7):
        plt.axis('off')
        plt.subplot(2, 3, i)
        if i % 2 == 1:
            plt.plot(x1, y1)
        else:
            plt.plot(x2, y2)
    plt.show()

plot_six_subplots()

# scatter plot
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([3, 8, 1, 10, 5, 7])
print("Scatter plot ")
plt.scatter(x,y, color = 'hotpink')
plt.show()


#draw two plots with the same figure
#day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)

#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color = '#88c999')

plt.show()


#  bar plot 
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()


# horizontal bar

plt.barh(x,y)
plt.show()

# bar color

plt.bar(x,y, color='red')
plt.show()

# width 
plt.bar(x,y,width=0.1)
plt.show()



# histogram
import numpy as np

x = np.random.normal(170, 10, 250)

print(x)

plt.hist(x)
plt.show()


# pie Chart

y = np.array([35,25,25,15])
mylabels = ['apples', 'Bnanas', 'Cherries','Dates']


plt.pie(y)
plt.show()

# pie with labels

plt.pie(y, labels=mylabels)
plt.show()


