#import matplotlib
import numpy
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves
from scipy import signal
import scipy
import fingerprint # se importa el archivo .py y para usar una funcion primero se # usa ese nombre
import WavHelp
import pickle


archivo = 'Ads/aster.wav'
#archivo = 'Comerciales/BIMBO-SPOT RADIO.wav'
muestreo, sonido = waves.read(archivo)
print(muestreo)

#monoa = sonido[:,0]

print("--- O K ---")


a = []
lista =[]
a =fingerprint.fingerprint(sonido)
#a =fingerprint.fingerprint(monoa)

for aw in a:
    #print(aw[0])
    lista.append(aw)

print("Tamano:" +str(len(lista)))
#print(lista)

#------------------------------- Parte 2 ----------------------------------
#-------------------------------------------------------------------------5
num=1
arreglo=[]

while num <(114):
	print("---Numero en seguimiento: "+str(num))
	archivo = 'Audio/'+str(num)+'>audio.wav'
	muestreo, sonido1 = waves.read(archivo)
	print(muestreo)

	#mono = sonido1[:,0]
	print("--- O K ---")
	b = []
	listab =[]
	b =fingerprint.fingerprint(sonido1)

	#b =fingerprint.fingerprint(mono)
	#with open('listfile.data', 'rb') as filehandle:
	#	placesListopen = pickle.load(filehandle)
	#b =fingerprint.fingerprint(placesListopen)

	for bw in b:
		listab.append(bw)
		#print("Tamano lista A:" +str(len(lista)))
		#print("Tamano lista B:" +str(len(listab)))

# -------------------------- Similitudes ----------------
	count =0
	for h in lista:
		for r in listab:
			if h[0] == r[0]:
				if h[0] == r[0]:
					count +=1
	print("Similitudes: "+str(count))
	num+=1

	if count >20:
		arreglo.append(archivo)
		arreglo.append(count)




print(arreglo)
print("Cantidad de iguales:"+str((len(arreglo))/2))









 




    #print(bw[0])
    








    
        
           




# ---------------------- comparacion
