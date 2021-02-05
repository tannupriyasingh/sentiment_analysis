from pathlib import Path
from live_predictions import LivePredictions
from audio_input import audio_input
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import os
import pandas as pd
import librosa
import glob 
import librosa.display

import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

while True:
    fname = Path( Path().cwd(), f'audio_liLivePredictions.wav')
    audio_input.audio_input(fname)
    live_prediction = LivePredictions(file=str(fname))
    val = live_prediction.make_predictions()

    data, sampling_rate = librosa.load(str(fname))
    plt.figure(figsize=(5, 5))
    librosa.display.waveplot(data, sr=sampling_rate, color='r')

    plt.show(block=False)
    plt.pause(1)
    plt.close()

    if val in ['disgust', 'angry', 'fearful', 'sad']:
        code = 0
    elif val in ['happy', 'surprised']:
        code = 1
    else:
        code = 2 # neutral, calm

    with open('game_state.txt', 'w') as f:
        f.write(str(code))
    print(val)
