    import pygame 

    pygame.init()

    res = input("Resolution : ").split(",")
    x = int(res[0])
    y = int(res[1])
    block = 600/x
    surface = pygame.display.set_mode((600,600)) 
    color = (255,0,0) 
    running = True
    pixel = pygame.Rect(30, 30, block,block)
    pygame.draw.rect(surface,color,pixel) 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
    pygame.display.flip()