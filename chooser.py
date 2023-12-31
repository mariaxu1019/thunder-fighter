import pygame
class Chooser():
    
    def __init__(self,screen):
        
        self.screen = screen
        self.image = pygame.image.load('resource\Cards\ChooserBackground.png')
        self.screen_rect = self.screen.get_rect()
        self.rect = self.image.get_rect()

        self.rect.left = self.screen_rect.left
        self.rect.top = self.screen_rect.top

        
        self.card_cherrybomb_image = pygame.image.load('resource\Cards\card_cherrybomb.png')
        self.card_snowpea_image = pygame.image.load('resource\Cards\card_snowpea.png')
        self.card_threepeashooter_image = pygame.image.load('resource\Cards\card_threepeashooter.png')

        self.card_cherrybomb_rect = self.card_cherrybomb_image.get_rect()
        self.card_snowpea_image_rect = self.card_snowpea_image.get_rect()
        self.card_threepeashooter_image_rect = self.card_threepeashooter_image.get_rect()
        
    def blitchooser(self):
        
        self.screen.blit(self.image,self.rect)

    def blitchooser_items(self):


        self.card_cherrybomb_rect.left = self.screen_rect.left + 75 
        self.card_cherrybomb_rect.top = self.screen_rect.top

        self.card_snowpea_image_rect.left = self.card_cherrybomb_rect.left + self.card_snowpea_image_rect.width
        self.card_snowpea_image_rect.top = self.screen_rect.top

        self.card_threepeashooter_image_rect.left = self.card_snowpea_image_rect.left + self.card_threepeashooter_image_rect.width
        self.card_threepeashooter_image_rect.top = self.screen_rect.top

        



        self.screen.blit(self.card_cherrybomb_image,self.card_cherrybomb_rect)
        self.screen.blit(self.card_snowpea_image,self.card_snowpea_image_rect)
        self.screen.blit(self.card_threepeashooter_image,self.card_threepeashooter_image_rect)
        