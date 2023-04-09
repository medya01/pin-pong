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
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_RIGHT] and self.rect.x < 630:
            self.rect.x += self.speed
        if key_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx - 7 , self.rect.top, -5, 15, 20 )
        bullets.add(bullet)

window = display.set_mode((500, 500))
clock = time.Clock()

game = True

while game:
    window.fill((200, 255 , 255))

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(60)
