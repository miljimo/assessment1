import math;
import functions as helper;
import matplotlib.pyplot as plt
import numpy as np

BASIC_FREQUENCY  =  (math.pi * 2) / 7;

def real(values:list):
    reals  =  list();
    if(isinstance(values[0], complex)):
        for c in values:
            reals.append(c.real);

    return reals;

def imag(values:list):
    reals  =  list();
    if(isinstance(values[0], complex)):
        for c in values:
            reals.append(c.imag);

    return reals;

def complex_signal_generator(freq = 1, period= 1,  harmonic = 1):
    """
        X(n)  =  cos(kwn) +jsin(kwn);
        k   =  the harmonic member of the signal.
        w   =  the  fundamental frequency of the basic periodic signal.
        n   =  the  linear period per sample 
    """
   
    period_per_cycle       =  1/freq; 
    period_per_sample      =  period_per_cycle / period
    x_linear_times_series  =  np.arange(0, period, period_per_sample / harmonic)

    # compute the amplitude for the signal in a complex form X(n)
    # amplitudes are in complex form.
    amplitudes = [ complex(math.cos(t  * freq * harmonic) , math.sin(t  * freq * harmonic)) for t in x_linear_times_series];    
    return (x_linear_times_series, amplitudes) 
    
   

def plot_complex(freq = BASIC_FREQUENCY ,  period = 7,  harmonic =  1,):

    results  =  complex_signal_generator(freq,period, harmonic);
    fig, ax      = plt.subplots()  # Create a figure containing a single axes.
    ax.plot(results[0], imag(results[1]), marker='o')  # Plot some data on the axes.
    plt.grid(linestyle='-', linewidth=0.1)
    plt.show();


def plot_axis(xvalues:list, yvalues:list):
    fig, ax   = plt.subplots()  # Create a figure containing a single axes.
    #ax.plot(real(values), imag(values))  # Plot some data on the axes.
    ax.plot(xvalues, yvalues)  # Plot some data on the axes.
    plt.show();
    


