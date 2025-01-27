import pyxel
import platform

try:
    from js import navigator
    is_web_launcher = True
except ImportError:
    is_web_launcher = False

class M_like_SE():
    def __init__(self):

        if is_web_launcher:
            # Web launcherから起動している場合、js関数でOS判定する
            self.user_agent = navigator.userAgent.lower()
            self.os_pc = not ("android" in self.user_agent or "iphone" in self.user_agent or "ipad" in self.user_agent)
        else:
            # ローカルから起動している場合、platformから判定する
            self.os_name = platform.system()
            self.os_pc =  self.os_name == "Windows" or self.os_name == "Darwin" or self.os_name == "Linux"

        self.display_width = 90
        self.display_height = 160
        self.padding = 5
        self.block_width = self.display_width - self.padding * 2
        self.block_height = self.display_height / 3 - self.padding * 2


        pyxel.init(width = self.display_width, height = self.display_height, title = "play M like SE")

        pyxel.mouse(self.os_pc)

        self.init_sound()
        
        pyxel.run(self.update, self.draw)


    def init_sound(self):
        pyxel.sounds[0].set(
            notes = "e4a3d3g2c2f1e4a3d3g2c2f1b0rrrrrrrrrrrrrrrrrrrrr" * 3,
            tones = "S",
            volumes = "7",
            effects = "F",
            speed = 1
        )   # 土管
        pyxel.sounds[1].set(
            notes = "b3e4e4e4e4e4e4e4",
            tones = "S",
            volumes = "7",
            effects = "NNNNNNNF",
            speed = 10
        )   # コイン
        pyxel.sounds[2].set(
            notes = "e3g3e4c4d4g4",
            tones = "S",
            volumes = "7",
            effects = "NNNNNF",
            speed = 15
        )   # 1UP

    def update(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            x, y = pyxel.mouse_x, pyxel.mouse_y
            if (y <= self.display_height // 3):
                pyxel.play(0,0)
            elif (self.display_height // 3 < y) and (y <= self.display_height * 2/3):
                pyxel.play(0,1)
            elif (self.display_height * 2/3) < y:
                pyxel.play(0,2)
            
        if pyxel.btnp(pyxel.KEY_D):
            pyxel.play(0,0)

        if pyxel.btnp(pyxel.KEY_C):
            pyxel.play(0,1)

        if pyxel.btnp(pyxel.KEY_R):
            pyxel.play(0,2)


    def draw(self):

        # writer = puf.Writer("misaki_gothic.ttf")

        pyxel.cls(1)

        pyxel.rect(
            x = self.padding,
            y = self.padding, 
            w = self.block_width, 
            h = self.block_height, 
            col = 11
        )
        pyxel.text(
            x = self.padding * 2, 
            y = self.padding * 2, 
            s = "DOKAN",
            col = 2
        )
        # writer.draw(x = 20, y = 20, text = "土管", font_size = 40, font_color = 2)
        # if self.os_pc:
        #     writer.draw(x = 20, y = 70, text = "D", font_size = 30, font_color = 2)
        
        pyxel.rect(
            x = self.padding, 
            y = self.display_height / 3 + self.padding, 
            w = self.block_width, 
            h = self.block_height, 
            col = 10
        )
        pyxel.text(
            x = self.padding * 2, 
            y = self.display_height / 3 + self.padding * 2, 
            s = "COIN", 
            col = 1
        )
        # writer.draw(x = 20, y = 130, text = "コイン", font_size = 40, font_color = 1)
        # if self.os_pc:
        #     writer.draw(x = 20, y = 180, text = "C", font_size = 30, font_color = 1)

        pyxel.rect(
            x = self.padding, 
            y = self.display_height * 2/3 + self.padding, 
            w = self.block_width, 
            h = self.block_height, 
            col = 2
        )
        pyxel.text(
            x = self.padding * 2, 
            y = self.display_height * 2/3 + self.padding * 2, 
            s = "1UP", 
            col = 11
        )
        # writer.draw(x = 20, y = 240, text = "1UP", font_size = 40, font_color = 11)
        # if self.os_pc:
        #     writer.draw(x = 20, y = 290, text = "R", font_size = 30, font_color = 11)


        

if __name__ == "__main__":
    M_like_SE()