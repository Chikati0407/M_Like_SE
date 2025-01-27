import pyxel

class M_like_SE():
    def __init__(self):

        pyxel.init(width = 200, height = 355, title = "play M like SE")
        # pyxel.load("audio.pyxres")
        self.init_se()
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)


    def init_se(self):
        pyxel.sounds[0].set(
            "e4a3d3g2c2f1e4a3d3g2c2f1b0rrrrrrrrrrrrrrrrrrrrr" * 3,
            "P",
            "7",
            "F",
            1
        )   # 土管の音
        pyxel.sounds[1].set(
            "b3e4e4e4e4e4e4e4",
            "S",
            "7",
            "NNNNNNNF",
            10
        )   # コインの音
        pyxel.sounds[2].set(
            "e3g3e4c4d4g4",
            "S",
            "7",
            "N",
            15
        )

    def update(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            pyxel.play(0,0)

        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.play(0,1)

        if pyxel.btnp(pyxel.KEY_W):
            pyxel.play(0,2)


    def draw(self):
        pyxel.cls(3)
        pyxel.text(50, 180, "Press SPACE to play sound", pyxel.frame_count % 16)
        

if __name__ == "__main__":
    M_like_SE()