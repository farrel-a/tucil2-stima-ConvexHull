#13520110 - Farrel Ahmad
import pandas as pd
import matplotlib.pyplot as plt
from myConvexHull import *

""" Wheat Seeds DataFrame """
df = pd.read_csv('../test/seeds_dataset.txt', sep="	", header=None, 
names=["Area", "Perimeter", "Compactness", 
       "Length of Kernel", "Width of Kernel", "Asymmetry Coefficient", 
       "Length of Kernel Groove", "Target"])
target_names = ["Class 1", "Class 2", "Class 3"]


""" Wheat Seeds DataFrame Convex Hull Visualization """
plt.figure(figsize = (10, 6))
plt.title('Length of Kernel vs Width of Kernel')
plt.xlabel(df.columns[3])
plt.ylabel(df.columns[4])
for i in range(1, len(target_names) + 1):
    # Find points (x,y) for each target
    bucket = df[df['Target'] == i]
    length = len(bucket)
    arrXY = []
    for j in range(length):
        try:
            x = bucket.loc[j+bucket.first_valid_index()][3]
            y = bucket.loc[j+bucket.first_valid_index()][4]
        except KeyError:
            continue
        else:
            arrXY.append([x,y])

    # Convex Hull Points
    hull = []
    ConvexHull(arrXY, result = hull)

    # Points Scatter Plot
    arrX, arrY = zip(*arrXY)
    plt.scatter(arrX, arrY, label = target_names[i-1])
    
    # Convex Hull Plot
    hullX, hullY = zip(*hull)
    plt.plot(hullX, hullY)

plt.legend()
plt.show()