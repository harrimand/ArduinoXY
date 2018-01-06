import csv

ptList = []

def settings():
    size(512, 512)

def setup():
    global ptList
    background(0)
    stroke(0, 255, 128)
    strokeWeight(1)   
    with open("xy2.txt", 'r') as xy:
        xylines = csv.reader(xy)
        for lines in xylines:
            for L in lines:
                if L:
                    print(L)
                    ptList.append(int(L))
    print(ptList)

def draw():
    global ptList
    # line(width/4, height/2, 3 * width/4, height/2)
    ix = 0
    while ix < len(ptList)-2:
        # print("{0:>10} {1:>10}".format(ix, ptList[ix]))
        if ptList[ix + 2] == 255:
            ix += 3        
        if ptList[ix] == 255:
            x1 = ptList[ix + 1]
            y1 = ptList[ix + 2]
            x2 = ptList[ix + 3]
            y2 = ptList[ix + 4]
            print(x1, y1, x2, y2)
            ix += 3
        else:
            x1 = ptList[ix]
            y1 = ptList[ix + 1]
            x2 = ptList[ix + 2]
            y2 = ptList[ix + 3]
            print(x1, y1, x2, y2)
            ix += 2
        line(x1+140, 320-y1, x2+140, 320-y2)
    # line(155, 320, 332, 320) #BOTTOM w = 177
    # line(332, 320, 332, 145) #RIGHT  h = 175
    # line(155, 145, 332, 145) #TOP   midT = 177
    # line(155, 145, 155, 320) #LEFT  midL = 175
    noLoop()