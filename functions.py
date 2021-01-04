import math
import numpy as np


def discrete_complex_signal_generator(period,  harmonic, repeats = 2, amp=1):
    """
        X(n)  =  cos(kwn) +jsin(kwn);
        k   =  the harmonic member of the signal.
        w   =  the  fundamental frequency of the basic periodic signal.
        n   =  the  linear period per sample 
    """
    
    freq                   =  harmonic * ((math.pi * 2) / period);
    period_per_cycle       =  1/ freq;
    length                 = abs(period * repeats);
    x_linear_times_series  =  np.arange(-1 * length/2 , length/2 + 1, 1)
  
    amplitudes = [ amp * complex(math.cos(t  * freq ) , math.sin(t  * freq)) for t in x_linear_times_series];    
    return (x_linear_times_series, amplitudes)


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


