import pygame
##########################################################

#�⺻ �ʱ�ȭ (�ݵ�� �ؾ� �ϴ� �͵�)
pygame.init() 

#ȭ�� ũ�� ����
screen_width = 480 #���� ũ��
screen_height = 640 #���� ũ��
screen = pygame.display.set_mode((screen_width,screen_height))

# ȭ�� Ÿ��Ʋ ����
pygame.display.set_caption("���� �̸�") 

# FPS
clock = pygame.time.Clock()

############################################################

# 1. ����� ���� �ʱ�ȭ(���ȭ��, ����, �̹���, ��ǥ, �ӵ�,��Ʈ ��)


# �̺�Ʈ ����
running = True # ������ �������ΰ�?
while running:
    dt = clock.tick(30) # ����ȭ���� �ʴ� ������ ���� ����

    # 2. �̺�Ʈ ó�� (Ű����, ���콺 ��)

    for event in pygame.event.get(): # � �̺�Ʈ�� �߻��Ͽ��°�?
        if event.type == pygame.QUIT: # â�� ������ �̺�Ʈ�� �߻��Ͽ��°�?
            running = False # ������ �������� �ƴ�

    # 3. ���� ĳ���� ��ġ ����

    # 4. �浹 ó��

    # 5. ȭ�鿡 �׸���

    pygame.display.update() # ����ȭ���� �ٽ� �׸���! (�ݵ�� ��� �ؾ���)

# pygame ����
pygame.quit()





