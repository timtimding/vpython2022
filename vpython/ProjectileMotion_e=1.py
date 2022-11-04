from vpython import *
import math
g=9.8           #Gravitational acceleration
size=0.25       #Radius
dt=0.001        
t=0             #Time start at 0
cnt=0           #Bounce counts
v=8             #Initial velocity
theta=60        #Angle

vh=v*cos(theta*math.pi/180)
vv=v*sin(theta*math.pi/180)

scene = canvas(width=2000, height=800, center =vec(0,5,0),background=vec(0.5,0.5,0) ) # open a window
floor = box(length=60, height=-0.01, width=10, color=color.green)
ball = sphere(radius = size, color=color.yellow, make_trail = True,interval=100 ,trail_type="points") # the ball
msg = text(text = "Projectile motion    v= %d m/s ,θ= %d°" %(v,theta), pos = vec(-12, 18, 0))

gd = graph(title="x-t , v-t graph", width=600, height=450, x=0, y=600, xtitle="t(s)", ytitle="x(m)")
gd2= graph(title="v-t plot (vertical velocity)", width=600, height=450, x=0, y=1050, xtitle="t(s)", ytitle="v(m/s)")
xt = gcurve(graph=gd, color=color.red)
vt = gcurve(graph=gd2, color=color.blue)

ball.pos = vec(-30,size,0) # ball center initial position
ball.v = vec(vh,vv,0) # ball initial velocity

while cnt<10: # until the ball hit the ground
    rate(1000) # run 1000 times per real second
    ball.pos += ball.v*dt
    t+=dt
    ball.v.y += -g*dt
    
    xt.plot(pos = (t,ball.pos.y-size))
    vt.plot(pos = (t,ball.v.y))
    if (ball.pos.y<size):
        ball.v.y=ball.v.y*(-1)
        cnt+=1
        if(cnt==1):
            msg =text(text = "Distance traveled after first bounce: {:.3f} m" .format(ball.pos.x+30), pos = vec(-17, 14, 0))
    
msg =text(text = "t = {:.3f} s".format(t), pos = vec(-17, 12, 0))
msg =text(text = "Distance traveled after bouncing for 10 times: {:.3f} m" .format(ball.pos.x+30), pos = vec(-17, 10, 0))
msg =text(text = "Horizontal range calculated with formula 2v²sinθcosθ/g= {:.3f} m".format(2*v*v*sin(theta*math.pi/180)*cos(theta*math.pi/180)/g),pos = vec(-17,8,0))
#msg =text(text = "(s = {:.2f} m, g=9.8 m/s²)".format(height-size),pos = vec(-17,6,0))