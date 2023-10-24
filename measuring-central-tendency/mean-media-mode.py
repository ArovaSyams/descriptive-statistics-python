import numpy as np
from scipy import stats

jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])

# mean
print(jumlah_kucing.mean())
print(np.mean(jumlah_kucing))

# median
print(np.median(jumlah_kucing))

mode_kucing = stats.mode(jumlah_kucing)[0]
print(mode_kucing)