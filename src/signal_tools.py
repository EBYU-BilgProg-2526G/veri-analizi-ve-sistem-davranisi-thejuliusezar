# -*- coding: utf-8 -*-
"""
Basit sinyal işleme fonksiyonları
"""

import numpy as np 

def moving_average(x, window_size):
    
    w = np.ones(window_size) / window_size
    
    return np.convolve(x, w, mode = "same")


""" moving_average fonksiyonunu kendim de yaptım fakat grafik çizme noktasında sıkıntılar yarattığı için direk numphy ile yapma kararı aldım.  """


# def moving_average(x, window_size = 10):
    
#     n = len(x)
    
#     hareketli_ortalama = []
#     for i in range(n - window_size + 1):
#         pencere_toplam = 0.0
#         for j in range(i, i + window_size):
#             pencere_toplam += x[j]
#         hareketli_ortalama.append(pencere_toplam / window_size)

#     return hareketli_ortalama
