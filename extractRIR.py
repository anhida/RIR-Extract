#!/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read as wavread
import scipy.signal as sig
import matplotlib.pyplot as plt

def extractRIR(recordedESS, inv_sweep, fs, debug=False):
    '''
    Function to extract impulse response based on Angelo Farina's method. The code adopted from https://dsp.stackexchange.com/questions/41696/calculating-the-inverse-filter-for-the-exponential-sine-sweep-method
    Input
    recordedESS         : recorded ESS signal in room
    inv_sweep           : inverse filter of generated ESS signal
    fs                  : sample rate of signal (Hz)
    debug               : option to plot the process and results or not, default: False

    Output
    impulse_response    : impulse response of room
    '''

    T = len(recordedESS)/fs
    t = np.linspace(0,(T*fs-1)/fs,int(T*fs))

    impulse_response = sig.fftconvolve(recordedESS, inv_sweep, mode='same')

    if debug == True:
        plt.figure()
        plt.subplot(3,1,1)
        plt.grid()
        plt.plot(t, recordedESS)
        plt.title('Recorded ESS signal')

        plt.subplot(3,1,2)
        plt.grid()
        plt.plot(t, inv_sweep)
        plt.title('Inverse Filter of ESS signal')

        plt.subplot(3,1,3)
        plt.grid()
        plt.plot(t, impulse_response)
        plt.title('Room Impulse Response')

        plt.show()

    return impulse_response

if __name__ == '__main__':

    # get shell arguments
    wavori = sys.argv[1]  # change to your recorded ESS file
    wavinv = sys.argv[2]

    # import recorded ESS signal and the inverse filter
    fs, ori_sweep = wavread(wavori)
    fs, inv_sweep = wavread(wavinv)
    debug = True

    impulse_response = extractRIR(ori_sweep, inv_sweep, fs, debug)

