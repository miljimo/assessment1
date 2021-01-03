import math;
import functions as helper;
import matplotlib.pyplot as plt
import numpy as np
from zerocrossing import count_zero_crossing;

BASIC_FREQUENCY  =  (math.pi * 2) / 7;


FUNCTIONAL_LABELS  =  ["X(n) = e^j(2π/{0})n",
            "X(n) = e^j(4π/{0})n",
            "X(n) = e^j(6π/{0})n",
            "X(n) = e^j(8π/{0})n",
            "X(n) = e^j(10π/{0})n",
            "X(n) = e^j(12π/{0})n",
            "X(n) = e^j(2π)n",
            "X(n) = e^j(16π/{0})n"]

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

def plot_complex_signal(period = 7,
                        harmonic =  1,
                        samples  = None,
                        amp = 1,
                        title  = None,
                        xlabel ="n - time",
                        ylabel ="X(n) - amplitude"):
    if(title == None):
        if harmonic < 9 : 
            title  =  FUNCTIONAL_LABELS[harmonic - 1].format(period)
    
    results      =  helper.complex_signal_generator(period, harmonic, samples, amp );
    fig, ax      = plt.subplots()  # Create a figure containing a single axes.
    
    plt.title("${0}$".format(title))
    #plot the imaginary numbers against the time line.
    ax.plot(results[0], imag(results[1]), marker='o',  label="Imaginary")  # Plot some data on the axes.      
    ax.plot(results[0], real(results[1]), marker='o',  label="Real")  # Plot some data on the axes.
    
    plt.grid(linestyle='-', linewidth=0.1)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show();



def plot_signal(step = 0,size  = 6,
                        title  = "X(n)",
                        xlabel = "n - time",
                        ylabel ="X(n) - amplitude"):
    LABEL ="u(n-{0})".format(step);
    values  = unit_signal(step, size);
    fig, ax      = plt.subplots() 
    plt.title("${0}$".format(title))
    ax.step(values[0], values[1],  label=LABEL)  # Plot some data on the axes.
    plt.grid(linestyle='-', linewidth=0.1)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show();

def plot_value_signals(xvalues:list, yvalues:list,
                       title  = "Unit Signal",
                       xlabel = "n - time",
                       ylabel ="u(n) - amplitude"):
    fig, ax      = plt.subplots() 
    plt.title("${0}$".format(title))
    ax.step(xvalues, yvalues,  label=title)  # Plot some data on the axes.
    plt.grid(linestyle='-', linewidth=0.1)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show();

def unit_signal(shift:float , size =  1):

    if(shift > size):
        size   = shift + 1;
        
    xvalues  =  np.arange(-1 * size , size, 0.1);
    yvalues  = list();
    
    for x in xvalues :
        if(x  >= shift):
            yvalues.append(1);
        else:
            yvalues.append(0);
    return (xvalues , yvalues);
            
      
  

def get_zero_crossing_counts(period= 7, harmonic = 1, samples = None):
    results  =  helper.complex_signal_generator(period, harmonic, samples);
   
    return count_zero_crossing(imag(results[1]))


    


