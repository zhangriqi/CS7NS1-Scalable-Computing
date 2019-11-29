import matplotlib.pyplot as plt
import scipy
from scipy import signal
from scipy.io import wavfile
import os
import wave
import pylab
import numpy as np


def convert2spectro(files):
    sample_rate, data = scipy.io.wavfile.read(files)
    sample_freq, segment_time, spec_data = signal.spectrogram(data, sample_rate)  
    plt.pcolormesh(segment_time, sample_freq, spec_data )
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.show()  


def convert2spectro2(files):
	graph_spectrogram(files)

def graph_spectrogram(wav_file):
    sound_info, frame_rate = get_wav_info(wav_file)
    pylab.figure(num=None, figsize=(19, 12))
    pylab.subplot(111)
    pylab.title('spectrogram of %r' % wav_file)
    pylab.specgram(sound_info, Fs=frame_rate, NFFT=2048, window=pylab.window_hanning, noverlap=int(256 * 0.5))
    pylab.savefig('spectrogram.png')

def get_wav_info(wav_file):
    wav = wave.open(wav_file, 'r')
    frames = wav.readframes(-1)
    sound_info = pylab.fromstring(frames, 'int16')
    frame_rate = wav.getframerate()
    wav.close()
    return sound_info, frame_rate


#The peaks now are clearly separated
def convert2spectro3(input, output):
    wavList = os.listdir(input)
    for wav in wavList:
        wav_path = input + "/" + wav
        # print(wav_path)
        sample_rate, data = scipy.io.wavfile.read(wav_path)
        f, t, Zxx = signal.stft(data, sample_rate, nperseg=256) 
        # cmap = plt.get_cmap('PiYG')
        plt.pcolormesh(t, f, np.abs(Zxx), alpha = 0.8)
        plt.savefig(output + "/" + wav.strip(".wav"))
        # plt.title('STFT Magnitude')
        # plt.ylabel('Frequency [Hz]')
        # plt.xlabel('Time [sec]')
        # plt.show()  

input_path = '/Users/zhangruiqi/Downloads/TCD/Modules/CS7NS1SC/Project3/audio_wav'
output_path = '/Users/zhangruiqi/Downloads/TCD/Modules/CS7NS1SC/Project3/audio_spectrogram'
# convert2spectro2(filepath)
# convert2spectro2(filepath)
convert2spectro3(input_path, output_path)
