import random
import statistics
import plotly.figure_factory as pf
import plotly.graph_objects as go
import pandas as pd
import csv

df = pd.read_csv("StudentsPerformance.csv")
dt = df["reading score"].tolist()

mean = sum(dt) / len(dt)
std_deviation = statistics.stdev(dt)
median = statistics.median(dt)
mode = statistics.mode(dt)

fstds , fstde = mean - std_deviation, mean + std_deviation
sstds , sstde = mean - (2*std_deviation), mean +(2*std_deviation)
tstds , tstde = mean - (3*std_deviation), mean +(3*std_deviation)

fig = pf.create_distplot([dt], ["reading scores"], show_hist=False)

fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[fstds,fstds],y=[0,0.17],mode="lines",name="STD1"))
fig.add_trace(go.Scatter(x=[fstde,fstde],y=[0,0.17],mode="lines",name="STD1"))
fig.add_trace(go.Scatter(x=[sstds,sstds],y=[0,0.17],mode="lines",name="STD2"))
fig.add_trace(go.Scatter(x=[sstde,sstde],y=[0,0.17],mode="lines",name="STD2"))
fig.show()

lsd1 = [result for result in dt if result > fstds and result < fstde]
lsd2 = [result for result in dt if result > sstds and result < sstde]
lsd3 = [result for result in dt if result > tstds and result < tstde]

print("Mean of this data is {}".format(mean))
print("Median of this data is {}".format(median))
print("Mode of this data is {}".format(mode))
print("Standard deviation of this data is {}".format(std_deviation))
print("{}% of data lies within 1 Standard Deviation".format(len(lsd1)*100.0 / len(dt)))
print("{}% of data lies within 2 Standard Deviation".format(len(lsd2)*100.0 / len(dt)))
print("{}% of data lies within 3 Standard Deviation".format(len(lsd3)*100.0 / len(dt)))