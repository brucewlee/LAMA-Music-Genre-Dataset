import pathlib
from glob import glob

import librosa as lr
import librosa.display as lrd
from pydub import AudioSegment
from pydub.utils import make_chunks

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''function map in respective order
crop_data -> for one-time use, crop music data set into 1min clips

five_sample_load_data
five_sample_plot_waveforms
five_sample_plot_ffts
five_sample_plot_stfts
five_sample_plot_mfccs

load_data -> load 1min cropped music data
plot_waveforms -> make waveforms
plot_ffts -> make ffts
plot_stfts -> make stfts
plot_mfccs -> make mfccs
'''
# choose style sheet
plt.style.use('ggplot')

# give current_path
current_path = str(pathlib.Path(__file__).parent.absolute())


# ONE_TIME_USE_ONLY: crop audio files to 1 mins
def crop_data(option):
    print("-----starting to crop data-----")
    dir_path = current_path + "/Data_Original/"
    exp_path = current_path + "/Data_Cropped/" + option
    target_audio_files = glob(dir_path + option + '/*.wav')
    bptracker = 1
    for target_file in target_audio_files:
        print("-----starting to crop data-----")
        target_audio = AudioSegment.from_file(target_file, "wav") 
        if len(target_audio) >= 60000:
            chunk_length_ms = 60000 
            chunks = make_chunks(target_audio, chunk_length_ms) 
            chunk_to_export = chunks[0]
            print ("exporting----" + str(bptracker))
            chunk_to_export.export(exp_path + "/max1min_cropped" + option + str(bptracker) + ".wav", format="wav")
            bptracker += 1
    return "complete"





################### FIVE_SAMPLE functions for quick testing ###################

# load
def five_sample_load_data(option):
    print("-----starting to fiveSAMPLE load data-----")
    raw_sounds = []
    dir_path = current_path + "/Data_Cropped/"
    target_audio_files = glob(dir_path + option + '/*.wav')
    bptracker = 0
    for target_file in target_audio_files:
        audio, sfreq = lr.load(target_file,sr=22050)
        raw_sounds.append(audio)
        bptracker += 1
        print("Processing" + str(bptracker))
        if bptracker == 5:
            break
    return raw_sounds


# waveform
def five_sample_plot_waveforms(option, raw_sounds):
    print("-----starting to fiveSAMPLE plot waveforms-----")
    exp_path = current_path + "/Sample_Graphs/Waveforms/" + option
    bptracker = 1
    for sound in raw_sounds:
        plt.subplot(5,1,bptracker,autoscale_on=True)
        lrd.waveplot(sound,sr=22050)
        plt.xlabel ("Time(sec)", fontsize = 5)
        plt.ylabel ("Amp", fontsize = 5)
        plt.xticks(fontsize = 5)
        plt.yticks(fontsize = 5)
        bptracker += 1
    #plt.show()
    plt.tight_layout()
    plt.savefig(exp_path + '/waveform_of_' + option + '.png', dpi=300)
    plt.clf()
    

# fft -> spectrum
def five_sample_plot_ffts(option, raw_sounds):
    print("-----starting to fiveSAMPLE plot fft-----")
    exp_path = current_path + "/Sample_Graphs/FFTs/" + option
    bptracker=1
    for sound in raw_sounds:

        fft = np.fft.fft(sound)
        magnitude = np.abs(fft)
        frequency = np.linspace(0, 22050, len(magnitude))
        needed_freq = frequency[:int(len(frequency)/2)]
        needed_mag = magnitude[:int(len(frequency)/2)]

        plt.subplot(5,1,bptracker,autoscale_on=True)
        plt.plot(needed_freq, needed_mag)
        plt.xlabel ("Freq", fontsize = 5)
        plt.ylabel ("Mag", fontsize = 5)
        plt.xticks(fontsize = 5)
        plt.yticks(fontsize = 5)
        bptracker+=1

    #plt.show()
    plt.tight_layout()
    plt.savefig(exp_path + '/FFT_of_' + option + '.png', dpi=300)
    plt.clf()


# stft -> spectogram
def five_sample_plot_stfts(option, raw_sounds):
    print("-----starting to fiveSAMPLE plot stft-----")
    exp_path = current_path + "/Sample_Graphs/STFTs/" + option
    bptracker=1
    for sound in raw_sounds:

        n_fft = 2048
        hop_length = 512

        stft = lr.core.stft(sound, hop_length=hop_length, n_fft=n_fft)
        spectrogram = np.abs(stft)
        log_spectogram = lr.amplitude_to_db(spectrogram)

        plt.subplot(5,1,bptracker,autoscale_on=True)
        lrd.specshow(log_spectogram, sr=22050, hop_length=hop_length)
        plt.xlabel ("Time", fontsize = 5)
        plt.ylabel ("Freq", fontsize = 5)
        plt.xticks(fontsize = 5)
        plt.yticks(fontsize = 5)
        bptracker+=1

    #plt.show()
    plt.tight_layout()
    plt.savefig(exp_path + '/STFT_of_' + option + '.png', dpi=300)
    plt.clf()


# mfcc
def five_sample_plot_mfccs(option, raw_sounds):
    print("-----starting to fiveSAMPLE plot mfcc-----")
    exp_path = current_path + "/Sample_Graphs/MFCCs/" + option
    bptracker=1
    for sound in raw_sounds:

        MFCC = lr.feature.mfcc(sound, n_fft = 2048, hop_length = 512, n_mfcc = 15)

        plt.subplot(5,1,bptracker,autoscale_on=True)
        lrd.specshow(MFCC, sr=22050, hop_length=512)
        plt.xlabel ("Time", fontsize = 5)
        plt.ylabel ("MFCC", fontsize = 5)
        plt.xticks(fontsize = 5)
        plt.yticks(fontsize = 5)
        bptracker+=1

    #plt.show()
    plt.tight_layout()
    plt.savefig(exp_path + '/MFCC_of_' + option + '.png', dpi=300)
    plt.clf()




################### full-run functions for through testing ###################

# load
def load_data(option):
    print("-----starting to load data-----")
    raw_sounds = []
    dir_path = current_path + "/Data_Cropped/"
    target_audio_files = glob(dir_path + option + '/*.wav')
    bptracker = 0
    for target_file in target_audio_files:
        audio, sfreq = lr.load(target_file,sr=22050)
        raw_sounds.append(audio)
        bptracker += 1
        print("Loading" + str(bptracker))
    return raw_sounds


# waveform
def plot_waveforms(option, raw_sounds):
    print("-----starting to plot waveforms-----")
    exp_path = current_path + "/Graphs/Waveforms/" + option
    bptracker = 0
    for sound in raw_sounds:
        lrd.waveplot(sound,sr=22050)
        plt.xlabel ("Time(sec)", fontsize = 5)
        plt.ylabel ("Amp", fontsize = 5)
        plt.xticks(fontsize = 5)
        plt.yticks(fontsize = 5)
        bptracker += 1
        plt.savefig(exp_path + '/waveform_of_' + option + str(bptracker) + '.png', dpi=500)
        print("Plotting" + str(bptracker))
        plt.clf()


# fft -> spectrum
def plot_ffts(option, raw_sounds):
    print("-----starting to plot fft-----")
    exp_path = current_path + "/Graphs/FFTs/" + option
    bptracker = 0
    for sound in raw_sounds:

        fft = np.fft.fft(sound)
        magnitude = np.abs(fft)
        frequency = np.linspace(0, 22050, len(magnitude))
        needed_freq = frequency[:int(len(frequency)/2)]
        needed_mag = magnitude[:int(len(frequency)/2)]

        plt.plot(needed_freq, needed_mag)
        plt.xlabel ("Freq", fontsize = 5)
        plt.ylabel ("Mag", fontsize = 5)
        plt.xticks(fontsize = 5)
        plt.yticks(fontsize = 5)

        bptracker += 1
        plt.savefig(exp_path + '/FFT_of_' + option + str(bptracker) + '.png', dpi=500)
        print("Plotting" + str(bptracker))
        plt.clf()


# STFTs -> spectogram
def plot_stfts(option, raw_sounds):
    print("-----starting to plot stft-----")
    exp_path = current_path + "/Graphs/STFTs/" + option
    bptracker = 0
    for sound in raw_sounds:
        
        n_fft = 2048
        hop_length = 512

        stft = lr.core.stft(sound, hop_length=hop_length, n_fft=n_fft)
        spectrogram = np.abs(stft)
        log_spectogram = lr.amplitude_to_db(spectrogram)

        lrd.specshow(log_spectogram, sr=22050, hop_length=hop_length)
        plt.xlabel ("Time", fontsize = 5)
        plt.ylabel ("Freq", fontsize = 5)
        plt.xticks(fontsize = 5)
        plt.yticks(fontsize = 5)

        bptracker += 1
        plt.savefig(exp_path + '/STFT_of_' + option + str(bptracker) + '.png', dpi=500)
        print("Plotting" + str(bptracker))
        plt.clf()

# mfcc
def plot_mfccs(option, raw_sounds):
    print("-----starting to plot mfcc-----")
    exp_path = current_path + "/Graphs/MFCCs/" + option
    bptracker=1
    for sound in raw_sounds:

        MFCC = lr.feature.mfcc(sound, n_fft = 2048, hop_length = 512, n_mfcc = 15)

        plt.subplot(5,1,bptracker,autoscale_on=True)
        lrd.specshow(MFCC, sr=22050, hop_length=512)
        plt.xlabel ("Time", fontsize = 5)
        plt.ylabel ("MFCC", fontsize = 5)
        plt.xticks(fontsize = 5)
        plt.yticks(fontsize = 5)
        bptracker+=1

    #plt.show()
    plt.tight_layout()
    plt.savefig(exp_path + '/MFCC_of_' + option + '.png', dpi=300)
    plt.clf()




################### Caller ###################

if __name__ == '__main__':

    #covered regions
    regions = ["Asia", "Africa", "LatinAmerica", "MiddleEastern"]

    #five_samplers
    '''
    sample_raw_sounds_Asia = five_sample_load_data("Asia")
    sample_raw_sounds_Africa = five_sample_load_data("Africa")
    sample_raw_sounds_LatinAmerica = five_sample_load_data("LatinAmerica")
    sample_raw_sounds_MiddleEastern = five_sample_load_data("MiddleEastern")

    five_sample_plot_waveforms("Asia", sample_raw_sounds_Asia)
    five_sample_plot_ffts("Asia", sample_raw_sounds_Asia)
    five_sample_plot_stfts("Asia",sample_raw_sounds_Asia)
    five_sample_plot_mfccs("Asia",sample_raw_sounds_Asia)

    five_sample_plot_waveforms("Africa", sample_raw_sounds_Africa)
    five_sample_plot_ffts("Africa", sample_raw_sounds_Africa)
    five_sample_plot_stfts("Africa", sample_raw_sounds_Africa)
    five_sample_plot_mfccs("Africa", sample_raw_sounds_Africa)

    five_sample_plot_waveforms("LatinAmerica", sample_raw_sounds_LatinAmerica)
    five_sample_plot_ffts("LatinAmerica", sample_raw_sounds_LatinAmerica)
    five_sample_plot_stfts("LatinAmerica", sample_raw_sounds_LatinAmerica)
    five_sample_plot_mfccs("LatinAmerica", sample_raw_sounds_LatinAmerica)

    five_sample_plot_waveforms("MiddleEastern", sample_raw_sounds_MiddleEastern)
    five_sample_plot_ffts("MiddleEastern", sample_raw_sounds_MiddleEastern)
    five_sample_plot_stfts("MiddleEastern", sample_raw_sounds_MiddleEastern)
    five_sample_plot_mfccs("MiddleEastern", sample_raw_sounds_MiddleEastern)
    '''

    #full graph generation
    bptracker = 0
    for region in regions:

        # Progress Tracker
        print ('Progress: {}/{} tasks processed'.format(bptracker, len(regions)*5))
        bptracker += 1

        '''Crop'''
        #crop_data(region)

        '''LoadData'''
        raw_sounds = load_data(region)

        # Progress Tracker
        print ('Progress: {}/{} tasks processed'.format(bptracker, len(regions)*5))
        bptracker += 1

        '''Waveforms'''
        plot_waveforms(region, raw_sounds)

        # Progress Tracker
        print ('Progress: {}/{} tasks processed'.format(bptracker, len(regions)*5))
        bptracker += 1

        '''FFTs'''
        plot_ffts(region, raw_sounds)

        # Progress Tracker
        print ('Progress: {}/{} tasks processed'.format(bptracker, len(regions)*5))
        bptracker += 1

        '''STFTs'''
        plot_stfts(region,raw_sounds)

        # Progress Tracker
        print ('Progress: {}/{} tasks processed'.format(bptracker, len(regions)*5))
        bptracker += 1

        '''MFCCs'''
        plot_stfts(region,raw_sounds)