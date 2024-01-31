import pygame
import math
import numpy as np

import main as main
import mainMenu as mainMenu

def drawPolygonsCanvas(draw=True):

    global lineColor
    lineColor = (main.Cosmetics.lineColorR, main.Cosmetics.lineColorG, main.Cosmetics.lineColorB)

    game_running = True

    main.surface.fill(main.Cosmetics.corFundo)
    
    if len(main.reconstruir) > 0:
        for element in main.reconstruir:
            main.surface.fill(element[1], (element[0], (element[2], element[2])))

    poligonoDesenhado = False
    points = []
    vertices = []

    while game_running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and not poligonoDesenhado:
                x, y = pygame.mouse.get_pos()
                vertices.append((x, y))
                main.surface.fill(lineColor, ((x, y), (main.Cosmetics.lineThickness, main.Cosmetics.lineThickness)))
                points.append((x,y))
                
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not poligonoDesenhado:
                    points.extend(getPolygonPoints(vertices, draw))
                    poligonoDesenhado = True
                    
                if event.key == pygame.K_r and poligonoDesenhado:
                    main.surface.fill(main.Cosmetics.corFundo)
                    points.clear()
                    vertices = rotatePolygon(vertices)
                    points.extend(getPolygonPoints(vertices, draw))

            
        pygame.display.flip()
        main.clock.tick(main.Cosmetics.targetFPS)

    for point in points:
        main.reconstruir.append((point, lineColor, main.Cosmetics.lineThickness))
    
    main.dataTela = pygame.surfarray.array3d(main.surface)
    
    game_running = False
    mainMenu.mainMenu()

def rotatePolygon(vertices, angle_degrees=45):
    angle_radians = math.radians(angle_degrees)
    center_x = sum(x for x, _ in vertices) / len(vertices)
    center_y = sum(y for _, y in vertices) / len(vertices)

    rotated_vertices = []
    for x, y in vertices:
        translated_x = x - center_x
        translated_y = y - center_y

        rotated_x = translated_x * math.cos(angle_radians) - translated_y * math.sin(angle_radians)
        rotated_y = translated_x * math.sin(angle_radians) + translated_y * math.cos(angle_radians)

        final_x = rotated_x + center_x
        final_y = rotated_y + center_y

        rotated_vertices.append((int(final_x), int(final_y)))

    return rotated_vertices
    
def getPolygonPoints(vertices, draw):
    points = []
    for i in range(len(vertices)):
        points.extend(getLinePoints(vertices[i][0], vertices[i][1], vertices[(i+1)%len(vertices)][0], vertices[(i+1)%len(vertices)][1], draw))
    return points

def getLinePoints(x1, y1, x2, y2, draw=False):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    points = []

    if dx > dy:
        err = dx / 2.0
        while x != x2:
            if draw: main.surface.fill(lineColor, ((x, y), (main.Cosmetics.lineThickness, main.Cosmetics.lineThickness)))
            points.append((x, y))
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx

    else:
        err = dy / 2.0
        while y != y2:
            if draw: main.surface.fill(lineColor, ((x, y), (main.Cosmetics.lineThickness, main.Cosmetics.lineThickness)))
            points.append((x, y))
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy

    return points
