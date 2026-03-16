import csv
import matplotlib.pyplot as plt
from datetime import datetime

with open(r"C:\Python_Beg_to_Adv\Assessments\weather.csv",'r') as f:
    reads= csv.reader(f)
    header = next(reads)
    print(header)

##printing the header and their positions..
    for index,head in enumerate(header):
     print(index,head)

    temp = []
    dates=[]
    hum = []
    for x in reads:
        temp.append(x[1])
        dat = datetime.strptime(x[0],'%Y-%m-%d')
        dates.append(dat)
        hum.append(x[2])

    #plotting the second Data series.
        
    # print(dates)
    # print(temp)
##The datetime module
    

       
   
       


##Plotting data in a temperature chart 

fig =plt.figure(dpi=128,figsize=(10,6)) ## size figure adjustment 
#shading an area in the chart
plt.plot(dates,temp, c ='red')
plt.plot(dates,hum,c='blue',alpha=0.5) ##alpha is used for shadding
# plt.title("Daily temperature",fontsize=15)
# plt.xlabel("Dates",fontsize=14)
# plt.ylabel("Temperature",fontsize=14)
fig.autofmt_xdate()  ##Printing the date diagonally for preventing from overlooping 
### for changing the size of the x and y axis line numbers 
# plt.tick_params(axis='x',which='major',labelsize=16)

plt.show()