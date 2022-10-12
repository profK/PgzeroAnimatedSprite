# This is a sample Python script.
from pygame.time import Clock
import pgzrun
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from AnimatedActor import AnimatedActor

WIDTH = 800
HEIGHT = 600




global isInitialized
isInitialized: bool = False

global animatedActor
# create in init

global clock
clock: Clock = Clock()

def init() :
   global animatedActor
   animatedActor = AnimatedActor("pacsprites.png", 14)

def draw():
    global animatedActor
    screen.clear()
    animatedActor.draw()
    pass

def update() :
    global isInitialized
    if (not isInitialized):
        init()
        isInitialized = True
    animatedActor.setCurrentFrame((animatedActor.currentFrame + 1) % 14)
    clock.tick(10)



# Press the green button in the gutter to run the script.
pgzrun.go()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
