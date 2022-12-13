import pygame as pg
import random
import sys

#終了
def quit():
    pg.quit()
    sys.exit()

#7
def check_bound(obj_rct, scr_rct):
    #第1引数:こうかとんとんrectまたは爆弾rect
    #第2引数:
    #範囲内：+1/範囲外：-1
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or obj_rct.right > scr_rct.right:
        yoko *= -1
    if obj_rct.top < scr_rct.top or obj_rct.bottom > scr_rct.bottom:
        tate *= -1
    return yoko, tate

def main(tori_x, tori_y):
    clock =pg.time.Clock()
    #1
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()
    pgbg_sfc = pg.image.load("fig/pg_bg.jpg")
    pgbg_rct = pgbg_sfc.get_rect()

    #3
    #こうかとんの基本の座標
    move = True
    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = tori_x, tori_y
    scrn_sfc.blit(tori_sfc, tori_rct) 

    #着弾した時のこうかとん
    tori_end_sfc = pg.image.load("fig/8.png")
    tori_end_sfc = pg.transform.rotozoom(tori_end_sfc, 0, 2.0)
    tori_end_rct = tori_end_sfc.get_rect()

    #5
    bomb_sfc = pg.Surface((80, 80)) # 正方形の空のSurface
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (40, 40), 40)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0, scrn_rct.width)
    bomb_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb_sfc, bomb_rct)

    #2個目の爆弾(速度３倍)
    bomb2_sfc = pg.Surface((40, 40))
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb2_sfc, (0, 0, 255), (20, 20), 20)
    bomb2_rct = bomb2_sfc.get_rect()
    bomb2_rct.centerx = random.randint(0, scrn_rct.width)
    bomb2_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb2_sfc, bomb2_rct)

    vx1, vy1 = random.uniform(-1.0,0.5), random.uniform(-1.0,0.5)
    vx2, vy2 = random.uniform(-1.0,0.5), random.uniform(-1.0,0.5)
    i = 0
    #2
    while True:
        scrn_sfc.blit(pgbg_sfc, pgbg_rct) 

        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()

        #4
        key_dct = pg.key.get_pressed() # 辞書型
        if move:
            if key_dct[pg.K_UP]:
                tori_rct.centery -= 2
                tori_y -= 2
            if key_dct[pg.K_DOWN]:
                tori_rct.centery += 2
                tori_y += 2
            if key_dct[pg.K_LEFT]:
                tori_rct.centerx -= 2
                tori_x -= 2
            if key_dct[pg.K_RIGHT]:
                tori_rct.centerx += 2
                tori_x += 2
        else:
            if key_dct[pg.K_r]:
                move = True
                main(tori_x, tori_y)
        if check_bound(tori_rct, scrn_rct) != (+1, +1):
            if key_dct[pg.K_UP]:
                tori_rct.centery += 2
                tori_y += 2
            if key_dct[pg.K_DOWN]:
                tori_rct.centery -= 2
                tori_y -= 2
            if key_dct[pg.K_LEFT]:
                tori_rct.centerx += 2
                tori_x += 2
            if key_dct[pg.K_RIGHT]:
                tori_rct.centerx -= 2
                tori_x -= 2

        scrn_sfc.blit(tori_sfc, tori_rct) 

        #速度をランダムに変化させる
        i += 1
        if i > 10000:
            i = 1
        if move and i%5 == 0.0:
            ver = random.randint(1,8)
            if ver == 1:
                vx1 = vx1+random.uniform(0.1,0.5)
            if ver == 2:
                vx1 = vx1-random.uniform(0.1,0.5)
            if ver == 3:
                vy1 = vy1+random.uniform(0.1,0.5)
            if ver == 4:
                vy1 = vy1-random.uniform(0.1,0.5)
            if ver == 5:
                vx2 = vx2+random.uniform(0.1,0.5)
            if ver == 6:
                vx2 = vx2-random.uniform(0.1,0.5)
            if ver == 7:
                vy2 = vy2+random.uniform(0.1,0.5)
            if ver == 8:
                vy2 = vy2-random.uniform(0.1,0.5)
        #6
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx1 *= yoko
        vy1 *= tate
        bomb_rct.move_ip(vx1,vy1)
        scrn_sfc.blit(bomb_sfc, bomb_rct) 

        yoko, tate = check_bound(bomb2_rct, scrn_rct)
        vx2 *= yoko
        vy2 *= tate
        bomb2_rct.move_ip(vx2,vy2)
        scrn_sfc.blit(bomb2_sfc, bomb2_rct) 

        #8
        if tori_rct.colliderect(bomb_rct) or tori_rct.colliderect(bomb2_rct):
            #動けなくなる
            move = False
            #リスタートを促す文字を表示する
            tmr = "Press the 'r' key and try again!"
            fonto = pg.font.Font(None, 80)
            txt = fonto.render(tmr, True, (0,0,0))
            scrn_sfc.blit(txt, (400,400))
            #こうかとんの画像が切り替わる
            tori_sfc = tori_end_sfc
            tori_rct = tori_end_rct
            tori_rct.center = tori_x, tori_y
            scrn_sfc.blit(tori_sfc, tori_rct)
            vx1, vx2, vy1, vy2 = 0, 0, 0, 0

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    #こうかとんの初期位置
    p_x = 900
    p_y = 400
    main(p_x, p_y)