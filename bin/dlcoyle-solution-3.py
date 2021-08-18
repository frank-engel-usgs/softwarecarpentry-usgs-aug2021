import matplotlib.pyplot
import numpy


data = numpy.loadtxt(fname='../data/080167500_Guadalupe_SpringBranch_DailyMeanQ.csv', delimiter=',')

#print(data)

print('*** solution-3:')

fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

axes1 = fig.add_subplot(1, 4, 1)
axes2 = fig.add_subplot(1, 4, 2)
axes3 = fig.add_subplot(1, 4, 3)
axes4 = fig.add_subplot(1, 4, 4)

axes1.set_ylabel('average')
axes1.plot(numpy.mean(data, axis=0))

axes2.set_ylabel('max')
axes2.plot(numpy.max(data, axis=0))

axes3.set_ylabel('min')
axes3.plot(numpy.min(data, axis=0))

axes4.set_ylabel('range')
axes4.plot(numpy.max(data, axis=0) - numpy.min(data, axis=0))

fig.tight_layout()
matplotlib.pyplot.show()