#pylint: disable = E1101
#pylint: disable = C0330
import pygame
from vector2 import Vector2
from draw_shapes import Rectangle
from draw_shapes import Line
from NodeClass import Node
from GraphClass import Graph
from A_starClass import Astar
from visusal_grid import VisualGraph
from visusal_grid import VisualNode

def main():
    '''function to test pygame'''
    pygame.init()
    screen_width = 1265
    screen_height = 720
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill((100, 20, 95))
    grid = Graph(45, 40)
    grid.create_grid()
    graph_visual = VisualGraph(grid, 28, screen)
    start_node = Rectangle(screen, (0, 255, 0), Vector2(0, 419), [25, 25])
    end_node = Rectangle(screen, (255, 0, 0), Vector2(700, 419), [25, 25])
    graph_visual.gen_visual()

    while True:
        screen.fill((100, 20, 95))

        for i in graph_visual.node_visual:
            i.draw()
        start_node.draw_rect()
        end_node.draw_rect()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.event.pump()

    for event in pygame.event.get():
        mouse_x, mouse_y = event.pos
        if mouse_x.pos and mouse_y.pos == start_node.pos:
            start_node.change_color((255, 255, 255))
        elif mouse_x.pos and mouse_y.pos == end_node.pos:
            start_node.change_color((255, 255, 255))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if start_node.collidepoint(event.pos):
                    drag_start = True
                    offset_x = start_node.pos.x_position - mouse_x
                    offset_y = start_node.pos.y_position - mouse_y
                elif end_node.collidpoint(event.pos):
                    drag_end = True
                    offset_x = end_node.pos.x_position - mouse_x
                    offset_y = end_node.pos.y_position - mouse_y
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                count = 0
                if drag_start is True or drag_end is True:
                    for node in grid.nodes:
                        if start_node.colliderect(node):
                            start_node.left = grid.nodes[count].get_x()
                            start_node.top = grid.nodes[count].get_y()
                            drag_start = False
                        if end_node.colliderect(node):
                            end_node.left = grid.nodes[count].get_x()
                            end_node.top = grid.nodes[count].get_y()
                            drag_end = False
                        count += 1
        elif event.type == pygame.MOUSEMOTION:
            if drag_start:
                start_node.pos.x_position = mouse_x + offset_x
                start_node.pos.x_position = mouse_y + offset_y
            elif drag_end:
                end_node.pos.x_position = mouse_x + offset_x
                end_node.pos.x_position = mouse_y + offset_y

        pygame.display.flip()



main()