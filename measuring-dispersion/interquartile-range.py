import numpy as np

jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])

# menghitung quartile 3 dikurang kuartil 1
iqr = np.percentile(jumlah_kucing, 75) - np.percentile(jumlah_kucing, 25)

print(iqr)