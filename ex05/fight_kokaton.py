import pygame as pg
import sys
from random import randint
from time import sleep

COLOR_INV = 1

class Screen:
    def __init__(self, title, wh, bgimg):
        pg.display.set_caption(title) #逃げろ！こうかとん
        self.sfc = pg.display.set_mode(wh) #(1600, 900)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bgimg) #"fig/pg_bg.jpg"
        self.bgi_rct = self.bgi_sfc.get_rect()
        
    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird:
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }

    def __init__(self, img, zoom, xy):
        sfc = pg.image.load(img) # "fig/6.png"
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom) # 2.0
        self.rct = self.sfc.get_rect()
        self.rct.center = xy # 900, 400

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        key_states = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_states[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
                if check_bound(self.rct, scr.rct) != (+1, +1):
                    self.rct.centerx -= delta[0]
                    self.rct.centery -= delta[1]
        self.blit(scr) # =scr.sfc.blit(self.sfc, self.rct)


class Bomb1:
    def __init__(self, color, radius, vxy, scr:Screen):
        self.sfc = pg.Surface((radius*2, radius*2)) # 空のSurface
        self.sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
        pg.draw.circle(self.sfc, color, (radius, radius), radius) # 爆弾用の円を描く
        self.rct = self.sfc.get_rect()
        self.rct.centerx = randint(0, scr.rct.width)
        self.rct.centery = randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        if yoko == -1 or tate == -1:
            self.vx *= 1.1
            self.vy *= 1.1
        self.blit(scr) # =scr.sfc.blit(self.sfc, self.rct)


class Bomb2:
    def __init__(self, color, radius, vxy, scr:Screen):
        self.sfc = pg.Surface((radius*2, radius*2)) # 空のSurface
        self.sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
        pg.draw.circle(self.sfc, color, (radius, radius), radius) # 爆弾用の円を描く
        self.rct = self.sfc.get_rect()
        self.rct.centerx = randint(0, scr.rct.width)
        self.rct.centery = randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        if yoko == -1 or tate == -1:
            self.vx *= 1.1
            self.vy *= 1.1
        self.blit(scr) # =scr.sfc.blit(self.sfc, self.rct)


class Inv_Bomb: #透明な爆弾
    def __init__(self, color, radius, vxy, scr:Screen):
        self.sfc = pg.Surface((radius*2, radius*2)) # 空のSurface
        self.sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
        pg.draw.circle(self.sfc, color, (radius, radius), radius) # 爆弾用の円を描く
        self.rct = self.sfc.get_rect()
        self.rct.centerx = randint(0, scr.rct.width)
        self.rct.centery = randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound_inv(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        if yoko == -1 or tate == -1:
            pg.draw.circle(self.sfc, (COLOR_INV, 0, 0), (10, 10), 10)
        self.blit(scr) # =scr.sfc.blit(self.sfc, self.rct)


class Music:
    def __init__(self,BGM):
        pg.mixer.init(frequency = 44100)    # 初期設定
        pg.mixer.music.load(BGM)     # 音楽ファイルの読み込み
        pg.mixer.music.play(1)              # 再生の終了
        for event in pg.event.get(): 
            if event.type == pg.QUIT:
                pg.mixer.music.stop()
                return

    def se(se):
        pg.mixer.init(frequency = 44100)    # 初期設定
        pg.mixer.music.load(se)     # 音楽ファイルの読み込み
        pg.mixer.music.play(1)              # 音楽の再生回数(1回)
        sleep(1)
        pg.mixer.music.stop()               # 再生の終了
        return 0


def check_bound(obj_rct, scr_rct):
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate

def check_bound_inv(obj_rct, scr_rct):
    global COLOR_INV
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
        if COLOR_INV == 1:
            COLOR_INV = 0
        else:
            COLOR_INV = 1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
        if COLOR_INV == 1:
            COLOR_INV = 0
        else:
            COLOR_INV = 1
    return yoko, tate
        

def main():
    scr = Screen("逃げろ！こうかとん", (1600, 900), "fig/pg_bg.jpg")

    kkt = Bird("fig/6.png", 2.0, (900, 400))

    bkd1 = Bomb1((255, 0, 0), 10, (+1, +1), scr)
    bkd2 = Bomb2((255, 0, 0), 10, (+1, +1), scr)
    bkd3 = Inv_Bomb((255, 0, 0), 10, (+1, +1), scr)

    fonto = pg.font.Font(None, 80)
    tmr = "START"
    RED = ("red")
    txt = fonto.render(str(tmr), True, RED)
    scr.sfc.blit(txt, (725, 450))
    pg.display.update()
    sleep(1)

    clock = pg.time.Clock() #練習1
    Music("data/house_lo.mp3")
    while True:
        scr.blit() # 練習2         
        for event in pg.event.get(): #練習2
            if event.type == pg.QUIT:
                return

        kkt.update(scr)

        bkd1.update(scr)
        bkd2.update(scr)
        bkd3.update(scr)

        scr.sfc.blit(bkd1.sfc, bkd1.rct)#練習5
        scr.sfc.blit(bkd2.sfc, bkd2.rct)
        scr.sfc.blit(bkd3.sfc, bkd3.rct)

        if kkt.rct.colliderect(bkd1.rct):
            return 

        if kkt.rct.colliderect(bkd2.rct):
            return 
        
        if kkt.rct.colliderect(bkd3.rct):
            return 
        

        pg.display.update() #練習2
        clock.tick(1000) 


if __name__ == "__main__":
    pg.init() #初期化
    main() #ゲームの本体
    pg.quit() #初期化の解除
    sys.exit() 