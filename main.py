from libs import gamelife

def main():
    obj_conway = gamelife.GameOfLife()
    obj_conway.run_animation(100)

if __name__ == '__main__':
    main()
