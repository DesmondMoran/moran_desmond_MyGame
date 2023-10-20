# content from kids can code: http://kidscancode.org/blog/

# import libraries and modules
import pygame as pg
from pygame.sprite import Sprite
import random 
from random import randint
import os
from settings import *
from sprites import *
from pygame.math import Vector2 as vec

vec = pg.math.Vector2

# setup asset folders here - images sounds etc.
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
snd_folder = os.path.join(game_folder, 'sounds')


# def draw_text(text, size, color, x, y):
#     font_name = pg.font.match_font('arial')
#     font = pg.font.Font(font_name, size)
#     text_surface = font.render(text, True, color)
#     text_rect = text_surface.get_rect()
#     text_rect.midtop = (x,y)
#     screen.blit(text_surface, text_rect)

class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("My Game...")
        clock = pg.time.Clock()
    def new(self):
        self.all_sprites = pg.sprite.Group
        self.all_platforms = pg.sprite.Group
        self.all_mobs = pg.sprite.Group
        # instantiate classes
        self.player = Player()
        # add instances to groups
        self.all_sprites.add(self.player)

        for p in PLATFORM_LIST:
            plat = Platform(*p)
            self.all_sprites.add(plat)
            self.all_platforms.add(plat)

        for m in range(0,15): 
            m = Mob(randint(0, WIDTH), randint(0, HEIGHT/2), 20, 20, " ")
            self.all_sprites.add(m)
            self.all_mobs.add(m)
        self.run()
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    def update(self):
        self.all_sprites.update()
 
    # # Game loop
    # running = True
    # while running:
    #     # keep the loop running using clock
    #     clock.tick(FPS)

    #     for event in pg.event.get():
    #         # check for closed window
    #         if event.type == pg.QUIT:
    #             running = False
        
    #     ############ Update ##############
    #     # update all sprites
    #     all_sprites.update()

        # this is what prevents the player from falling through the platform when falling down...
        if self.player.vel.y > 0:
                hits = pg.sprite.spritecollide(self.player, self.all_platforms, False)
                if hits:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
                    
        # this prevents the player from jumping up through a platform
        # if player.vel.y < 0:
        #     hits = pg.sprite.spritecollide(player, all_platforms, False)
        #     if hits:
        #         print("ouch")
        #         SCORE -= 1
        #         if player.rect.bottom >= hits[0].rect.top - 5:
        #             player.rect.top = hits[0].rect.bottom
        #             player.acc.y = 5
        #             player.vel.y = 0

        if self.player.vel.y == 0 and self.player.pos.y == HEIGHT/10 :
            SCORE += 1

    def events(self):
        for event in pg.event.get():
        # check for closed window
            if event.type == pg.QUIT:
                self.running = False
    def draw(self):            
        ############ Draw ################
        # draw the background screen
        self.screen.fill(BLACK)
        # draw all sprites
        self.all_sprites.draw(self.screen)
        self.draw_text("Score: " + str(SCORE), 22, BLACK, WIDTH/2, HEIGHT-40)
        # buffer - after drawing everything, flip display
        pg.display.flip()
    
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)

    # def show_start_screen(self):
    #     pass
    # def show_go_screen(self):
    #     pass

# g = Game()
# while g.running:
#     g.new()

pg.quit()