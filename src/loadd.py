# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 08:26:15 2024

@author: Admin
"""

import os
import joblib


def get_model(model_path):
    try:
        current_dir = os.path.dirname(__file__)  # Directory of loadd.py
        model_file = os.path.join(current_dir, model_path)
        with open(model_file, "rb") as mh:
            rf = joblib.load(mh)
            return rf
    except FileNotFoundError:
        print(f"Model file not found at: {model_file}")
        return None
    except Exception as e:
        print(f"Failed to load the model: {e}")
        return None
