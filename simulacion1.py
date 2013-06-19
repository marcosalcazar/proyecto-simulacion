import numpy as np
from scipy.stats import poisson
from pylab import plot, show, legend



print "define variables"
mu = 2
L = 3
Q = 5
r = 7
N = 20 # number of periods to be simulated

print "Inicializo variables"
QQ = np.zeros(N) # is Q(t)
I = np.zeros(N)
IP = np.zeros(N)
d = np.zeros(N)

IP[0] = I[0] = r+Q
D = poisson(mu).rvs(N)

for t in range(1,L):
    d[t] = min(D[t], I[t-1])
    I[t] = I[t-1] - d[t]
    QQ[t] = Q * (IP[t-1] <= r)
    IP[t] = IP[t-1] + QQ[t] - d[t]

for t in range(L, N):
    d[t] = min(D[t], I[t-1] + QQ[t-L])
    I[t] = I[t-1] + QQ[t-L] - d[t]
    QQ[t] = Q * (IP[t-1] <= r)
    IP[t] = IP[t-1] + QQ[t] - d[t]


print "Plot results"
plot(I, label = "I", drawstyle="steps-post")
plot(IP, label = "IP", drawstyle = "steps-post")
plot(QQ, "8", label = "Q")
plot(d, "D", label = "d")
plot(D, "o", label = "D")
legend()
show()