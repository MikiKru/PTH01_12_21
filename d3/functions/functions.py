from random import random


def hello_world():
    print('Hello world')

def hello_me(name):
    print(f"Hello {name}")

def get_random_value():
    return random()

def division(a, b):
    if not b:
        return "Błąd dzielenia przez zero!"
    return a / b

def filter_by_treshold(seq, treshold):
    print("treshold", treshold)
    return [element for element in seq if element > treshold]

