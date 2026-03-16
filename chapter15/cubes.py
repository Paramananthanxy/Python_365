import matplotlib.pyplot as plt

x_axis = list(range(1,5000))
y_axis = [x**3 for x in x_axis]

plt.scatter(x_axis,y_axis,c=y_axis,cmap=plt.cm.Blues,edgecolor='none',s=40)
plt.title("Cube",fontsize=24)
plt.xlabel("x_axis",fontsize=10)
plt.ylabel("Y_axis",fontsize=10)
plt.tick_params(axis='both',labelsize=10)
plt.plot(x_axis,y_axis,linewidth=5)

plt.plot(x_axis,y_axis)

plt.show()