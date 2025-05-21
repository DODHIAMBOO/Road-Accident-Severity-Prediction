# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 08:26:15 2024

@author: Admin
"""

import joblib

def get_model(model_path):
    try:
        # Try to load the model from the specified local path
        with open(model_path, "rb") as mh:
            rf = joblib.load(mh)
            return rf
    except FileNotFoundError:
        print(f"Model file not found at {model_path}")
        return None
    except Exception as e:
        print(f"Failed to load the model: {e}")
        return None

# Usage example
model_path = "rt_reduced.joblib"
model = get_model(model_path)
if model:
    print("Model loaded successfully")
else:
    print("Failed to load the model")
