from webbrowser import open
from time import sleep
from random import randint
from pyautogui import moveTo, click

while 1:
    moveTo(randint(1, 1900), randint(1, 1900))
    click()
    print("You're welcome")
    open('https://bit.ly/3lExwNG', new= 2)
    moveTo(randint(1, 1900), randint(1, 1900))
    click()
    sleep(0.5)
