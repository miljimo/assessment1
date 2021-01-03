import math
import numpy as np


def complex_signal_generator(period= 1,  harmonic = 1, samples = None, amp = 0.5):
    """
        X(n)  =  cos(kwn) +jsin(kwn);
        k   =  the harmonic member of the signal.
        w   =  the  fundamental frequency of the basic periodic signal.
        n   =  the  linear period per sample 
    """
    
    freq                   =  harmonic * ((math.pi * 2) / period);
    period_per_cycle       =  1/ freq;
    
    if(samples is None):
        period_per_sample      =  period_per_cycle / period;
    else:
        period_per_sample      =  get_period_per_sample(samples, period)
    
    length                 = abs(period);
    x_linear_times_series  =  np.arange(-1 * length/2 , length/2, period_per_sample)
   
    # compute the amplitude for the signal in a complex form X(n)
    # amplitudes are in complex form.
    amplitudes = [ amp * complex(math.cos(t  * freq ) , math.sin(t  * freq)) for t in x_linear_times_series];    
    return (x_linear_times_series, amplitudes) 



def get_period_per_sample(number_of_sample : int, period:float = 1):
    return (period / number_of_sample);


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
