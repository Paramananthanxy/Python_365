import matplotlib.pyplot as plt

x_values = [1,2,3,4,5,6,7,8]
y_values = [1,2,3,4,5,6,7,8]

plt.scatter(x_values, y_values,c=y_values, cmap=plt.cm.Greens,edgecolor='none', s=100)
plt.plot(x_values,y_values,linewidth=5)
plt.title("square Number",fontsize = 24)
plt.xlabel("value",fontsize=15)
plt.ylabel("Sqare of value", fontsize= 15)


plt.tick_params(axis='both',labelsize=10)


plt.plot(x_values,y_values)
plt.savefig('sqare_plot.png',bbox_inches='tight')
plt.show()

