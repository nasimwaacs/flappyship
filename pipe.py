import pygame

class Pipe(pygame.sprite.Sprite):
	def __init__(self, x=490, y=0, width = 10, height = 400, speed = -2, col=(240, 100, 0)):		
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface( (width, height))
		self.image.fill(col)
		self.rect = self.image.get_rect(center=(x, y))
		#self.rect = self.image.get_rect(topleft=(x, y))
		self.speed = speed
		self.x = x
		self.y = y

	def update(self):
		self.rect.x += self.speed
		if self.rect.right < 0:
			self.kill()

	def setSpeed(self, speed):
		self.speed = speed

