import pygame
import sys
import random

# Pygame'ı başlat
pygame.init()

# Oyun ekranı ayarları
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird")

# Renkler
white = (255, 255, 255)
black = (0, 0, 0)

# Kuşun özellikleri
bird_size = 30
bird_x = width // 4
bird_y = height // 2
bird_velocity = 0
gravity = 1

# Boru özellikleri
pipe_width = 50
pipe_height = random.randint(100, 300)
pipe_x = width
pipe_y = height - pipe_height
pipe_velocity = 5
pipe_gap = 100

# Skor
score = 0
font = pygame.font.Font(None, 36)

# Oyun döngüsü
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird_velocity = -10

    # Kuşun hareketi
    bird_y += bird_velocity
    bird_velocity += gravity

    # Borunun hareketi
    pipe_x -= pipe_velocity

    # Boru geldi mi kontrolü
    if pipe_x < 0:
        pipe_x = width
        pipe_height = random.randint(100, 300)
        pipe_y = height - pipe_height
        score += 1

    # Çarpışma kontrolü
    if (
        bird_x < pipe_x + pipe_width
        and bird_x + bird_size > pipe_x
        and (bird_y < pipe_y or bird_y + bird_size > pipe_y + pipe_gap)
    ):
        pygame.time.delay(1000)
        bird_y = height // 2
        pipe_x = width
        score = 0

    # Ekranı temizle
    screen.fill(white)

    # Kuşu çiz
    pygame.draw.rect(screen, black, [bird_x, bird_y, bird_size, bird_size])

    # Boruyu çiz
    pygame.draw.rect(screen, black, [pipe_x, 0, pipe_width, pipe_y])
    pygame.draw.rect(screen, black, [pipe_x, pipe_y + pipe_gap, pipe_width, height - pipe_y - pipe_gap])

    # Skoru ekrana yazdır
    score_text = font.render(f"Score: {score}", True, black)
    screen.blit(score_text, (10, 10))

    # Ekranı güncelle
    pygame.display.update()

    # FPS ayarı
    clock.tick(30)
