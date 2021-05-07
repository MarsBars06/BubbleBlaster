# Bubble Blaster - Made by MarsBars06 on Github
import tkinter as tk
# Imports tkinter library, using "tk" as the alias (i.e. reference)
from random import randint
# Imports the randint function from random library - needed for bubble generation
from time import sleep, time
# Imports the sleep function from the time library, needed to slow the game down a bit.
# import playsound
# Imports playsound for SFX
HEIGHT = 500
WIDTH = 800
# These variables will be used to set the height and width of the window, but also to calculate
# the exact middle of the window (where the submarine is initially placed).  To change the height
# or the width of the window, just change these variables.
window = tk.Tk()
# The window variable now holds an empty tkinter window.
window.title("Bubble Blaster")
# Setting the window title
# window.iconbitmap("¬/
ocean = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="darkblue")
# The ocean varibale is a tkinter canvas which shapes can be drawn on
ocean.pack()
# Packing the ocean canvas into the window
ship_id = ocean.create_oval(0, 0, 30, 30, outline="red")
ship_id2 = ocean.create_polygon(5, 5, 5, 25, 30, 15, fill="red")
# Puts these canvas-drawn shapes into variables.  These make up the submarine.
SHIP_R = 15
# This variable is used for the bubble collision events?
MID_X = WIDTH / 2
MID_Y = HEIGHT / 2
# Puts the X and Y coordinates into respective MID_X and MID_Y variables
ocean.move(ship_id, MID_X, MID_Y)
ocean.move(ship_id2, MID_X, MID_Y)
# Moves the submarine to the middle of the screen.
SHIP_SPD = 30
# The SHIP_SPD variable is how many pixels the sub will go when it moves in any direction
def move_ship(event):
  # Defines an event
  if event.keysym == 'Up' or event.keysym == 'w':
    # When the up arrow/W key is pressed...
    ocean.move(ship_id, 0, -SHIP_SPD)
    ocean.move(ship_id2, 0, -SHIP_SPD)
    # Moves the sub up.
  elif event.keysym == 'Down' or event.keysym == 's':
    ocean.move(ship_id, 0, SHIP_SPD)
    ocean.move(ship_id2, 0, SHIP_SPD)
  elif event.keysym == 'Left' or event.keysym == 'a':
    ocean.move(ship_id, -SHIP_SPD, 0)
    ocean.move(ship_id2, -SHIP_SPD, 0)
  elif event.keysym == 'Right' or event.keysym == 'd':
    ocean.move(ship_id, SHIP_SPD, 0)
    ocean.move(ship_id2, SHIP_SPD, 0)
ocean.bind_all('<Key>', move_ship)
bub_id = list()
# Stores a uniques ID number assigned to each bubble so it can be manipulated later
bub_r = list()
# Stores the radi of bubbles
bub_speed = list()
# Stores the speed of bubbles (i.e. how fast they move across the screen)
MIN_BUB_R = 10
# The smallest radius a bubble can have.
MAX_BUB_R = 30
# The largest radius a bubble can have
MAX_BUB_SPD = 10
# The fastest a bubble can move across the screen
GAP = 100
# WTF is this variable used for?
def create_bubble():
  # Function which will generate bubbles.  This function will be called constantly.
  x = WIDTH + GAP
  y = randint(0, HEIGHT)
  r = randint(MIN_BUB_R, MAX_BUB_R)
  # Generating 3 variable:
  #   - the x coordinate of the generated bubble
  #   - the y coordinate of the generated bubble
  #   - the radius of the generated bubble
  id1 = ocean.create_oval(x-r, y-r, x+r, y+r,  outline="white", fill="lightblue")
  # This generates the bubble in the canvas.  It's just called id1 for now
  # but it will be appended onto the bub_id list.
  bub_id.append(id1)
  # Appending the generated bubble to the bub_id list
  bub_r.append(r)
  # Appending the generated bubble's radius (size) to the bub_r list
  bub_speed.append(randint(1, MAX_BUB_SPD))
  # Appending the generated bubble's random speed to the bub_speed list
def move_bubbles():
  # This function will make the bubbles move across the screen.  Like the 
  # create_bubble() function, move_bubble() will be called constantly.
  for i in range(len(bub_id)):
    # Goes through each bubble in the bub_id list to move them one at a time.
    ocean.move(bub_id[i], -bub_speed[i], 0)
    # Moves the bubble
def get_coords(id_num):
  # This function gets the coordintes of a bubble based on its id
  pos = ocean.coords(id_num)
  x = (pos[0] + pos[2]) / 2
  y = (pos[1] + pos[3]) / 2
  # Puts the x and y coordinate of the middle of the specifed
  # bubble into respective x and y variables
  return x, y
  # Returns the x and y coordinates
def del_bubble(i):
  # This function deletes a specified bubble
  del bub_r[i]
  # Deletes the bubble's radius from the bub_r list
  del bub_speed[i]
  # Deletes the bubble's speed from the bub_speed list
  ocean.delete(bub_id[i])
  # Deletes the bubble from the canvas
  del bub_id[i]
  # Deletes the bubble's id from the bub_id list
def clean_up_bubs():
  # Deletes the bubbles that have gone off the screen, freeing up memory
  # and reducing lag.
  for i in range(len(bub_id)-1, 1, -1):
    # Goes through the list backwards as if it goes forwards, this function
    # will try to delete bubble which don't exist.
    x, y = get_coords(bub_id[i])
    # Puts the x and y coordinates of the bubble in respective
    # x and y variables
    if x < -GAP:
      del_bubble(i)
      # Deletes the bubble

# MAIN GAME LOOP
BUB_CHANCE = 10
# The chance of a bubble being generated (1/10)
while True:
  if randint(1, BUB_CHANCE) == 1:
    create_bubble()
    move_bubbles()
    clean_up_bubs()
    window.update()
    # Updates the window to redraw the bubbles as they have moved.
    sleep(0.01)
window.mainloop()
