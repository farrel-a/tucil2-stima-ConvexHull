import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
import matplotlib.pyplot as plt
from myConvexHull import *

""" Linnerud DataFrame """
data = datasets.load_wine()
df = pd.DataFrame(data.data, columns = data.feature_names)
df['Target'] =  pd.DataFrame(data.target)

""" Digits DataFrame Convex Hull Visualization """
plt.figure(figsize = (10, 6))
plt.title('Alcohol vs Alcalinity of Ash')
plt.xlabel(data.feature_names[0])
plt.ylabel(data.feature_names[3])
for i in range(len(data.target_names)):
    bucket = df[df['Target'] == i]
    length = len(bucket)
    arrXY = []
    for j in range(length):
        try:
            x = bucket.loc[j+bucket.first_valid_index()][0]
            y = bucket.loc[j+bucket.first_valid_index()][1]
        except KeyError:
            continue
        else:
            arrXY.append([x,y])

    hull = []
    ConvexHull(arrXY, result = hull)

    arrX, arrY = zip(*arrXY)
    plt.scatter(arrX, arrY, label = data.target_names[i])
    
    hullX, hullY = zip(*hull)
    plt.plot(hullX, hullY)
plt.legend()
plt.show()