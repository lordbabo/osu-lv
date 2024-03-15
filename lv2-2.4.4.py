import numpy as np
import matplotlib . pyplot as plt

crna_matrica = np.zeros((50,50))
bijela_matrica = np.ones((50,50))

prvi_red = np.hstack([crna_matrica,bijela_matrica])
drugi_red = np.hstack([bijela_matrica,crna_matrica])

img = np.vstack([prvi_red, drugi_red])

plt.figure()
plt.imshow(img, cmap="gray")
plt.show()