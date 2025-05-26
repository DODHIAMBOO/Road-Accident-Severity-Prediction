# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 08:26:15 2024

@author: Admin
"""

import os
import joblib


def get_model(model_path):
    try:
        current_dir = os.path.dirname(__file__)
        model_file = os.path.join(current_dir, model_path)
        with open(model_file, "rb") as mh:
            rf = joblib.load(mh)
            return rf
    except FileNotFoundError:
        return None
    except Exception:
        return None
