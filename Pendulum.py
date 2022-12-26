from vpython import *
g = 9.8
t = 0
dt = 0.001
size = 0.02
m = 0.5
L = 0.5
k = 15000

scene = canvas(width=500, height=500, center=vec(0, -0.2, 0), background=vec(0.5,0.5,0))
ceiling = box(length=0.8, height=0.005, width=0.8, color=color.blue)
ball = sphere(radius = size, color=color.red)
spring = cylinder(radius=0.005,pos = vec(0, 0, 0))

ball.v = vec(0.6, 0, 0)
ball.pos = vec(0, -L - m*g/k, 0)

gd= graph(title="v-t Graph", width=600, height=450, x=0, y=1050, xtitle="t(s)", ytitle="v(m/s)")
vt = gcurve(graph=gd, color=color.blue)

while True:
    rate(1000)
    t += dt
    spring.axis = ball.pos - spring.pos                           #spring extended from endpoint to ball
    spring_force = - k * (mag(spring.axis) - L) * spring.axis.norm()        # to get spring force vector
    ball.a = vector(0, - g, 0) + spring_force / m       # ball acceleration = - g in y + spring force /m
    ball.v += ball.a*dt
    ball.pos += ball.v*dt
    vt.plot(pos = (t,ball.v.mag))