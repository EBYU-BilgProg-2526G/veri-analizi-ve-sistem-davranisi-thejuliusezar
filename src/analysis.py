# -*- coding: utf-8 -*-
"""
Temel sinyal analiz fonksiyonları
"""

import numpy as np

def sampling_rate(t):
    dt = np.gradient(t)
    
    fs = np.mean(1 / dt) 
    
    return fs


def basic_stats(x):
    Mean = np.mean(x)
    Std = np.std(x)
    Rms = np.sqrt(np.mean(x**2))
    Min = np.min(x)
    Max = np.max(x)
    

    with open("report.csv", "w", newline = "", encoding="utf-8") as file: 
        
        yazici = file.write()
        yazici.writerow(["Mean",  "Std", "Rms", "Min", "Max"])
        yazici.writerows(["Mean", Mean], ["Std", Std], ["Rms", Rms], ["Min", Min], ["Max", Max])
        
    return Mean, Std, Rms, Min, Max
