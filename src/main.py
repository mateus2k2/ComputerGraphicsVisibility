import pygame

class GlobalVars:
    def __init__(self):
        self.lineColorR = 100
        self.lineColorG = 255
        self.lineColorB = 50
        self.lineThickness = 6
        self.targetFPS = 600
        self.slowMode = False
        
        self.corFundo = (228, 230, 246)
        self.disp_size = (1000, 700)
        
        self.corLoadingText = (104, 153, 180)
    
    def setLineColorR(self, value):
        if value >= 0 and value <= 255:
            self.lineColorR = value
        else:
            self.lineColorR = 0
    def setLineColorG(self, value):
        if value >= 0 and value <= 255:
            self.lineColorG = value
        else:
            self.lineColorG = 0
    def setLineColorB(self, value):
        if value >= 0 and value <= 255:
            self.lineColorB = value
        else:
            self.lineColorB = 0
        
Cosmetics = GlobalVars()

pygame.init()
surface = pygame.display.set_mode(Cosmetics.disp_size)
pygame.display.set_caption('Grafica')
clock = pygame.time.Clock()

reconstruir = []
dataTela = None