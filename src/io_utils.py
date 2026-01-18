# -*- coding: utf-8 -*-
"""
CSV dosyasından sinyal verisi okuma yardımcı fonksiyonları
"""

import csv 
import numpy as np 

def load_signal_csv(path):
    with open(path, "r", encoding="utf-8") as f:
        okuyucu = csv.reader(f)
        
        t_list = []
        x_list = []
        
        
        for i, j in okuyucu:
        
            try: 
                t_list.append(float(i))
                x_list.append(float(j))
            except ValueError:
                continue
        
    t = np.array(t_list)
    x = np.array(x_list)
    
    return t, x 
