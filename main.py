import pygame

pygame.init()
WIDTH = 750
HEIGHT = 500
canvas = pygame.display.set_mode((WIDTH, HEIGHT))
rect_color = (255,0,0) 

pygame.display.set_caption("Binary Tree Visualizer")
exit = False
while not exit:
    canvas.fill((255, 255, 255)) 
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            exit= True

    pygame.draw.circle(canvas, rect_color, 
                    (WIDTH/2,HEIGHT/2), 20) 
    pygame.display.update()