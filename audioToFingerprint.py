import pickle
import scipy.io.wavfile as waves
from scipy import signal
import scipy
import fingerprint as fp 
import os
import time
import userdb


def dbsearch(hora, minutos,ap,lista):
	h = int(hora)
	m = int(minutos)

	if m<55 and m>5:
		m=m-5

	if m>= 55:
		me = 59-m
		m = m-me

	for i in range(10):

		if m == 59 and h==12:
			h=1
			m=0
		if m == 59 and h>0 and h<=11:
			m =0
			h+=1
		m+=1
		ho = str(h)
		mi = str(m)

		a,b =userdb.busquedaFing(ho,mi,ap)
		if a[0] !=0:
			print(a)
			print(b)
			comparacion(lista,b)   # comparar lista de datos 
		
		


def comparacion(lista1,lista2):
	contador = 0
	for i in lista1:
		for j in  lista2:
			if i==j:
				contador+=1

	if contador>3:
		print("++++++++++++++")
		print(f"----Existe Similitud---- Datos iguales: {contador}")
		print("++++++++++++++")
	else:
		print("NO EXISTEN SIMILITUDES")
	




			

#########################################################333
def fingerprint(index, hora, minutos):
	filename = ">audio.wav"
	direccion="Audio/"+str(index)+filename
	#direccion2 = "Ads/tauroturbo.wav"
	while True:
		time.sleep(1)
		if os.path.isfile(direccion):
			muestreo, sonido = waves.read(direccion)
			print(direccion)
			#monoa = sonido[:,0]
			a =fp.fingerprint(sonido)
			print("Fingerprint generado ..... Numero de Proceso: "+str(os.getpid()))
			lista=[]
			for aw in a:
				lista.append(aw[0])

			#lista2 =None

			#comparacion(lista,lista2)
			dbsearch(hora,minutos,'pm',lista)
			break

  	
	

#dbsearch('5','40','pm',['4','6','8','3'])