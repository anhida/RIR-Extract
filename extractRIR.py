#!/bin/python

import sys
import numpy as np
from scipy.io.wavfile import read as wavread
import scipy.signal as sig
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
from scipy.io import savemat

def extractRIR(sweep_ori, sweep_inv, fs, debug=True):
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

    T = len(sweep_ori)/fs
    t = np.linspace(0,(T*fs-1)/fs,int(T*fs))

    # change into float -1 to 1 based on max value
    sweep_norm = sweep_ori/max(sweep_ori)

    # convolve both to get impulse response
    impulse_response = sig.fftconvolve(sweep_norm, sweep_inv, mode='same')

    # change into float -1 to 1 based on max value
    norm_impulse_resp = impulse_response/max(impulse_response)

    if debug == True:
        plt.figure()
        plt.subplot(3,1,1)
        plt.grid()
        plt.plot(t, sweep_norm)
        plt.title('Recorded signal')

        plt.subplot(3,1,2)
        plt.grid()
        plt.plot(t, sweep_inv)
        plt.title('Inverse Filter of signal')

        plt.subplot(3,1,3)
        plt.grid()
        plt.plot(t, norm_impulse_resp)
        plt.title('Room Impulse Response')

        plt.show()

    return norm_impulse_resp

if __name__ == '__main__':

    # get shell arguments
    wavori = sys.argv[1]  # change to your recorded ESS file
    wavinv = sys.argv[2]

    # import recorded ESS signal and the inverse filter
    fs, ori_sweep = wavread(wavori)
    fs, inv_sweep = wavread(wavinv)

    # get normaized impulse response array
    impulse_response = extractRIR(ori_sweep, inv_sweep, fs)

    #save impulse response as WAV
    write("impulse_response.wav", fs, impulse_response)

    #create impulse response .mat
    savemat("impulse_response.mat",{'risp_imp':impulse_response})
