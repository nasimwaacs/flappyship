import pygame

class HealthBar(pygame.sprite.Sprite):
	def __init__(self, x, y, color=(255, 0, 0), size=100, height= 20):
		pygame.sprite.Sprite.__init__(self)
		self.x = x
		self.y = y
		self.color = color
		self.size = size
		self.height = height
		self.image = pygame.Surface( (size, height))
		self.image.fill(color)
		self.rect = self.image.get_rect(center=(x, y))
		
	
	def update(self, screen, size):
		if size > 0:
			self.back = pygame.Surface((self.size, self.height))
			self.back_rect = self.back.get_rect(center=(self.x, self.y))
			self.back.fill((200, 200, 200))
			screen.blit(self.back, self.back_rect)
			
			self.image = pygame.Surface((size, self.height))
			self.image.fill(self.color)
			screen.blit(self.image, self.rect)