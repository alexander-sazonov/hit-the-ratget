import turtle
from turtle import Turtle, Screen
from random import randint

player = Turtle()
screen = Screen()
# настройки
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
TARGET_SIZE = 30
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor('lightblue')
# рисование мишени
target_x = randint(-SCREEN_WIDTH // 2 + TARGET_SIZE, SCREEN_WIDTH // 2 - TARGET_SIZE)
target_y = randint(-SCREEN_HEIGHT // 2 + TARGET_SIZE, SCREEN_HEIGHT // 2 - TARGET_SIZE)
player.penup()
player.hideturtle()
player.speed(0)
player.goto(target_x, target_y)
player.pendown()
for _ in range(4):
    player.forward(TARGET_SIZE)
    player.left(90)
player.penup()
player.goto(0, 0)
player.showturtle()
player.speed(2)
angle = screen.numinput('Угол', 'Введите угол (0 - 360)')
player.setheading(angle)
distance = screen.numinput('Расстояние', 'Введите расстояние')
player.forward(distance)
# Проверка на выигрыш

screen.exitonclick()
