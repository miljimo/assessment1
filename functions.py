import math
import numpy


def factorial(n:int):
    if(n <= 1):
        return 1;
    return n * factorial(n -1);

"""
   A simple sequence generate of time internals
"""
def generate_sequence(start:int = 0, end:int=10, step:int  = 1):
    result  =  list();
    result.append(start);        
    if (start < end) and (step > 0):
        while(start != end):
            start += step;
            result.append(start)
    return result

"""
 complex exponential for e^1 = exp(1)
 # exp(x)  =  1 + x + x^2/2! + x^3/3! + x^4/4! ... x^[N-1]/[N-1]!; 
"""
def complex_exponential(x:float, N:int=100):
    N  =  N - 1;
    if N <= 0:
        return 1;
    return((x**N)/ factorial(N)) + complex_exponential(x, N)


def sine_generator(frequency:int , start:int  = 0, end:int  =  10 , step:int  =  1):
    xvalues  =  generate_sequence(start, end, step);
    yvalues  =  list();
    for i in  range(0, len(xvalues)):
        x =  xvalues[i]
        yvalues.append( (math.sin(math.pi * 2 * frequency * x * (i+1)))/ (i +1));
        
    return (xvalues, yvalues)

"""
  Harmonic generation
where N= is the mean of the harmonics to generated and sum.
"""
def harmonic_series(x:int = 1, N:int  = 100):
    N = N- 1;
    if(N <= 0):
        return 1;
    return  (x**N/N) + harmonic_series(x, N);
