import cmath
import random
import time
# Discrete fourier transform
def dft(x):
  t = []
  N = len(x)
  for k in range(N):
    a = 0
    for n in range(N):
      a += x[n]*cmath.exp(-2j*cmath.pi*k*n*(1/N))
      t.append(a)
  return t
  
#Test
complex_doubles = []
for i in range (0,8000):
  complex_doubles.append(random.randrange(10) + random.random() + 1j*(random.randrange(10) + random.random()))

start = time.clock()
res = dft(complex_doubles)
end = time.clock()
duration = end - start
print ("Duration(s) : ",duration)