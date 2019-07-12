import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.ndimage.filters import maximum_filter
from scipy.ndimage.morphology import (generate_binary_structure,
                                      iterate_structure, binary_erosion)
import hashlib
from operator import itemgetter

from rtlsdr import RtlSdr
from fuzzywuzzy import fuzz

import os
import wave
import array
import struct
import logging
from numpy.fft import fft
from numpy.fft import fft, ifft

# -------------- D E F A U L T  V A L U E S ---------------------------------------

IDX_FREQ_I = 0
IDX_TIME_J = 1
DEFAULT_FS = 48000#44100
DEFAULT_WINDOW_SIZE = 4096 
DEFAULT_OVERLAP_RATIO = 0.37#0.37 #0.37 #0.5
DEFAULT_FAN_VALUE = 20#20#2#15
DEFAULT_AMP_MIN = 10#-10 #-20 #10
PEAK_NEIGHBORHOOD_SIZE = 20#20#-10- #11 #20 # default poner a 20, estaba en 25
MIN_HASH_TIME_DELTA = 0
MAX_HASH_TIME_DELTA = 200#20#200
PEAK_SORT = True
FINGERPRINT_REDUCTION = 20


def fingerprint(channel_samples, Fs=DEFAULT_FS,
                wsize=DEFAULT_WINDOW_SIZE,
                wratio=DEFAULT_OVERLAP_RATIO,
                fan_value=DEFAULT_FAN_VALUE,
                amp_min=DEFAULT_AMP_MIN):
    
    arr2D = mlab.specgram(
        channel_samples,
        NFFT=wsize,
        Fs=Fs,
        window=mlab.window_hanning,
        noverlap=int(wsize * wratio))[0]

    # apply log transform since specgram() returns linear array
    arr2D = 10 * np.log10(arr2D)
    arr2D[arr2D == -np.inf] = 0  # replace infs with zeros

    # find local maxima
    local_maxima = get_2D_peaks(arr2D, plot=False, amp_min=amp_min)
    local_m= list(local_maxima)
    

    for i in range(len(local_m)):
        #print(f"Holamundo soy: {i}")
        for j in range(1, fan_value):
            if (i + j) < len(local_m):

                freq1 = str(local_m[i][IDX_FREQ_I])
                freq2 = str(local_m[i + j][IDX_FREQ_I])
                t1 = local_m[i][IDX_TIME_J]
                t2 = local_m[i + j][IDX_TIME_J]
                t_delta = t2 - t1

                if t_delta >= MIN_HASH_TIME_DELTA and t_delta <= MAX_HASH_TIME_DELTA:
                    t_delta= str(t_delta)
                    #print(freq2)
                    h= hashlib.sha3_512(b"hola mundo")

                    h = hashlib.sha1(
                        b"%s|%s|%s" % (bytes(freq1.encode('utf-8')), bytes(freq2.encode('utf-8')), bytes(t_delta.encode('utf-8'))))

                    yield (h.hexdigest()[0:FINGERPRINT_REDUCTION], t1)
                    #return (h.hexdigest()[0:FINGERPRINT_REDUCTION], t1)



def get_2D_peaks(arr2D, plot=False, amp_min=DEFAULT_AMP_MIN):
    # http://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.morphology.iterate_structure.html#scipy.ndimage.morphology.iterate_structure
    struct = generate_binary_structure(2, 1)
    neighborhood = iterate_structure(struct, PEAK_NEIGHBORHOOD_SIZE)

    # find local maxima using our fliter shape
    local_max = maximum_filter(arr2D, footprint=neighborhood) == arr2D
    background = (arr2D == 0)
    eroded_background = binary_erosion(background, structure=neighborhood,
                                       border_value=1)

    # Boolean mask of arr2D with True at peaks
    local_max = local_max.astype(np.float32)
    eroded_background = eroded_background.astype(np.float32)
    detected_peaks = local_max - eroded_background
    #print(detected_peaks)
    detected_peaks = detected_peaks.astype(np.bool)
    #print(detected_peaks)


    # extract peaks
    amps = arr2D[detected_peaks]
    j, i = np.where(detected_peaks)

    # filter peaks
    amps = amps.flatten()

    peaks = zip(i, j, amps)

    #conversion a una lists
    listapeaks = list(peaks)
    #print(listapeaks[0][2])
    #print(amp_min)
    #print(listapeaks[0])


    peaks_filtered =[]
    time_idx = []
    frequency_idx = []
    for i in range(len(listapeaks)):

        if (listapeaks[i][2]) > amp_min:

            peaks_filtered.append((listapeaks[i][2]))
            time_idx.append(listapeaks[i][0])
            frequency_idx.append(listapeaks[i][1])


    if plot:
        # scatter of the peaks
        fig, ax = plt.subplots()
        ax.imshow(arr2D)
        ax.scatter(time_idx, frequency_idx)
        ax.set_xlabel('Time')
        ax.set_ylabel('Frequency')
        ax.set_title("Spectrogram")
        plt.gca().invert_yaxis()
        plt.show()
        #print(frequency_idx)

    fdxtim = zip(frequency_idx, time_idx)
    #print("hola--------")
    return fdxtim
