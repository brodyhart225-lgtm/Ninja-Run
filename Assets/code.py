import pygame, sys
pygame.init()
from .pygame_assets import *
from .classes import *
from .images.images import *
from .sounds.sounds import *
version = '0.0'
def main():
    global running
    player_surface = player(player_idle, player_jump)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                """if event.key == pygame.K_SPACE:
                    player_surface.jump(jump_noise)"""
                pass
        clock.tick(60)
        keys= pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            player_surface.jump(jump_noise)
            player_surface.current_image = player_surface.jump_frames[player_surface.index]
        screen.fill('black')
        ##### screen stuff #####
        player_surface.get_state()
        player_surface.apply_all()
        player_surface.draw(screen)
        pygame.display.flip()