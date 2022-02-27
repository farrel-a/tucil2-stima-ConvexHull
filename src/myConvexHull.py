from math import sqrt, atan2

def ConvexHull(arrXY, left=[], right=[], i=0, result = [], up=False):
    # Convex Hull Algorithm
    if (arrXY != [] and i==0):
        # Main Processs
        arrXY.sort()
        left = arrXY[0]
        right = arrXY[-1]
        result.append(left)
        result.append(right)
        LeftUpPoints = FindLeftUp(arrXY, left, right)
        RightDownPoints = FindRightDown(arrXY, left, right)

        # Recursive (go to i = 1) ; (i = 0 is for main process)
        ConvexHull(LeftUpPoints, left, right, 1, result, True)
        ConvexHull(RightDownPoints, left, right, 1, result, False)

        # Sort clockwise and add first element to plot circularly
        sort_cw(result)
        result.append(result[0])

    elif (arrXY != [] and i != 0 ):
        # Array of distance
        dist = []

        # Gradient not 0 nor infinity
        if (right[0] - left[0] != 0 and right[1] - left[1] != 0):
            gradient = (right[1]-left[1])/(right[0] - left[0])
            xleft = left[0]
            yleft = left[1]
            for i in range(len(arrXY)):
                point = arrXY[i]
                x = point[0] 
                y = point[1]
                A = gradient
                B = -1
                C = gradient * -xleft + yleft
                distance = abs((A*x + B*y + C)) / (sqrt(A**2 + B**2))
                dist.append(distance)
        
        # Gradient infinity (Vertical Line)
        elif (right[0] - left[0] == 0): 
            for i in range(len(arrXY)):
                point = arrXY[i]
                x = point[0]
                distance = abs(x-left[0])
                dist.append(distance)

        # Gradient zero (Horizontal line)
        elif (right[1] - left[1] == 0):
            for i in range(len(arrXY)):
                point = arrXY[i]
                y = point[1]
                distance = abs(y-left[1])
                dist.append(distance)

        # Find point with max distance to line
        dist_max = max(dist)
        idx_max = dist.index(dist_max)

        # If point not in result, add the point to the result
        if (arrXY[idx_max] not in result):
            result.append(arrXY[idx_max])

        # If checking points above line
        if (up):
            LeftUpPoints = FindLeftUp(arrXY, left, arrXY[idx_max])
            RightUpPoints = FindLeftUp(arrXY, arrXY[idx_max], right)
            # If there are points on left up
            if (len(LeftUpPoints) != 0):
                ConvexHull(LeftUpPoints, left, arrXY[idx_max], 1, result, up)
            # If there are points of right up
            if (len(RightUpPoints) != 0):
                ConvexHull(RightUpPoints, arrXY[idx_max], right, 1, result, up)
        
        # If checking points below line
        else:
            LeftDownPoints = FindRightDown(arrXY, left, arrXY[idx_max])
            RightDownPoints = FindRightDown(arrXY, arrXY[idx_max], right)
            # If there are points on left down
            if (len(LeftDownPoints) != 0):
                ConvexHull(LeftDownPoints, left, arrXY[idx_max], 1, result, up)
            # If there are points on right down
            if (len(RightDownPoints) != 0):
                ConvexHull(RightDownPoints, arrXY[idx_max], right, 1, result, up)

def PointDeterminant(p1, p2, p3):
    # Calculate determinant of points to determine point's position relative to line
    return p1[0]*p2[1] + p3[0]*p1[1] + p2[0]*p3[1] - p3[0]*p2[1] - p2[0]*p1[1] - p1[0]*p3[1]

def FindLeftUp(arrXY, Pleft, Pright):
    # Find points on left up based on PointDeterminant
    arr = []
    for i in range(len(arrXY)):
        if (PointDeterminant(Pleft, Pright, arrXY[i]) > 0  and arrXY[i] != Pleft and arrXY[i] != Pright):
            arr.append(arrXY[i])
    return arr

def FindRightDown(arrXY, Pleft, Pright):
    # Find points on right down based on PointDeterminant
    arr = []
    for i in range(len(arrXY)):
        if (PointDeterminant(Pleft, Pright, arrXY[i]) <= 0 and arrXY[i] != Pleft and arrXY[i] != Pright):
            arr.append(arrXY[i])
    return arr

def sort_cw(points):
    # Sort points in a clockwise sequence
    total_x = 0
    total_y = 0
    for x, y in points:
        total_x += x
        total_y += y
    centre_x = total_x/len(points)
    centre_y = total_y/len(points)

    angles = []
    for x, y in points :
        angle = atan2(y - centre_y, x - centre_x)
        angles.append(angle)

    angles_sorted = sorted(angles, reverse=True)

    idx = []
    for angle_sorted in angles_sorted:
        idx.append(angles.index(angle_sorted))
    cw_points = []

    for i in idx:
        cw_points.append(points[i])
    
    points.clear()
    for i in range(len(cw_points)):
        points.append(cw_points[i])