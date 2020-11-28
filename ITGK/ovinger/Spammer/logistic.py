# plot periodic orbits and iterations for the logistic map
#
import numpy as np
import matplotlib.pyplot as plt

LogisticMap = lambda x, r: r*x*(1.0-x)

def Iterate(g, x0, N, args=()):
    """
    Iterate the passed 1D function g N times, using x0 as the initial value.
    The parameters are passed as a tuple that is unpacked and appended to the arguments of g.
    """
    for i in range(N):
        x0 = g(x0, *args)
    return x0

def FindAttractors(r,x0,M):
    """ Finds at most M attractors of the LogisticMap at parameter r starting at x0
        We assume the iteration converges in itersteps"""
    itersteps = 100
    result = [] # initialize an empty result list
    for i in range(M):
        result.append(Iterate(LogisticMap, x0, itersteps+i, (r,)))
    return result

""" 1 fixed point"""
rtmp = 1.5

""" 2 fixed points"""
rtmp = 3.2

""" chaos"""
rtmp = 3.7
FindAttractors(rtmp,0.5,4)

x0 = 0.5 # initial value
maxa = 200 # maximum number of fixed points that we search for for a given r
attractor = []
x = np.linspace(0,4,440) # values of r

for r in x:
    attractor.append(FindAttractors(r,x0,maxa))

for xe, ye in zip(x, attractor):
    plt.scatter([xe] * len(ye), ye,s=0.2,c='g')

plt.ylabel('Attractor/fixed point')
plt.xlabel('r')
plt.title('Logistic map $x_{n+1} = r x_n (1 - x_n)$')
plt.savefig('LM.png')
plt.show()