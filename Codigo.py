from pygame import *
' ' 'Clases requeridas' ' '

#clase padre para los objetos
class GameSprite(sprite.Sprite):
    #Constructor de clase
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
 
        #Cada objeto debe almacenar la propiedad image
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
 
        #cada objeto debe tener la propiedad rect - el rectángulo en el que se encuentra
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)

    def update(self):
        keys = key.get_pressed()
        if keys [K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys [K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
    
    side = 'izquierda'
    
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'derecha'
        if self.rect.x >= win_width - 85:
            self.direction = 'izquierda'

        if self.direction == 'izquierda':
            self.rect.x -= self.speed
        else: 
            self.rect.x += self.speed
 



#Escena del juego:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

#Personajes del juego:
packman = Player('hero.png', 5, win_height - 80, 4)
monster = Enemy('cyborg.png', win_width - 80, 280, 2)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)

game = True
clock = time.Clock()
FPS = 60

#música
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
           
    
    if finish != True:
        window.blit(background,(0, 0))
        packman.update()
        monster.update()

        packman.reset()
        monster.reset()
        final.reset()



    display.update()
    clock.tick(FPS)
