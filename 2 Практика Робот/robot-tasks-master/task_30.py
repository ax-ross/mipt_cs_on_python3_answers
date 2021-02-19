#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    n = 0
    while not wall_is_on_the_right():
        move_right()
        n += 1
    while not wall_is_on_the_left():
        move_left()
    for i in range(n + 1):
        for j in range(n):
            if not (i == j or i + j == n):
                fill_cell()
            move_right()
        if j == n - 1 and i != 0 and i != n:
            fill_cell()
        move_left(n)
        if i != n:
            move_down()




if __name__ == '__main__':
    run_tasks()
