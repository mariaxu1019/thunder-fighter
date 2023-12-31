import pygame
class Display_settings():
    def __init__(self):
        self.width = 800
        self.height = 700
        self.bg_color = (255,255,255)
        self.image = pygame.image.load('resource\Background\Background.jpg')
        self.rect  = self.image.get_rect()



        



class Ship_settings():
    def __init__(self):
        self.speed_factor = 1
        self.limit = 3



class Bullet_settings():
    def __init__(self):
        self.speed_factor = 1
        

class Trick_settings():
    def __init__(self):
        self.speed_factor = 10
        self.width = 100
        self.height = 1000
        self.color = 60,60,60
        self.allowed = 0

class Sun_settings():
    def __init__(self):

        self.x_speed = 1
        self.y_speed = -50

        self.fleet_direction = 1


class Alien_settings():
    def __init__(self):
        self.width = 100
        self.height = 100
       
        self.x_speed = 1
        self.y_speed = 10
        
        self.fleet_direction = 1


        self.point = 50


        


    def initialize_dynamic_settings(self):
     
        self.x_speed = 1
        self.y_speed = 10
        self.fleet_direction = 1

    def increase_speed(self):
        
        self.x_speed *=1.1 
        self.y_speed *=1.1 

        self.point += 50



        


        
        
        
