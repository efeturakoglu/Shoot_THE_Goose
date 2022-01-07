import pygame, sys
from os import getcwd

path = getcwd()
pygame.init()

# ASSETS

Aim = pygame.image.load(path + "/assets/aim_dot.png")

goose_fly_left = [
    pygame.image.load(path + "/assets/goose/fly_left/1.png"),
    pygame.image.load(path + "/assets/goose/fly_left/2.png"),
    pygame.image.load(path + "/assets/goose/fly_left/3.png"),
    pygame.image.load(path + "/assets/goose/fly_left/4.png")]

goose_fly_right = [
    pygame.image.load(path + "/assets/goose/fly_right/1.png"),
    pygame.image.load(path + "/assets/goose/fly_right/2.png"),
    pygame.image.load(path + "/assets/goose/fly_right/3.png"),
    pygame.image.load(path + "/assets/goose/fly_right/4.png")]


dog_search = [
    pygame.image.load(path + "/assets/dog/search/1.png"),
    pygame.image.load(path + "/assets/dog/search/2.png"),
    pygame.image.load(path + "/assets/dog/search/3.png"),
    pygame.image.load(path + "/assets/dog/search/4.png"),
    pygame.image.load(path + "/assets/dog/search/5.png")

]

dog_found = [
    pygame.image.load(path + "/assets/dog/found/1.png"),
    pygame.image.load(path + "/assets/dog/found/2.png"),
    pygame.image.load(path + "/assets/dog/found/3.png"),

]

dog_aport= [
    pygame.image.load(path + "/assets/dog/aport/1.png"),
    pygame.image.load(path + "/assets/dog/aport/2.png")
]

Background = pygame.image.load(path + "/assets/background.png")
aim_dot = pygame.image.load(path + "/assets/aim_dot.png")



Goose_size = (84, 84)
Dog_size = (104,84)

for i in range(len(goose_fly_right)): goose_fly_right[i] = pygame.transform.scale(goose_fly_right[i], Goose_size)
for i in range(len(goose_fly_left)): goose_fly_left[i] = pygame.transform.scale(goose_fly_left[i], Goose_size)

for i in range(len(dog_search)): dog_search[i] = pygame.transform.scale(dog_search[i],Dog_size)
for i in range(len(dog_found)): dog_found[i] = pygame.transform.scale(dog_found[i],Dog_size)

# Type: Class
# Syntax: Cursor
# Description : Cursor and Mouse position

class Cursor:
    def __init__(self, Window):
        self.Window = Window
        self.X = 0
        self.Y = 0

    def Get(self):
        self.X= pygame.mouse.get_pos()[0]
        self.Y = pygame.mouse.get_pos()[1]
        pos = (self.X, self.Y)

        self.Hitbox = pygame.draw.circle(self.Window, (255, 0, 0), (self.X, self.Y), 5,1)

        return pos

    def Draw(self):
        self.Window.blit(aim_dot,(self.X-20,self.Y-20))


# Type: Class
# Syntax: Goose
# Description: İn-Game object

class Goose:
    def __init__(self, window, x, y):
        self.Window = window
        # self.Cursor = cursor

        self.X = x
        self.Y = y

        self.Dead = False
        self.Direction = "right"

        self.fly_count = 0

    def Calculate_Hitbox(self):
        self.Hitbox = pygame.draw.rect(self.Window, (0, 255, 0), (self.X, self.Y + 10, 62, 48), 1)

    def Draw(self):

        if self.Dead:
            pass

        else:
            if self.Direction == "left":
                self.Window.blit(goose_fly_left[self.fly_count // 1 % len(goose_fly_left)],(self.X - 14, self.Y - 14))

                self.fly_count += 1

            elif self.Direction == "right":
                self.Window.blit(goose_fly_right[self.fly_count // 1 % len(goose_fly_right)],(self.X-6, self.Y-19))

                self.fly_count += 1

        if self.fly_count >= 4:
            self.fly_count = 0

    def Move(self):
        pass


# Type: Class
# Syntax: Window
# Description: Game Window

class Window:
    def __init__(self):

        self.W = 800
        self.H = 600
        self.Res = (self.W, self.H)
        self.frame = pygame.display.set_mode(self.Res, pygame.DOUBLEBUF, 32)
        pygame.display.set_caption("shoot THE goose")

        for i in goose_fly_right: i.convert()
        for i in goose_fly_left: i.convert()
        for i in dog_search: i.convert()
        for i in dog_found: i.convert()
        for i in dog_aport: i.convert()

#Type: Class
#Syntax: Dog
#Description: goose hound

class Dog:
    def __init__(self,window, x, y):
        self.Window = window
        self.X = x
        self.Y = y

        self.state = "search"

        self.count = 0

    def Draw(self):

        if self.state == "search":
            self.Window.blit(dog_search[self.count // 5 % len(dog_search)], (self.X , self.Y ))
            self.X += 3
            self.count += 1
            if self.X >= 200:
                self.state = "found"
                self.count = 0

        elif self.state == "found":

            if self.count > 6:
                self.Window.blit(dog_found[2],(self.X,self.Y))
                self.Y += 15
                if self.Y >= 400:
                    self.state = "pause"
            else:
                self.Window.blit(dog_found[self.count // 3 % len(dog_found)], (self.X, self.Y))
                self.X += 1
                self.Y -= 15
                self.count += 1

        elif self.state == "aport":
            pass

Window = Window()
Cursor = Cursor(Window.frame)
Clock = pygame.time.Clock()
Dog_1 = Dog(Window.frame, 0, 460)
pygame.mouse.set_visible(False)

FPS = 60

while 1:
    Window.frame.blit(Background,(0,0))

    Clock.tick(FPS)
    Dog_1.Draw()
    Cursor.Get()
    Cursor.Draw()

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit(0)

    pygame.display.update()
