import keyboard
from random import randint, choice
import subprocess
import platform
import time
import keyboard
from colorama import init

init(convert=True)
from colorama import Fore, Back, Style
import sys
import os

os.system("mode con:cols=40 lines=25")
import random
import winsound
from random import randrange
import shutil

columns = shutil.get_terminal_size().columns
Map = (

    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", ' ', " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", ' ', " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
)

start_time = time.time()

y = 0
x = 0
p = 0
d = 0
u = 0
l = 0
r = 0

g = 5
v = 0
b = 5
z = 0


# py = 2
# px = 2
Map[x][y] = '@'

colors = [(Fore.RED, Style.BRIGHT), (Fore.YELLOW, Style.BRIGHT), (Fore.BLUE, Style.BRIGHT)]



def win():
    winsound.PlaySound('SystemHand', winsound.SND_ASYNC)
    print(Fore.RED, Style.BRIGHT)
    clear()
    draw_map()
    time.sleep(0.5)
    winsound.PlaySound('SystemHand', winsound.SND_ASYNC)
    print(Fore.YELLOW, Style.BRIGHT)
    clear()
    draw_map()
    time.sleep(0.5)
    winsound.PlaySound('SystemHand', winsound.SND_ASYNC)
    print(Fore.GREEN, Style.BRIGHT)
    clear()
    draw_map()
    clear()
    time.sleep(0.5)
    print(Style.RESET_ALL)
    print(Back.GREEN + Fore.BLACK)
    print("                                        ")
    print(Style.RESET_ALL)
    print(Fore.GREEN, Style.BRIGHT)
    print('CONGRATULATIONS!'.center(columns))
    print("  ----- %s seconds -----" % (time.time() - start_time))

    print("\n")
    print("UP:                                 ", u)
    print("DOWN:                               ", d)
    print("LEFT:                               ", l)
    print("RIGHT:                              ", r)
    print("BOMB USED:                          ", v)
    print("PORTAL USED:                        ", z)
    print("POINTS: 100 -", u, "-", d, "-", l, "-", r, "-", v, "-", z, "=")
    w = 100 - u -d - l - r - v - z
    print(w)
    print(Style.RESET_ALL)
    print(Back.GREEN + Fore.BLACK)
    print("                                        ")
    print(Style.RESET_ALL)
    print(Fore.GREEN, Style.BRIGHT)
    print('Hit ESC to quit.')


def draw_map2():
    print(Map[2][0] + Map[2][1] + Map[2][2] + Map[2][3] + Map[2][4] + Map[2][5] + Map[2][6] + Map[2][7] + Map[2][8] + Map[2][9] + Map[2][10] + Map[2][11] + Map[2][12] + Map[2][13] + Map[2][14] + Map[2][15])
    print(Map[3][0] + Map[3][1] + Map[3][2] + Map[3][3] + Map[3][4] + Map[3][5] + Map[3][6] + Map[3][7] + Map[3][8] + Map[3][9] + Map[3][10] + Map[3][11] + Map[3][12] + Map[3][13] + Map[3][14] + Map[3][15])
    print(Map[4][0] + Map[4][1] + Map[4][2] + Map[4][3] + Map[4][4] + Map[4][5] + Map[4][6] + Map[4][7] + Map[4][8] + Map[4][9] + Map[4][10] + Map[4][11] + Map[4][12] + Map[4][13] + Map[4][14] + Map[4][15])
    print(Map[5][0] + Map[5][1] + Map[5][2] + Map[5][3] + Map[5][4] + Map[5][5] + Map[5][6] + Map[5][7] + Map[5][8] + Map[5][9] + Map[5][10] + Map[5][11] + Map[5][12] + Map[5][13] + Map[5][14] + Map[5][15])
    print(Map[6][0] + Map[6][1] + Map[6][2] + Map[6][3] + Map[6][4] + Map[6][5] + Map[6][6] + Map[6][7] + Map[6][8] + Map[6][9] + Map[6][10] + Map[6][11] + Map[6][12] + Map[6][13] + Map[6][14] + Map[6][15])
    print(Map[7][0] + Map[7][1] + Map[7][2] + Map[7][3] + Map[7][4] + Map[7][5] + Map[7][6] + Map[7][7] + Map[7][8] + Map[7][9] + Map[7][10] + Map[7][11] + Map[7][12] + Map[7][13] + Map[7][14] + Map[7][15])
    print(Map[8][0] + Map[8][1] + Map[8][2] + Map[8][3] + Map[8][4] + Map[8][5] + Map[8][6] + Map[8][7] + Map[8][8] + Map[8][9] + Map[8][10] + Map[8][11] + Map[8][12] + Map[8][13] + Map[8][14] + Map[8][15])
    print(Map[9][0] + Map[9][1] + Map[9][2] + Map[9][3] + Map[9][4] + Map[9][5] + Map[9][6] + Map[9][7] + Map[9][8] + Map[9][9] + Map[9][10] + Map[9][11] + Map[9][12] + Map[9][13] + Map[9][14] + Map[9][15])
    print(Map[10][0] + Map[10][1] + Map[10][2] + Map[10][3] + Map[10][4] + Map[10][5] + Map[10][6] + Map[10][7] + Map[10][8] + Map[10][9] + Map[10][10] + Map[10][11] + Map[10][12] + Map[10][13] + Map[10][14] + Map[10][15])
    print(Map[11][0] + Map[11][1] + Map[11][2] + Map[11][3] + Map[11][4] + Map[11][5] + Map[11][6] + Map[11][7] + Map[11][8] + Map[11][9] + Map[11][10] + Map[11][11] + Map[11][12] + Map[11][13] + Map[11][14] + Map[11][15])
    print(Map[12][0] + Map[12][1] + Map[12][2] + Map[12][3] + Map[12][4] + Map[12][5] + Map[12][6] + Map[12][7] + Map[12][8] + Map[12][9] + Map[12][10] + Map[12][11] + Map[12][12] + Map[12][13] + Map[12][14] + Map[12][15])
    print(Map[13][0] + Map[13][1] + Map[13][2] + Map[13][3] + Map[13][4] + Map[13][5] + Map[13][6] + Map[13][7] + Map[13][8] + Map[13][9] + Map[13][10] + Map[13][11] + Map[13][12] + Map[13][13] + Map[13][14] + Map[13][15])

def draw_map():
    global d
    global u
    global l
    global r
    global g
    global b
    global w
    global z
    t = u + d + l + r
    print(Map[0][0] + Map[0][1] + Map[0][2] + Map[0][3] + Map[0][4] + Map[0][5] + Map[0][6] + Map[0][7] + Map[0][8] + Map[0][9] + Map[0][10] + Map[0][11] + Map[0][12] + Map[0][13] + Map[0][14] + Map[0][15] + "\n" + Map[1][0] + Map[1][1] + Map[1][2] + Map[1][3] + Map[1][4] + Map[1][5] + Map[1][6] + Map[1][7] + Map[1][8] + Map[1][9] + Map[1][10] + Map[1][11] + Map[1][12] + Map[1][13] + Map[1][14] + Map[1][15] + "\n" + Map[2][0] + Map[2][1] + Map[2][2] + Map[2][3] + Map[2][4] + Map[2][5] + Map[2][6] + Map[2][7] + Map[2][8] + Map[2][9] + Map[2][10] + Map[2][11] + Map[2][12] + Map[2][13] + Map[2][14] + Map[2][15] + "\n" + Map[3][0] + Map[3][1] + Map[3][2] + Map[3][3] + Map[3][4] + Map[3][5] + Map[3][6] + Map[3][7] + Map[3][8] + Map[3][9] + Map[3][10] + Map[3][11] + Map[3][12] + Map[3][13] + Map[3][14] + Map[3][15] + "\n" + Map[4][0] + Map[4][1] + Map[4][2] + Map[4][3] + Map[4][4] + Map[4][5] + Map[4][6] + Map[4][7] + Map[4][8] + Map[4][9] + Map[4][10] + Map[4][11] + Map[4][12] + Map[4][13] + Map[4][14] + Map[4][15] + "\n" + Map[5][0] + Map[5][1] + Map[5][2] + Map[5][3] + Map[5][4] + Map[5][5] + Map[5][6] + Map[5][7] + Map[5][8] + Map[5][9] + Map[5][10] + Map[5][11] + Map[5][12] + Map[5][13] + Map[5][14] + Map[5][15] + "\n" + Map[6][0] + Map[6][1] + Map[6][2] + Map[6][3] + Map[6][4] + Map[6][5] + Map[6][6] + Map[6][7] + Map[6][8] + Map[6][9] + Map[6][10] + Map[6][11] + Map[6][12] + Map[6][13] + Map[6][14] + Map[6][15] + "\n" + Map[7][0] + Map[7][1] + Map[7][2] + Map[7][3] + Map[7][4] + Map[7][5] + Map[7][6] + Map[7][7] + Map[7][8] + Map[7][9] + Map[7][10] + Map[7][11] + Map[7][12] + Map[7][13] + Map[7][14] + Map[7][15] + "\n" + Map[8][0] + Map[8][1] + Map[8][2] + Map[8][3] + Map[8][4] + Map[8][5] + Map[8][6] + Map[8][7] + Map[8][8] + Map[8][9] + Map[8][10] + Map[8][11] + Map[8][12] + Map[8][13] + Map[8][14] + Map[8][15] + "\n" + Map[9][0] + Map[9][1] + Map[9][2] + Map[9][3] + Map[9][4] + Map[9][5] + Map[9][6] + Map[9][7] + Map[9][8] + Map[9][9] + Map[9][10] + Map[9][11] + Map[9][12] + Map[9][13] + Map[9][14] + Map[9][15] + "\n" + Map[10][0] + Map[10][1] + Map[10][2] + Map[10][3] + Map[10][4] + Map[10][5] + Map[10][6] + Map[10][7] + Map[10][8] + Map[10][9] + Map[10][10] + Map[10][11] + Map[10][12] + Map[10][13] + Map[10][14] + Map[10][15] + "\n" + Map[11][0] + Map[11][1] + Map[11][2] + Map[11][3] + Map[11][4] + Map[11][5] + Map[11][6] + Map[11][7] + Map[11][8] + Map[11][9] + Map[11][10] + Map[11][11] + Map[11][12] + Map[11][13] + Map[11][14] + Map[11][15] + "\n" + Map[12][0] + Map[12][1] + Map[12][2] + Map[12][3] + Map[12][4] + Map[12][5] + Map[12][6] + Map[12][7] + Map[12][8] + Map[12][9] + Map[12][10] + Map[12][11] + Map[12][12] + Map[12][13] + Map[12][14] + Map[12][15] + "\n" + Map[13][0] + Map[13][1] + Map[13][2] + Map[13][3] + Map[13][4] + Map[13][5] + Map[13][6] + Map[13][7] + Map[13][8] + Map[13][9] + Map[13][10] + Map[13][11] + Map[13][12] + Map[13][13] + Map[13][14] + Map[13][15])
    item()




def item():
    global d
    global u
    global l
    global r
    global g
    global b
    t = u + d + l + r
    print(Style.RESET_ALL)
    print(Back.GREEN + Fore.BLACK)
    print("                                        ")
    print(Style.RESET_ALL)
    print(Fore.GREEN, Style.BRIGHT)
    print("PORTALS *G         UNUSED: ", g)
    print("BOMBS   *IJKL      UNUSED: ", b)
    print("MOVE:   *WASD      TOTAL   ", t)
    print('GIVE UP *T                    ')
    print("ESC      TO        QUIT")


# MOVES

def coin():
    for i in range(13):

        # i para cada linha de 0 a 9 fazer
        for j in range(15):
            # j para cada coluna de 0 a 9 fazer

            flip_coin = randrange(4)

            if flip_coin == 0:
                Map[i][j] = " "

            elif flip_coin == 1:
                Map[i][j] = " "
            elif flip_coin == 2:
                Map[i][j] = "$"
            else:
                Map[i][j] = u"\u2588"


def move_player(move):
    global x
    global y
    global d
    global u
    global l
    global r
    global g
    global b
    global v
    global z
    # global fix th error

    if move.name == 's':  # DOWN
        if x < 12 and Map[x + 1][y] != u"\u2588" and Map[x + 1][y] != "$" and Map[x + 1][y] != "E":  # 4 is the edge of the map
            clear()
            x += 1  # it is x = x + 1
            d += 1
            Map[x][y] = "@"
            Map[x - 1][y] = ' '  # this remove last player possition
            draw_map()
        elif Map[x + 1][y] == "E":
            win()
        else:
            return

    elif move.name == 'w':  # UP
        if x > 0 and Map[x - 1][y] != u"\u2588" and Map[x - 1][y] != "$" and Map[x - 1][y] != "E":
            clear()
            x -= 1
            u += 1
            Map[x][y] = "@"
            Map[x + 1][y] = ' '
            draw_map()
        elif Map[x - 1][y] == "E":
            win()
        else:
            return

    elif move.name == 'a':  # LEFT
        if y > 0 and Map[x][y - 1] != u"\u2588" and Map[x][y - 1] != "$" and Map[x][y - 1] != "E":
            clear()
            y -= 1
            l += 1
            Map[x][y] = "@"
            Map[x][y + 1] = ' '
            draw_map()
        elif Map[x][y - 1] == "E":
            win()
        else:
            return


    elif move.name == 'd':  # RIGHT
        if y < 14 and Map[x][y + 1] != u"\u2588" and Map[x][y + 1] != "$" and Map[x][y + 1] != "E":
            clear()
            y += 1
            r += 1
            Map[x][y] = "@"
            Map[x][y - 1] = ' '
            draw_map()
        elif Map[x][y + 1] == "E":
            win()
        else:
            return

    elif move.name == 'k':  # BOOM DOWN
        if b > 0 and Map[x + 1][y] != u"\u2588" and Map[x + 1][y] != "E":  # 4 is the edge of the map
            Map[x + 1][y] = " "
            b -= 1
            v += 1
            clear()
            draw_map()
        else:  # no action if x = 4 (out of range)
            winsound.PlaySound("SystemExit", winsound.SND_ASYNC)
            return

    elif move.name == 'i':  # boom up
        if b > 0 and Map[x - 1][y] != u"\u2588" and Map[x - 1][y] != "E":
            Map[x - 1][y] = " "
            b -= 1
            v += 1
            clear()
            draw_map()
        else:
            winsound.PlaySound("SystemExit", winsound.SND_ASYNC)
            return

    elif move.name == 'j':  # boom LEFT
        if b > 0 and Map[x][y - 1] != u"\u2588" and Map[x][y - 1] != "E":
            Map[x][y - 1] = " "
            b -= 1
            v += 1
            clear()
            draw_map()
        else:
            winsound.PlaySound("SystemExit", winsound.SND_ASYNC)
            return

    elif b > 0 and move.name == 'l':  # boom RIGHT
        if Map[x][y + 1] != u"\u2588" and Map[x][y + 1] != "E":
            Map[x][y + 1] = " "
            b -= 1
            v += 1
            clear()
            draw_map()
        else:
            winsound.PlaySound("SystemExit", winsound.SND_ASYNC)
            return

    elif move.name == 'g':  # portal
        if g > 0:
            g -= 1
            z += 1
            coin()
            clear()
            #print(Fore.BLUE, Style.BRIGHT)
            #draw_map()
            #time.sleep(0.05)
            #clear()
            #print(Fore.GREEN, Style.BRIGHT)
            Map[x][y] = '@'
            Map[12][13] = "E"
            draw_map()
        else:
            winsound.PlaySound("SystemExit", winsound.SND_ASYNC)
            return
    elif move.name == "t":
        clear()
        print(Style.RESET_ALL)
        print(Fore.RED, Style.BRIGHT)
        print('GIVE UP  GIVE UP  GIVE UP  GIVE UP')
        print('GIVE UP  GIVE UP  GIVE UP  GIVE UP')
        print('GIVE UP  GIVE UP  GIVE UP  GIVE UP')
        print('GIVE UP  GIVE UP  GIVE UP  GIVE UP')
        print(Style.RESET_ALL)
        print(Fore.GREEN, Style.BRIGHT)
        time.sleep(1.5)
        clear()
        y = 0
        x = 0
        p = 0
        d = 0
        u = 0
        l = 0
        r = 0
        g = 5
        v = 0
        b = 5
        z = 0
        coin()
        Map[x][y] = '@'
        Map[12][13] = "E"
        draw_map()





    elif move.name == 'esc':  # RIGHT
        print('thx m8')
        time.sleep(0.5)
        sys.exit()

    else:  # NO ACTION IF HIT NAY OTHER KEY
        return
        move_player(move)


# KEYBOARD

def keybild():
    keyboard.on_press(move_player, leave)
    while True:
        pass


# CLEAR

def clear():
    subprocess.Popen("cls" if platform.system() == "Windows" else "clear", shell=True)
    time.sleep(.1)


def menu():

    print(Fore.GREEN, Style.BRIGHT)
    #print(random.choice(colors))
    #print(random.sample(colors))
    print(Style.RESET_ALL)
    print(Back.GREEN + Fore.BLACK)
    print("                                        ")
    print(Style.RESET_ALL)
    print(Fore.GREEN, Style.BRIGHT)
    print(">>Rogue Neumann for python")
    print("TO Move: WASD")
    print("*TO BOMB $'s: IJKL*")
    print("*TO REMAKE THE MAP: G*")
    print('*E MARKS THE EXIT*')
    print('Your points = 100 - 1*(any action)')
    print('>Use ESC to quit')
    print(Style.RESET_ALL)
    print(Back.GREEN + Fore.BLACK)
    command = input("HIT ENTER".center(columns))
    print(Style.RESET_ALL)
    print(Fore.GREEN, Style.BRIGHT)
    if "" in command:
        clear()
        coin()
        Map[0][0] = '@'
        Map[12][13] = "E"
        draw_map()
        keybild()
    else:
        return




def leave():
    sys.exit()

menu()
