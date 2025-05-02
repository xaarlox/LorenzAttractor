import pygame
import os
import colorsys
import math

from matrix import matrix_multiplication

os.environ["SDL_VIDEO_CENTERED"] = '1'
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Lorenz attractor 3D")
pygame.init()
clock = pygame.time.Clock()
fps = 60


def hsv_to_rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))


sigma = 10
row = 28
beta = 8 / 3
x, y, z = 0.01, 0, 0
points = []
scale = 15
angle_x, angle_y = 0, 0

run = True
while run:
    screen.fill((0, 0, 0))
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
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

    rotation_x = [[1, 0, 0],
                  [0, math.cos(angle_x), -math.sin(angle_x)],
                  [0, math.sin(angle_x), math.cos(angle_x)]]

    rotation_y = [[math.cos(angle_y), 0, -math.sin(angle_y)],
                  [0, 1, 0],
                  [math.sin(angle_y), 0, math.cos(angle_y)]]

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

    for i, p in enumerate(points):
        rotated = matrix_multiplication(rotation_x, p)
        rotated = matrix_multiplication(rotation_y, rotated)

        distance = 5
        z_val = 1 / (distance - rotated[2][0])

        projection_matrix = [[1, 0, 0], [0, 1, 0]]
        projected = matrix_multiplication(projection_matrix, rotated)
        x_pos = int(projected[0][0] * scale) + width // 2
        y_pos = int(projected[1][0] * scale) + height // 2
        color = hsv_to_rgb(i / len(points), 1, 1)
        pygame.draw.circle(screen, color, (x_pos, y_pos), 2)

    pygame.display.update()
pygame.quit()
