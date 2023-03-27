import numpy as np
import scipy.signal as sig
from scipy.io.wavfile import read
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
    T = round(T)

    t = np.linspace(0,(T*fs-1)/fs,T*fs)

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
    # import recorded ESS signal and the inverse filter
    fs, recordedESS = read('sweep.wav') # change to your recorded ESS file
    fs, inv_sweep = read('inv_sweep.wav')
    debug = True

    impulse_response = extractRIR(recordedESS, inv_sweep, fs, debug)

