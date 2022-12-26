from vpython import *

g = vec(0,-9.8,0)   #graviation acceleration
t = 0               #initialize time
dt = 0.0001         #time step of simulation
L = 2.00            #spring length
k = 15000           #force constant of spring
size=0.2            #radius
m=1                 #mass
n=2                 #balls lifted at the beginning
sk=0                #average kenitic energy
su=0                #average graviational potential

scene = canvas(width=500, height=500, center=vec(0, -0.2, 0), background=vec(0.5,0.5,0),align="left")
ceiling = box(length=6, height=0.005, width=2, color=color.blue)
msg =text(text = "Newton's cradle, n= {:x}".format(n),pos = vec(-2, 0.8, 0),height = 0.3)

def af_col_v(m1, m2, v1, v2, x1, x2):   #collision
    v1_prime = v1 + 2*(m2/(m1+m2))*(x1-x2) * dot (v2-v1, x1-x2) / dot (x1-x2, x1-x2)
    v2_prime = v2 + 2*(m1/(m1+m2))*(x2-x1) * dot (v1-v2, x2-x1) / dot (x2-x1, x2-x1)
    return (v1_prime, v2_prime)

def kin_e(v1,v2,v3,v4,v5,m):            #kenetic energy
    tkk=0.5*m*(v1*v1+v2*v2+v3*v3+v4*v4+v5*v5)
    return tkk
    
def pot_e(y1,y2,y3,y4,y5,m,g,k):        #graviational potential(with correction of spring position)
    tuu=m*g.mag*(y1+y2+y3+y4+y5+5*L+5*m*g.mag/k)
    return tuu

balls=[]
springs=[]

for i in range (5):                 #ball initial position
    ball=sphere(pos = vec(-5*size+i*2*size,-L-m*g.mag/k,0), radius = size, color=color.white)
    ball.v = vec(0,0,0)
    ball.m = m
    balls.append(ball)
    
    spring = cylinder(radius=0.02,pos = vec(-5*size+i*size*2,0,0))
    spring.axis = balls[i].pos - spring.pos
    springs.append(spring)

for i in range (n):                 #"lift" n balls
    balls[i].pos = vec(-5*size+i*2*size-sqrt(2*2-1.95*1.95),-m*g.mag/k-1.95,0)
    springs[i].axis = balls[i].pos - springs[i].pos

gd= graph(title="Instant total Kenetic Energy(red) & Graviational Potential(blue) to time", width=600, height=450, x=0, y=1050, xtitle="t(s)", ytitle="Energy(J)",align="left")
gd2= graph(title="Average total Kenetic Energy(red) & Graviational Potential(blue) to time", width=600, height=450, x=0, y=1050, xtitle="t(s)", ytitle="Energy(J)",align="left")
tkt = gcurve(graph=gd, color=color.red)
tut = gcurve(graph=gd, color=color.blue)
skt = gcurve(graph=gd2, color=color.red)
sut = gcurve(graph=gd2, color=color.blue)

while True:
    rate(5000)
    t += dt
    for i in range (5):
        springs[i].axis = balls[i].pos - springs[i].pos                                 #spring extended from endpoint to ball
        spring_force = - k * (mag(springs[i].axis) - L) * springs[i].axis.norm()        #to get spring force vector
        balls[i].a = g + spring_force/m                                                 #ball acceleration = - g in y + spring force /m
        balls[i].v += balls[i].a*dt
        balls[i].pos += balls[i].v*dt

    for i in range (4):
        if (mag(balls[i].pos - balls[i+1].pos) <= size*2 and dot(balls[i].pos-balls[i+1].pos, balls[i].v-balls[i+1].v) <= 0) :
            (balls[i].v, balls[i+1].v) = af_col_v(balls[i].m, balls[i+1].m, balls[i].v, balls[i+1].v, balls[i].pos, balls[i+1].pos)
   
    tk=kin_e(balls[0].v.mag,balls[1].v.mag,balls[2].v.mag,balls[3].v.mag,balls[4].v.mag,m)
    tu=pot_e(balls[0].pos.y,balls[1].pos.y,balls[2].pos.y,balls[3].pos.y,balls[4].pos.y,m,g,k)
    #tk instant kenitic energy
    #tu instant graviational potential
    sk+=tk
    su+=tu
    
    tkt.plot(pos=(t,tk))
    tut.plot(pos=(t,tu))
    skt.plot(pos=(t,sk/t))
    sut.plot(pos=(t,su/t))