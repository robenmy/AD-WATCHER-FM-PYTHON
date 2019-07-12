
import demudalate_sample as dem
#import read_sample as sdr
import threading
import audioToFingerprint as af
import client
import datetime

indice =1
if __name__ == '__main__':
	while True:
		#sdr.guardar()
		now = datetime.datetime.now()
		client.client()
		print(f"Hora: {now.hour}:{now.minute}")
		t0 = threading.Thread(target=dem.frec_inte, args=(dem.load(), indice,))
		t1 = threading.Thread(target=af.fingerprint, args=(indice,now.hour,now.minute,))
		t0.start()
		t1.start()
		indice +=1
	
	
	
	
	