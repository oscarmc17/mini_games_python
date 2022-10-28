import curses
from curses import wrapper
import enum
import queue
import time

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):  # Grabs the index of full row.
        for j, value in enumerate(row):  # Grabs the column index and value of every row.
            stdscr.addstr(i, j, value)  # Grabs index, column, and value of Maze.

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    stdscr.clear()  # Clear screen
    print_maze(maze, stdscr)
    stdscr.refresh()  # Refreshes the screen
    stdscr.getch()  # Get Character. Waits until user hits a key to exit the program.


wrapper(main)


arr = ["lambo", "nissan", "bmw", "porsche"]

for i, brand in enumerate(arr):
    print(i, brand)
