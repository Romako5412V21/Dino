import pygame 
pygame.init()
y = 1
p = 7
f = 0


class Player():
    def __init__(self,x,y,width,height,image):
        self.original_image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.original_image, (width, height))  # Зміна розміру зображення
        self.rect = self.image.get_rect()
        self.rect.x = x # координати по ширині
        self.rect.y = y # координати по висоті
        self.width = width # ширина
        self.height = height # висотаaaaaaa 
        self.is_jump = False  # змінна для визначення стану прижку
        self.jump_count = 13   # лічильник для керування прижком
    def jumping(self):  # функція для виконання прижку
        if not self.is_jump:  # якщо персонаж не в стані прижку
            self.is_jump = True  # зміна стану прижку
            self.jump_count = 13  # початкове значення лічильника прижку


    def jump(self):  # метод для руху персонажа
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:  # якщо натиснута клавіша пробілу
            self.jumping()  # виконати прижок

        if self.is_jump:  # якщо персонаж у стані прижку
            if self.jump_count >= -13:  # поки лічильник більше або рівний -10
                neg = 1  # коефіцієнт для керування напрямком прижку
                if self.jump_count < 0:  # якщо лічильник менше 0
                    neg = -1  # змінити напрямок прижку
                self.rect.y -= (self.jump_count ** 2) * 0.2 * neg  # формула для прижку
                self.jump_count -= 0.5  # зменшення лічильника
            else:  # якщо лічильник вийшов за межі -10
                self.is_jump = False  # зміна стану прижку

    def move(self):
        self.rect.x -= p
        if self.rect.x <= -100:
            self.rect.x = 1550
    
     

    
    



window = pygame.display.set_mode((1366,700))
pygame.display.set_caption("Гра з персонажем")

background_image = pygame.image.load('pole.jpg')  # Замість 'background.jfif' вкажіть шлях до вашого зображення фону
background_image = pygame.transform.scale(background_image, (1366,700)) # задання розмірів фонового зображення

# Колір фону
bg_color = (255, 255, 255)
player = Player(100, 480, 50, 50, 'Dino.png')
kak = Player(400, 430, 100, 100, 'kak.png')
kak1 = Player(700, 230, 100, 100, 'Ptah.png')
kak2 = Player(850, 230, 100, 100, 'Ptah.png')
kak3 = Player(1150, 430, 100, 100, 'KAKTES.png')
kak4 = Player(1500, 230, 100, 100, 'Ptah.png')
start1 = Player(683,350,500, 100, 'Start1.png')

# Головний цикл гри
clock = pygame.time.Clock()


font1 = pygame.font.Font(None, 36) # 36 - це розмір тексту, при потребі можна змінити на бажаний розмір
text = font1.render(str(f), True, (0,0,0)) # "Привіт!" - текст, який виводиться; (0,0,0) - колір у форматі RGB
game = True
while game:
    p +=  0.001
    f += 1 

       # Відображення фону
    window.blit(background_image, (0, 0))

    # Перевірка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    text = font1.render(str(f), True, (0,0,0))
    window.blit(text, (100,100)) # (10,10) - координати розміщення тексту


    # виклик функції прижку до персонажу
    player.jump()

    

    
    # Оновлення екрану
    window.blit(player.image, (player.rect.x, player.rect.y))  # Відображення зображення гравця
    window.blit(kak.image, (kak.rect.x, kak.rect.y))  
    window.blit(kak1.image, (kak1.rect.x, kak1.rect.y))  
    window.blit(kak2.image, (kak2.rect.x, kak2.rect.y)) 
    window.blit(kak3.image, (kak3.rect.x, kak3.rect.y)) 
    window.blit(kak4.image, (kak4.rect.x, kak4.rect.y)) 
    

    
    if player.rect.colliderect(kak.rect):
       print('Зіткнення відбулося')
       game = False        
    if player.rect.colliderect(kak1.rect):
       print('Зіткнення відбулося')
       game = False
    if player.rect.colliderect(kak2.rect):
       print('Зіткнення відбулося')
       game = False
    if player.rect.colliderect(kak3.rect):
       print('Зіткнення відбулося')
       game = False
    if player.rect.colliderect(kak4.rect):
       print('Зіткнення відбулося')
       game = False
       game = False


    kak.move()
    kak1.move()
    kak2.move()
    kak3.move()
    kak4.move()


    clock.tick(60)
    pygame.display.update()


pygame.quit()
start1.move()    




   