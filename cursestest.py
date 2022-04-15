import curses

def main():
    curses.wrapper(curses_main)

def curses_main(w):
    w.addstr("-----------------\n")
    w.addstr("| curses demo   |\n")
    w.addstr("-----------------\n")
    w.refresh()
    printing(w)
    w.addstr("\npress any key to exit...")
    w.refresh()
    w.getch()

def printing(w):
    w.addstr("This was printed using addstr\n\n")
    w.refresh()
    w.addstr("The following letter was printed using addch:- ")
    w.addch('a')
    w.refresh()
    w.addstr("\n\nThese numbers were printed using addstr:-\n{}\n{:.6f}\n".format(123, 456.789))
    w.refresh()

def moving_and_sleeping(w):
    row = 5
    col = 0
    curses.curs_set(False)
    for c in range(65, 91):
        w.addstr(row, col, chr(c))
        w.refresh()
        row += 1
        col += 1
        curses.napms(100)
    curses.curs_set(True)
    w.addch('\n')

def colouring(w):
    if curses.has_colors():
        curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_RED)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_GREEN)
        curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_CYAN)
        w.addstr("Yellow on red\n\n", curses.color_pair(1))
        w.refresh()
        w.addstr("Green on green + bold\n\n", curses.color_pair(2) | curses.A_BOLD)
        w.refresh()
        w.addstr("Magenta on cyan\n", curses.color_pair(3))
        w.refresh()
    else:
        w.addstr("has_colors() = False\n");
        w.refresh()

main()
