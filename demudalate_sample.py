#from pylab import *
import numpy as np
from multiprocessing import Process, current_process, Lock
#from scipy.io import wavfile
from scipy import signal
import os # get current process id
import pickle # para guardar .dat
import time
import os
import soundfile as sf

#---- variables
sample_rate= 3e6
sample_rate_fm = 200000


def frec_inte(sample,indice):
    #indice = "Frecuencias/98.3/" +str(ind)+">Frecuencia 98.3"
    #print(f"Soy la {indice}--- id de Proceso: {os.getpid()}")
    #sample_rate_fm = 240000  # decimate by 10
    #lockm.acquire
    #indice="demodulado.mp3"
    iq_comercial = signal.decimate(sample, int(sample_rate // sample_rate_fm))  # iq_samples


    angle_comercial = np.unwrap(np.angle(iq_comercial))
    demodulated_comercial = np.diff(angle_comercial)
    #time.sleep(10)

    audio_rate = 48000
    audio_comercial = signal.decimate(demodulated_comercial, \
                                      sample_rate_fm // audio_rate, zero_phase=True)
    #lockm.release()
    audio_comercial = np.int16(1e4 * audio_comercial)
#print("Guadando .dat ....")
 #   with open('listfile.data', 'wb') as filehandle:
  #      pickle.dump(audio_comercial, filehandle)
    #print("Escribiendo wavfile.....")
    #wavfile.write("Audio/Frecuencia 98.3", rate=audio_rate, data=audio_comercial)
    sf.write('Audio/'+str(indice)+'>audio.wav', audio_comercial, 48000)
    #pf0 = Process(target=wavfile.write(indice, rate=audio_rate, data=audio_comercial))
    #pf0.start()
    #pf0.join()
    #wavfile.write(indice, rate=audio_rate, data=audio_comercial)
    print("Archivo generado: "+str(indice)+">audio")








def select_frec_nucleo_2(lista, fec_pos, direccion_nombre):
    f_shift = fec_pos #-400000
    #print(f"Soy la {direccion_nombre}--- id de Proceso: {os.getpid()}")
    #print(f"Soy la {direccion_nombre}--- ")
    #lockm.acquire()
    iq_shifted = lista * \
                 np.exp(1j * 2 * np.pi * f_shift / sample_rate * np.arange(len(lista)))

    iq_comercial = signal.decimate(iq_shifted, int(sample_rate // sample_rate_fm))  # iq_samples


    angle_comercial = np.unwrap(np.angle(iq_comercial))
    demodulated_comercial = np.diff(angle_comercial)

    audio_rate = 44100
    audio_comercial = signal.decimate(demodulated_comercial, \
                                      sample_rate_fm // audio_rate, zero_phase=True)
    #lockm.release()
    audio_comercial = np.int16(1e4 * audio_comercial)
    wavfile.write(direccion_nombre, rate=audio_rate, data=audio_comercial)
    print("Archivo wav generado en direccion: "+direccion_nombre)



def load():
	with open('Data/muestra.data', 'rb') as filehandle: 
		datos = pickle.load(filehandle)
	return datos


#frec_inte(load())


