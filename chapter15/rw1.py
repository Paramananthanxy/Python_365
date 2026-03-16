from rw import Randomwalk
import matplotlib.pyplot as plt 

rw=Randomwalk(5000)
rw.randomwalks()


plt.scatter(rw.x_values,rw.y_values,s=14)
plt.show()