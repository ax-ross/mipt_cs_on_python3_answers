#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    def go_down():
        while not wall_is_on_the_left():
            move_left()
        while not wall_is_on_the_right():
            if not wall_is_beneath():
                while not wall_is_beneath():
                    move_down()
                return 1
            move_right()
        return 0
    while True:
        if go_down() != 1:
            while not wall_is_on_the_left():
                move_left()
            break


if __name__ == '__main__':
    run_tasks()
