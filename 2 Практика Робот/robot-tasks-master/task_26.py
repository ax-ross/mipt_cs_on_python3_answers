#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
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
    for i in range(5):

        for j in range(9):
            fill_cross()
            if i % 2 == 0:
                move_right(4)
            else:
                move_left(4)
        fill_cross()
        if i == 4:
            while not wall_is_on_the_left():
                move_left()
        else:
            move_down(4)



if __name__ == '__main__':
    run_tasks()
