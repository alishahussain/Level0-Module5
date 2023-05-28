"""
Make an obedient turtle that will obey commands to draw shapes.
"""
from tkinter import messagebox, simpledialog, Tk
import turtle
def draw_square(length1, obi):
    for i in range(4):
        obi.forward(length1)
        obi.right(90)
def draw_triangle(length2, obi):
    for i in range(3):
        obi.forward(length2)
        obi.right(60)
def draw_circle(rad, obi):
    obi.circle(radius=rad)

if __name__ == '__main__':
    # TODO)
    #   1. Create a turtle.
    obi = turtle.Turtle()
    #   2. Write 3 method definitions for drawing a square, triangle, and
    #      circle.


    #   3. Ask the user for the for a shape to draw.
    ask = simpledialog.askstring(title=None, prompt='what shape would you like to draw?')
    if ask =='square':
        length= simpledialog.askinteger(title=None, prompt='what length do you want your square to be?')
        draw_square(length1,obi)
    if ask =='triangle':
        length= simpledialog.askinteger(title=None, prompt='what length do you want your triangle to be?')
        draw_triangle(length2,obi)
    if ask =='circle':
        rad= simpledialog.askinteger(title=None, prompt='what radius do you want your circle to be?')
        draw_triangle(rad,obi)

    #   4. Draw the appropriate shape depending on their answer (call the right
    #      function)
    pass
