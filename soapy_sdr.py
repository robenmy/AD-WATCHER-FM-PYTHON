import simplesoapy
import numpy
import pickle

# List all connected SoapySDR devices
print(simplesoapy.detect_devices(as_string=True))

# Initialize SDR device
sdr = simplesoapy.SoapyDevice('driver=sdrplay')

# Set sample rate
sdr.sample_rate = 3e6

# Set center frequency
sdr.freq = 96.3e6
sdr.start_stream()
# Setup base buffer and start receiving samples. Base buffer size is determined
# by SoapySDR.Device.getStreamMTU(). If getStreamMTU() is not implemented by driver,
# SoapyDevice.default_buffer_size is used instead

def read_sample():
    
    samples = numpy.empty(len(sdr.buffer) * 600, numpy.complex64)
    sdr.read_stream_into_buffer(samples)

    return samples




def stop():
    # Stop receiving
    sdr.stop_stream()

def capturarSamples():
    data = read_sample()
    print("Guardando data...")
    file = "muestra.data"

    with open(file,'wb') as filehandle:
        pickle.dump(data,filehandle)
    return

#capturarSamples()
#stop()