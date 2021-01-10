import math;
import os;
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


def plot_complex_continous_signal(period = 7,
                        harmonic =  1,
                        samples  = None,
                        title  = None,
                        xlabel ="n - time",
                        ylabel ="X(n) - amplitude"):
    if(title == None):
        if harmonic < 9 : 
            title  =  FUNCTIONAL_LABELS[harmonic - 1].format(period)
    
    results      =  helper.complex_signal_generator(period, harmonic, samples);
    fig, ax      = plt.subplots()  # Create a figure containing a single axes.
    
    plt.title("${0}$".format(title))
    #plot the imaginary numbers against the time line.
    ax.stem(results[0], imag(results[1]), linefmt='-',  label="Imaginary")  # Plot some data on the axes.      
    
    plt.grid(linestyle='-', linewidth=0.1)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show();


def plot_discrete_complex_signal(period = 7,
                        harmonic =  1,
                        repeats  =  1,
                        title  = None,
                        xlabel ="n - time",
                        ylabel ="X(n) - amplitude",
                        func_type =1):
    """
       period : the sample frame
       harmonic :the harmonic member of the basic fundamental signal.
       repeats : the number of times to repeat the sample frame
       title   : the title of the graph must the formula here.
    """
    
    if(title == None):
        if harmonic < 9 : 
            title  =  FUNCTIONAL_LABELS[harmonic - 1].format(period)
    
    results      =  helper.discrete_complex_signal_generator(period, harmonic, repeats);
    fig, ax      =  plt.subplots() 

    
    plt.title("${0}$".format(title))
    if(func_type == 0):
        ax.stem(results[0], real(results[1]), linefmt='-',  label="Real")  # Plot some data on the axes.
    else:
        ax.stem(results[0], imag(results[1]), linefmt='-',  label="Imaginary")  # Plot some data on the axes.
    
    plt.grid(linestyle='-', linewidth=0.1)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show();



def plot_unit_signal(step = 0,size  = 6,
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
    plt.ylabel( ylabel)
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
            
      
  
def energy(complex_numbers):
    results  =  0;
    
    for c in complex_numbers:
        results +=  abs(c)**2;
    return results;

def get_complex_signal_energy(period= 7, harmonic = 1):
    results  =  helper.discrete_complex_signal_generator(period, harmonic, repeats=1);
    return energy(results[1])


def signal_save(filename , period=7, harmonic=1):
    if(type(filename) == str):
        
        results  =  helper.discrete_complex_signal_generator(period, harmonic, repeats=1);
        with open(filename , mode='w+') as writer:
            for c in results[1]:
                writer.write("({0},{1})\n".format(c.real, c.imag));
            
            
     
     
def get_zero_crossing_counts(period= 7, harmonic = 1,func_type = 1, repeats = 2 ):
    results  =  helper.discrete_complex_signal_generator(period, harmonic, repeats=repeats);
    amplitudes  = real(results[1]) if(func_type == 0) else imag(results[1])
    return count_zero_crossing(amplitudes)


    


