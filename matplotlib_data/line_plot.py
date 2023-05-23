from matplotlib import pyplot as plt
import numpy as np
x = np.arange(1,10)
y = x*2.1
y1 = y+4
# print(x,y)

#------------plot graph as x and y axis

plt.plot(x,y,color='g',linestyle=':',linewidth=5)
plt.title('X vs Y')
plt.xlabel('this is x axis ')
plt.ylabel('this is y axis ')
# plt.show() # to plot the graph

#-----------plot 2 line graph
plt.plot(x,y,color='g',linestyle=':',linewidth=5)
plt.plot(x,y1,color='r',linestyle=':',linewidth=2)
plt.title('X vs Y')
plt.xlabel('this is x axis ')
plt.ylabel('this is y-2 axis ')
plt.grid=True
plt.show() # to plot the graph

#-----------subplot  in one page
 