import random
from math import trunc

pnt1 = []
pnt2 = []


def greatest_common_factor(numX, numY):
    if numX > numY:
        x = numY
    else:
        x = numX
    while x > 1:
        if numX % x == 0 and numY % x == 0:
            break
        x -= 1
    return x


def simplify(a, b):

    # If both x and y are negative make them both positive
    if a < 0 and b < 0:
        return a * -1, b * -1

    # 0/64 = 0/1
    if a == 0:
        a = 0
        b = 1
        return a, b

    # 64/0 = 1/0
    if b == 0:
        a = 1
        b = 0
        return a, b

    a = trunc(a / greatest_common_factor(abs(a), abs(b)))
    b = trunc(b / greatest_common_factor(abs(b), abs(a)))
    return a, b


for i in range(18):

    # Generate random points (the arbitrary sizes are the dimensions of my graph paper)
    pnt1.append([random.randint(-21, 22), random.randint(-16, 17)])
    pnt2.append([random.randint(-21, 22), random.randint(-16, 17)])

    # Calculate slope and simplify
    numM = [pnt2[i][1] - pnt1[i][1], pnt2[i][0] - pnt1[i][0]]
    numM = simplify(numM[0],numM[1])

    # Calculate y-intercept and simplify
    numB = [pnt2[i][1] * numM[1] - numM[0] * pnt2[i][0], numM[1]]
    numB = simplify(numB[0],numB[1])
    
    # Check if slope is negative, if so adjust equation to be correct
    if numM[0] < 0 or numM[1] < 0:
        standard_form = f"{abs(numM[0])}/{abs(numM[1])} x - y = {numB[0]}/{numB[1]}"
    else:
        standard_form = f"{numM[0]}/{numM[1]} x + y = {numB[0]}/{numB[1]}"

    # Output
    print(
        f"points: {pnt1[i][0],pnt1[i][1]},{pnt2[i][0],pnt2[i][1]} \nslope: {numM[0]}/{numM[1]} \ny-intercept: {numB[0]}/{numB[1]} \nslope-intercept form: y = {numM[0]}/{numM[1]}x + {numB[0]}/{numB[1]} \npoint-slope form: y - {pnt1[i][1]} = {numM[0]}/{numM[1]} (x - {pnt1[i][0]})\nstandard form: {standard_form}\n"
    )
