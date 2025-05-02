import pygame
import os
import colorsys
import math

os.environ["SDL_VIDEO_CENTERED"] = '1'
width, height = 1280, 720
size = (width, height)
white, black = (200, 200, 200), (0, 0, 0)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Lorenz attractor 3D")
pygame.init()
clock = pygame.time.Clock()
fps = 60

sigma = 10
row = 28
beta = 8 / 3
x, y, z = 0.01, 0, 0
points = []
scale = 15
angle_x, angle_y = 0, 0

run = True
while run:
    screen.fill(black)
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.type == pygame.K_ESCAPE):
            run = False
        elif event.type == pygame.MOUSEWHEEL:
            scale += event.y
            if scale < 1:
                scale = 1

    if pygame.mouse.get_pressed()[0]:
        dx, dy = pygame.mouse.get_rel()
        angle_y += dx * 0.005
        angle_x += dy * 0.005
    else:
        pygame.mouse.get_rel()

    dt = 0.009
    dx = (sigma * (y - x)) * dt
    dy = (x * (row - z) - y) * dt
    dz = (x * y - beta * z) * dt

    x += dx
    y += dy
    z += dz

    point = [[x], [y], [z]]
    points.append(point)
    if len(points) > 10000:
        points.pop(0)

    pygame.display.update()
pygame.quit()
