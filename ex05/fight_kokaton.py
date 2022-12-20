import pygame as pg
import random
import sys
import os


#音楽を入れる
main_dir = os.path.split(os.path.abspath(__file__))[0]


#終了
def quit():
    pg.quit()
    sys.exit()


class Screen:
    def __init__(self, title, wh, img_path):
        pg.display.set_caption(title) 
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(img_path)
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

    def __init__(self, img_path, ratio, xy):
        self.sfc = pg.image.load(img_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy
        #着弾した時のこうかとん
        self.end_sfc = pg.image.load("../fig/8.png")
        self.end_sfc = pg.transform.rotozoom(self.end_sfc, 0, 2.0)
        self.end_rct = self.end_sfc.get_rect()

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        global move, first_x, first_y
        key_dct = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if move:
                #スローにする能力
                if key_dct[pg.K_SPACE]:
                    clock.tick(1000)
                if key_dct[key]:
                    self.rct.centerx += delta[0]
                    first_x += delta[0]
                    self.rct.centery += delta[1] 
                    first_y += delta[1] 
                if check_bound(self.rct, scr.rct) != (+1, +1):
                    self.rct.centerx -= delta[0]
                    first_x -= delta[0]
                    self.rct.centery -= delta[1] 
                    first_y -= delta[1] 
            else:
                #再スタート
                if key_dct[pg.K_r]:
                    move = True
                    main()
        self.blit(scr)              


class Bomb:
    def __init__(self, color, rad, vxy, scr:Screen):
        self.sfc = pg.Surface((2*rad, 2*rad)) # 正方形の空のSurface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (rad, rad), rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        if move:
            self.rct.move_ip(self.vx, self.vy)
            yoko, tate = check_bound(self.rct, scr.rct)
            self.vx *= yoko
            self.vy *= tate
        self.blit(scr)


class enemy:
    def __init__(self, color, rad, vxy, scr:Screen):
        self.sfc = pg.Surface((2*rad, 2*rad)) # 正方形の空のSurface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (rad, rad), rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        global i        
        #速度をランダムに変化させる
        i += 1
        if i > 10000:
            i = 1
        if move and i%2 == 0.0:
            self.rct.move_ip(self.vx, self.vy)
            ver = random.randint(1,5)
            if ver == 1:
                self.vx = self.vx+random.uniform(0.1,0.5)
            if ver == 2:
                self.vx = self.vx-random.uniform(0.1,0.5)
            if ver == 3:
                self.vy = self.vy+random.uniform(0.1,0.5)
            if ver == 4:
                self.vy = self.vy-random.uniform(0.1,0.5)
            yoko, tate = check_bound(self.rct, scr.rct)
            self.vx *= yoko
            self.vy *= tate
        self.blit(scr)


# テキストの設定 
class Text: 
    def __init__(self): 
        #リスタートを促す文字を表示する
        self.tmr = "Press the 'r' key and try again!"
        self.fonto = pg.font.Font(None, 80)
        self.txt = self.fonto.render(self.tmr, True, (0,0,0))

    def blit(self, scr:Screen):
        scr.sfc.blit(self.txt, (400,400))


def check_bound(obj_rct, scr_rct):
    """
    第1引数：こうかとんrectまたは爆弾rect
    第2引数：スクリーンrect
    範囲内：+1／範囲外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


def finish(scr:Screen, kkt:Bird, bkd:Bomb):
    global move
    #動けなくなる
    move = False
    #こうかとんの画像が切り替わる
    kkt.sfc = kkt.end_sfc
    kkt.rct = kkt.end_rct
    kkt.rct.center = (first_x, first_y)
    scr.sfc.blit(kkt.sfc, kkt.rct)
    bkd.vx, bkd.vy = 0, 0
    text = Text()
    text.blit(scr)
    

def main():
    global clock
    clock =pg.time.Clock()
    #音楽を流す
    if pg.mixer:
        music = os.path.join(main_dir, "data", "house_lo.wav")
        pg.mixer.music.load(music)
        pg.mixer.music.play(-1)
    # 練習１
    scr = Screen("負けるな！こうかとん", (1600,900), "../fig/pg_bg.jpg")
    # 練習３
    kkt = Bird("../fig/6.png", 2.0, (first_x,first_y))
    kkt.update(scr)
    # 練習５
    vx = 1
    vy = 1
    bkd = Bomb((255, 0, 0), 10, (vx, vy), scr)
    bkd.update(scr)
    emy = enemy((0, 0, 255), 20, (vx, vy), scr)
    emy.update(scr)
    # 練習２
    while True:        
        scr.blit()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
        kkt.update(scr)
        bkd.update(scr)
        emy.update(scr)
        if kkt.rct.colliderect(bkd.rct) or kkt.rct.colliderect(emy.rct):
            finish(scr, kkt, bkd)
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    move = True
    clock  = 0
    i = 0
    #こうかとんの初期位置
    first_x = 900
    first_y = 400
    main()