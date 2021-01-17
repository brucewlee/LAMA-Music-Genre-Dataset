# LAMA : A World Music Genre Dataset
> LAMA - LatinAmerica, Asia, MiddleEastern, Africa Genre Dataset

This Dataset consists of the .wav files, training dataset (MFCC), and graph plots (FFTs, MFCCs, STFTs, Waveforms) of YouTube videos classified into four categories: LatinAmerica, Asia, MiddleEastern, and Africa. 

I hope that this work can help in several Deep Learning, Machine Learning projects in *Music Genre Classification*. 

<p align="left">
<img src="/readme_images/LAMA-LOGO.png" alt="MusicGenreClassification" width="400">
</p>

**Anyone is free to use/change/contribute to this Dataset. Please cite if you use this Dataset in your research/projects.**

## Getting Started
> Some data couldn't be uploaded to GitHub because the file size was too large. Instead, I attached a Harvard Dataverse link below to retrieve the data.

The data contained in **LAMA** can be classified into three categories: 
1. **.wav files** (`Data_Original`, `Data_Cropped`) -> Uploaded in Harvard Dataverse. Link below.
2. **Waveform, FFT, STFT, MFCC graph plots** (`Graphs`, `Sample_Graphs`) -> Uploaded in Harvard Dataverse. Link below.
3. **mfcc training data** (`training_data.json`)

## Statistics
- `Data_Original` : 113 (Africa), 83 (Asia), 90 (LatinAmerica), 80 (MiddleEast)
- `Data_Cropped` (1 min clips of original) : 108 (Africa), 77 (Asia), 87 (LatinAmerica), 77 (MiddleEast)
- `Graphs` -> FFT : 108 (Africa), 77 (Asia), 87 (LatinAmerica), 77 (MiddleEast)

[Link to the full audio data](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/13BPFB)

### graph plot EXAMPLES:
*from `Graphs`*
![Image of SFTS](/readme_images/SFTS_example.png)
*from `Sample_Graphs`*
![Image of MFCC](/readme_images/MFCC_example.png)

## Acknowledgements
The classification of genre in this Dataset is mostly from the "AudioSet" project by the Sound and Video Understanding teams at Google Research. I chose the best examples from their website and preprocessed them to create this Dataset.

In addition, I obtained much of the knowledge needed to create this Dataset from the YouTube Channel, "Valerio Velardo - The Sound of AI. Mr. Velardo makes amazing videos, and I believe that he deserves more recognition.

## Citing this DataSet
```
@data{DVN/13BPFB_2020,
author = {Lee, Bruce W},
publisher = {Harvard Dataverse},
title = {{LAMA World Music Genre Dataset}},
year = {2020},
version = {DRAFT VERSION},
doi = {10.7910/DVN/13BPFB},
url = {https://doi.org/10.7910/DVN/13BPFB}
}
```
