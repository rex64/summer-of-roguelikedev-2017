import tdl


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
        self.player = Object(0, 0, '@')
        self.objects.append(self.player)
        self.objects.append(Object(5, 2, 'D'))

    def render(self):
        self.console.clear(bg=(25, 25, 25))
        self.console.draw_str(1, self.height//2, "Hello r/roguelikedev !")
        self.console.draw_frame(1,1,10,10,'x',(255,0,0))
        for obj in self.objects:
            obj.render(self.console)

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
    game = Game(40, 22)
    game.run()


if __name__ == "__main__":
    main()
