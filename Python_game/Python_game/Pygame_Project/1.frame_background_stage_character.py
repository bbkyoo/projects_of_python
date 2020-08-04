﻿import os
import pygame
##########################################################

pygame.init() 

screen_width = 480 
screen_height = 640 
screen = pygame.display.set_mode((screen_width,screen_height))


pygame.display.set_caption("") 

clock = pygame.time.Clock()

current_path = os.path.dirname(__file__) # 현재 파일의 위치 변환
image_path = os.path.join(current_path, "images") # images 폴더 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path,"background.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path,"stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 스테이지의 높이 위에 캐릭터를 두기 위해 사용

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path,"character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width /2)
character_y_pos = screen_height - character_height - stage_height

running = True
while running:
    dt = clock.tick(30)

   

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 

   
    screen.blit(background, (0,0))
    screen.blit(stage, (0,screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() 

pygmae.quit()






