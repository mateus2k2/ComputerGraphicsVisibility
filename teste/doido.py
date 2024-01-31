import pygame
from pygame.math import Vector2
import numpy

width, height = 1280, 720

window = pygame.display.set_mode((width, height))
fps = pygame.time.Clock()
FPS = 60

class Segment:
    def __init__(self, pos: Vector2, length: int, target=None) -> None:
        self.pos = pos
        self.length = length
        self.angle = 0
        self.endpos = self.pos + self.length * Vector2(numpy.cos(self.angle), numpy.sin(self.angle))
        self.color = (35, 43, 43)
        self.target = target

    def show(self, win: pygame.surface.Surface) -> None:
        pygame.draw.aaline(win, self.color, (self.pos.x, self.pos.y), (self.endpos.x, self.endpos.y))
        #pygame.draw.line(win, self.color, (self.pos.x, self.pos.y), (self.endpos.x, self.endpos.y), 1)
        #pygame.draw.circle(win, self.color, (self.endpos.x, self.endpos.y), 3)

    def update(self) -> None:
        if self.target != None:
            angle = numpy.arctan2(self.target.y - self.pos.y, self.target.x - self.pos.x)
            self.endpos = self.target
            # self.pos = self.endpos - self.length * Vector2(numpy.cos(angle), numpy.sin(angle))
            this_number = 2
            self.pos = self.endpos - self.length * Vector2(numpy.cos(angle), numpy.sin(angle)) * this_number


class Wire:
    def __init__(self, pos: Vector2, units: int) -> None:
        self.pos = pos
        self.units = units
        self.unitLength = 7
        self.segments = [
            Segment(
                self.pos + (i * self.unitLength * Vector2(1, 0)),
                self.unitLength
            ) for i in range(units)
        ]
        self.segments[-1].target = Vector2(pygame.mouse.get_pos())

    def show(self, win: pygame.surface.Surface) -> None:
        self.segments[-1].target = Vector2(pygame.mouse.get_pos())

        for i in range(1, len(self.segments)):
            self.segments[-i-1].target = self.segments[-i].pos

        for segment in self.segments:
            segment.update()
            segment.show(win)

wire = Wire(Vector2(0, height//2), 50)


def draw() -> None:
    wire.show(window)

def update() -> None:
    window.fill((251, 251, 253))
    draw()
    pygame.display.update()
    fps.tick(FPS)

def run() -> None:
    while True:
        update()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()

run()
