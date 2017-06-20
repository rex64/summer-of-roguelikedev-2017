import tdl


def main():
    console = tdl.init(24, 16)
    console.draw_str(1, 16//2, 'Hello r/roguelikedev !')
    tdl.flush()
    tdl.event.keyWait()


if __name__ == "__main__":
    main()
