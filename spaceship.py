import pygame
from healthbar import *

class SpaceShip(pygame.sprite.Sprite):
	def __init__(self, imagefile, x=50, y=250, speed_x=1, speed_y=1, scale_x=0.3, scale_y=0.3):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imagefile)
		
		w = self.image.get_width()*scale_x
		h = self.image.get_height()*scale_y
		self.image = pygame.transform.scale(self.image, (w, h))
		self.image = pygame.transform.rotate(self.image, -90)
		
		self.rect = self.image.get_rect()
		
		self.x = x
		self.y = y
		
		self.rect.x = self.x
		self.rect.y = self.y

		self.speed_x = speed_x
		self.speed_y = speed_y

		self.health = 100
		self.healthBar = HealthBar(50, 50, (0, 0, 255), 100, 20)
		


	def move(self, speed):
		self.rect = self.rect.move(speed)
	

	def update(self):
		#check for keys pressed		
		keys_pressed = pygame.key.get_pressed()

		if keys_pressed[pygame.K_LEFT]:
			self.move([-self.speed_x, 0])

		if keys_pressed[pygame.K_RIGHT]:
			self.move([self.speed_x, 0])

		if keys_pressed[pygame.K_UP]:
			self.move([0, -self.speed_y])

		if keys_pressed[pygame.K_DOWN]:
			self.move([0, self.speed_y])

	def blit(self, screen):
		screen.blit(self.image, self.rect)

	def updateHealth(self, screen):
		self.healthBar.update(screen, self.health)

	def damage(self, amount):
		self.health -= amount
		if self.health < 0:
			self.health = 0