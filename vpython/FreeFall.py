from vpython import *
g=9.8
size=0.25
height=15.00
dt=0.001
t=0
scene = canvas(width=800, height=800, center =vec(0,height/4,0),background=vec(0.5,0.5,0) ) # open a window
floor = box(length=30, height=0.01, width=10, color=color.green)
ball = sphere(radius = size, color=color.yellow, make_trail = True,interval=100 ,trail_type="points") # the ball
msg =text(text = 'Free Fall', pos = vec(-12, 15, 0))

ball.pos = vec(0,height,0) # ball center initial position
ball.v = vec(0,0,0) # ball initial velocity

gd = graph(title="x-t Graph", width=600, height=450, x=0, y=600, xtitle="t(s)", ytitle="x(m)")
gd2= graph(title="v-t Graph", width=600, height=450, x=0, y=1050, xtitle="t(s)", ytitle="v(m/s)")
xt = gcurve(graph=gd, color=color.red)
vt = gcurve(graph=gd2, color=color.blue)

while ball.pos.y >= size:
    rate(1000)
    t+=dt
    ball.pos += ball.v*dt
    ball.v.y += -g*dt
    xt.plot(pos = (t,ball.pos.y-size))
    vt.plot(pos = (t,ball.v.y))
    
msg.visible = True
msg =text(text = "t = {:.3f} s".format(t), pos = vec(-17, 12, 0))
msg =text(text = "Vmax = {:+.3f} m/s" .format(ball.v.y), pos = vec(-17, 10, 0))
msg =text(text = "√2gs= {:.3f} m/s ≈ Vmax".format(sqrt(2*g*14.75)),pos = vec(-17,8,0))#v^2≈2as
msg =text(text = "(s = {:.2f} m, g=9.8 m/s²)".format(height-size),pos = vec(-17,6,0))#ball bottom to ground