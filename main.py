import tdl


SCREEN_WIDTH = 40
SCREEN_HEIGHT = 22

COLOR_RED = 0xff0000
COLOR_WHITE = 0x000000
COLOR_GRAY = 0x95a5a6

class Floor:

    def __init__(self):
        pass

    def render(self, console):
        console.draw_frame(1, 1, SCREEN_WIDTH-2, SCREEN_HEIGHT-2, '#', COLOR_GRAY)


class Object:

    def __init__(self, x, y, char='?', color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, x, y):
        self.x += x
        self.y += y

    def render(self, console):
        console.draw_str(self.x, self.y, self.char, fg=self.color)


class Game:
    
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.console = console = tdl.init(w, h)

        self.objects = []
        self.player = Object(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, '@')
        self.floor = Floor()
        self.objects.append(Object(5, 2, 'D', color=COLOR_RED))
        self.objects.append(Object(15, 4, 'p', color=COLOR_RED))
        self.objects.append(Object(10, 6, '*', color=COLOR_RED))


    def render(self):
        self.console.clear(bg=(25, 25, 25))
        self.floor.render(self.console)
        for obj in self.objects:
            obj.render(self.console)
        self.player.render(self.console)
        tdl.flush()

    def run(self):
        while not tdl.event.is_window_closed():          
            for e in tdl.event.get():
                if e.type == "KEYDOWN":
                    key = e.text.lower()
                    x, y = 0, 0
                    if key == "w":
                        y = -1
                    if key == "a":
                        x = -1
                    if key == "s":
                        y = 1
                    if key == "d":
                        x = 1

                    self.player.move(x, y)

            self.render()
            tdl.event.keyWait()
            

def main():
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.run()


if __name__ == "__main__":
    main()
