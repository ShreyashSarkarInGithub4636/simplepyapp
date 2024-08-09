import curses
import pywebview
from urllib.request import urlopen

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.curs_set(1)

    height, width = stdscr.getmaxyx()
    browser_height = height - 3

    webview = pywebview.create_window("Web Browser", width=width, height=browser_height)

    url_bar = curses.newwin(1, width, 0, 0)
    url_bar.bkgd(curses.color_pair(1))
    url_bar.addstr(0, 0, "URL: ")
    url_bar.refresh()

    status_bar = curses.newwin(1, width, height - 1, 0)
    status_bar.bkgd(curses.color_pair(1))
    status_bar.refresh()

    while True:
        c = stdscr.getch()
        if c == ord('\n'):
            url = url_bar.getstr(0, 5).decode('utf-8')
            try:
                response = urlopen(url)
                webview.load_html(response.read().decode('utf-8'))
            except:
                pass
        elif c == 27:
            curses.endwin()
            pywebview.destroy_window()
            exit(0)

curses.wrapper(main)
