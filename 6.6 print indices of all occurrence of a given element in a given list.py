import numpy
l = numpy.array([1,2,4,3,5,1,7,9,8,6,5])
for i in l:
    indices = numpy.where(l == i)[0]
    print(indices,end='')