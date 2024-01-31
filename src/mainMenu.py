import pygame_menu
import pickle

import drawLine as drawLine
import midpoint as midpoint
import fillPolygons as fillPolygons
import drawPolygons as drawPolygons 
import rayCastingMap as rayCastingMap 
import main as main

def mainMenu():
    menu = pygame_menu.Menu('Grafica', main.Cosmetics.disp_size[0], main.Cosmetics.disp_size[1], theme=pygame_menu.themes.THEME_BLUE)

    menu.add.button('Linhas'         ,drawLine.drawLineCanvas)
    menu.add.button('Circulos'       ,midpoint.drawCircleCanvas)
    menu.add.button('Poligonos'      ,drawPolygons.drawPolygonsCanvas)
    menu.add.button('Fill Poligonos' ,fillPolygons.drawPolygonsCanvas)
    menu.add.button('Ray Casting'    ,rayCastingMap.run)
    
    menu.add.vertical_fill()
    
    menu.add.button('Settings' ,settingsMenu)
    menu.add.button('Quit'     ,pygame_menu.events.EXIT)

    menu.mainloop(main.surface)

def settingsMenu():
    menu = pygame_menu.Menu('Settings', main.Cosmetics.disp_size[0], main.Cosmetics.disp_size[1], theme=pygame_menu.themes.THEME_BLUE)

    menu.add.text_input    ('Line Color R: '   ,maxchar=3 ,input_type=pygame_menu.locals.INPUT_INT ,default=main.Cosmetics.lineColorR    ,onchange=lambda value: main.Cosmetics.setLineColorR(value))
    menu.add.text_input    ('Line Color G: '   ,maxchar=3 ,input_type=pygame_menu.locals.INPUT_INT ,default=main.Cosmetics.lineColorG    ,onchange=lambda value: main.Cosmetics.setLineColorG(value))
    menu.add.text_input    ('Line Color B: '   ,maxchar=3 ,input_type=pygame_menu.locals.INPUT_INT ,default=main.Cosmetics.lineColorB    ,onchange=lambda value: main.Cosmetics.setLineColorB(value))
    menu.add.text_input    ('Line Thickness: ' ,maxchar=2 ,input_type=pygame_menu.locals.INPUT_INT ,default=main.Cosmetics.lineThickness ,onchange=lambda value: main.Cosmetics.__setattr__('lineThickness' ,value))
    menu.add.text_input    ('Target FPS: '     ,maxchar=3 ,input_type=pygame_menu.locals.INPUT_INT ,default=main.Cosmetics.targetFPS     ,onchange=lambda value: main.Cosmetics.__setattr__('targetFPS'     ,value))
    menu.add.toggle_switch ('Slow Mode: '                                                          ,default=main.Cosmetics.slowMode      ,onchange=lambda value: main.Cosmetics.__setattr__('slowMode'      ,value))
    
    menu.add.vertical_fill()
    
    menu.add.button('Load'  ,laodCanvas)
    menu.add.button('Save'  ,saveCanvas)
    menu.add.button('Clear' ,clearCanvas)
    menu.add.button('Back'  ,mainMenu)
    
    menu.mainloop(main.surface)

def clearCanvas():
    main.reconstruir.clear()
    main.dataTela = None
    settingsMenu()
    
def laodCanvas():
    file = open(f'data/dataTela.pkl', 'rb+')
    main.dataTela = None
    main.dataTela = pickle.load(file)
    
    file = open(f'data/reconstruir.pkl', 'rb+')
    main.reconstruir.clear()
    main.reconstruir = pickle.load(file)

def saveCanvas():
    file = open(f'data/dataTela.pkl', 'wb+')
    pickle.dump(main.dataTela, file)
    
    file = open(f'data/reconstruir.pkl', 'wb+')
    pickle.dump(main.reconstruir, file)
