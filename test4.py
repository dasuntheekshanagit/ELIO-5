from matplotlib import pyplot as plt
from skimage.io import imread
import numpy as np

def line_curve():
    H = np.hstack((x ** 2, x, ones))
    return H

image = imread(r"image8.png",as_gray=True)

mean = image.mean()
print(mean)

filter_image = image > mean

x = []
y = []

j = 0

#print(filter_image)
for row in filter_image:
    i = 0
    j += 1
    for colomn in row:
        i += 1
        if not(colomn):
            x.append(i)
            y.append(j) # len(row)-i)

x = np.array(x).reshape((len(x),1))
y = np.array(y).reshape((len(y), 1))

ones = np.ones(len(x)).reshape((len(x), 1))

H = line_curve()

abc1 = np.linalg.inv(np.dot(H.T,H))
abc2 = np.dot(H.T,y)

abc = np.dot(abc1,abc2)
print(abc)
yhat = np.dot(H,abc)
#print(x)
#print(len(yhat))
for i in range(0,len(yhat),500):
    #print(i)
    plt.plot(x,yhat,'w.')

plt.imshow(filter_image)
plt.show()
