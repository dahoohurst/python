# -*- coding: utf-8 -*-
"""
Created on Sat May  2 16:36:02 2020

@author: dahoo
"""

import matplotlib.pyplot as plt
import librosa
import numpy as np

musicFileName = './old/vocals.wav'
y, sr = librosa.load(musicFileName, sr=None)


plt.figure(figsize=(14, 5))
librosa.display.waveplot(y, sr=sr)

clips = librosa.effects.split(y, top_db=40)
clipss = clips / sr
seg = np.empty(shape=[0,2])

for i in clipss:
    diff = i[1] - i[0]
    print(i)
    if(diff > 1):
        seg = np.append(seg, [np.array(i)], axis=0)

print(seg)
# =============================================================================
# X = librosa.stft(y)
# Xdb = librosa.amplitude_to_db(abs(X))
# plt.figure(figsize=(14, 5))
# librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
# plt.colorbar()
# =============================================================================
 