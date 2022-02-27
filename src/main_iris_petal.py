import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from myConvexHull import *

""" Iris DataFrame  """
data = datasets.load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)

""" Iris DataFrame Convex Hull Visualization """
plt.figure(figsize = (10, 6))
plt.title('Petal Length vs Petal Width')
plt.xlabel(data.feature_names[2])
plt.ylabel(data.feature_names[3])
for i in range(len(data.target_names)):
    # Find points (x,y) for each target
    bucket = df[df['Target'] == i]
    length = len(bucket)
    arrXY = []
    for j in range(length):
        try:
            x = bucket.loc[j+bucket.first_valid_index()][2]
            y = bucket.loc[j+bucket.first_valid_index()][3]
        except KeyError:
            continue
        else:
            arrXY.append([x,y])

    # Convex Hull Points
    hull = []
    ConvexHull(arrXY, result = hull)

    # Points Scatter Plot
    arrX, arrY = zip(*arrXY)
    plt.scatter(arrX, arrY, label = data.target_names[i])
    
    # Convex Hull Plot
    hullX, hullY = zip(*hull)
    plt.plot(hullX, hullY)

plt.legend()
plt.show()