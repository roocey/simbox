#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 17:13:48 2020

@author: roocey
"""
import random
import datetime

begin_time = datetime.datetime.now()

maximum_simulations = 100000


class cycler:
    def __init__(self):
        self.colors = ["Red", "Yellow", "Green", "Purple", "Blue"]
        self.original_colors = list(self.colors)
        self.cycles = 0


class simulator():
    def __init__(self):
        self.real_combinations = []
        self.simulations = 0
        self.running_total = 0


cycler_ = cycler()
simulator_ = simulator()
maximum_combinations = len(cycler_.colors) * int(len(cycler_.colors)-1)


def cycle():
    primary_color = random.choice(cycler_.colors)
    cycler_.colors.remove(primary_color)
    secondary_color = random.choice(cycler_.colors)
    color_choice = primary_color + secondary_color
    cycler_.cycles += 1
    cycler_.colors = cycler_.original_colors[:]
    if (color_choice not in simulator_.real_combinations):
        simulator_.real_combinations.append(color_choice)


def simulate():
    simulator_.real_combinations = []
    simulator_.simulations += 1
    simulator_.running_total += cycler_.cycles
    cycler_.cycles = 0


def commify(num=1000):
    return f"{num:,}"


while simulator_.simulations < maximum_simulations:
    while len(simulator_.real_combinations) < maximum_combinations:
        cycle()
    else:
        simulate()
else:
    end_time = (datetime.datetime.now() - begin_time)
    print("Simulations concluded! (n=" + str(commify(simulator_.simulations)) +
          ")")
    print("The average number of cycles taken to find every unique" +
          "combination was " +
          str(simulator_.running_total / simulator_.simulations))
    print("The simulations took " + str(end_time))
    print("Average sim time: " + str(end_time / simulator_.simulations))
