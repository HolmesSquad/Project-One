#import modules
from Tkinter import *
#Set Initial Velocities
vx = 0.0 #x velocity
vy = 10.0 #y velocity
#Create Window
main = Tk(className=" Advanced Obstacle Course")
canvas = Canvas(main, width=1000, height=860, bg='white')
canvas.pack()
#Create Borders
obb1 = canvas.create_rectangle(0,0, 100, 860, fill ='black')
obb1x1, obb1y1, obb1x2, obb1y2 = canvas.coords(obb1)
obb2 = canvas.create_rectangle(0, 100, 1000, 0, fill = 'black')
obb2x1, obb2y1, obb2x2, obb2y2 = canvas.coords(obb2)
obb3 = canvas.create_rectangle(0, 860, 1000, 760, fill = 'black')
obb3x1, obb3y1, obb3x2, obb3y2 = canvas.coords(obb3)
obb4 = canvas.create_rectangle(1000, 0, 900, 760, fill = 'black')
obb4x1, obb4y1, obb4x2, obb4y2 = canvas.coords(obb4)
#Create Obstacles

main.mainloop()
