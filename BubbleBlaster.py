# Bubble Blaster - Made by MarsBars06 on Github
import tkinter as tk
# Imports tkinter library, using "tk" as the alias (i.e. reference)
HEIGHT = 500
WIDTH = 800
# These variables will be used to set the height and width of the window, but also to calculate
# the exact middle of the window (where the submarine is initially placed).  To change the height
# or the width of the window, just change these variables.
window = tk.Tk()
# The window variable now holds an empty tkinter window.
window.title("Bubble Blaster")
# Setting the window title
window.iconbitmap("¬/
ocean = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="darkblue")
# The ocean varibale is a tkinter canvas which shapes can be drawn on
ocean.pack()
# Packing the ocean canvas into the window

