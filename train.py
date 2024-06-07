import os
import librosa
import numpy as np
from python_speech_features import mfcc
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

# Data Collection
def collect_voice_samples(audio_folder):
    voice_samples = []
    labels = []

    # Collect authorized user's voice samples
    for i in range(1, 48):
        audio_file = os.path.join(audio_folder, f"PedroVoice{i}.wav")
        voice_sample, sr = librosa.load(audio_file, sr=None)
        voice_samples.append(voice_sample)
        labels.append(1)  # Label 1 for authorized user

    # Collect random voice samples (unauthorized users)
    for i in range(1, 40):
        audio_file = os.path.join(audio_folder, f"{i}.wav")
        voice_sample, sr = librosa.load(audio_file, sr=None)
        voice_samples.append(voice_sample)
        labels.append(0)  

    return voice_samples, labels

# Feature Extraction
def extract_features(voice_samples, max_length):
    features = []
    for sample in voice_samples:
        mfcc_features = mfcc(sample, sample_rate)
        if mfcc_features.shape[0] < max_length:
            pad_width = ((0, max_length - mfcc_features.shape[0]), (0, 0))
            mfcc_features = np.pad(mfcc_features, pad_width, mode='constant')
        else:
            mfcc_features = mfcc_features[:max_length, :]
        features.append(mfcc_features.flatten())
    return features

# Model Training
def train_model(features, labels):
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

    svm = SVC(kernel='linear', probability=True)
    svm.fit(X_train, y_train)
    return svm

# Save Model
def save_model(model, model_path):
    import joblib
    joblib.dump(model, model_path)

# Parameters
sample_rate = 16000
audio_folder = 'audios'
model_path = 'voice_auth_model.pkl'
max_length = 200

# Collect voice samples
voice_samples, labels = collect_voice_samples(audio_folder)

# Extract features
features = extract_features(voice_samples, max_length)

# Train the model
model = train_model(features, labels)

# Save the trained model
save_model(model, model_path)