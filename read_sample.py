from rtlsdr import RtlSdr
import pickle
import numpy

sdr = RtlSdr()
sdr.sample_rate =sample_rate= 2.4e6
sdr.center_freq = 96.3e6#96.3e6
sdr.gain = 40
#sample_rate_fm = 240000


def read_sample():
  
  samples_1=[]
  samples_2=[]
  samples_3=[]
  print("Leyendo muestra ...")

  	
  samples_1=sdr.read_samples(8150*1024)
  samples_2=sdr.read_samples(8150*1024)
  samples_3=sdr.read_samples(8150*1024)
    #samples_3= sdr.read_samples(8000*1024)
  samples_2 = numpy.append(samples_1,samples_2)
  samples_3= numpy.append(samples_2,samples_3)
   

  return samples_3


def guardar():

  data =read_sample()
  print("Guardando...")
  filen ="muestra.data"  
  #f = open(filen, 'wb')
  #f.write(data)
  with open(filen,'wb') as filehandle:
    pickle.dump(data, filehandle)
  return



#guardar()




