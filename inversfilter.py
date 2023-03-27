import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

# import sweep file from measurement 
fs, sweep = read('R1P1Tr1_1.wav') #change file with sweep wav file

# create inverse filter
G = np.exp(t/L)
inv_sweep = sweep[::-1]/G

# plot sweep signal and its inverse
if debug == True:
    plt.figure()
    plt.subplot(2,1,1)
    plt.grid()
    plt.plot(t, sweep)
    plt.title('ESS signal')

    plt.subplot(2,1,2)
    plt.grid()
    plt.plot(t, inv_sweep)
    plt.title('Inverse filter of ESS signal')

    plt.show()

    write('sweep.wav', fs, sweep)
    write('inv_sweep.wav', fs, inv_sweep)
