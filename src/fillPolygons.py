import pygame
import math
from collections import defaultdict as dd

import main as main
import mainMenu as mainMenu

def drawPolygonsCanvas():

    global lineColor
    lineColor = (main.Cosmetics.lineColorR, main.Cosmetics.lineColorG, main.Cosmetics.lineColorB)

    game_running = True

    main.surface.fill(main.Cosmetics.corFundo)
    
    if len(main.reconstruir) > 0:
        for element in main.reconstruir:
            main.surface.fill(element[1], (element[0], (element[2], element[2])))

    drawing = False
    points = []
    vertices = []
    count = 0

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

            elif ((event.type == pygame.MOUSEBUTTONDOWN) and (not drawing)) or ((event.type == pygame.MOUSEBUTTONDOWN) and (not main.Cosmetics.slowMode)):
                x, y = pygame.mouse.get_pos()
                vertices.append((x,y))
                main.surface.fill(lineColor, ((x, y), (main.Cosmetics.lineThickness, main.Cosmetics.lineThickness)))
                points.extend([(x,y)])
                
                
            elif ((event.type == pygame.KEYDOWN) and (not drawing)) or ((event.type == pygame.KEYDOWN) and (not main.Cosmetics.slowMode)):
                if event.key == pygame.K_SPACE:
                    points.extend(scanLineUtil(vertices, not main.Cosmetics.slowMode))
                    vertices.clear()
                    drawing = True
            
        pygame.display.flip()
        main.clock.tick(main.Cosmetics.targetFPS)

    for point in points:
        main.reconstruir.append((point, lineColor, main.Cosmetics.lineThickness))
    
    main.dataTela = pygame.surfarray.array3d(main.surface)
    
    game_running = False
    mainMenu.mainMenu()

def scanLine(edge_table,y_min,y_max, draw = False):
    active_edge = []
    points = []
    
    for curr_y in range(y_min,y_max+1):
        i=0
        while i<len(active_edge):
            if active_edge[i][2]==curr_y:
                active_edge.pop(i)
            else:
                i+=1
        for e in range(len(active_edge)):
            if e%2: active_edge[e][1]+=active_edge[e][3];active_edge[e][0]=math.floor(active_edge[e][1]);
            else:	 active_edge[e][1]+=active_edge[e][3];active_edge[e][0]=math.ceil(active_edge[e][1]);

        active_edge+=edge_table[curr_y]
        active_edge.sort()

        for cur in range(0,len(active_edge)-1,2):
            for x in range(active_edge[cur][0],active_edge[cur+1][0]+1):
                if draw: main.surface.fill(lineColor, ((x, curr_y), (main.Cosmetics.lineThickness, main.Cosmetics.lineThickness)))
                points.append((x, curr_y)) 
    return points
    
def scanLineUtil(vert, draw = False):
	vert+=[vert[0]]
	edge_table =dd(list)
	for i in range(len(vert)-1):
		x,y,x1,y1 =*vert[i],*vert[i+1]
		if y>y1:
			x,y,x1,y1 =x1,y1,x,y 
		if y==y1:
			continue
		if x1==x:
			slope_inv = 0
		else:	
			slope_inv = (x1-x)/(y1-y)
				 
		edge_table[y].append([x,x,y1,slope_inv])

	y_max = max(v[1] for v in vert)
	y_min = min(v[1] for v in vert)
	
	return scanLine(edge_table,y_min,y_max, draw)
