import pygame
import sys
import random

pygame.init()

image_width = 320
image_height = 240
dimensions = (image_width, image_height)
screen = pygame.display.set_mode(dimensions)
screen.fill((0, 0, 0))

surface = pygame.Surface((image_width, image_height))

# for y in range(0, image_height):
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()

#     for x in range(0, image_width):
#         surface.fill((255, 255, 255), (x, y, 1, 1))
    
#     screen.blit(surface, (0, 0))
#     pygame.display.flip()

MinRe = -0.5
MaxRe = 1.0
MinIm = -0.2
MaxIm = MinIm + (MaxRe - MinRe) * image_height / image_width

Re_factor = (MaxRe - MinRe) / (image_width - 1)
Im_factor = (MaxIm - MinIm) / (image_height - 1)
max_iterations = 30

for y in range(0, image_height):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    c_im = MaxIm - y * Im_factor
    for x in range(0, image_width):
        c_re = MinRe + x * Re_factor

        Z_re = c_re
        Z_im = c_im
        color = 0

        for n in range(0, max_iterations):
            Z_re2 = Z_re * Z_re
            Z_im2 = Z_im * Z_im
    
            if Z_re2 + Z_im2 > 4:
                break

            Z_im = 2 * Z_re * Z_im + c_im
            Z_re = Z_re2 - Z_im2 + c_re
            color += 1

        actual_color = (255, 255, 255)
        if color % 2 == 0:
            actual_color = (0, 0, 0)

        surface.fill(actual_color, (x, y, 1, 1))

    screen.blit(surface, (0, 0))
    pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
