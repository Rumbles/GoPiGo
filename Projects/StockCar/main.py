#!/usr/bin/env python

# Trying out some basic GoPiGo stuff

import time
from easygopigo3 import EasyGoPiGo3

# Create an instance of the EasyGoPiGo3 class as an object we can use called gpg
gpg = EasyGoPiGo3()

# Create a distance sensor object
my_distance_sensor = gpg.init_distance_sensor()


def forward(time_length):
    gpg.forward()
    time.sleep(time_length)
    gpg.stop()


def turn_right(turn_time=1):
    gpg.right()
    time.sleep(turn_time)
    gpg.stop()


def turn_left(turn_time=1):
    gpg.left()
    time.sleep(turn_time)
    gpg.stop()


def distance_detect():
    while True:
        if my_distance_sensor.read_mm() > 10:
            forward(1)
        else:
            turn_left()
            left_distance = my_distance_sensor.read_mm()
            turn_right(2)
            right_distance = my_distance_sensor.read_mm()

            if left_distance > right_distance:
                turn_left(2)


if __name__ == "__main__":
    distance_detect()
