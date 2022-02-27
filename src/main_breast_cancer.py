import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
import matplotlib.pyplot as plt
from myConvexHull import *

""" Breast Cancer DataFrame """
data = datasets.load_breast_cancer()
df = pd.DataFrame(data.data, columns = data.feature_names)
df['Target'] = pd.DataFrame(data.target)

""" Breast Cancer Dataframe Convex Hull Visualization """
plt.figure(figsize = (10, 6))
plt.title('Mean Radius vs Mean Texture')
plt.xlabel(data.feature_names[0])
plt.ylabel(data.feature_names[1])
for i in range(len(data.target_names)):
    # Find points (x,y) for each target
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