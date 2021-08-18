import matplotlib.pyplot
import numpy

data = numpy.loadtxt(fname='../data/080167500_Guadalupe_SpringBranch_DailyMeanQ.csv', delimiter=',')
#print(data)

print('*** solution-2:')

meanQ = numpy.mean(data, axis=0)
minQ = numpy.min(data, axis=0)
maxQ = numpy.max(data, axis=0)
rangeQ = maxQ - minQ
print(meanQ)
print(minQ)
print(maxQ)
print(rangeQ)