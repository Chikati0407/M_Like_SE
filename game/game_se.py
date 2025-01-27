import pyxel

class M_like_SE():
    def __init__(self):

        pyxel.init(width = 200, height = 355, title = "play M like SE")
        self.init_se()
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)


    def init_se(self):
        pyxel.sounds[0].set(
            "e4a3d3g2c2f1e4a3d3g2c2f1b0rrrrrrrrrrrrrrrrrrrrr" * 3,
            "S",
            "7",
            "F",
            1
        )   # 土管
        pyxel.sounds[1].set(
            "b3e4e4e4e4e4e4e4",
            "S",
            "7",
            "NNNNNNNF",
            10
        )   # コイン
        pyxel.sounds[2].set(
            "e3g3e4c4d4g4",
            "S",
            "7",
            "NNNNNF",
            15
        )   # レベルアップ

    def update(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) or pyxel.btnp(pyxel.KEY_SPACE):
            x, y = pyxel.mouse_x, pyxel.mouse_y
            pyxel.play(0,0)
            
        if pyxel.btnp(pyxel.KEY_D):
            pyxel.play(0,0)

        if pyxel.btnp(pyxel.KEY_C):
            pyxel.play(0,1)



        if pyxel.btnp(pyxel.KEY_R):
            pyxel.play(0,2)


    def draw(self):
        pyxel.cls(3)
        pyxel.rect(x = 10,y = 10, w = 180, h = 100, col = 2)
        pyxel.rect(x = 10, y = 120, w = 180, h = 100, col = 5)
        pyxel.rect(x = 10, y = 230, w = 180, h = 100, col = 5)
        

if __name__ == "__main__":
    M_like_SE()