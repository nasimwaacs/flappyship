import pygame, sys, random
from pygame.locals import QUIT
from pipe import *
from spaceship import *
	
WHITE = (255, 255, 255)
FPS = 60
WIDTH = 600
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Ship')

spaceship = SpaceShip("assets/space_ship.png", 50, 200)

# Create a Sprite Group for the pipes.
pipes = pygame.sprite.Group()
pipe = Pipe()
pipes.add(pipe)

clock = pygame.time.Clock()
count = 1 

while True:
	screen.fill((15, 0, 0))
	count += 1

	# reset count every 100 fames... time = 100/FPS seconds
	# if FPS = 60, count gets reset every ~1.67 seconds
	count = count % 100

	# Spawn a new pipe at the top right of the window
	# every 100/FPS seconds
	if count == 0:
		# add a pipe at the top: default y position = 0
		pipes.add(Pipe(x = WIDTH-10, height=random.randint(100, 500)))
	
	# Spawn a new pipe from the bottom right every 
	# every (100/(2*FPS)) = ~0.83 seconds
	elif count == 50:
		y_pos = random.randint(400, 500)
		#pipes.add(Pipe(x = WIDTH-10, y = 300, height=300, col=(0, 0, 255)))
		pipes.add(Pipe(x = WIDTH-10, y = HEIGHT, height=HEIGHT-y_pos))
											 
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

		'''if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				spaceship.fire()'''

	pipe_collided = pygame.sprite.spritecollideany(spaceship, pipes)

	if (pipe_collided):
		#pipe_collided.image.fill((255, 0, 0))
		spaceship.damage(2)
		pipe_collided.kill()
		
	# Update and blit all pipes
	pipes.update()
	pipes.draw(screen)
	
	spaceship.update()
	spaceship.updateHealth(screen)
	spaceship.blit(screen)

	pygame.display.update()
	clock.tick(FPS)