import pygame as pg
import sys
from random import randint
n = 1

def check_bound(obj_rct, scr_rct):
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate

def check_bound_im(obj_rct, scr_rct):
    global n
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
        if n == 1:
            n = 0
        else:
            n = 1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
        if n == 1:
            n = 0
        else:
            n = 1
    return yoko, tate
        

def main():
    #練習1　　
    pg.display.set_caption("逃げろ！こうかとん") 
    scrn_sfc = pg.display.set_mode((1600, 900)) 
    scrn_rct = scrn_sfc.get_rect()
    bg_sfc = pg.image.load("fig/pg_bg.jpg") 
    bg_rct = bg_sfc.get_rect()

    #練習3
    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400

    #練習5
    bomb_sfc = pg.Surface((20, 20)) # 空のsurface
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10) #円を描く
    bomb_sfc.set_colorkey((0, 0, 0))
    bomb_rct  =bomb_sfc.get_rect()
    bomb_rct.centerx = randint(0, scrn_rct.width)
    bomb_rct.centery = randint(0,scrn_rct.height)

    bomb_sfc2 = pg.Surface((20, 20)) # 空のsurface
    pg.draw.circle(bomb_sfc2, (255, 0, 0), (10, 10), 10) #円を描く
    bomb_sfc2.set_colorkey((0, 0, 0))
    bomb_rct2  =bomb_sfc2.get_rect()
    bomb_rct2.centerx = randint(0, scrn_rct.width)
    bomb_rct2.centery = randint(0,scrn_rct.height)

    bomb_sfc3 = pg.Surface((20, 20)) # 空のsurface
    pg.draw.circle(bomb_sfc3, (1, 0, 0), (10, 10), 10) #円を描く
    bomb_sfc3.set_colorkey((0, 0, 0))
    bomb_rct3  =bomb_sfc3.get_rect()
    bomb_rct3.centerx = randint(0, scrn_rct.width)
    bomb_rct3.centery = randint(0,scrn_rct.height)

    #練習6
    vx, vy = +1, +1
    vx2, vy2 = +1, +1
    vx3, vy3 = +1, +1

    clock = pg.time.Clock() #練習1
    while True:
        scrn_sfc.blit(bg_sfc, bg_rct) #練習2
         
        for event in pg.event.get(): #練習2
            if event.type == pg.QUIT:
                return

        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP]: tori_rct.centery -= 1  #こうかとんの縦座標-1
        if key_states[pg.K_DOWN]: tori_rct.centery += 1  #こうかとんの縦座標+1
        if key_states[pg.K_LEFT]: tori_rct.centerx -= 1  #こうかとんの横座標-1
        if key_states[pg.K_RIGHT]: tori_rct.centerx += 1  #こうかとんの横座標+1
        yoko, tate = check_bound(tori_rct, scrn_rct)
        if yoko == -1:
            if key_states[pg.K_LEFT]: 
                tori_rct.centerx += 1
            if key_states[pg.K_RIGHT]:
                tori_rct.centerx -= 1
        if tate == -1:
            if key_states[pg.K_UP]: 
                tori_rct.centery += 1  
            if key_states[pg.K_DOWN]: 
                tori_rct.centery -= 1
        

        scrn_sfc.blit(tori_sfc, tori_rct) #練習3


        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko
        vy *= tate
        bomb_rct.move_ip(vx, vy)
        if yoko == -1 or tate == -1:
            vx *= 1.1
            vy *= 1.1

        yoko, tate = check_bound(bomb_rct2, scrn_rct)
        vx2 *= yoko
        vy2 *= tate
        bomb_rct2.move_ip(vx2, vy2)
        if yoko == -1 or tate == -1:
            vx2 *= 1.1
            vy2 *= 1.1

        yoko, tate = check_bound_im(bomb_rct3, scrn_rct)
        vx3 *= yoko
        vy3 *= tate
        if yoko == -1 or tate == -1:
            pg.draw.circle(bomb_sfc3, (n, 0, 0), (10, 10), 10)
        bomb_rct3.move_ip(vx3, vy3)



        scrn_sfc.blit(bomb_sfc, bomb_rct)#練習5
        scrn_sfc.blit(bomb_sfc2, bomb_rct2)
        scrn_sfc.blit(bomb_sfc3, bomb_rct3)

        if tori_rct.colliderect(bomb_rct):
            return 

        if tori_rct.colliderect(bomb_rct2):
            return 
        
        if tori_rct.colliderect(bomb_rct3):
            return 

        pg.display.update() #練習2
        clock.tick(1000) 


if __name__ == "__main__":
    pg.init() #初期化
    main() #ゲームの本体
    pg.quit() #初期化の解除
    sys.exit() 