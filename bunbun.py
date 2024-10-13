import pygame
import random
import sys

pygame.init()

window_width = 550
window_height = 600
window = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Bun Bun")
running = True
clock = pygame.time.Clock()
background = pygame.image.load("Bitmaps/background.png").convert_alpha()
background = pygame.transform.scale(background,(800,600))
grass_image = pygame.image.load("Bitmaps/ground_grass.png").convert_alpha()
grass_image_broken = pygame.image.load("Bitmaps/ground_grass_broken.png").convert_alpha()
small_grass_image_broken = pygame.image.load("Bitmaps/ground_grass_small_broken.png").convert_alpha()
small_grass_image = pygame.image.load("Bitmaps/ground_grass_small.png").convert_alpha()
bunny_stand_image = pygame.image.load("Bitmaps/bunny_stand.png").convert_alpha()
bunny_stand_image = pygame.transform.smoothscale_by(bunny_stand_image,0.7)
bunny_ready_image = pygame.image.load("Bitmaps/bunny_ready.png").convert_alpha()
bunny_ready_image = pygame.transform.smoothscale_by(bunny_ready_image,0.7)
bunny_walk1_image = pygame.image.load("Bitmaps/bunny_walk1.png").convert_alpha()
bunny_walk1_image = pygame.transform.smoothscale_by(bunny_walk1_image,0.7)
bunny_walk2_image = pygame.image.load("Bitmaps/bunny_walk2.png").convert_alpha()
bunny_walk2_image = pygame.transform.smoothscale_by(bunny_walk2_image,0.7)
bunny_walk1_image_flipped = pygame.transform.flip(bunny_walk1_image,True,False)
bunny_walk2_image_flipped = pygame.transform.flip(bunny_walk2_image,True,False)
bunny_jump_image = pygame.image.load("Bitmaps/bunny1_jump.png").convert_alpha()
bunny_jump_image = pygame.transform.smoothscale_by(bunny_jump_image,0.7)
carrot_image = pygame.image.load("Bitmaps/carrot.png").convert_alpha()
carrot_image = pygame.transform.smoothscale_by(carrot_image,0.5)
life_image = pygame.image.load("Bitmaps/life.png").convert_alpha()
life_image = pygame.transform.smoothscale_by(life_image,0.75)
flyman_fly_image = pygame.image.load("Bitmaps/flyman_fly.png").convert_alpha()
flyman_fly_image = pygame.transform.smoothscale_by(flyman_fly_image,0.55)
flyman_jump_image = pygame.image.load("Bitmaps/flyman_jump.png").convert_alpha()
flyman_jump_image = pygame.transform.smoothscale_by(flyman_jump_image,0.55)
plant_image1 = pygame.image.load("Bitmaps/grass1.png").convert_alpha()
plant_image1 = pygame.transform.smoothscale_by(plant_image1,0.5)
plant_image2 = pygame.image.load("Bitmaps/grass2.png").convert_alpha()
plant_image2 = pygame.transform.smoothscale_by(plant_image2,0.5)
wingman1_image = pygame.image.load("Bitmaps/wingman1.png").convert_alpha()
wingman1_image = pygame.transform.smoothscale_by(wingman1_image,0.55)
wingman2_image = pygame.image.load("Bitmaps/wingman2.png").convert_alpha()
wingman2_image = pygame.transform.smoothscale_by(wingman2_image,0.55)
wingman3_image = pygame.image.load("Bitmaps/wingman3.png").convert_alpha()
wingman3_image = pygame.transform.smoothscale_by(wingman3_image,0.55)
wingman4_image = pygame.image.load("Bitmaps/wingman4.png").convert_alpha()
wingman4_image = pygame.transform.smoothscale_by(wingman4_image,0.55)
wingman5_image = pygame.image.load("Bitmaps/wingman5.png").convert_alpha()
wingman5_image = pygame.transform.smoothscale_by(wingman5_image,0.55).convert_alpha()
gold1_image = pygame.image.load("Bitmaps/gold1.png").convert_alpha()
gold1_image = pygame.transform.smoothscale_by(gold1_image,0.46)
gold2_image = pygame.image.load("Bitmaps/gold2.png").convert_alpha()
gold2_image = pygame.transform.smoothscale_by(gold2_image,0.46)
gold3_image = pygame.image.load("Bitmaps/gold3.png").convert_alpha()
gold3_image = pygame.transform.smoothscale_by(gold3_image,0.46)
gold4_image = pygame.image.load("Bitmaps/gold4.png").convert_alpha()
gold4_image = pygame.transform.smoothscale_by(gold4_image,0.46)
gold_hud_image = pygame.image.load("Bitmaps/gold_hud.png").convert_alpha()
gold_hud_image = pygame.transform.smoothscale_by(gold_hud_image,0.7)
fps = 60
joysticks = []

class Platform():
    def __init__(self,x,y,image,scale=0.6):
        self.image = pygame.transform.smoothscale_by(image,scale)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

    def draw(self):
        window.blit(self.image,self.rect)

class Animation():
    def __init__(self,images,max_count=0):
        self.index = 0
        self.counter = 0
        self.max_count = max_count
        self.frames = images
        self.image = self.frames[self.index]
        self.rect = self.image.get_rect()

    def update(self):
        self.counter+=1
        if self.counter > self.max_count:
            self.index += 1
            if self.index > len(self.frames)-1:
                self.index = 0
            self.image = self.frames[self.index]
            self.rect = self.image.get_rect()
            self.counter = 0

class Carrot():
    def __init__(self,x,y):
        self.image = carrot_image
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y

    def draw(self):
        window.blit(self.image,self.rect)

class Plant():
    def __init__(self,x,y):
        self.image = random.choice((plant_image1,plant_image2))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y

    def draw(self):
        window.blit(self.image,self.rect)

class Coin():
    def __init__(self,x,y):
        self.animation = Animation((gold1_image,gold2_image,gold3_image,gold4_image),20)
        self.x = x
        self.y = y

    def update(self):
        self.animation.update()
        self.animation.rect.centerx = self.x
        self.animation.rect.bottom = self.y

    def draw(self):
        window.blit(self.animation.image,self.animation.rect)

class Mob():
    def __init__(self,player,animation):
        self.player = player
        self.animation = animation
        sprite_width = self.animation.image.get_width()
        sprite_height = self.animation.image.get_height()
        half_sprite_width = sprite_width / 2
        random_x_pos = random.choice((-half_sprite_width,window_width+half_sprite_width))
        random_y_pos = random.randrange(0,self.player.y-self.player.animation.rect.height)
        self.direction = 0
        if random_x_pos == window_width+half_sprite_width:
            self.direction = -1
        elif random_x_pos == -half_sprite_width:
            self.direction = 1
        self.x = random_x_pos
        self.y = random_y_pos
        self.vel_x = 4
        self.vel_y = 0
        self.accel_y = 0.25

    def update(self):
        self.x += self.direction * self.vel_x
        self.vel_y += self.accel_y
        if self.vel_y > 2.5:
            self.accel_y = -0.25
        if self.vel_y < -2.5:
            self.accel_y = 0.25
        self.y += self.vel_y
        self.animation.update()
        self.animation.rect.centerx = self.x
        self.animation.rect.centery = self.y

    def draw(self):
        window.blit(self.animation.image,self.animation.rect)

class Player():
    def __init__(self,platforms):
        self.platforms = platforms
        self.animations = {"idle":Animation((bunny_stand_image,bunny_ready_image),20),
                           "walking_right":Animation((bunny_walk1_image,bunny_walk2_image),20),
                           "walking_left":Animation((bunny_walk1_image_flipped,bunny_walk2_image_flipped),20),
                           "jump":Animation((bunny_jump_image,))}
        self.animation = self.animations["idle"]
        self.jump_sound = pygame.mixer.Sound("Sounds/jump sound.wav")
        self.x = self.animation.rect.midbottom[0] + 70
        self.y = self.animation.rect.midbottom[1] + 400
        self.vel_y = 0
        self.vel_x = 0
        self.jump_power = 25
        self.jumped = False
        self.on_ground = False

    def handle_keyboard_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.vel_x += 0.45
            if not self.jumped:
                self.animation = self.animations["walking_right"]
        if keys[pygame.K_a]:
            self.vel_x -= 0.45
            if not self.jumped:
                self.animation = self.animations["walking_left"]

    def jump(self):
        self.vel_y -= self.jump_power
        self.animation = self.animations["jump"]
        self.jump_sound.play()
        self.jumped = True

    def handle_controller_input(self):
        for joystick in joysticks:
            horizontal = joystick.get_axis(0)
            if horizontal < -0.4:
                self.vel_x -= 0.45
                if not self.jumped:
                    self.animation = self.animations["walking_left"]
            elif horizontal > 0.4:
                self.vel_x += 0.45
                if not self.jumped:
                    self.animation = self.animations["walking_right"]
            
    def update(self):
        if not self.jumped:
            self.animation = self.animations["idle"]
        self.vel_y += 1
        if self.vel_y > 18:
            self.vel_y = 18
        self.handle_keyboard_input()
        self.handle_controller_input()
        self.animation.update()
        self.vel_x += -0.10 * self.vel_x
        if abs(self.vel_x) < 0.01:
            self.vel_x = 0
        self.x += self.vel_x
        self.y += self.vel_y
        self.animation.rect.centerx = self.x
        self.animation.rect.bottom = self.y
        if self.x - self.animation.image.get_width() / 2 > window_width:
            self.x = 0
        if self.x + self.animation.image.get_width() / 2 < 0:
            self.x = window_width
        if self.vel_y > 0:
            self.on_ground = False
            for platform in self.platforms:
                if self.animation.rect.colliderect(platform.rect) and self.animation.rect.top < platform.rect.top-95:
                    self.y = platform.rect.top
                    self.vel_y = 0
                    self.jumped = False
                    self.on_ground = True

    def draw(self):
        window.blit(self.animation.image,self.animation.rect)
        
class Game():
    def __init__(self):
        pygame.mixer.music.load("Music/happy tune.wav")
        pygame.mixer.music.set_volume(0.8)
        pygame.mixer.music.play(loops=-1)
        pygame.mouse.set_visible(False)
        window_icon = pygame.image.load("Bitmaps/icon.png")
        window_icon = pygame.transform.smoothscale(window_icon,(32,32))
        pygame.display.set_icon(window_icon)
        self.platforms = self.gen_initial_platforms()
        self.carrots = []
        self.carrot_counter = 0
        self.plants = []
        self.plant_counter = 0
        self.player = Player(self.platforms)
        self.score = 0
        self.lives = 3
        self.max_lives = 3
        self.coins = []
        self.coin_counter = 0
        self.coin_count = 0
        self.eat_sound = pygame.mixer.Sound("Sounds/eat sound.mp3")
        self.start_sound = pygame.mixer.Sound("Sounds/start sound.mp3")
        self.hit_sound = pygame.mixer.Sound("Sounds/hit sound.ogg")
        self.pause_sound = pygame.mixer.Sound("Sounds/pause sound.mp3")
        self.coin_sound = pygame.mixer.Sound("Sounds/coin sound.wav")
        self.start_screen = True
        self.pause_screen = False
        self.go_screen = False
        self.mobs = []
        self.start_time = 0
        self.mob_spawn_time = 1.5
        self.carrot_freq = 20
        self.plant_freq = 2
        self.coin_freq = 10

    def gen_initial_platforms(self):
        platforms = [Platform(20,500,grass_image),
                          Platform(300,400,small_grass_image),
                          Platform(100,250,grass_image),Platform(400,100,small_grass_image)]
        return platforms

    def display_lives(self):
        for life in range(self.lives):
            life_rect = life_image.get_rect()
            life_rect.x = 34 * life + 400
            life_rect.y = 16
            window.blit(life_image,life_rect)
            
    def display_score(self):
        self.draw_text(str(self.score),31,(255,255,255),window_width/2,20)

    def display_coins(self):
        self.draw_coin_text(str(self.coin_count),29,(255,255,255),90,25)
        window.blit(gold_hud_image,(40,15))

    def show_start_screen(self):
        self.draw_text("Bun Bun",65,(255,255,0),window_width/2,100)
        self.draw_text("Press A and D keys to move or the left stick",25,(255,255,255),270,240)
        self.draw_text("Press space bar or A button to jump",25,(255,255,255),275,300)
        self.draw_text("Press E key or B button to play",25,(255,255,255),270,360)

    def show_pause_screen(self):
        self.draw_text("Paused",65,(255,255,0),window_width/2,230)
        self.draw_text("Press E key or B button to unpause",25,(255,255,255),270,320)
        self.start_time = pygame.time.get_ticks() / 1000

    def spawn_mobs(self):
        if pygame.time.get_ticks()/1000 - self.start_time > self.mob_spawn_time:
            mob_animations = (Animation((flyman_fly_image,flyman_jump_image),
                              20),Animation((wingman1_image,wingman2_image,
                                            wingman3_image,wingman4_image,wingman5_image),15))
            mob_animation = random.choice(mob_animations)
            mob = Mob(self.player,mob_animation)
            self.mobs.append(mob)
            self.start_time = pygame.time.get_ticks()/1000
        for mob in self.mobs:
            mob.update()

    def start_game(self):
        self.start_screen = False
        self.start_sound.play()
        self.start_time = pygame.time.get_ticks()/1000

    def pause_game(self):
        self.pause_screen = not self.pause_screen
        self.pause_sound.play()

    def reset_game(self):
        pygame.mixer.music.unload()
        pygame.mixer.music.load("Music/happy tune.wav")
        pygame.mixer.music.play(loops=-1)
        self.go_screen = False
        self.score = 0
        self.lives = 3
        self.coin_count = 0
        self.carrot_counter = 0
        self.coin_counter = 0
        self.plant_counter = 0
        self.start_time = pygame.time.get_ticks()/1000
        self.platforms = self.gen_initial_platforms()
        self.player = Player(self.platforms)
        self.start_sound.play()

    def end_game(self):
        pygame.mixer.music.unload()
        pygame.mixer.music.load("Music/game over.wav")
        pygame.mixer.music.play(loops=-1)
        self.carrots.clear()
        self.coins.clear()
        self.plants.clear()
        self.mobs.clear()
        self.go_screen = True
        
    def show_go_screen(self):
        self.draw_text("Game over",65,(255,255,0),window_width/2,230)
        self.draw_text("Press E key or B button to restart",25,(255,255,255),280,320)

    def draw_text(self,text,size,colour,x,y,alpha=255):
        font = pygame.font.Font("Fonts/Fancake.ttf",size)
        text_image = font.render(text,True,colour)
        text_image.set_alpha(alpha)
        text_rect = text_image.get_rect()
        text_rect.midtop = (x,y)
        window.blit(text_image,text_rect)

    def draw_coin_text(self,text,size,colour,x,y):
        font = pygame.font.Font("Fonts/Fancake.ttf",size)
        text_image = font.render(text,True,colour)
        text_rect = text_image.get_rect()
        text_rect.x = x
        text_rect.y = y
        window.blit(text_image,text_rect)


    def scroll_sprites(self):
        if self.player.y <= window_height / 2:
            self.player.y += abs(self.player.vel_y)
            for platform in self.platforms[:]:
                platform.rect.y += abs(self.player.vel_y)
                if platform.rect.top > window_height:
                    self.score += 10
                    self.platforms.remove(platform)
            for coin in self.coins[:]:
                coin.y += abs(self.player.vel_y)
                past_screen = False
                if coin.animation.rect.top > window_height:
                    past_screen = True
                    self.coins.remove(coin)
                if coin.animation.rect.bottom > window_height-20 and not past_screen:
                    self.coins.remove(coin)
            for carrot in self.carrots[:]:
                carrot.rect.y += abs(self.player.vel_y)
                past_screen = False
                if carrot.rect.top > window_height:
                    past_screen = True
                    self.carrots.remove(carrot)
                if carrot.rect.bottom > window_height-20 and not past_screen:
                    self.carrots.remove(carrot)
            for plant in self.plants[:]:
                plant.rect.y += abs(self.player.vel_y)
                if plant.rect.bottom > window_height:
                    self.plants.remove(plant)
            for mob in self.mobs[:]:
                mob.y += abs(self.player.vel_y)
                if mob.animation.rect.top > window_height:
                    self.mobs.remove(mob)
        self.spawn_platforms()
            
    def spawn_platforms(self):
         if len(self.platforms) < 4:
            platform_images = (grass_image,small_grass_image)
            platform_image = random.choice(platform_images)
            platform = Platform(random.randrange(40,window_width-platform_image.get_width()-40),-30,platform_image)
            self.carrot_counter += 1
            carrot_spawned = False
            if self.carrot_counter > self.carrot_freq:
                carrot_spawned = True
                self.spawn_carrot(platform.rect.centerx,platform.rect.y)
                self.carrot_counter = 0
            self.plant_counter += 1
            if self.plant_counter > self.plant_freq:
                self.plant_freq = random.choice((2,3))
                self.spawn_plant(platform.rect.x,platform.rect.y,platform.image)
                self.plant_counter = 0
            self.coin_counter += 1
            if self.coin_counter > self.coin_freq and not carrot_spawned:
                self.spawn_coin(platform.rect.centerx,platform.rect.y)
                self.coin_counter = 0
            if self.coin_counter > self.coin_freq:
                self.coin_counter = 0
            self.platforms.append(platform)

    def spawn_carrot(self,platform_x,platform_y):
        carrot = Carrot(platform_x,platform_y-10)
        self.carrots.append(carrot)
        
    def spawn_coin(self,platform_x,platform_y):
        coin = Coin(platform_x,platform_y-10)
        self.coins.append(coin)

    def spawn_plant(self,platform_x,platform_y,platform_image):
        plant_positions = ((platform_x+30,platform_y),
                           (platform_x+platform_image.get_width()-30,platform_y))
        plant_pos = random.choice(plant_positions)
        plant = Plant(plant_pos[0],plant_pos[1])
        self.plants.append(plant)

    def handle_collisions(self):
        for carrot in self.carrots[:]:
            if carrot.rect.colliderect(self.player.animation.rect):
                self.carrots.remove(carrot)
                self.eat_sound.play()
                self.lives+=1
                if self.lives > self.max_lives:
                    self.lives = self.max_lives
        for mob in self.mobs[:]:
            if mob.animation.rect.colliderect(self.player.animation.rect):
                self.hit_sound.play()
                self.mobs.remove(mob)
                self.lives-=1
                if self.lives == 0:
                   self.end_game()
        for coin in self.coins[:]:
            if coin.animation.rect.colliderect(self.player.animation.rect):
                self.coin_sound.play()
                self.coin_count += 1
                self.coins.remove(coin)

    def move_sprites_upward(self):
        if self.player.animation.rect.bottom > window_height:
            for platform in self.platforms[:]:
                platform.rect.y -= max(self.player.vel_y,25)
                if platform.rect.bottom < 0:
                    self.platforms.remove(platform)
            if len(self.platforms) == 1:
                self.platforms.clear()
            for carrot in self.carrots[:]:
                carrot.rect.y -= max(self.player.vel_y,25)
                if carrot.rect.bottom < 0:
                    self.carrots.remove(carrot)
            for plant in self.plants[:]:
                plant.rect.y -= max(self.player.vel_y,25)
                if plant.rect.bottom < 0:
                    self.plants.remove(plant)
            for mob in self.mobs[:]:
                mob.y -= max(self.player.vel_y,25)
                if mob.animation.rect.bottom < 0:
                    self.mobs.remove(mob)
            for coin in self.coins[:]:
                coin.y -= max(self.player.vel_y,25)
                if coin.animation.rect.bottom < 0:
                    self.coins.remove(coin)
            if len(self.platforms) == 0 and len(self.mobs) == 0:
                self.end_game()

    def draw_sprites(self):
        for platform in self.platforms:
            platform.draw()
        for plant in self.plants:
            plant.draw()
        for carrot in self.carrots:
            carrot.draw()
        for coin in self.coins:
            coin.draw()
        for mob in self.mobs:
            mob.draw()
        self.player.draw()

    def update(self):
        self.player.update()
        self.scroll_sprites()
        self.spawn_mobs()
        for coin in self.coins:
            coin.update()
        self.handle_collisions()
        self.move_sprites_upward()
                    
    def draw(self):
        self.draw_sprites()
        self.display_score()
        self.display_lives()
        self.display_coins()

game = Game()

while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game.start_screen:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                game.start_game()
            if event.type == pygame.JOYBUTTONDOWN and event.button == 1:
                game.start_game()
        elif game.go_screen:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                game.reset_game()
            if event.type == pygame.JOYBUTTONDOWN and event.button == 1:
                game.reset_game()
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE \
            and not game.player.jumped and game.player.on_ground:
                game.player.jump()
            if event.type == pygame.JOYBUTTONDOWN and event.button == 0 \
            and not game.player.jumped and game.player.on_ground:
                game.player.jump()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                game.pause_game()
            if event.type == pygame.JOYBUTTONDOWN and event.button == 1:
                game.pause_game()
        if event.type == pygame.JOYDEVICEADDED:
            joystick = pygame.joystick.Joystick(event.device_index)
            joysticks.append(joystick)
    window.blit(background,(0,0))
    if game.start_screen:
        game.show_start_screen()
    elif game.go_screen:
        game.show_go_screen()
    elif game.pause_screen:
        game.show_pause_screen()
    else:
        game.update()
        game.draw()
    pygame.display.update()

pygame.quit()
sys.exit()

