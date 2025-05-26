# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 08:26:15 2024

@author: Admin
"""

import os
import joblib


import joblib
import os


def get_model(model_path):
    try:
        # Get absolute path relative to the current script
        base_path = os.path.dirname(os.path.abspath(__file__))
        # One level up from src
        full_path = os.path.join(base_path, "..", model_path)
        print(f"Loading model from: {full_path}")
        with open(full_path, "rb") as mh:
            rf = joblib.load(mh)
            return rf
    except FileNotFoundError:
        print(f"Model file not found at: {full_path}")
        return None
    except Exception as e:
        print(f"Failed to load the model: {e}")
        return None
