from vpython import*
import math

G=6.673E-11
mass = {'earth': 5.97E24, 'moon': 7.36E22, 'sun':1.99E30}
radius = {'earth': 6.371E6*10, 'moon': 1.317E6*10, 'sun':6.95E8*10}
earth_orbit = {'r': 1.495E11, 'v': 2.9783E4}
moon_orbit = {'r': 3.84E8, 'v': 1.022E3}
theta = 5.145*pi/180.0

def G_force(m,m2, pos_vec):
    return -G *m2* m / mag2(pos_vec) * norm(pos_vec)

scene = canvas(width=800, height=800, background=vector(0.5,0.5,0))
sun = sphere(pos=vector(0,0,0), radius = radius['sun'], color = color.orange, emissive=True)
local_light(pos=vector(0,0,0))
earth = sphere( radius = radius['earth'], m = mass['earth'], texture={'file':textures.earth})
moon = sphere( radius = radius['moon'], m = mass['moon'],trail_radius=0.23*radius['moon'])

earth.pos = vector(0,0,0)
moon.pos = vector(moon_orbit['r']*cos(theta),moon_orbit['r']*sin(theta),0)
com=(moon.m*moon.pos+earth.m*earth.pos)/(earth.m+moon.m)
earth.pos=vector(earth_orbit['r'],0,0)-com
moon.pos+=vector(earth_orbit['r'],0,0)-com

earth.v = vector(0, 0, 0)
moon.v = vector(0, 0, - moon_orbit['v'])
vc=(moon.m*moon.v+earth.m*earth.v)/(earth.m+moon.m)
earth.v+=vector(0,0,-earth_orbit['v'])-vc
moon.v+=vector(0,0,-earth_orbit['v'])-vc

dt=60*6*60
t=0
T=0

while True:
    scene.center = earth.pos
    rate(1000)
    earth.a = (G_force(earth.m, mass['moon'] , earth.pos-moon.pos)+ G_force(earth.m, mass['sun'] , earth.pos-sun.pos))/earth.m
    moon.a = (G_force(moon.m, mass['earth'] , moon.pos-earth.pos)+ G_force(moon.m, mass['sun'] , moon.pos-sun.pos))/moon.m
    
    
    
    norm_x = norm(cross(cross(norm(moon.v - earth.v), norm(moon.pos - earth.pos)), vec(0, 1, 0))).z
    if math.isclose(1,norm_x) and T==0 and t>86400:
        T=t/(86400*365)
        print('Period of precession : '+str(T)+' years')
    moon.v += moon.a * dt
    moon.pos += moon.v * dt
    earth.v += earth.a * dt
    earth.pos += earth.v * dt
    t+=dt