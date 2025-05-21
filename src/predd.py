# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 08:33:20 2024

@author: Admin
"""

import joblib
import gdown
import numpy as np
import os

def ordinal_encoder(input_val, feats):
    feat_val = list(1 + np.arange(len(feats)))
    feat_key = feats
    feat_dict = dict(zip(feat_key, feat_val))
    value = feat_dict[input_val]
    return value



def get_prediction(data, model):
    """
    Predict the class of a given data point.
    """
    severity = ["Fatal injury", "Serious Injury", "Slight Injury"]
    
    try:
        pred = model.predict(data)
        return severity[pred[0] - 1]
    except Exception as e:
        print(f"Failed to make predictions: {e}")
        return None


