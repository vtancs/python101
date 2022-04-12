# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 13:19:07 2021

@author: Victor
"""

import numpy as np
import matplotlib.pyplot as plt

p = 1/2
n = np.arange(0,10)
X = np.power(p,n)
plt.bar(n,X)