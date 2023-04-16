from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_widht, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_widht, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.width = player_widht
        self.height = player_height

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update1(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < 500 - self.height - 5:
            self.rect.y += self.speed

    def update2(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 500 - self.height - 5:
            self.rect.y += self.speed


rocket1 = Player('ракетка.png', 390 , 100 , 5, 100 , 100 )
rocket2 = Player('ракетка.png', 50 , 100 , 5, 100 , 100 )

ball = GameSprite('мячик пингпонг.png', 250 , 400 , 10 , 50 , 50)

window = display.set_mode((500, 500))
clock = time.Clock()

speedx = 5
speedy = 5

font.init()
font1 = font.Font(None , 30)
lose1 = font1.render('первый игрок проиграл' , True , (0, 0 ,0))
lose2 = font1.render('второй игрок проиграл' , True , (0, 0 ,0))


game = True
finish = False

while game:
    if finish != True:
        window.fill((200, 255 , 255))

        ball.rect.x += speedx
        ball.rect.y += speedy

        if ball.rect.y < 0 or ball.rect.y > 500-50:
            speedy *= -1

        if sprite.collide_rect(ball , rocket1 ) or sprite.collide_rect(ball, rocket2):
            speedx *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose2, (200, 200))

        if ball.rect.x > 500-50:
            finish = True
            window.blit(lose1, (200, 200))

        ball.reset()
        rocket1.reset()
        rocket1.update1()
        rocket2.reset()
        rocket2.update2()

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(60)
