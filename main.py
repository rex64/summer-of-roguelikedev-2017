import tdl


class Game:
    
    def __init__(self, w, h):
        self.width = w
        self.height = h
        
        self.player_x = 0 
        self.player_y = 0
        
        self.console = console = tdl.init(w, h)

    def render(self):
        self.console.clear()
        self.console.draw_str(1, self.height//2, "Hello r/roguelikedev !")
        self.console.draw_str(self.player_x, self.player_y, "@", fg=(255, 0, 0))
        
        tdl.flush()

    def run(self):
        
        while not tdl.event.is_window_closed():          
            for e in tdl.event.get():
                if e.type == "KEYDOWN":
                    key = e.text.lower()
                    if key == "w":
                        self.player_y -= 1
                    if key == "a":
                        self.player_x -= 1
                    if key == "s":
                        self.player_y += 1
                    if key == "d":
                        self.player_x += 1

            self.render()
            tdl.event.keyWait()
            

def main():
    game = Game(24, 16)
    game.run()


if __name__ == "__main__":
    main()
