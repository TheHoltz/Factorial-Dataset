from math import exp
from math import ceil

#Using Stirling formula
def factorialAproximation(n)
  return(ceil((n)((2*pi*n)^.5)*(n/exp(1))**n))

#Recursive
def Factorial(n):
  if n == 1 or n==0:
    return(1);
  else:
    return(n*fatorial(n-1));
