import random
import math

numberOfTriangles = int(input("How many triangles? "))

radius = int(input("Input disperse radius: "))

randomIntensity = 5

sineIntensity = 5

triangleScale = int(input("Input scale: "))

listOfPoints = []

#Generate a list of points on the radius of the circle

for i in range(numberOfTriangles):
    
    theta = 2 * math.pi * i / numberOfTriangles
    x = radius * math.cos(theta)
    y = math.sin(theta + math.pi / 2)*sineIntensity
    z = radius * math.sin(theta)
    listOfPoints.append((x, y, z, theta))

# From list of points, generate triangles

listTriangles = []

for i in listOfPoints:

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    colorAssembled = f'#{r:02X}{g:02X}{b:02X}'

    yFinal = i[1] + (random.random()-0.5)*randomIntensity

    positionAssembled = f'{i[0]} {i[1]} {i[2]}'

    rotationAssembled = f'0 {(2*math.pi-i[3])*180/math.pi-90} {random.randint(0, 360)}' 

    listTriangles.append(f"<a-triangle color=\"{colorAssembled}\" position=\"{positionAssembled}\" rotation = \"{rotationAssembled}\" scale = \"{triangleScale}, {triangleScale}, {triangleScale}\"></a-triangle>")


with open("output.txt", "a", encoding="utf-8") as f:
    for i in listTriangles:
        f.write("    ")
        f.write(i)
        f.write("\n")
