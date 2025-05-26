# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 08:26:15 2024

@author: Admin
"""

import os
import joblib


def get_model(model_path):
    try:
        full_path = os.path.join(os.path.dirname(__file__), model_path)
        with open(full_path, "rb") as mh:
            rf = joblib.load(mh)
            return rf
    except FileNotFoundError:
        print(f"Model file not found at: {full_path}")
        return None
    except Exception as e:
        print(f"Failed to load the model: {e}")
        return None
