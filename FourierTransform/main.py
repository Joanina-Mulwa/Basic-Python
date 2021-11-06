import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import tkinter as tk;

mag  = 2;     # magnitude (arbitrary units)
freq = 5;     # frequency in Hz
samp = 100;   # sampling rate in Hz

t = np.arange(0.0,1.0,1.0/samp)  # time (1s of data)
N = len(t)                       # store the number of time points

x = mag*np.cos(2*np.pi*freq*t)   # the signal equation
plt.plot(t,x,'.-')lt.show(*-/)