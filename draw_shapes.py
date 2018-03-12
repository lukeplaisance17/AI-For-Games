#pylint: disable = E1101
#pylint: disable = C0330
import pygame
from vector2 import Vector2
from NodeClass import Node

class Shape(object):
    '''default class for all shapes'''
    def __init__(self, surface, color, pos):
        self.pos = pos
        self.color = color
        self.surface = surface

    def change_color(self, color):
        '''function to change the color of a shape'''
        self.color = color

class Rectangle(Shape):
    '''class for the properties of a rectangle'''
    def __init__(self, surface, color, pos, scale):
        Shape.__init__(self, surface, color, pos)
        self.pygame_object = None
        self.scale_x = scale
        self.scale_y = scale

    def draw_rect(self):
        '''draws a square to the screen'''
        self.pygame_object = pygame.draw.rect(self.surface, (self.color[0],
        self.color[1], self.color[2]), (self.pos.x_position, self.pos.y_position),
        self.scale)

class Line(Shape):
    '''class for the properties of a line'''
    def __init__(self, surface, color, start_pos, end_pos, width):
        Shape.__init__(self, surface, color, start_pos, end_pos, width)
        self.width = width

    def draw_line(self):
        '''draws a line to the screen'''
        pygame.draw.line(self.surface, (self.color[0], self.color[1], self.color[2]),
        (self.pos.x_position, self.pos.y_position), self.length)

class Circle(Shape):
    '''class for the properties of a circle'''
    def __init__(self, surface, color, pos, radius):
        Shape.__init__(self, surface, color, pos)
        self.radius = radius

    def draw_circle(self):
        '''draws a circle to the screen'''
        pygame.draw.circle(self.surface, (self.color[0], self.color[1], self.color[2]),
        (self.pos.x_position, self.pos.y_position), self.radius)
