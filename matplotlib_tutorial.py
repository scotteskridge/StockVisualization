import matplotlib.pyplot as plt
import random
import numpy as np
import math
import pprint

# x,y = 0
X = []
Y = []
X2 = []
Y2 = []
# bins = [x for x in range(200)]
# gaussian_numbers = np.random.randn(1000)
#
# randnums = []
# for x in range(250):
#     randnums.append(random.gauss(0, 10))
#
# plt.hist(randnums)
# plt.show()

def addLabel(line):
    ids = [x for x in range(len(line))]
    return ids

def stichPoints(Y):
    line = []
    for x in range(len(Y)):
        line.append([x, Y[x]])
    return line

def makeLine(x, slope, offset):
    return ((slope *x) + offset)

def meanError(prediction, data):
    error = 0
    #sum up all the abs of errors
    for i in range(len(data)):
        error += math.fabs(data[i] - prediction[i])
    return error/len(data)



for x in range(2500):
    Y.append(makeLine(x , 1, random.gauss(0, 100)))

line = random.sample(stichPoints(Y), 10)
line = sorted(line,  key=lambda points: points[0])
print (line)

X = []
Y = []
for x, y in line:
    X.append(x)
    Y.append(y)



# slope1 = makeLine(20, slope, 1 )
# slope2 = makeLine(20, slope, 2 )
#
#
# for x,y in slope1:
#     X.append(x*2)
#     Y.append(y)
#
# for x,y in slope2:
#     X2.append(x*2 + 1)
#     Y2.append(y)
#
# plt.bar(addLabel(X),X, label= "First Line")
# plt.plot(X2,Y2, label= "Second Line")
#

############################################
#plt.plot(X2,Y2, label= "Second Line")
#plt.bar(addLabel(X),X, label= "First Line")
# plt.hist(ages, bins, histtype = "bar", rwidth = 0.8)
# plt.show()
# X = addLabel(Y)
x = np.array(X)
y = np.array(Y)




plt.scatter(X,Y, label = "scatter plot", color = "b")

#######################################
#####this is the linear regression#####
#######################################
denominator = x.dot(x) - x.mean() * x.sum()
a = (x.dot(y) - y.mean() * x.sum()) / denominator
b = (y.mean() * x.dot(x) - x.mean() * x.dot(y)) / denominator
yHat = a * x + b
plt.plot(x, yHat)



d1 = y - yHat
d2 = y - y.mean()
rSquared = 1 - d1.dot(d1) / d2.dot(d2)
print("rSquared is: ", rSquared )


def findSlope(x,y):
    return (y[1]-y[0])/(x[1]-x[0])
print("The slope is: ", findSlope(x,yHat))
print("The mean of y is: ", y.mean())
print("The mean of yHat is: ", yHat.mean())
print("The mean Error is: ",  meanError(y, yHat))
print("The variance of y is: ", np.var(y) - np.var(yHat))


# plt.hist(randnums, bins, label = "random numbers", histtype = "bar", rwidth = 0.8)


plt.xlabel("X")
plt.ylabel("Y")
plt.title("plt tutorial\nCheck it Out")
plt.legend()
plt.show()
