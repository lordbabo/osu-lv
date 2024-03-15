import numpy as np
import matplotlib . pyplot as plt
img = plt . imread ("road.jpg")
img = img [:,:,0]. copy ()
print ( img . shape )
print ( img . dtype )
plt . figure ()
plt . imshow (img , cmap ="gray", alpha = 0.5)
plt . show ()

plt.imshow(img[:,150:300], cmap="gray")
plt.show()

plt.imshow(np.rot90(img,3), cmap="gray")
plt.show()

plt.imshow(np.flip(img,axis=1),cmap="gray")
plt.show()
