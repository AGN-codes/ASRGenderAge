
# age predictor model
import torch
from tensorflow import keras
import librosa

import os
def get_age():
    os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
    # put the absolute path of the code folder and files here (leads to age_regression-mfcc):
    model = keras.models.load_model('/.../age_regression-mfcc/')
    # put the absolute path of the code folder and files here (leads to new_file.wav, the converted voice message):
    y, sr = librosa.load("/.../new_file.wav", sr = 48000)
    data = librosa.feature.mfcc(y = y, sr = sr, n_mfcc = 30, hop_length = int(y.shape[0]/199))
    input_vector = data[:,:].T.reshape(-1,200,30)
    a = torch.tensor(model.predict(input_vector)).item()
    return ' & age: ' + str(round(a))