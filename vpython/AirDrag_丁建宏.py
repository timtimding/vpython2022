from vpython import *

g=9.8
size=0.25               #ball radius
dt=0.001
theta=pi/4              #Launch angle
c=0.9                   #drag coefficient
s=0                     #displacement
hmax=-1                 #largest height 
cnt=0                   #bouncing count
t=0

scene = canvas(width=800, height=800, center =vec(0,15/4,0),background=vec(0.5,0.5,0)) # open a window
floor = box(length=35, height=0.01, width=10, color=color.green)
ball = sphere(radius = size, color=color.yellow, make_trail = True,trail_radius=0.05) # the ball and trail
msg =text(text = 'Air Drag', pos = vec(-12, 16, 0))

#graph
#gd = graph(title="h-t (height) Graph", width=600, height=450, x=0, y=600, xtitle="t(s)", ytitle="h(m)",align='left')
gd2= graph(title="v-t Graph", width=600, height=450, x=0, y=1050, xtitle="t(s)", ytitle="v(m/s)")
#ht = gcurve(graph=gd, color=color.red)
vt = gcurve(graph=gd2, color=color.blue)

#ball initial state
ball.v=vec(20*cos(theta), 20*sin(theta), 0)     #ball initial velocity
ball.pos=vec(-15, size, 0)                      #ball center initial position

#arrow
a = arrow(color = color.red, shaftwidth = 0.05,round=True,pos=ball.pos,axis=ball.v*0.4)

while(cnt<3):           # until the ball hit the ground for 3 times
    rate(1000)          # run 1000 times per real second
    t+=dt
    s+=ball.v.mag*dt
    ball.v += vec(0,-g,0)*dt-c*ball.v*dt
    a.pos=ball.pos
    a.axis=ball.v*0.4
    #ht.plot(pos=(t,ball.pos.y-size))
    ball.pos += ball.v*dt
    vt.plot(pos = (t,ball.v.mag))
    if (ball.pos.y<size):           #bounce
        ball.v.y=ball.v.y*(-1)
        cnt+=1
    if(ball.pos.y>hmax):            #record max height(from mass center to the ground)
        hmax=ball.pos.y

# Display : displacement & total distance traveled largest height
msg.visible = True
msg =text(text = "Displacement in x = {:+.3f} m".format(ball.pos.x+15),pos = vec(-17,14,0))#Displacement
msg =text(text = "Distance traveled = {:.3f} m".format(s),pos = vec(-17,12,0))                #Distance
msg =text(text = "Largest height (from mass center ",pos = vec(-17,10,0))
msg =text(text = "to the ground)= {:.3f} m".format(hmax),pos = vec(-17,8,0))