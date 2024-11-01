import os
import time
from tkinter import *
os.system('cls')

flag=0
step=20
win=Tk()

win_h,win_w=705,440
win.geometry(str(win_h)+'x'+str(win_w))
win.resizable(False,False)
win.title("TOWER OF HANOI")

can_h,can_w=400,700
can=Canvas(win,height=can_h,width=can_w,bg="gray")
can.grid(row=0,column=0)

can.create_rectangle(0, 300, 800, 330,outline = "black", fill = "black",width = 2)
p1=can.create_rectangle(190, 100, 210, 300,outline = "black", fill = "black",width = 2)
p2=can.create_rectangle(390, 100, 410, 300,outline = "black", fill = "black",width = 2)
p3=can.create_rectangle(590, 100, 610, 300,outline = "black", fill = "black",width = 2)

# Initial disks placement
d1x,d1y=200,250
d2x,d2y=200,270
d3x,d3y=200,290

fd1,fd2,fd3=0,0,0

""" Use this location for three disk placement
d1x1,d1y1,d1x2,d1y2=180, 240, 220, 260
d2x1,d2y1,d2x2,d2y2=160, 260, 240, 280
d3x1,d3y1,d3x2,d3y2=140, 280, 260, 300
 """
d1=can.create_rectangle(d1x-20,d1y-10,d1x+20,d1y+10,outline = "black", fill = "orange",width = 1)
d2=can.create_rectangle(d2x-40,d2y-10,d2x+40,d2y+10,outline = "black", fill = "white",width = 1)
d3=can.create_rectangle(d3x-60,d3y-10,d3x+60,d3y+10,outline = "black", fill = "green",width = 1)
# disk placement ends

    

def start():
    global fd1,fd2,fd3

    step1()
        

def step1():
    global d1,d2,d3,d1x,d1y,d2x,d2y,d3x,d3y,step,flag
           
    if(d1y > 50 and flag==0): # check top edge 
            d1y=d1y-step # decrease the vertical coordinates   
            can.delete(d1) # delete the rectangle     
            d1=can.create_rectangle(d1x-20, d1y-10,d1x+20,d1y+10,fill="orange") 
            can.after(100,step1)   
    elif(d1x<600):
            flag=1
            d1x=d1x+step # decrease the vertical coordinates   
            can.delete(d1) # delete the rectangle     
            d1=can.create_rectangle(d1x-20, d1y-10,d1x+20,d1y+10,fill="orange") 
            can.after(100,step1)
    elif(d1y<290 and flag==1):
            d1y=d1y+step # decrease the vertical coordinates   
            can.delete(d1) # delete the rectangle     
            d1=can.create_rectangle(d1x-20, d1y-10,d1x+20,d1y+10,fill="orange") 
            can.after(100,step1)
    else: 
         flag=0
         step2()
        
def step2():
    global d1,d2,d3,d1x,d1y,d2x,d2y,d3x,d3y,step,flag
    if (d2y>50 and flag==0):   # check top edge 
            d2y=d2y-step # decrease the vertical coordinates   
            can.delete(d2) # delete the rectangle     
            d2=can.create_rectangle(d2x-40, d2y-10,d2x+40,d2y+10,fill="white") 
            can.after(100,step2)
    elif(d2x<400):
            flag=1
            d2x=d2x+step # decrease the vertical coordinates   
            can.delete(d2) # delete the rectangle     
            d2=can.create_rectangle(d2x-40, d2y-10,d2x+40,d2y+10,fill="white") 
            can.after(100,step2)
    elif(d2y<290 and flag==1):
            d2y=d2y+step # decrease the vertical coordinates   
            can.delete(d2) # delete the rectangle     
            d2=can.create_rectangle(d2x-40, d2y-10,d2x+40,d2y+10,fill="white") 
            can.after(100,step2)
    else: 
         flag=0
         step3()

def step3():
    global d1,d2,d3,d1x,d1y,d2x,d2y,d3x,d3y,step,flag
           
    if(d1y > 50 and flag==0): # check top edge 
            d1y=d1y-step # decrease the vertical coordinates   
            can.delete(d1) # delete the rectangle     
            d1=can.create_rectangle(d1x-20, d1y-10,d1x+20,d1y+10,fill="orange") 
            can.after(100,step3)   
    elif(d1x>400):
            flag=1
            d1x=d1x-step # decrease the vertical coordinates   
            can.delete(d1) # delete the rectangle     
            d1=can.create_rectangle(d1x-20, d1y-10,d1x+20,d1y+10,fill="orange") 
            can.after(100,step3)
    elif(d1y<270 and flag==1):
            d1y=d1y+step # decrease the vertical coordinates   
            can.delete(d1) # delete the rectangle     
            d1=can.create_rectangle(d1x-20, d1y-10,d1x+20,d1y+10,fill="orange") 
            can.after(100,step3)
    else: 
         flag=0
         step4()

def step4():
    global d1,d2,d3,d1x,d1y,d2x,d2y,d3x,d3y,step,flag
    if (d3y>50 and flag==0):   # check top edge 
            d3y=d3y-step # decrease the vertical coordinates   
            can.delete(d3) # delete the rectangle     
            d3=can.create_rectangle(d3x-60, d3y-10,d3x+60,d3y+10,fill="green") 
            can.after(100,step4)
    elif(d3x<600):
            flag=1
            d3x=d3x+step # decrease the vertical coordinates   
            can.delete(d3) # delete the rectangle     
            d3=can.create_rectangle(d3x-60, d3y-10,d3x+60,d3y+10,fill="green") 
            can.after(100,step4)
    elif(d3y<290 and flag==1):
            d3y=d3y+step # decrease the vertical coordinates   
            can.delete(d3) # delete the rectangle     
            d3=can.create_rectangle(d3x-60, d3y-10,d3x+60,d3y+10,fill="green") 
            can.after(100,step4)
    else: 
         flag=0
         step5()

def step5():
    global d1,d2,d3,d1x,d1y,d2x,d2y,d3x,d3y,step,flag
           
    if(d1y > 50 and flag==0): # check top edge 
            d1y=d1y-step # decrease the vertical coordinates   
            can.delete(d1) # delete the rectangle     
            d1=can.create_rectangle(d1x-20, d1y-10,d1x+20,d1y+10,fill="orange") 
            can.after(100,step5)   
    elif(d1x>200):
            flag=1
            d1x=d1x-step # decrease the vertical coordinates   
            can.delete(d1) # delete the rectangle     
            d1=can.create_rectangle(d1x-20, d1y-10,d1x+20,d1y+10,fill="orange") 
            can.after(100,step5)
    elif(d1y<290 and flag==1):
            d1y=d1y+step # decrease the vertical coordinates   
            can.delete(d1) # delete the rectangle     
            d1=can.create_rectangle(d1x-20, d1y-10,d1x+20,d1y+10,fill="orange") 
            can.after(100,step5)
    else: 
         flag=0
         step6()

def step6():
    global d1,d2,d3,d1x,d1y,d2x,d2y,d3x,d3y,step,flag
    if (d2y>50 and flag==0):   # check top edge 
            d2y=d2y-step # decrease the vertical coordinates   
            can.delete(d2) # delete the rectangle     
            d2=can.create_rectangle(d2x-40, d2y-10,d2x+40,d2y+10,fill="white") 
            can.after(100,step6)
    elif(d2x<600):
            flag=1
            d2x=d2x+step # decrease the vertical coordinates   
            can.delete(d2) # delete the rectangle     
            d2=can.create_rectangle(d2x-40, d2y-10,d2x+40,d2y+10,fill="white") 
            can.after(100,step6)
    elif(d2y<270 and flag==1):
            d2y=d2y+step # decrease the vertical coordinates   
            can.delete(d2) # delete the rectangle     
            d2=can.create_rectangle(d2x-40, d2y-10,d2x+40,d2y+10,fill="white") 
            can.after(100,step6)
    else: 
         flag=0
         step7()

def step7():
    global d1,d2,d3,d1x,d1y,d2x,d2y,d3x,d3y,step,flag
           
    if(d1y > 50 and flag==0): # check top edge 
            d1y=d1y-step # decrease the vertical coordinates   
            can.delete(d1) # delete the rectangle     
            d1=can.create_rectangle(d1x-20, d1y-10,d1x+20,d1y+10,fill="orange") 
            can.after(100,step7)   
    elif(d1x<600):
            flag=1
            d1x=d1x+step # decrease the vertical coordinates   
            can.delete(d1) # delete the rectangle     
            d1=can.create_rectangle(d1x-20, d1y-10,d1x+20,d1y+10,fill="orange") 
            can.after(100,step7)
    elif(d1y<250 and flag==1):
            d1y=d1y+step # decrease the vertical coordinates   
            can.delete(d1) # delete the rectangle     
            d1=can.create_rectangle(d1x-20, d1y-10,d1x+20,d1y+10,fill="orange") 
            can.after(100,step7)
    else: 
         flag=0 
         b1=Button(win,text='Restart',command=lambda:restart())
         b1.grid(row=2,column=0)

start()

def restart():
    global d1,d2,d3,d1x,d1y,d2x,d2y,d3x,d3y
       # Initial disks placement
    d1x,d1y=200,250
    d2x,d2y=200,270
    d3x,d3y=200,290

    can.delete(d1)
    can.delete(d2)
    can.delete(d3)

    d1=can.create_rectangle(d1x-20,d1y-10,d1x+20,d1y+10,outline = "black", fill = "orange",width = 1)
    d2=can.create_rectangle(d2x-40,d2y-10,d2x+40,d2y+10,outline = "black", fill = "white",width = 1)
    d3=can.create_rectangle(d3x-60,d3y-10,d3x+60,d3y+10,outline = "black", fill = "green",width = 1)

    start()



win.mainloop()