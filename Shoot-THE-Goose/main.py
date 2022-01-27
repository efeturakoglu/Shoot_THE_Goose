import pygame, sys,random
from os import getcwd

from pygame.constants import MOUSEBUTTONDOWN
from waves import *

path = getcwd()
pygame.init()

# ASSETS


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

goose_dead = []


grey_goose_left = [ 
    pygame.image.load(path + "/assets/grey_goose/fly_left/1.png"),
    pygame.image.load(path + "/assets/grey_goose/fly_left/2.png"),
    pygame.image.load(path + "/assets/grey_goose/fly_left/3.png"),
    pygame.image.load(path + "/assets/grey_goose/fly_left/4.png")]

grey_goose_right = [ 
    pygame.image.load(path + "/assets/grey_goose/fly_right/1.png"),
    pygame.image.load(path + "/assets/grey_goose/fly_right/2.png"),
    pygame.image.load(path + "/assets/grey_goose/fly_right/3.png"),
    pygame.image.load(path + "/assets/grey_goose/fly_right/4.png")]

grey_goose_dead = [
    pygame.image.load(path + "/assets/grey_goose/dead/1.png"),
    pygame.image.load(path + "/assets/grey_goose/dead/2.png"),
    pygame.image.load(path + "/assets/grey_goose/dead/3.png"),
    pygame.image.load(path + "/assets/grey_goose/dead/4.png")]

dog_search = [
    pygame.image.load(path + "/assets/dog/search/1.png"),
    pygame.image.load(path + "/assets/dog/search/2.png"),
    pygame.image.load(path + "/assets/dog/search/3.png"),
    pygame.image.load(path + "/assets/dog/search/4.png"),
    pygame.image.load(path + "/assets/dog/search/5.png")]

dog_found = [
    pygame.image.load(path + "/assets/dog/found/1.png"),
    pygame.image.load(path + "/assets/dog/found/2.png"),
    pygame.image.load(path + "/assets/dog/found/3.png"),]

dog_aport= [
    pygame.image.load(path + "/assets/dog/aport/1.png"),
    pygame.image.load(path + "/assets/dog/aport/2.png")]

dog_laugh = [
    pygame.image.load(path + "/assets/dog/laugh/1.png"),
    pygame.image.load(path + "/assets/dog/laugh/2.png")
]

Foreground = pygame.image.load(path + "/assets/foreground.png")
Background = pygame.image.load(path + "/assets/background.png")
aim_dot = pygame.image.load(path + "/assets/aim_dot.png")
Aim = pygame.image.load(path + "/assets/aim_dot.png")
İnfo_background = pygame.image.load(path + "/assets/stat.png")
Heart = pygame.image.load(path + "/assets/heart.png")
Shell = pygame.image.load(path + "/assets/shell.png")
Menu_background = pygame.image.load(path + "/assets/settingbg.png")

Goose_size = (84, 84)
Dog_size = (104,84)

for i in range(len(goose_fly_right)): goose_fly_right[i] = pygame.transform.scale(goose_fly_right[i], Goose_size)
for i in range(len(goose_fly_left)): goose_fly_left[i] = pygame.transform.scale(goose_fly_left[i], Goose_size)

for i in range(len(grey_goose_right)): grey_goose_right[i] = pygame.transform.scale(grey_goose_right[i], Goose_size)
for i in range(len(grey_goose_left)): grey_goose_left[i] = pygame.transform.scale(grey_goose_left[i], Goose_size)

for i in range(len(dog_search)): dog_search[i] = pygame.transform.scale(dog_search[i],Dog_size)
for i in range(len(dog_found)): dog_found[i] = pygame.transform.scale(dog_found[i],Dog_size)
for i in range(len(dog_aport)): dog_aport[i] = pygame.transform.scale(dog_aport[i],(134,96))
for i in range(len(dog_laugh)): dog_laugh[i] = pygame.transform.scale(dog_laugh[i],(72,96))




#____________________________




class Button:
    def __init__(self, Window, Cursor, X, Y, Heigth, Width, Color=(0,0,0), Font_size = 18 ,Text="None") -> None:
        self.Window = Window
        self.X = X
        self.Y = Y
        self.Heigth = Heigth
        self.Width = Width        
        self.Color = Color
        self.Cursor = Cursor
        self.Font_size = Font_size
        self.Text= Text

    def Draw(self,Font_name = "consolas",  Color = (0,0,0)):


        self.Shape = pygame.draw.rect(self.Window.frame, self.Color, (self.X, self.Y, self.Width, self.Heigth))
        
        Font = pygame.font.SysFont(Font_name, self.Font_size, False)

        if Font.size(self.Text)[0] >= self.Width:
            self.Font_size = (self.Font_size - 1 ) - 2


        Text_render = Font.render(self.Text, True, Color)

        self.Window.frame.blit(Text_render, (self.X + (self.Width * (1 / 10)), self.Y + (self.Heigth * (3/10))))


    def Collide(self, event):

        if self.Shape.colliderect(self.Cursor.Hitbox):
            self.Color = (0,0,255)
            if event.type == MOUSEBUTTONDOWN:       
                return True



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
        self.name = "Goose"
        self.Window = window
        # self.Cursor = cursor

        self.X = x
        self.Y = y

        self.Dead = False
        self.Delete = False
        self.Direction = "right"
        self.Move_direction = randint(1,2)
        self.Hitbox = pygame.draw.rect(self.Window, (0, 255, 0), (self.X, self.Y , 62, 48), 1)


        self.price = 1
        self.fly_count = 0
        self.speed = 10

    def Calculate_Hitbox(self):
        if self.Direction == "right":
            self.Hitbox = pygame.draw.rect(self.Window, (0, 255, 0), (self.X-15, self.Y + 20, 62, 48), 1)
        else:
            self.Hitbox = pygame.draw.rect(self.Window, (0, 255, 0), (self.X+20, self.Y + 20, 62, 48), 1)
           

    def Draw(self,Cursor,Mouse_button_down):
        global level_point
        global point
        global Dog_1


        if self.Hitbox.colliderect(Cursor.Hitbox):
            if Mouse_button_down:
                if ammo > 0:
                    self.Dead = True
                    level_point += 1
                    point += 1
                    Dog_1.aport_state += 1


        if self.Dead:
            self.Delete = True

        else:
            if self.Direction == "left":
                self.Window.blit(goose_fly_left[self.fly_count // 1 % len(goose_fly_left)],(self.X - 14, self.Y - 14))

                self.fly_count += 1

            elif self.Direction == "right":
                self.Window.blit(goose_fly_right[self.fly_count // 1 % len(goose_fly_right)],(self.X-6, self.Y-19))

                self.fly_count += 1

        if self.fly_count > 4:
            self.fly_count = 0

    def Move(self):

        if self.Move_direction == 1:
            self.Direction = "right"
            self.X += self.speed
            self.Y -= self.speed
        
        elif self.Move_direction == 2:
            self.Direction = "left"
            self.X -= self.speed
            self.Y -= self.speed

        if self.X > 900 or self.X < 0:
            self.Delete = True

        if self.Y > 700 or self.Y < 0:
            self.Delete = True


#Type: Class
#Syntax: Grey_Goose
#Description: Different colored Goose

class Grey_Goose:
    def __init__(self, window, x, y):
        self.name = "Grey_Goose"
        self.Window = window
        #self.Cursor = cursor

        self.X = x
        self.Y = y

        self.Dead = False
        self.Delete = False
        self.Direction = "right"
        self.Move_direction = randint(1,2)
        self.Hitbox = pygame.draw.rect(self.Window, (0, 255, 0), (self.X, self.Y , 62, 48), 1)


        self.price = 1
        self.fly_count = 0
        self.speed = 10

    def Calculate_Hitbox(self):
        if self.Direction == "right":
            self.Hitbox = pygame.draw.rect(self.Window, (0, 255, 0), (self.X-15, self.Y + 20, 62, 48), 1)
        else:
            self.Hitbox = pygame.draw.rect(self.Window, (0, 255, 0), (self.X+20, self.Y + 20, 62, 48), 1)

    def Draw(self,Cursor,Mouse_button_down):
        global level_point
        global point
        global Dog_1

        if self.Hitbox.colliderect(Cursor.Hitbox):
            if Mouse_button_down:
                if ammo > 0:
                    self.Dead = True
                    level_point += 1
                    point += 1
                    Dog_1.aport_state += 1

        if self.Dead:
            self.Delete = True

        else:
            if self.Direction == "left":
                self.Window.blit(grey_goose_left[self.fly_count // 1 % len(grey_goose_left)],(self.X - 14, self.Y - 14))

                self.fly_count += 1

            elif self.Direction == "right":
                self.Window.blit(grey_goose_right[self.fly_count // 1 % len(grey_goose_right)],(self.X-6, self.Y-19))

                self.fly_count += 1

        if self.fly_count > 4:
            self.fly_count = 0

    def Move(self):

        if self.Move_direction == 1:
            self.Direction = "right"
            self.X += self.speed
            self.Y -= self.speed
        
        elif self.Move_direction == 2:
            self.Direction = "left"
            self.X -= self.speed
            self.Y -= self.speed

        if self.X > 900 or self.X < 0:
            self.Delete = True

        if self.Y > 700 or self.Y < 0:
            self.Delete = True



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
        pygame.font.init()

        Background.convert()
        for i in goose_fly_right: i.convert()
        for i in goose_fly_left: i.convert()
        for i in grey_goose_right: i.convert()
        for i in grey_goose_left: i.convert()
        for i in dog_search: i.convert()
        for i in dog_found: i.convert()
        for i in dog_aport: i.convert()
        for i in dog_laugh: i.convert()


    def Draw_text(self, size, x, y, color = (0,0,0), text = "None", font_name = "consolas"):
        Font = pygame.font.SysFont(font_name, size, False)
        Text = Font.render(text, True, color)
        self.frame.blit(Text, (x, y))

    def Draw_info(self):
        global wave
        global level_number
        global ammo
        global level_point
        global health

        self.frame.blit(İnfo_background,(600,500))
        self.Draw_text(12,690,510,color=(255,255,255),text=f"Point : {level_point}")
        self.Draw_text(12,690,525,color=(255,255,255),text=f"Level : {level_number + 1}")
        self.Draw_text(12,690,540,color=(255,255,255),text=f"Wave : {wave + 1}")

        if health == 3:
            self.frame.blit(Heart,(620,510))
            self.frame.blit(Heart,(620,540))
            self.frame.blit(Heart,(620,570))

        elif health == 2:
            self.frame.blit(Heart,(620,510))
            self.frame.blit(Heart,(620,540))

        elif health == 1:
            self.frame.blit(Heart,(620,510))
        
        else:
            pass

        if ammo == 3:
            self.frame.blit(Shell,(650,510))
            self.frame.blit(Shell,(650,540))
            self.frame.blit(Shell,(650,570))

        elif ammo == 2:
            self.frame.blit(Shell,(650,510))
            self.frame.blit(Shell,(650,540))

        elif ammo == 1:
            self.frame.blit(Shell,(650,510))




#Type: Class
#Syntax: Dog
#Description: goose hound

class Dog:
    def __init__(self,window, x, y):
        self.Window = window
        self.X = x
        self.Y = y

        self.state = "search"
        self.aport_state = 0

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
            if self.aport_state == 1:
                if self.Y <= 400:
                    self.Y = 400
                self.Window.blit(dog_aport[0],(self.X,self.Y))
                self.Y -= 3

            elif self.aport_state == 2:

                if self.Y <= 400:
                    self.Y = 400
                self.Window.blit(dog_aport[1],(self.X,self.Y))
                self.Y -= 3
            elif self.aport_state == 0:
                self.state = "laugh"

        elif self.state == "laugh":
            
            self.Window.blit(dog_laugh[self.count // 3 % len(dog_laugh)], (self.X, self.Y))
            self.count += 1





#____________________________ 

#Type: Function
#Syntax: update_level
#Desrciption: none

def update_level(level_number,wave,counter):
    level = levels[level_number]

    if level_number == counter:
        if wave == 0:
            for npc in level[wave]:
                if npc == "!":
                    level[wave].remove(npc)
                    npc = Goose(Window.frame,random.randint(200,500),400)
                    npc_list.append(npc)

                elif npc== "+":
                    level[wave].remove(npc)
                    npc = Grey_Goose(Window.frame,random.randint(200,500),400)
                    npc_list.append(npc)


        elif wave == 1:
            for npc in level[wave]:
                if npc == "!":
                    level[wave].remove(npc)
                    npc = Goose(Window.frame,200,400)
                    npc_list.append(npc)

                elif npc== "+":
                    level[wave].remove(npc)
                    npc = Grey_Goose(Window.frame,200,400)
                    npc_list.append(npc)



        elif wave == 2:
            for npc in level[wave]:
                if npc == "!":
                    level[wave].remove(npc)
                    npc = Goose(Window.frame,200,400)
                    npc_list.append(npc)

                elif npc== "+":
                    level[wave].remove(npc)
                    npc = Grey_Goose(Window.frame,200,400)
                    npc_list.append(npc)


        elif wave == 3:
            for npc in level[wave]:
                if npc == "!":
                    level[wave].remove(npc)
                    npc = Goose(Window.frame,200,400)
                    npc_list.append(npc)

                elif npc== "+":
                    level[wave].remove(npc)
                    npc = Grey_Goose(Window.frame,200,400)
                    npc_list.append(npc)


        elif wave == 4:
            for npc in level[wave]:
                if npc == "!":
                    level[wave].remove(npc)
                    npc = Goose(Window.frame,200,400)
                    npc_list.append(npc)

                elif npc== "+":
                    level[wave].remove(npc)
                    npc = Grey_Goose(Window.frame,200,400)
                    npc_list.append(npc)



    
#Type: Function
#Syntax: render_npcs
#Description: none

def render_npcs(Dog,npc_list):
    

    if Dog.state== "pause":
        for npc in npc_list:
            if npc.name =="Goose" or npc.name == "Grey_Goose":
                npc.Draw(Cursor,Mouse_button_down)
                npc.Move()

                

#Type: Function
#Syntax: update_npc_list
#Description: none

def update_npc_list(npc_list,level_point,point):
 

    for npc in npc_list:
        
        if npc.Delete:
            npc_list.remove(npc)
            level_point += npc.price
            point += npc.price

def render_menu(event):
    global health
    global level_counter
    global ammo
    global point 
    global level_point
    global wave

    Play_Button = Button(Window,Cursor,350,200,50,250,(0,0,0),Text="Play")
    Play_Button.Draw()

    if Play_Button.Collide(event):
        health = 3
        level_counter = 0
        wave = 0
        point = 0
        level_point = 0
        ammo = 3
        



Window = Window()
Cursor = Cursor(Window.frame)
Clock = pygame.time.Clock()
Dog_1 = Dog(Window.frame, 0, 460)
Mouse_button_down = False
pygame.mouse.set_visible(False)

level_counter = 0
wave = 0
point = 0
level_point = 0
FPS = 60
level_number = 0
item = 0
ammo = 3
health = 0
npc_list = []

while 1:

    for event in pygame.event.get():
        Event = event

        if event.type == pygame.QUIT:
            sys.exit(0)

        if event.type == MOUSEBUTTONDOWN:
            Mouse_button_down = True
            ammo -= 1
        else:
            Mouse_button_down = False


    Clock.tick(FPS)
    Cursor.Get()
    print(Clock.get_fps())

    if health <= 0:
        Window.frame.blit(Background,(0,0))
        Window.frame.blit(Menu_background,(0,0))
        render_menu(Event)

        Cursor.Draw()



        pygame.display.update()

    else:


        for npc in npc_list:
            npc.Calculate_Hitbox()

        if wave >= 5:
            health = 3
            wave = 0
            level_number += 1
            level_counter += 1
            
        Window.frame.blit(Background,(0,0))
        
        if Dog_1.state =="aport":
            Dog_1.Draw()
        
        if Dog_1.state == "laugh":
            Dog_1.Draw()
        
        Window.frame.blit(Foreground,(0,424))
        
        if Dog_1.state == "found" or Dog_1.state == "search":
            Dog_1.Draw()
    

        update_level(level_number,wave,level_counter)

        render_npcs(Dog_1, npc_list)
        
        update_npc_list(npc_list,level_point,point)

        Cursor.Draw()

        Window.Draw_info()

        pygame.display.update()
        
        print(ammo,wave,point,level_number)

        unnamed_level = levels[level_number]

        if npc_list == []:
            if point > 0 :
                Dog_1.state = "aport"
                item += 1
                if item >= 30:
                    Dog_1.aport_state = 0
                    Dog_1.state = "pause"
                    point = 0
                    item = 0
                    wave += 1
                    ammo = 3


            elif point == 0 :
                if ammo <= 0 :
                    Dog_1.state = "laugh"
                    item += 1
                    if item == 30:
                        Dog_1.aport_state = 0
                        Dog_1.state = "pause"
                        point = 0
                        item = 0
                        wave += 1
                        ammo = 3
                        health -= 1


                elif ammo > 0:
                    Dog_1.state = "laugh"
                    item += 1
                    if item == 30:
                        Dog_1.aport_state = 0
                        Dog_1.state = "pause"
                        point = 0
                        item = 0
                        wave += 1
                        ammo = 3
                        health -= 1


    


