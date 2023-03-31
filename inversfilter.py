#!/bin/python

# original inversion script
# https://github.com/maasyraf-project/rir-analysis/blob/main/generateESS.py

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write as wavwrite
from scipy.io.wavfile import read as wavread

# create inverse filter
def invertwav(sweep_ori,sweep_fs,f1,f2,debug=True,scaling=False):

    # this function is questionable?????
    inv_sweep = sweep_ori[::-1]
    T = len(sweep_ori)/(sweep_fs)
    t = np.linspace(0,(T*fs-1)/fs,int(T*fs))

    # array awal
    inv_scaled = inv_sweep

    if scaling:
        # create ESS signal
        w1 = 2 * np.pi * f1
        w2 = 2 * np.pi * f2
        K = T*w1/np.log(w2/w1)
        L = T/np.log(w2/w1)
        G = np.exp(t/L)

        # scaling amplitude of the inverted
        inv_scaled = inv_sweep/G

    # plot sweep signal and its inverse
    if debug:
        plt.figure()
        plt.subplot(2,1,1)
        plt.grid()
        plt.plot(t, sweep_ori)
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
        return inv_scaled
    else:
        return inv_sweep

# convert PCM signal to floating point signal
def pcm2float(signal, dtype='float32'):
    '''
    Function to convert PCM signal to floating point signal, as shown in https://gist.github.com/HudsonHuang/fbdf8e9af7993fe2a91620d3fb86a182
    Input
    signal      : input signal array (should be int type)
    dtype       : desired (floating point) data type, default: float32 (high precision)

    Output
    output      : normalized floating point signal
    '''
    signal = np.asarray(signal)
    if signal.dtype.kind not in 'iu':
        raise TypeError('Signal should be an array of integer')

    dtype = np.dtype(dtype)

    if dtype.kind != 'f':
        raise TypeError('The dtype should be a floating point type')

    limit = np.iinfo(signal.dtype)
    absolute_max = 2 ** (limit.bits - 1)
    offset = limit.min + absolute_max

    return (signal.astype(dtype) - offset) / absolute_max

if __name__ == '__main__':
    wavinput = sys.argv[1]

    freq1 = float(sys.argv[2])
    freq2 = float(sys.argv[3])

    # import sweep file from measurement
    fs, sweep = wavread(wavinput)

    # check audio data type, converting int16 to float32
    if sweep.dtype.kind != 'f':
        sweep = pcm2float(sweep)

    inverted_sweep = invertwav(sweep,fs,freq1,freq2,scaling=True)
    wavwrite('inv_sweep.wav', fs, inverted_sweep.astype(np.float32))
