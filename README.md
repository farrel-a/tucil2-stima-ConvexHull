# Tugas Kecil 2 IF2211 Strategi Algoritma Convex Hull Implementation for Linear Separability Test with Divide and Concquer Algorithm

## 13520110 - Farrel Ahmad

<br>

## Introduction
This is a program to test linear separability between data using convex hull visualization. Two or more data is called linear separable if each of the convex hull does not intersect. If the convex hull intersects between two or more other convex hulls, the data is not linear separable. 

Using 2 dimension points that represent the data, the convex hull can be made using divide and conquer Algorithm. The idea is to divide into two parts the upper and lower part of convex hull, find the farthest point, divide until no more points are found, and then combine it into whole convex hull. The illustration of the algorithm looks like this:

![](https://i.ibb.co/71s187r/Screenshot-2022-02-27-191356.png)

<br>

## Requirements
1. Pandas
2. Matplotlib
3. sklearn
```sh
# using pip
$ pip install pandas
$ pip install matplotlib
$ pip install sklearn
```

## How to Run
```sh
$ git clone https://github.com/farrel-a/tucil2-stima-ConvexHull.git
$ cd tucil2-stima-ConvexHull
$ cd src
```
There are 5 main files with each has different output and different datasets. Run one of these 5 files, for example at `/src`
```sh
$ python main_iris_petal.py
# or
$ python main_seeds.py
# or
$ python main_wine.py
# or
$ python main_breast_cancer.py
# or
$ python main_iris_sepal.py
```

<br>

## Result Example
`main_iris_sepal.py`

![](https://i.ibb.co/wgst6VB/sepal.png)

Based on this visualization, it can be concluded that Setosa is linearly separable while Versicolor and Virginica are not linearly separable because they intersect each other. 

<br>

`main_breast_cancer.py`

![](https://i.ibb.co/3Cz47b9/bc.png)

Based on this visualization, it can be concluded that Malignant and  Benign are not linearly separable because they intersect each other.

<br>

For more algorithm details and results, read the paper at `/doc`.