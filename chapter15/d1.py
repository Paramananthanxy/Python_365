from Dice import Dice
import pygal

d1 = Dice()
d2 = Dice()
d1.roll()
print(d1.roll())

d123 = []

for x in range(5000):
  
    d12 = d1.roll() +d2.roll()
    d123.append(d12)

# print(d123)
freq = []
for fre in range(1,13):
    frequ = d123.count(fre)
    freq.append(frequ)
print(freq)


hist = pygal.Bar()

hist.title = "Resulting of rolling one D6 for 5000 times.."
hist.x_labels = ['1','2','3','4','5','6']
hist._x_title = "Results"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6',freq)

hist.render_to_file('die_visual.svg')