#import modules
from Tkinter import *
import random
import time
#Set Initial Velocities
vx = 0.0 #x velocity
vy = 10.0 #y velocity
#Create Window
main = Tk(className=" Obstacle Course")
canvas = Canvas(main, width=600, height=460, bg='white')
canvas.pack()
#Create Obstacles
ob1=canvas.create_rectangle(0,0,20,200, fill='red')
ob1x1,ob1y1,ob1x2,ob1y2=canvas.coords(ob1)
ob2=canvas.create_rectangle(0,200,150,220, fill='red')
ob2x1,ob2y1,ob2x2,ob2y2=canvas.coords(ob2)
ob3=canvas.create_rectangle(60,40,190,160, fill='red')
ob3x1,ob3y1,ob3x2,ob3y2=canvas.coords(ob3)
ob4=canvas.create_rectangle(190,40,210,260, fill='red')
ob4x1,ob4y1,ob4x2,ob4y2=canvas.coords(ob4)
ob5=canvas.create_rectangle(0,260,310,280, fill='red')
ob5x1,ob5y1,ob5x2,ob5y2=canvas.coords(ob5)
ob6=canvas.create_rectangle(250,0,270,220, fill='red')
ob6x1,ob6y1,ob6x2,ob6y2=canvas.coords(ob6)
ob7=canvas.create_rectangle(310,60,330,400, fill='red')
ob7x1,ob7y1,ob7x2,ob7y2=canvas.coords(ob7)
ob8=canvas.create_rectangle(100,380,310,400, fill='red')
ob8x1,ob8y1,ob8x2,ob8y2=canvas.coords(ob8)
ob9=canvas.create_rectangle(40,320,270,340, fill='red')
ob9x1,ob9y1,ob9x2,ob9y2=canvas.coords(ob9)
ob10=canvas.create_rectangle(40,340,60,460, fill='red')
ob10x1,ob10y1,ob10x2,ob10y2=canvas.coords(ob10)
ob11=canvas.create_rectangle(370,200,390,440, fill='red')
ob11x1,ob11y1,ob11x2,ob11y2=canvas.coords(ob11)
ob12=canvas.create_rectangle(60,440,600,460, fill='red')
ob12x1,ob12y1,ob12x2,ob12y2=canvas.coords(ob12)
ob13=canvas.create_rectangle(430,60,450,400, fill='red')
ob13x1,ob13y1,ob13x2,ob13y2=canvas.coords(ob13)
ob14=canvas.create_rectangle(490,0,600,220, fill='red')
ob14x1,ob14y1,ob14x2,ob14y2=canvas.coords(ob14)
ob15=canvas.create_rectangle(330,140,430,160, fill='red')
ob15x1,ob15y1,ob15x2,ob15y2=canvas.coords(ob15)
ob16=canvas.create_rectangle(370,20,390,100, fill='red')
ob16x1,ob16y1,ob16x2,ob16y2=canvas.coords(ob16)
ob17=canvas.create_rectangle(270,0,490,20, fill='red')
ob17x1,ob17y1,ob17x2,ob17y2=canvas.coords(ob17)
ob18=canvas.create_rectangle(450,380,560,400, fill='red')
ob18x1,ob18y1,ob18x2,ob18y2=canvas.coords(ob18)
ob19=canvas.create_rectangle(450,260,560,280, fill='red')
ob19x1,ob19y1,ob19x2,ob19y2=canvas.coords(ob19)
ob20=canvas.create_rectangle(490,320,600,340, fill='red')
ob20x1,ob20y1,ob20x2,ob20y2=canvas.coords(ob20)
#Set Arena Boundaries
x_max = 600.0
x_min = 0.0 
y_min = 0.0
y_max = 460.0
#Movement Loop
bot1=canvas.create_rectangle(10,430,30,450, fill='yellow')
x1,y1,x2,y2=canvas.coords(bot1)
#Set Velocities
vx=0.0
vy=-10.0
#Initiate Movement Loop
for t in range(1, 500):
    x1,y1,x2,y2=canvas.coords(bot1)
    canvas.coords(bot1,x1+vx,y1+vy,x2+vx,y2+vy)
    canvas.update()
    x1,y1,x2,y2=canvas.coords(bot1)
    time.sleep(0.1)
    #If Boundary Detected Change Direction
    if vx==0.0 and vy<0:
        if (y1-10)==y_min or ((y1-10)==ob1y2 and x1<=ob1x2 and x2>=ob1x1) or ((y1-10)==ob2y2 and x1<=ob2x2 and x2>=ob2x1) or ((y1-10)==ob3y2 and x1<=ob3x2 and x2>=ob3x1) or ((y1-10)==ob4y2 and x1<=ob4x2 and x2>=ob4x1) or ((y1-10)==ob5y2 and x1<=ob5x2 and x2>=ob5x1) or ((y1-10)==ob6y2 and x1<=ob6x2 and x2>=ob6x1) or ((y1-10)==ob7y2 and x1<=ob7x2 and x2>=ob7x1) or ((y1-10)==ob8y2 and x1<=ob8x2 and x2>=ob8x1) or ((y1-10)==ob9y2 and x1<=ob9x2 and x2>=ob9x1) or ((y1-10)==ob10y2 and x1<=ob10x2 and x2>=ob10x1) or ((y1-10)==ob11y2 and x1<=ob11x2 and x2>=ob11x1) or ((y1-10)==ob1y2 and x1<=ob12x2 and x2>=ob12x1) or ((y1-10)==ob1y2 and x1<=ob13x2 and x2>=ob13x1) or ((y1-10)==ob14y2 and x1<=ob14x2 and x2>=ob14x1) or ((y1-10)==ob15y2 and x1<=ob15x2 and x2>=ob15x1) or ((y1-10)==ob16y2 and x1<=ob16x2 and x2>=ob16x1) or ((y1-10)==ob1y2 and x1<=ob17x2 and x2>=ob17x1) or ((y1-10)==ob18y2 and x1<=ob18x2 and x2>=ob18x1) or ((y1-10)==ob19y2 and x1<=ob19x2 and x2>=ob19x1) or ((y1-10)==ob20y2 and x1<=ob20x2 and x2>=ob20x1):
            if (x1-10)==x_min or ((x1-10)==ob1x2 and y1<=ob1y2 and y2>=ob1y1) or ((x1-10)==ob2x2 and y1<=ob2y2 and y2>=ob2y1) or ((x1-10)==ob3x2 and y1<=ob3y2 and y2>=ob3y1) or ((x1-10)==ob4x2 and y1<=ob4y2 and y2>=ob4y1) or ((x1-10)==ob5x2 and y1<=ob5y2 and y2>=ob5y1) or ((x1-10)==ob6x2 and y1<=ob6y2 and y2>=ob6y1) or ((x1-10)==ob7x2 and y1<=ob7y2 and y2>=ob7y1) or ((x1-10)==ob8x2 and y1<=ob8y2 and y2>=ob8y1) or ((x1-10)==ob9x2 and y1<=ob9y2 and y2>=ob9y1) or ((x1-10)==ob10x2 and y1<=ob10y2 and y2>=ob10y1) or ((x1-10)==ob11x2 and y1<=ob11y2 and y2>=ob11y1) or ((x1-10)==ob1x2 and y1<=ob12y2 and y2>=ob12y1) or ((x1-10)==ob1x2 and y1<=ob13y2 and y2>=ob13y1) or ((x1-10)==ob14x2 and y1<=ob14y2 and y2>=ob14y1) or ((x1-10)==ob15x2 and y1<=ob15y2 and y2>=ob15y1) or ((x1-10)==ob16x2 and y1<=ob16y2 and y2>=ob16y1) or ((x1-10)==ob1x2 and y1<=ob17y2 and y2>=ob17y1) or ((x1-10)==ob18x2 and y1<=ob18y2 and y2>=ob18y1) or ((x1-10)==ob19x2 and y1<=ob19y2 and y2>=ob19y1) or ((x1-10)==ob20x2 and y1<=ob20y2 and y2>=ob20y1):
                vy=0.0
                vx=10.0
            else:
                vy=0.0
                vx=-10.0
    elif vx==0.0 and vy>0.0:
        if (y2+10)==y_max or ((y2+10)==ob1y1 and x1<=ob1x2 and x2>=ob1x1) or ((y2+10)==ob2y1 and x1<=ob2x2 and x2>=ob2x1) or ((y2+10)==ob3y1 and x1<=ob3x2 and x2>=ob3x1) or ((y2+10)==ob4y1 and x1<=ob4x2 and x2>=ob4x1) or ((y2+10)==ob5y1 and x1<=ob5x2 and x2>=ob5x1) or ((y2+10)==ob6y1 and x1<=ob6x2 and x2>=ob6x1) or ((y2+10)==ob7y1 and x1<=ob7x2 and x2>=ob7x1) or ((y2+10)==ob8y1 and x1<=ob8x2 and x2>=ob8x1) or ((y2+10)==ob9y1 and x1<=ob9x2 and x2>=ob9x1) or ((y2+10)==ob10y1 and x1<=ob10x2 and x2>=ob10x1) or ((y2+10)==ob11y1 and x1<=ob11x2 and x2>=ob11x1) or ((y2+10)==ob1y1 and x1<=ob12x2 and x2>=ob12x1) or ((y2+10)==ob1y1 and x1<=ob13x2 and x2>=ob13x1) or ((y2+10)==ob14y1 and x1<=ob14x2 and x2>=ob14x1) or ((y2+10)==ob15y1 and x1<=ob15x2 and x2>=ob15x1) or ((y2+10)==ob16y1 and x1<=ob16x2 and x2>=ob16x1) or ((y2+10)==ob1y1 and x1<=ob17x2 and x2>=ob17x1) or ((y2+10)==ob18y1 and x1<=ob18x2 and x2>=ob18x1) or ((y2+10)==ob19y1 and x1<=ob19x2 and x2>=ob19x1) or ((y2+10)==ob20y1 and x1<=ob20x2 and x2>=ob20x1):
            vy=0.0        
    elif vx<0.0 and vy==0.0:
        if (x1-10)==x_min or ((x1-10)==ob1x2 and y1<=ob1y2 and y2>=ob1y1) or ((x1-10)==ob2x2 and y1<=ob2y2 and y2>=ob2y1) or ((x1-10)==ob3x2 and y1<=ob3y2 and y2>=ob3y1) or ((x1-10)==ob4x2 and y1<=ob4y2 and y2>=ob4y1) or ((x1-10)==ob5x2 and y1<=ob5y2 and y2>=ob5y1) or ((x1-10)==ob6x2 and y1<=ob6y2 and y2>=ob6y1) or ((x1-10)==ob7x2 and y1<=ob7y2 and y2>=ob7y1) or ((x1-10)==ob8x2 and y1<=ob8y2 and y2>=ob8y1) or ((x1-10)==ob9x2 and y1<=ob9y2 and y2>=ob9y1) or ((x1-10)==ob10x2 and y1<=ob10y2 and y2>=ob10y1) or ((x1-10)==ob11x2 and y1<=ob11y2 and y2>=ob11y1) or ((x1-10)==ob1x2 and y1<=ob12y2 and y2>=ob12y1) or ((x1-10)==ob1x2 and y1<=ob13y2 and y2>=ob13y1) or ((x1-10)==ob14x2 and y1<=ob14y2 and y2>=ob14y1) or ((x1-10)==ob15x2 and y1<=ob15y2 and y2>=ob15y1) or ((x1-10)==ob16x2 and y1<=ob16y2 and y2>=ob16y1) or ((x1-10)==ob1x2 and y1<=ob17y2 and y2>=ob17y1) or ((x1-10)==ob18x2 and y1<=ob18y2 and y2>=ob18y1) or ((x1-10)==ob19x2 and y1<=ob19y2 and y2>=ob19y1) or ((x1-10)==ob20x2 and y1<=ob20y2 and y2>=ob20y1):
            vy=0.0
    elif vx>0.0 and vy==0.0:
        if (x2+10)==x_max or ((x2+10)==ob1x1 and y1<=ob1y2 and y2>=ob1y1) or ((x2+10)==ob2x1 and y1<=ob2y2 and y2>=ob2y1) or ((x2+10)==ob3x1 and y1<=ob3y2 and y2>=ob3y1) or ((x2+10)==ob4x1 and y1<=ob4y2 and y2>=ob4y1) or ((x2+10)==ob5x1 and y1<=ob5y2 and y2>=ob5y1) or ((x2+10)==ob6x1 and y1<=ob6y2 and y2>=ob6y1) or ((x2+10)==ob7x1 and y1<=ob7y2 and y2>=ob7y1) or ((x2+10)==ob8x1 and y1<=ob8y2 and y2>=ob8y1) or ((x2+10)==ob9x1 and y1<=ob9y2 and y2>=ob9y1) or ((x2+10)==ob10x1 and y1<=ob10y2 and y2>=ob10y1) or ((x2+10)==ob11x1 and y1<=ob11y2 and y2>=ob11y1) or ((x2+10)==ob1x1 and y1<=ob12y2 and y2>=ob12y1) or ((x2+10)==ob1x1 and y1<=ob13y2 and y2>=ob13y1) or ((x2+10)==ob14x1 and y1<=ob14y2 and y2>=ob14y1) or ((x2+10)==ob15x1 and y1<=ob15y2 and y2>=ob15y1) or ((x2+10)==ob16x1 and y1<=ob16y2 and y2>=ob16y1) or ((x2+10)==ob1x1 and y1<=ob17y2 and y2>=ob17y1) or ((x2+10)==ob18x1 and y1<=ob18y2 and y2>=ob18y1) or ((x2+10)==ob19x1 and y1<=ob19y2 and y2>=ob19y1) or ((x2+10)==ob20x1 and y1<=ob20y2 and y2>=ob20y1):
            vy=0.0
    else:
        print "Error"
    
main.mainloop()
