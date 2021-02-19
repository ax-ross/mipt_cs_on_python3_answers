#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
    def fill_cross():
        move_right()
        fill_cell()
        for i in range(2):
            move_down()
            fill_cell()
        move_up()
        move_left()
        fill_cell()
        move_right(2)
        fill_cell()
        move_up()
        move_left(2)

    move_down()
    for i in range(4):
        fill_cross()
        move_right(4)
    fill_cross()


if __name__ == '__main__':
    run_tasks()
