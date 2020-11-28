import pygame, math

pygame.init()
screen = pygame.display.set_mode((750, 650))
pygame.display.set_caption("Fractal Tree")
display = pygame.display.get_surface()

def drawTree(a, b, pos, deepness):
    if deepness:
        c = a + int(math.cos(math.radians(pos)) * deepness**2)
        d = b + int(math.sin(math.radians(pos)) * deepness**2)
        pygame.draw.line(display, (127,255,0), (a, b), (c, d), 1)
        drawTree(c, d, pos - 25, deepness - 1)
        drawTree(c, d, pos + 25, deepness- 1)

def process(event):
    if event.type == pygame.QUIT:
        exit(0)

drawTree(370, 650, -90, 12)
pygame.display.flip()
while True:
    process(pygame.event.wait())
