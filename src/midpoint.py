import pygame
import math

import main as main
import mainMenu as mainMenu

def drawCircleCanvas():
    x1, y1, x2, y2 = 100, 100, 700, 500

    global lineColor
    lineColor = (main.Cosmetics.lineColorR, main.Cosmetics.lineColorG, main.Cosmetics.lineColorB)

    clickCount = 0

    game_running = True

    main.surface.fill(main.Cosmetics.corFundo)

    if len(main.reconstruir) > 0:
        for element in main.reconstruir:
            main.surface.fill(element[1], (element[0], (element[2], element[2])))

    points = []
    count = 0
    drawing = False

    while game_running:
        if drawing and main.Cosmetics.slowMode:
            if count < len(points):
                main.surface.fill(lineColor, (points[count], (main.Cosmetics.lineThickness, main.Cosmetics.lineThickness)))
                count += 1
            else:
                drawing = False
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if ((clickCount % 2 == 0) and (not drawing)) or ((clickCount % 2 == 0) and (not main.Cosmetics.slowMode)):
                    x1, y1 = pygame.mouse.get_pos()

                if ((clickCount % 2 == 1) and (not drawing)) or ((clickCount % 2 == 1) and (not main.Cosmetics.slowMode)):
                    x2, y2 = pygame.mouse.get_pos()
                    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                    points.extend(circlePoints((x1, y1), distance, not main.Cosmetics.slowMode))
                    drawing = True
                
                clickCount += 1
            
        pygame.display.flip()
        main.clock.tick(main.Cosmetics.targetFPS)

    for point in points:
        main.reconstruir.append((point, lineColor, main.Cosmetics.lineThickness))
    
    main.dataTela = pygame.surfarray.array3d(main.surface)
    
    game_running = False
    mainMenu.mainMenu()

def circlePoints(center, radius, draw = False):
    pointsToReturn = []
    x, y = center
    x = round(x)
    y = round(y)
    radius = round(radius)

    p = 1 - radius
    x_val, y_val = 0, radius

    pointsToReturn.extend(plotPoints(x, y, x_val, y_val, draw))

    while x_val < y_val:
        x_val += 1
        if p < 0:
            p = p + 2 * x_val + 1
        else:
            y_val -= 1
            p = p + 2 * (x_val - y_val) + 1

        pointsToReturn.extend(plotPoints(x, y, x_val, y_val, draw))

    return pointsToReturn

def plotPoints(x, y, x_val, y_val, draw = False):
    points = [
        (x + x_val, y - y_val),
        (x - x_val, y - y_val),
        (x + x_val, y + y_val),
        (x - x_val, y + y_val),
        (x + y_val, y - x_val),
        (x - y_val, y - x_val),
        (x + y_val, y + x_val),
        (x - y_val, y + x_val),
    ]

    if draw:
        for point in points:
            main.surface.fill(lineColor, (point, (main.Cosmetics.lineThickness, main.Cosmetics.lineThickness)))

    return points
