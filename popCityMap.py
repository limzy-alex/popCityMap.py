import turtle
import math
def createCityPopDict():
    D = {}
    f = open('pop3.txt', 'r')
    for line in f:
        L = line.split()
        if len(L) == 3:
            key = str(L[1])
            val = int(L[-1])
            D[key] = val
        else:
            key = str(L[1]+' '+L[-2])
            val = int(L[-1])
            D[key] = val
    f.close()
    return D

def createCityLatLonDict():
    D = {}
    f = open('latlon3.txt', 'r')
    for line in f:
        L = line.split()
        if len(L) == 3:
            key = str(L[2])
            val = (float(L[0]), float(L[1]))
            D[key] = val
        else:
            key = str(L[2]+' '+L[-1])
            val = (float(L[0]), float(L[1]))
            D[key] = val
    f.close()
    return D
        

def createStateColorDict():
    D = {}
    f = open('stateAdj.txt', 'r')
    i = 1
    key = ''
    for line in f:
        if i % 2 == 0:
            val = int(line)
            i += 1
            D[key] = val
        else:
            key = line[0:2].lower()
            i += 1
    f.close()
    return D

def drawLower48Map():
    cityPopDict = createCityPopDict()
    cityLatLonDict = createCityLatLonDict()
    stateColorDict = createStateColorDict()
    colorList = ['red', 'blue', 'green', 'yellow']

    latlonTuples= list(cityLatLonDict.values())
    latList = []
    lonList = []

    for i in range(len(latlonTuples)):
        latList.append(latlonTuples[i][0])
        lonList.append(latlonTuples[i][1])
        

    latMax = max(latList)
    latMin = min(latList)
    lonMax = max(lonList)
    lonMin = min(lonList)

    matthew = turtle.Turtle ('turtle')
    s = turtle.Screen()
    s.setworldcoordinates(lonMax, latMin, lonMin, latMax)
    matthew.speed(100000)
    matthew.ht()

    f = open('output.txt', 'w')
    f.write('{:<30}'.format('cityname:')\
            +'{:<15}'.format('latitude:')\
            +'{:<15}'.format('longitude:')\
            +'{:<15}'.format('population:')\
            +'{:<15}'.format('dot size:')\
            +'{:<15}'.format('dot color:')\
            +'\n')

    for city in cityLatLonDict:
        x = cityLatLonDict[city][1]
        y = cityLatLonDict[city][0]
        cityColor = colorList[stateColorDict[city[-2:]]]
        dotSize = 4
        
        
        if city in cityPopDict:
            population = cityPopDict [city]
            dotSize = 4 + math.ceil(math.sqrt(population/50000))
            f.write('{:<30}'.format(city)\
            +'{:<15}'.format(x)\
            +'{:<15}'.format(y)\
            +'{:<15}'.format(population)\
            +'{:<15}'.format(dotSize)\
            +'{:<15}'.format(cityColor)\
            +'\n')
        else:
            f.write('{:<30}'.format(city)\
            +'{:<15}'.format(x)\
            +'{:<15}'.format(y)\
            +'{:<15}'.format(' ')\
            +'{:<15}'.format(dotSize)\
            +'{:<15}'.format(cityColor)\
            +'\n')
            

        matthew.penup()
        matthew.setposition(x, y)
        matthew.pendown()
        matthew.dot(dotSize, str(cityColor))
    s.exitonclick()
        

       

        

