#!/bin/python

# original inversion script
# https://github.com/maasyraf-project/rir-analysis/blob/main/generateESS.py

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write as wavwrite
from scipy.io.wavfile import read as wavread

# create inverse filter
def invertwav(sweep_ori,sweep_fs,f1,f2,debug=True,scaling=True):

    # change into float -1 to 1 based on max value
    sweep_norm = sweep_ori/max(sweep)

    # this function is questionable?????
    inv_sweep = sweep_norm[::-1]
    T = len(sweep_norm)/(sweep_fs)
    t = np.linspace(0,(T*fs-1)/fs,int(T*fs))

    # array awal
    inv_scaled = inv_sweep
    if scaling:
        # create ESS signal
        w1 = 2 * np.pi * f1
        w2 = 2 * np.pi * f2
        #K = T*w1/np.log(w2/w1)
        L = T/np.log(w2/w1)
        G = np.exp(t/L)

        # scaling amplitude of the inverted
        inv_scaled = inv_sweep/G

    # plot sweep signal and its inverse
    if debug:
        plt.figure()
        plt.subplot(2,1,1)
        plt.grid()
        plt.plot(t, sweep_norm)
        plt.title('ESS signal')

        plt.subplot(2,1,2)
        plt.grid()
        if scaling:
            plt.plot(t,inv_scaled)
        else:
            plt.plot(t, inv_sweep)
        plt.title('Inverse filter of ESS signal')

        plt.show()

    if scaling:
        return [sweep_norm,inv_scaled]
    else:
        return [sweep_norm,inv_sweep]


if __name__ == '__main__':
    wavinput = sys.argv[1]
    freq1 = float(sys.argv[2])
    freq2 = float(sys.argv[3])

    # import sweep file from measurement
    fs, sweep = wavread(wavinput)

    # get normalized sweep and its inverse
    norm_sweep,inverted_sweep = invertwav(sweep,fs,freq1,freq2)

    # write outputs as wav
    wavwrite('norm_sweep.wav', fs, norm_sweep)
    wavwrite('inv_sweep.wav', fs, inverted_sweep)
