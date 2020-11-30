'''
credits to 
Valerio Velardo
Github: musikalkemist
'''
import os
import librosa
import math
import json

DATASET_PATH = "Data_Cropped"
JSON_PATH = "training_data.json"

SAMPLE_RATE = 22050
DURATION = 30 # unit is seconds
SAMPLES_PER_TRACK = SAMPLE_RATE * DURATION

def save_mfcc(dataset_path, json_path, n_mfcc=13, n_fft=2048, hop_length=512, num_segments=5):
    
    data={
        "mapping": [],
        "mfcc": [],
        "labels": []
    }

    num_samples_per_segment = int(SAMPLES_PER_TRACK / num_segments)
    expected_num_mfcc_vectors_per_segment = math.ceil(num_samples_per_segment / hop_length) # 1.2 -> 2

    # loop through all the genres
    for bptracker, (dirpath, dirnames, filenames) in enumerate(os.walk(dataset_path)):
        
        # check that we're not at the root level
        if dirpath is not dataset_path:

            dirpath_components = dirpath.split("/")
            semantic_label = dirpath_components[-1]
            data["mapping"].append(semantic_label)
            print("\nProcessing: {}".format(semantic_label))

            # process files for a specific genre
            for f in filenames:

                # load audio file
                file_path = os.path.join(dirpath, f)
                signal, sr = librosa.load(file_path, sr=SAMPLE_RATE)

                # process and store segment data (MFCC)
                for s in range(num_segments):
                    try:
                        start_sample = num_samples_per_segment * s # s=0 -> 0
                        finish_sample = start_sample + num_samples_per_segment # s=0 -> num_samples_per_segment
                        
                        try:
                            mfcc = librosa.feature.mfcc(signal[start_sample: finish_sample],sr=SAMPLE_RATE, n_fft=n_fft, n_mfcc=n_mfcc, hop_length=hop_length)
                            mfcc = mfcc.T
                        except:
                            pass

                        # store mfcc for segment if it has the expected length
                        if len(mfcc) == expected_num_mfcc_vectors_per_segment:
                            data["mfcc"].append(mfcc.tolist())
                            data["labels"].append(bptracker - 1)
                            print("{}, segment:{}".format(file_path, s+1))
                    except:
                        pass


    with open(JSON_PATH, "w") as fp:
        json.dump(data, fp, indent=4)

if __name__ == "__main__":
    save_mfcc(DATASET_PATH, JSON_PATH, num_segments=10)