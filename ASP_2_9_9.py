import numpy
from numpy import zeros

N=100
x=numpy.random.rand(N)
y=numpy.random.rand(N)
p=zeros(N,float)
in_rad=0

for i in range(1,N):
    if x[i]**2+y[i]**2 < 1:
        in_rad+=1
    p=4*in_rad/i
    print(p)
