import pygame, math
h = 650
w = 750
pygame.init()
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Circle")
display = pygame.display.get_surface()

x = w/2
y = h/2
def draw(r,n):
    if n:
        r = r-5
        pygame.draw.circle(screen, 'red', (x,y),r,1)
        draw(r, n-1)

def process(event):
    if event.type == pygame.QUIT:
        exit(0)


draw(300, 400)
pygame.display.flip()
while True:
    process(pygame.event.wait())
