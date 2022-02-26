import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
import matplotlib.pyplot as plt
from myConvexHull import *


data = datasets.load_iris()
#create a DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)
df.head()

#visualisasi hasil ConvexHull
plt.figure(figsize = (10, 6))
plt.title('Sepal Width vs Sepal Length')
plt.xlabel(data.feature_names[0])
plt.ylabel(data.feature_names[1])
for i in range(len(data.target_names)):
    bucket = df[df['Target'] == i]
    length = len(bucket)
    arrXY = []
    for i in range(length):
        x = bucket.loc[i+bucket.first_valid_index()][0]
        y = bucket.loc[i+bucket.first_valid_index()][1]
        arrXY.append([x,y])
    arrXY.sort()
    hull = []
    ConvexHull(arrXY, [], [], 0, hull, False)
    hull = sort_cw(hull)
    hull.append(hull[0])

    arrX, arrY = zip(*arrXY)
    plt.scatter(arrX, arrY)
    
    hullX, hullY = zip(*hull)
    plt.plot(hullX, hullY)

plt.legend()
plt.show()