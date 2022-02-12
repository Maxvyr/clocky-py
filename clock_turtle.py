from turtle import *
from datetime import *

def Skip(step):
    penup()
    forward(step)
    pendown()
    
def mkHand(name, length):
    #Register the Turtle shape and create the needle Turtle
    reset() #Clear the current window and reset the location and other information to default values
    Skip(-length*0.1)
    begin_poly()
    forward(length*1.1)
    end_poly()
    handForm = get_poly()
    register_shape(name, handForm)
        
def Init():
    global secHand, minHand, hurHand, printer
    mode("logo")# Reset Turtle to point north
    #Create three pointer Turtle and initialize
    mkHand("secHand", 225)
    mkHand("minHand", 200)
    mkHand("hurHand", 180)
    secHand = Turtle()
    secHand.shape("secHand")
    minHand = Turtle()
    minHand.shape("minHand")
    hurHand = Turtle()
    hurHand.shape("hurHand")
    for hand in secHand, minHand, hurHand:
        hand.shapesize(1, 1, 6)
        hand.speed(0)
        #Create output text Turtle
    printer = Turtle()
    printer.color("blue")
    printer.hideturtle()
    printer.penup()
            
def SetupClock(radius):
    #Build the outer frame of the clock
    reset()
    pensize(10)
    for i in range(60):
        Skip(radius)
        if i % 5 == 0:
            forward(30)
            Skip(-radius-30)
        else:
            Skip(-radius)
            right(7.5)
                  
def Week(t):
    week = [ 'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi','Dimanche']
    return week[t.weekday()]
       
def Date(t):
    y = t.year
    m = t.month
    d = t.day
    return f"{d}/{m}/{y}"
      
def Tick():
    #Draw the dynamic display of the hands
    t = datetime.today()
    second = t.second + t.microsecond*0.000001
    minute = t.minute + second/60.0
    hour = t.hour + minute/60.0
    secHand.setheading(6*second) #Orientation, rotate 6 degrees per second
    minHand.setheading(6*minute)
    hurHand.setheading(30*hour)
    tracer(False)
    printer.forward(240)
    printer.write(f"{Week(t)} {Date(t)}", align="center",font=("Roboto", 24, "bold"))
    printer.back(30)
    printer.write("By M4xvyr", align="center",font=("Roboto", 14, "italic"))
    printer.home()
    tracer(True)
    ontimer(Tick, 1000)#Continue to call tick after 1000ms
          
def main():
    tracer(False) #Make multiple drawing objects appear at the same time
    Init()
    SetupClock(360)
    tracer(True)
    Tick()
    mainloop()


if __name__ == "__main__":
    main()