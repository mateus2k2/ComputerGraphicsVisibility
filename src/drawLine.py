import pygame

import main as main
import mainMenu as mainMenu


def drawLineCanvas():
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
    temp = []
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
                    temp = []

                if ((clickCount % 2 == 1) and (not drawing)) or ((clickCount % 2 == 1) and (not main.Cosmetics.slowMode)):
                    x2, y2 = pygame.mouse.get_pos()
                    points.extend(Bresenham(x1, y1, x2, y2, not main.Cosmetics.slowMode))
                    drawing = True
                
                clickCount += 1
            elif event.type == pygame.MOUSEMOTION and (clickCount % 2 == 1):
                for p in temp:
                    main.surface.fill(main.Cosmetics.corFundo, (p, (main.Cosmetics.lineThickness, main.Cosmetics.lineThickness)))
                x, y = pygame.mouse.get_pos()
                temp = Bresenham(x1, y1, x, y,False)
                pygame.display.flip()
                    
                
            
        pygame.display.flip()
        main.clock.tick(main.Cosmetics.targetFPS)

    for point in points:
        main.reconstruir.append((point, lineColor, main.Cosmetics.lineThickness))
    
    main.dataTela = pygame.surfarray.array3d(main.surface)
    
    game_running = False
    mainMenu.mainMenu()

def Bresenham(x1, y1, x2, y2, draw=False):

    def draw(x,y):
        main.surface.fill(lineColor, ((x,y), (main.Cosmetics.lineThickness, main.Cosmetics.lineThickness)))

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    points = []

    if dx > dy:
        err = 2 * dy - dx
        while x != x2:
            if draw: draw(x,y)
            points.append((x, y))
            err += dy
            if err > 0:
                y += sy
                err -= dx
            x += sx

    else:
        err = 2 * dx - dy
        while y != y2:
            if draw: draw(x,y)
            points.append((x, y))
            err += dx
            if err > 0:
                x += sx
                err -= dy
            y += sy

    return points





# import pygame

# import main as main
# import mainMenu as mainMenu

# def drawLineCanvas():
#     x1, y1, x2, y2 = 100, 100, 700, 500

#     global lineColor
#     lineColor = (main.Cosmetics.lineColorR, main.Cosmetics.lineColorG, main.Cosmetics.lineColorB)

#     clickCount = 0

#     game_running = True

#     main.surface.fill(main.Cosmetics.corFundo)
    
#     if len(main.reconstruir) > 0:
#         for element in main.reconstruir:
#             main.surface.fill(element[1], (element[0], (element[2], element[2])))

#     points = []
#     count = 0
#     drawing = False

#     while game_running:
#         if drawing and main.Cosmetics.slowMode:
#             if count < len(points):
#                 main.surface.fill(lineColor, (points[count], (main.Cosmetics.lineThickness, main.Cosmetics.lineThickness)))
#                 count += 1
#             else:
#                 drawing = False
                
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 game_running = False

#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 if ((clickCount % 2 == 0) and (not drawing)) or ((clickCount % 2 == 0) and (not main.Cosmetics.slowMode)):
#                     x1, y1 = pygame.mouse.get_pos()

#                 if ((clickCount % 2 == 1) and (not drawing)) or ((clickCount % 2 == 1) and (not main.Cosmetics.slowMode)):
#                     x2, y2 = pygame.mouse.get_pos()
#                     points.extend(getLinePoints(x1, y1, x2, y2, not main.Cosmetics.slowMode))
#                     drawing = True
                
#                 clickCount += 1
                
            
#         pygame.display.flip()
#         main.clock.tick(main.Cosmetics.targetFPS)

#     for point in points:
#         main.reconstruir.append((point, lineColor, main.Cosmetics.lineThickness))
    
#     main.dataTela = pygame.surfarray.array3d(main.surface)
    
#     game_running = False
#     mainMenu.mainMenu()

# def getLinePoints(x1, y1, x2, y2, draw=False):
#     dx = abs(x2 - x1)
#     dy = abs(y2 - y1)
#     x, y = x1, y1
#     sx = 1 if x1 < x2 else -1
#     sy = 1 if y1 < y2 else -1

#     points = []

#     if dx > dy:
#         err = dx / 2.0
#         while x != x2:
#             if draw: main.surface.fill(lineColor, ((x,y), (main.Cosmetics.lineThickness, main.Cosmetics.lineThickness)))
#             points.append((x, y))
#             err -= dy
#             if err < 0:
#                 y += sy
#                 err += dx
#             x += sx

#     else:
#         err = dy / 2.0
#         while y != y2:
#             if draw: main.surface.fill(lineColor, ((x,y), (main.Cosmetics.lineThickness, main.Cosmetics.lineThickness)))
#             points.append((x, y))
#             err -= dx
#             if err < 0:
#                 x += sx
#                 err += dy
#             y += sy

#     return points