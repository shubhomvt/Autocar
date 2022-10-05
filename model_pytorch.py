import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint
from keras.layers import Lambda, Conv2D, MaxPooling2D, Dropout, Dense, Flatten
from utils import INPUT_SHAPE, batch_generator
import argparse
import os

import torch
import torch.nn as nn
import torchvision.transforms.functional as TF

def load_data():
    data_df = pd.read_csv('driving_log.csv')
    print(data_df)
    # X = data_df[['center','left','right']].values
    # y = data_df['steering'].values

    # X_train, X_valid, y_train, y_valid = train_test_split(X,y, test_size=0.2,random_state=0)#
    # #0.2 input
    # return X_train, X_valid, y_train, y_valid

load_data()
