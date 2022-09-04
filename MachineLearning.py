""" Main Game """
def drawHomeFrame():
    drawTiles()
    drawText(PLAYER["show_score"])
    gridCoord = convertNumToCoord((PLAYER["home_number"],PLAYER["home_letter"]))
    command = 'pg.draw.rect(screen,'+gridCoord+'["colour"],('+gridCoord+'["x"],'+gridCoord+'["y"],'+gridCoord+'["w"],'+gridCoord+'["h"]))'
    exec(command)
def drawTiles():
    # Part 1/4 # Draw the background squares (A)
    pg.draw.rect(screen,A1["colour"],(A1["x"],A1["y"],A1["w"],A1["h"]))
    pg.draw.rect(screen,A2["colour"],(A2["x"],A2["y"],A2["w"],A2["h"]))
    pg.draw.rect(screen,A3["colour"],(A3["x"],A3["y"],A3["w"],A3["h"]))
    pg.draw.rect(screen,A4["colour"],(A4["x"],A4["y"],A4["w"],A4["h"]))
    # Part 2/4 # Draw the background squares (B)
    pg.draw.rect(screen,B1["colour"],(B1["x"],B1["y"],B1["w"],B1["h"]))
    pg.draw.rect(screen,B2["colour"],(B2["x"],B2["y"],B2["w"],B2["h"]))
    pg.draw.rect(screen,B3["colour"],(B3["x"],B3["y"],B3["w"],B3["h"]))
    pg.draw.rect(screen,B4["colour"],(B4["x"],B4["y"],B4["w"],B4["h"]))
    # Part 3/4 # Draw the background squares (C)
    pg.draw.rect(screen,C1["colour"],(C1["x"],C1["y"],C1["w"],C1["h"]))
    pg.draw.rect(screen,C2["colour"],(C2["x"],C2["y"],C2["w"],C2["h"]))
    pg.draw.rect(screen,C3["colour"],(C3["x"],C3["y"],C3["w"],C3["h"])) # Kill square
    pg.draw.rect(screen,C4["colour"],(C4["x"],C4["y"],C4["w"],C4["h"]))
    # Part 4/4 # Draw the background squares (D)
    pg.draw.rect(screen,D1["colour"],(D1["x"],D1["y"],D1["w"],D1["h"]))
    pg.draw.rect(screen,D2["colour"],(D2["x"],D2["y"],D2["w"],D2["h"]))
    pg.draw.rect(screen,D3["colour"],(D3["x"],D3["y"],D3["w"],D3["h"]))
    pg.draw.rect(screen,D4["colour"],(D4["x"],D4["y"],D4["w"],D4["h"])) # Yay Square
def drawSpecialText():
    # Part 5/6 # Draw the text on the squares (Special Squares)
    writeText(SCORE["C3"],C3["x"],C3["y"])
    writeText("(KILL)",C3["x"],(C3["y"]+TEXT_SIZE),(TEXT_SIZE//2),WHITE)
    writeText(SCORE["D4"],D4["x"],D4["y"])
    writeText("(YAY)",D4["x"],(D4["y"]+TEXT_SIZE),(TEXT_SIZE//2),WHITE)
    # Part 6/5 # Draw special text
    writeText(("GENERATION: "+str(PLAYER["gen"])),60,550,TEXT_SIZE//4*3,TOMATO)
    if ARTIFICIAL_INTELLIGENCE == True:
        writeText(("AI On: "+str(ARTIFICIAL_INTELLIGENCE)),370,630,TEXT_SIZE//4*3,DARK_CYAN)
    if ARTIFICIAL_INTELLIGENCE == False:
        writeText(("AI On: "+str(ARTIFICIAL_INTELLIGENCE)),370,630,TEXT_SIZE//4*3,GREY)
    writeText(("FAILED RUNS: "+str(PLAYER["fail"])),60,630,TEXT_SIZE//4*3,RED)
    if PLAYER["ignore_previous_square"] == True:
        writeText(("Ignore Last Tile: "+str(PLAYER["ignore_previous_square"])),370,550,TEXT_SIZE//4*3,DARK_CYAN)
    if PLAYER["ignore_previous_square"] == False:
        writeText(("Ignore Last Tile: "+str(PLAYER["ignore_previous_square"])),370,550,TEXT_SIZE//4*3,GREY)
    if PLAYER["aim_for_max"] == True:
        writeText(("Aim For Max: "+str(PLAYER["aim_for_max"])),370,590,TEXT_SIZE//4*3,DARK_CYAN)
    if PLAYER["aim_for_max"] == False:
        writeText(("Aim For Max: "+str(PLAYER["aim_for_max"])),370,590,TEXT_SIZE//4*3,GREY)
    if PLAYER["show_score"] == True:
        writeText(("Show Score: "+str(PLAYER["show_score"])),370,670,TEXT_SIZE//4*3,DARK_CYAN)
    if PLAYER["show_score"] == False:
        writeText(("Show Score: "+str(PLAYER["show_score"])),370,670,TEXT_SIZE//4*3,GREY)
    writeText(("POSITION: "+str(convertNumToCoord((PLAYER["letter"],PLAYER["number"])))),50,590,TEXT_SIZE//4*3,GREEN)
    writeText("FRAMERATE: "+str(FRAMERATE),60,670,TEXT_SIZE//4*3,TOMATO)
def drawText(isScoreAllowed):
    if isScoreAllowed == True:
        # Part 1/6 # Draw the text on the squares (A)
        writeText(SCORE["A1"], A1["x"], A1["y"])
        writeText(SCORE["A2"], A2["x"], A2["y"])
        writeText(SCORE["A3"], A3["x"], A3["y"])
        writeText(SCORE["A4"], A4["x"], A4["y"])
        # Part 2/6 # Draw the text on the squares (B)
        writeText(SCORE["B1"], B1["x"], B1["y"])
        writeText(SCORE["B2"], B2["x"], B2["y"])
        writeText(SCORE["B3"], B3["x"], B3["y"])
        writeText(SCORE["B4"], B4["x"], B4["y"])
        # Part 3/6 # Draw the text on the squares (C)
        writeText(SCORE["C1"], C1["x"], C1["y"])
        writeText(SCORE["C2"], C2["x"], C2["y"])
        writeText(SCORE["C4"], C4["x"], C4["y"])
        # Part 4/6 # Draw the text on the squares (D)
        writeText(SCORE["D1"], D1["x"], D1["y"])
        writeText(SCORE["D2"], D2["x"], D2["y"])
        writeText(SCORE["D3"], D3["x"], D3["y"])
        drawSpecialText()
    elif isScoreAllowed == False:
        drawSpecialText()
def removeIllegalMoves():
    global movePos
    # Part 1/4 # Calculate the possible squares you can move to
    movePos = [(PLAYER["letter"]-1,PLAYER["number"]),(PLAYER["letter"]+1,PLAYER["number"]),
    (PLAYER["letter"],PLAYER["number"]-1),(PLAYER["letter"],PLAYER["number"]+1)]
    corruptTrack = []
    if 0 in movePos[0]:
        corruptTrack.append(movePos[0])
    if 0 in movePos[1]:
        corruptTrack.append(movePos[1])
    if 0 in movePos[2]:
        corruptTrack.append(movePos[2])
    if 0 in movePos[3]:
        corruptTrack.append(movePos[3])
    if 5 in movePos[0]:
        corruptTrack.append(movePos[0])
    if 5 in movePos[1]:
        corruptTrack.append(movePos[1])
    if 5 in movePos[2]:
        corruptTrack.append(movePos[2])
    if 5 in movePos[3]:
        corruptTrack.append(movePos[3])
    count = len(corruptTrack);int
    i = 0
    for i in range(count):
        movePos.remove(corruptTrack[i])
        i+=1
def resetPlayer():
    PLAYER["mem"] = []
    PLAYER["letter"] = PLAYER["home_letter"]
    PLAYER["number"] = PLAYER["home_number"]
def AIplaysGame():
    removeIllegalMoves()
    if (PLAYER["letter"],PLAYER["number"]) == (4,4):
        allTiles = refineList(PLAYER["mem"])
        i = 0
        for i in range(0, len(allTiles)):
            SCORE[allTiles[i]]+=1
            i+=1
        SCORE["D4"]+=1
        PLAYER["gen"]+=1
        resetPlayer()
    elif (PLAYER["letter"],PLAYER["number"]) == (3,3):
        allTiles = refineList(PLAYER["mem"])
        i = 0
        for i in range(0, len(allTiles)):
            SCORE[allTiles[i]]-=1
            i+=1
        SCORE["C3"]-=1
        PLAYER["gen"]+=1
        PLAYER["fail"]+=1
        resetPlayer()
    else:
        # Part 2/4 # See the best square to move to
        if PLAYER["ignore_previous_square"] == True:
            try:
                previousSquareNumCoords = "("+str(TILEMAP_Y[PLAYER["mem"][-1]])+", "+str(TILEMAP_X[PLAYER["mem"][-1]])+")"
            except:
                previousSquareNumCoords = "("+str(PLAYER["home_letter"])+", "+str(PLAYER["home_number"])+")"
            finally:
                i = 0
                for i in range(0,(len(movePos)-1)):
                    if previousSquareNumCoords == str(movePos[i]):
                        del movePos[i]
                    else:
                        i+=1
        i = 0
        valueOfEachSquare = {}
        for i in range(0,(len(movePos))):
            valueOfEachSquare[str(convertNumToCoord(movePos[i]))] = SCORE[str(convertNumToCoord(movePos[i]))]
            i+=1
        bestTilesForTheSituation = findBestSquares(valueOfEachSquare, PLAYER["aim_for_max"])
        if ALLOW_RANDOM == True:
            random.shuffle(bestTilesForTheSituation)
            bestTile = bestTilesForTheSituation[0]
        if ALLOW_RANDOM == False:
            if PLAYER["aim_for_max"] == True:
                bestTile = max(valueOfEachSquare, key=valueOfEachSquare.get)
            elif PLAYER["aim_for_max"] == False:
                bestTile = min(valueOfEachSquare, key=valueOfEachSquare.get)
        # Part 3/4 # Adjust all variables for the next loop
        PLAYER["mem"].append(TILEMAP_Y[PLAYER["letter"]]+TILEMAP_X[PLAYER["number"]])
        (PLAYER["letter"],PLAYER["number"]) = TILEMAP_Y[bestTile],TILEMAP_X[bestTile]
        # Part 4/4 # Draw the player tile
        squareCommand = 'pg.draw.rect(screen,'+str(PLAYER["colour"])+',('+bestTile+'["x"],'+bestTile+'["y"],'+bestTile+'["w"],'+bestTile+'["h"]))'
        textCommand = 'writeText("Player",'+bestTile+'["x"],'+bestTile+'["y"])'
        exec(squareCommand)
        exec(textCommand)
def playerPlaysGame():
    removeIllegalMoves()
    if (PLAYER["letter"],PLAYER["number"]) == (4,4):
        allTiles = refineList(PLAYER["mem"])
        i = 0
        for i in range(0, len(allTiles)):
            SCORE[allTiles[i]]+=1
            i+=1
        SCORE["D4"]+=1
        PLAYER["gen"]+=1
        resetPlayer()
    elif (PLAYER["letter"],PLAYER["number"]) == (3,3):
        allTiles = refineList(PLAYER["mem"])
        i = 0
        for i in range(0, len(allTiles)):
            SCORE[allTiles[i]]-=1
            i+=1
        SCORE["C3"]-=1
        PLAYER["gen"]+=1
        PLAYER["fail"]+=1
        resetPlayer()
    else:
        selectedTile = convertNumToCoord((PLAYER["letter"],PLAYER["number"]))
        if pressed_up_ == True:
            if (PLAYER["letter"]-1,PLAYER["number"]) in movePos:
                selectedTile = convertNumToCoord((PLAYER["letter"]-1,PLAYER["number"]))
                PLAYER["letter"]-=1
        elif pressed_down_ == True:
            if (PLAYER["letter"]+1,PLAYER["number"]) in movePos:
                selectedTile = convertNumToCoord((PLAYER["letter"]+1,PLAYER["number"]))
                PLAYER["letter"]+=1
        elif pressed_left_ == True:
            if (PLAYER["letter"],PLAYER["number"]-1) in movePos:
                selectedTile = convertNumToCoord((PLAYER["letter"],PLAYER["number"]-1))
                PLAYER["number"]-=1
        elif pressed_right_ == True:
            if (PLAYER["letter"],PLAYER["number"]+1) in movePos:
                selectedTile = convertNumToCoord((PLAYER["letter"],PLAYER["number"]+1))
                PLAYER["number"]+=1
        squareCommand = 'pg.draw.rect(screen,'+str(PLAYER["colour"])+',('+selectedTile+'["x"],'+selectedTile+'["y"],'+selectedTile+'["w"],'+selectedTile+'["h"]))'
        textCommand = 'writeText("Player",'+selectedTile+'["x"],'+selectedTile+'["y"])'
        PLAYER["mem"].append(convertNumToCoord((PLAYER["letter"], PLAYER["number"])))
        exec(squareCommand)
        exec(textCommand)
def doFullGame():
    drawTiles()
    drawText(PLAYER["show_score"])
    if ARTIFICIAL_INTELLIGENCE == True:
        AIplaysGame()
    elif ARTIFICIAL_INTELLIGENCE == False:
        playerPlaysGame()

""" QUICK CHANGES """
def CODE_RESOURCES():
    # Colours
    global CYAN,RED,GREY,BLACK,TOMATO,BISQUE,SANDY_BROWN,LIGHT_GREEN,LIME_GREEN,WHITE,GREYISH_WHITE,DARK_CYAN,GREEN,PURPLE
    CYAN = (45,191,196)
    RED = (219,39,39)
    GREY = (110,110,110)
    BLACK = (0,0,0)
    TOMATO = (255,99,71)
    BISQUE = (255,228,196)
    SANDY_BROWN = (244,164,96)
    LIGHT_GREEN = (144,238,144)
    LIME_GREEN = (50,205,50)
    WHITE = (255,255,255)
    GREYISH_WHITE = (210,210,210)
    DARK_CYAN = (0,139,139)
    GREEN = (0,139,0)
    PURPLE = (170,100,239)
    # Exit Code Colours
    global ecBOLD_RED,ecNORMAL_WHITE
    ecBOLD_RED = "\033[1;31;49m"
    ecNORMAL_WHITE = "\033[0;37;49m"
    # Screen Settings
    global WIDTH,HEIGHT,FRAMERATE,NAME,BACKGROUND
    WIDTH, HEIGHT = 600, 800
    FRAMERATE = 9
    NAME = "Machine Learning"
    BACKGROUND = BISQUE
    # Pygame things
    global KEYS,TEXT_SIZE
    KEYS = pg.key.get_pressed()
    TEXT_SIZE = 32
    # Toggle Switches
    global RUN,ALLOW_RANDOM,DO_BEGINNING_FRAME,ARTIFICIAL_INTELLIGENCE
    RUN = True
    ALLOW_RANDOM = True
    DO_BEGINNING_FRAME = True
    ARTIFICIAL_INTELLIGENCE = True
def SQUARE_RESOURCES():
    # Score,Tilemaps, and the PLAYER variables
    global SCORE,TILEMAP_X,TILEMAP_Y,PLAYER
    SCORE = {
        "A1":0, "A2":0, "A3":0, "A4":0,
        "B1":0, "B2":0, "B3":0, "B4":0,
        "C1":0, "C2":0, "C3":0, "C4":0, # C3 is kill square
        "D1":0, "D2":0, "D3":0, "D4":0} # D4 is yay square
    TILEMAP_X = {
        "A1":1, "A2":2, "A3":3, "A4":4,
        "B1":1, "B2":2, "B3":3, "B4":4,
        "C1":1, "C2":2, "C3":3, "C4":4, # C3 is kill square
        "D1":1, "D2":2, "D3":3, "D4":4,
        1:"1",2:"2",3:"3",4:"4"} # D4 is yay square
    TILEMAP_Y = {
        "A1":1, "A2":1, "A3":1, "A4":1,
        "B1":2, "B2":2, "B3":2, "B4":2,
        "C1":3, "C2":3, "C3":3, "C4":3, # C3 is kill square
        "D1":4, "D2":4, "D3":4, "D4":4, # D4 is yay square
        1:"A",2:"B",3:"C",4:"D"}
    PLAYER = {
        "colour":LIME_GREEN,
        "number": 1,
        "letter":1,
        "gen": 1,
        "mem":[],
        "aim_for_max": True,
        "ignore_previous_square": True,
        "home_number": 1,
        "home_letter": 1,
        "show_score": True,
        "fail": 0}
    # Linking
    global BASE_SQUARE
    KILL_SQUARE = RED
    YAY_SQUARE = CYAN 
    NORM_SQUARE = SANDY_BROWN
    BASE_SQUARE = 120
    # Coordinate related (A section or Y-column 1)
    global A1,A2,A3,A4
    A1 = {"colour": NORM_SQUARE, "x": autoSpacing(BASE_SQUARE,WIDTH,1,0), "y": autoSpacing(BASE_SQUARE,WIDTH,0,1), "w": BASE_SQUARE, "h": BASE_SQUARE}
    A2 = {"colour": NORM_SQUARE, "x": autoSpacing(BASE_SQUARE,WIDTH,2,0), "y": autoSpacing(BASE_SQUARE,WIDTH,0,1), "w": BASE_SQUARE, "h": BASE_SQUARE}
    A3 = {"colour": NORM_SQUARE, "x": autoSpacing(BASE_SQUARE,WIDTH,3,0), "y": autoSpacing(BASE_SQUARE,WIDTH,0,1), "w": BASE_SQUARE, "h": BASE_SQUARE}
    A4 = {"colour": NORM_SQUARE, "x": autoSpacing(BASE_SQUARE,WIDTH,4,0), "y": autoSpacing(BASE_SQUARE,WIDTH,0,1), "w": BASE_SQUARE, "h": BASE_SQUARE}
    # Coordinate related (B section or Y-column 2)
    global B1,B2,B3,B4
    B1 = {"colour": NORM_SQUARE, "x": autoSpacing(BASE_SQUARE,WIDTH,1,0), "y": autoSpacing(BASE_SQUARE,WIDTH,0,2), "w": BASE_SQUARE, "h": BASE_SQUARE}
    B2 = {"colour": NORM_SQUARE, "x": autoSpacing(BASE_SQUARE,WIDTH,2,0), "y": autoSpacing(BASE_SQUARE,WIDTH,0,2), "w": BASE_SQUARE, "h": BASE_SQUARE}
    B3 = {"colour": NORM_SQUARE, "x": autoSpacing(BASE_SQUARE,WIDTH,3,0), "y": autoSpacing(BASE_SQUARE,WIDTH,0,2), "w": BASE_SQUARE, "h": BASE_SQUARE}
    B4 = {"colour": NORM_SQUARE, "x": autoSpacing(BASE_SQUARE,WIDTH,4,0), "y": autoSpacing(BASE_SQUARE,WIDTH,0,2), "w": BASE_SQUARE, "h": BASE_SQUARE}
    # Coordinate related (C section or Y-column 3)
    global C1,C2,C3,C4
    C1 = {"colour": NORM_SQUARE, "x": autoSpacing(BASE_SQUARE,WIDTH,1,0), "y": autoSpacing(BASE_SQUARE,WIDTH,0,3), "w": BASE_SQUARE, "h": BASE_SQUARE}
    C2 = {"colour": NORM_SQUARE, "x": autoSpacing(BASE_SQUARE,WIDTH,2,0), "y": autoSpacing(BASE_SQUARE,WIDTH,0,3), "w": BASE_SQUARE, "h": BASE_SQUARE}
    C3 = {"colour": KILL_SQUARE, "x": autoSpacing(BASE_SQUARE,WIDTH,3,0), "y": autoSpacing(BASE_SQUARE,WIDTH,0,3), "w": BASE_SQUARE, "h": BASE_SQUARE}
    C4 = {"colour": NORM_SQUARE, "x": autoSpacing(BASE_SQUARE,WIDTH,4,0), "y": autoSpacing(BASE_SQUARE,WIDTH,0,3), "w": BASE_SQUARE, "h": BASE_SQUARE}
    # Coordinate related (D section or Y-column 4)
    global D1,D2,D3,D4
    D1 = {"colour": NORM_SQUARE, "x": autoSpacing(BASE_SQUARE,WIDTH,1,0), "y": autoSpacing(BASE_SQUARE,WIDTH,0,4), "w": BASE_SQUARE, "h": BASE_SQUARE}
    D2 = {"colour": NORM_SQUARE, "x": autoSpacing(BASE_SQUARE,WIDTH,2,0), "y": autoSpacing(BASE_SQUARE,WIDTH,0,4), "w": BASE_SQUARE, "h": BASE_SQUARE}
    D3 = {"colour": NORM_SQUARE, "x": autoSpacing(BASE_SQUARE,WIDTH,3,0), "y": autoSpacing(BASE_SQUARE,WIDTH,0,4), "w": BASE_SQUARE, "h": BASE_SQUARE}
    D4 = {"colour": YAY_SQUARE, "x": autoSpacing(BASE_SQUARE,WIDTH,4,0), "y": autoSpacing(BASE_SQUARE,WIDTH,0,4), "w": BASE_SQUARE, "h": BASE_SQUARE}

""" Functions """
def FPS(frames):
    theDelay = 1000//frames
    pg.time.delay(theDelay)
def keyReset():
    global pressed_up_,pressed_left_,pressed_down_,pressed_right_
    pressed_up_ = False
    pressed_left_ = False
    pressed_down_ = False
    pressed_right_ = False
def autoSpacing(squareLength,screenWidth,number=0,letter=0):
    inBetweenSpace = (screenWidth - (squareLength * 4)) // 5
    x = (number * (squareLength + inBetweenSpace)) - (squareLength // 2)
    y = (letter * (squareLength + inBetweenSpace)) - (squareLength // 2)
    return x+y
def writeText(text,rawSquareCoordinateX, rawSquareCoordinateY,size=32,innerColour=(255,255,255),outerColour=None):
    font = pg.font.Font('freesansbold.ttf', size)
    text = font.render(str(text), True, innerColour, None)
    textRect = text.get_rect()
    textRect.center = ((rawSquareCoordinateX + (BASE_SQUARE//2)),(rawSquareCoordinateY + (BASE_SQUARE//2)))
    screen.blit(text, textRect)
def convertNumToCoord(coords):
    (y,x) = coords
    return TILEMAP_Y[y]+TILEMAP_X[x]
def findBestSquares(sampleDict, findBiggest=True):
    if findBiggest == True:
        itemMaxValue = max(sampleDict.items(), key=lambda x: x[1])
    elif findBiggest == False:
        itemMaxValue = min(sampleDict.items(), key=lambda x: x[1])
    listOfKeys = list()
    for key, value in sampleDict.items():
        if value == itemMaxValue[1]:
            listOfKeys.append(key)
    return listOfKeys
def refineList(theList):
    res = []
    for i in theList:
        if i not in res:
            res.append(i)
    return res

""" Pygame Screen Creation """
global screen
import pygame as pg
pg.init()
CODE_RESOURCES()
SQUARE_RESOURCES()
if ALLOW_RANDOM == True:
    import random
screen = pg.display.set_mode([WIDTH, HEIGHT], pg.RESIZABLE)
pg.display.set_caption(NAME)

""" Game Loop """
while RUN == True:
    # Keys
    keyReset()
    FPS(FRAMERATE)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            RUN = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                pressed_up_ = True
            elif event.key == pg.K_LEFT:
                pressed_left_ = True
            elif event.key == pg.K_DOWN:
                pressed_down_ = True
            elif event.key == pg.K_RIGHT:
                pressed_right_ = True
            else:
                print("I dont know what was pressed (-_-)")
    # Draw the screen
    screen.fill(BACKGROUND)
    if DO_BEGINNING_FRAME == False:
        doFullGame()
    elif DO_BEGINNING_FRAME == True:
        drawHomeFrame()
        DO_BEGINNING_FRAME = False
    pg.display.update()
