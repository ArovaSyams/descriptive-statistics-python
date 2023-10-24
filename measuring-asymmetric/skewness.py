import numpy as np
import pandas as pd
 
jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])

# Skewness merupakan parameter statistik yang digunakan untuk mengukur kesimetrisan sebuah distribusi data. 
kucing_series = pd.Series(jumlah_kucing)

skewness = kucing_series.skew()
print(skewness)