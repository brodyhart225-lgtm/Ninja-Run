import pygame
class player:
    def __init__(self, idle, jump):
        self.idle_image = idle
        self.jump_image = jump
        self.idle_frames = []
        for col in range(2):
            for row in range(2):
                frame = self.idle_image.subsurface(col*22, row*22, 22, 22)
                framebig = pygame.transform.scale(frame, (88, 88))
                self.idle_frames.append(framebig)
        self.jump_frames = []
        for row in range(2):
            for col in range(2):
                frame = self.jump_image.subsurface(col*22, row*22, 22, 22)
                framebig = pygame.transform.scale(frame, (88, 88))
                self.jump_frames.append(framebig)
        self.state = 'idle'
        self.y_velocity = 0
        self.y = 320
        self.x = 100
        self.current_image = self.idle_frames[0]
        self.current_rect = self.current_image.get_rect(midbottom = (self.x, self.y))
        self.index = 0
        self.frame_timer = 0
        self.frame_limit = 5
        self.frames = self.idle_frames
        self.frame_index_limit = 3
    def draw(self, screen):
        screen.blit(self.frames[self.index], self.current_rect)
    def ground_self(self):
        pass
    def jump(self, sound):
        if self.y >= 320:
            self.y_velocity = -26
            sound.play()
    def apply_all(self):
        if self.y >= 320 and self.y_velocity != -26:
            self.y = 320
            self.y_velocity = 0
        self.y += self.y_velocity
        self.y_velocity += 2
        self.current_rect = self.current_image.get_rect(midbottom = (self.x, self.y))
        self.frame_timer += 1
        if self.frame_timer > self.frame_limit:
            self.index += 1
            if self.index >= self.frame_index_limit:
                self.index = 0
            self.frame_timer = 0
    def get_state(self):
        if self.y >= 320:
            self.frames = self.idle_frames
        else:
            self.frames = self.jump_frames
        
        
