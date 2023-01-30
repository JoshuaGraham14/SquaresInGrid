import math
import numpy as np                 # v 1.19.2
import matplotlib.pyplot as plt    # v 3.3.2
import pylab
import random

def formulaNumOfSquares(n):
    return int((math.pow(n, 4) + 4*math.pow(n, 3) + 5*math.pow(n, 2) + 2*n)/12)

def solution(x, y, allowDiags):   
    squares = []
    sortedSquares = []
    
    midpoints = []
    lengths = []
    diags = []
    
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            midpoints.append(calcMidpoint(x[i], y[i], x[j], y[j]))
            lengths.append(calcLength(x[i], y[i], x[j], y[j]))
            diags.append((x[i], y[i], x[j], y[j]))
            
    t = 0
    for i in range (len(midpoints)):
        for j in range (i+1, len(midpoints)):
            if(midpoints[i] == midpoints[j] and lengths[i] == lengths[j] and reqIsSquare(diags[i], diags[j])):
                if not allowDiags:
                    if not (diags[i][1] == diags[j][1] or diags[i][0] == diags[j][2] or diags[i][1] == diags[j][3] or diags[i][0] == diags[j][0]):
                        continue
                square = ((diags[i][0], diags[i][1]), (diags[j][0], diags[j][1]), (diags[i][2], diags[i][3]), (diags[j][2], diags[j][3]))
                sortedSquare = sorted(square, key=lambda p: math.atan2(p[1], p[0]))
                square = (lengths[i], (diags[i][0], diags[i][1]), (diags[j][0], diags[j][1]), (diags[i][2], diags[i][3]), (diags[j][2], diags[j][3]))
                #sort square into counter-clockwise order
                # 
                if sortedSquare not in sortedSquares:
                    squares.append(square)
                    sortedSquares.append(sortedSquare)
                    t+=1

    return t, sortSquaresInLengthOrder(squares)

def sortSquaresInLengthOrder(squares):
    sorted = False
    while sorted == False:
        sorted = True
        for i in range(len(squares)-1):
            if(squares[i][0] > squares[i+1][0]):
                temp = squares[i]
                squares[i] = squares[i+1]
                squares[i+1] = temp
                sorted = False
    return squares
        
def calcLength(x1, y1, x2, y2):
    x = (math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2)))
    x = round(x, 4)
    return x
    
def calcMidpoint(x1, y1, x2, y2):
    return (((x1+x2)/2, (y1+y2)/2))

def reqIsSquare(diag1, diag2):
    side1 = (diag1[0], diag1[1], diag2[0], diag2[1])
    side2 = (diag1[0], diag1[1], diag2[2], diag2[3])
    if(calcLength(side1[0], side1[1], side1[2], side1[3]) != calcLength(side2[0], side2[1], side2[2], side2[3])):
        return False
    return True

def setupGrid():
    # Enter x and y coordinates of points and colors
    # colors = ['m', 'g', 'r', 'b']
    
    # Select length of axes and the space between tick labels
    xmin, xmax, ymin, ymax = -5, 5, -5, 5
    ticks_frequency = 1

    fig, ax = plt.subplots(figsize=(4, 4))
    
    # Set identical scales for both axes
    ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect='equal')
    
    # Set bottom and left spines as x and y axes of coordinate system
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    
    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # Create 'x' and 'y' labels placed at the end of the axes
    ax.set_xlabel('x', size=14, labelpad=-24, x=1.03)
    ax.set_ylabel('y', size=14, labelpad=-21, y=1.02, rotation=0)
    
    # Create custom major ticks to determine position of tick labels
    x_ticks = np.arange(xmin, xmax+1, ticks_frequency)
    y_ticks = np.arange(ymin, ymax+1, ticks_frequency)
    ax.set_xticks(x_ticks[x_ticks != 0])
    ax.set_yticks(y_ticks[y_ticks != 0])
    
    # Create minor ticks placed at each integer to enable drawing of minor grid
    # lines: note that this has no effect in this example with ticks_frequency=1
    ax.set_xticks(np.arange(xmin, xmax+1), minor=True)
    ax.set_yticks(np.arange(ymin, ymax+1), minor=True)
    
    # Draw major and minor grid lines
    ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)
    
    # Draw arrows
    arrow_fmt = dict(markersize=4, color='black', clip_on=False)
    ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
    ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)
    
    #plt.show()

def plotSquares(x, y, squares, speed=0.8):
    squareSideLengthsSet = set()
    
    colors = ['m', 'g', 'r', 'b']
    colourIndex = -1
    xs = x
    ys = y
    # Plot points
    plt.scatter(xs, ys)

    #plt.pause(30)
    
    for squareIndex in range(len(squares)):
        plt.pause(speed)
        
        if squares[squareIndex][0] not in squareSideLengthsSet:
            squareSideLengthsSet.add(squares[squareIndex][0])
            colourIndex +=1
            if(colourIndex >= 4):
                colourIndex = 0

        plt.plot([squares[squareIndex][1][0], squares[squareIndex][2][0]], [squares[squareIndex][1][1], squares[squareIndex][2][1]], colors[colourIndex])
        plt.plot([squares[squareIndex][2][0], squares[squareIndex][3][0]], [squares[squareIndex][2][1], squares[squareIndex][3][1]], colors[colourIndex])
        plt.plot([squares[squareIndex][3][0], squares[squareIndex][4][0]], [squares[squareIndex][3][1], squares[squareIndex][4][1]], colors[colourIndex])
        plt.plot([squares[squareIndex][4][0], squares[squareIndex][1][0]], [squares[squareIndex][4][1], squares[squareIndex][1][1]], colors[colourIndex])
        fig = pylab.gcf()
        fig.canvas.manager.set_window_title(str(squareIndex+1))

        # ax.plot([squares[squareIndex][verticeIndex][0], squares[squareIndex][verticeIndex][1]], [squares[squareIndex][verticeIndex+1][0], squares[squareIndex][verticeIndex+1][1]], c=colors[colourIndex], ls='--', lw=3, alpha=0.5)

def generateUniformPoints(minx, miny, maxx, maxy, stepx=1, stepy=1):
    x = []
    y = []
    for i in range (miny, maxy+1, stepy):
        for j in range (minx, maxx+1, stepx):
            x.append(j)
            y.append(i)
    return x, y

def generateRandomPoints(minx, miny, maxx, maxy, numOfPoints=20):
    x=[]
    y=[]
    pointsSet = set()
    while len(pointsSet) < numOfPoints:
        randx = random.randint(minx, maxx)
        randy = random.randint(minx, maxx)
        pointsSet.add((randx, randy))
    
    for i in pointsSet:
        x.append(i[0])
        y.append(i[1])

    return x, y

# x = [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]
# y = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5]

# x = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
# y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4]

# x = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]
# y = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]

# x = [0, 1, 2, 0, 1, 2, 0, 1, 2]
# y = [0, 0, 0, 1, 1, 1, 2, 2, 2]

#x = [0, 0, -1, -1, 0, -1, -1, 1]
#y = [0, 1, 1, 0, -1, -1, 0, 0]

#x, y = generateUniformPoints(0, 0, 5, 5)
x, y = generateRandomPoints(0, 0, 5, 5, numOfPoints=20)

t, squares = solution(x, y, allowDiags=True)
# for i in squares:
#     print(i)
print(t)

setupGrid()
plotSquares(x, y, squares, speed=0.5)

plt.show()