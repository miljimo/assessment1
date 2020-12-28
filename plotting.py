import math;
import functions as helper;
import matplotlib.pyplot as plt
import numpy as np


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


def plot(freq = 0.5 , time= 10 , N = 7):
            
    freq      = 0.1;
    xvalues   =  np.arange(-1 * time, time , 0.1)
    
    values  =  list();
    for t in xvalues:
        c =   helper.complex_exponential(complex(math.cos( (t  * 2 * math.pi) / N ) , math.sin((t  * 2 * math.pi) / N)))
        values.append(c);
    fig, ax   = plt.subplots()  # Create a figure containing a single axes.
    ax.plot(real(values), imag(values))  # Plot some data on the axes.
    ax.plot(xvalues, imag(values))  # Plot some data on the axes.
    plt.show();


def plot_axis(xvalues:list, yvalues:list):
    fig, ax   = plt.subplots()  # Create a figure containing a single axes.
    #ax.plot(real(values), imag(values))  # Plot some data on the axes.
    ax.plot(xvalues, yvalues)  # Plot some data on the axes.
    plt.show();
    


