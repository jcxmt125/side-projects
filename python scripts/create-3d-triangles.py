import random
import math

numberOfTriangles = int(input("How many objects? "))

radius = int(input("Input disperse radius: "))

randomIntensity = 20

randomPosIntensity = 3

sineIntensity = 20

triangleScale = int(input("Input scale: "))

listOfPoints = []

#Generate a list of points on the radius of the circle

for i in range(numberOfTriangles):
    
    theta = 2 * math.pi * i / numberOfTriangles
    x = radius * math.cos(theta)
    y = math.sin(theta + math.pi / 2)*sineIntensity + 5
    z = radius * math.sin(theta)
    listOfPoints.append((x, y, z, theta))

# From list of points, generate triangles

listObjects = []

for i in listOfPoints:

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    colorAssembled = f'#{r:02X}{g:02X}{b:02X}'

    yFinal = i[1] + (random.random()-0.5)*randomIntensity

    randomPos = 1+(random.random())*randomPosIntensity

    positionAssembled = f'{i[0]*randomPos} {yFinal*randomPos} {i[2]*randomPos}'

    if random.randint(0, 1) == 0:

        rotationAssembled = f'0 {(2*math.pi-i[3])*180/math.pi-90} {random.randint(0, 360)}' 

        listObjects.append(f"<a-triangle color=\"{colorAssembled}\" position=\"{positionAssembled}\" rotation = \"{rotationAssembled}\" scale = \"{triangleScale*randomPos}, {triangleScale*randomPos}, {triangleScale*randomPos}\"></a-triangle>")

    else:

        rotationAssembled = f'{random.randint(0,360)} {random.randint(0,360)} {random.randint(0, 360)}'

        listObjects.append(f"<a-tetrahedron color=\"{colorAssembled}\" position=\"{positionAssembled}\" rotation = \"{rotationAssembled}\" scale = \"{triangleScale*randomPos*0.9}, {triangleScale*randomPos*0.9}, {triangleScale*randomPos*0.9}\"></a-tetrahedron>")


with open("output.txt", "a", encoding="utf-8") as f:
    for i in listObjects:
        f.write("    ")
        f.write(i)
        f.write("\n")
