import numpy as np
from vpython import *

A, N, omega = 0.10, 50, 2*pi/1.0
size, m, k, d = 0.06, 0.1, 10.0, 0.4


#scene = canvas(title='Spring Wave', width=800, height=300, background=vec(0.5,0.5,0), center = vec((N-1)*d/2, 0, 0))
#c = curve([vector(i*d, 1.0, 0) for i in range(N)], color=color.black)
p = graph(title="Dispersion Relationship", width=800, height=300, x=0, y=600, xtitle="Wavevector", ytitle="Angular frequency")
pl = gcurve(graph = p, color = color.blue)
po = gdots(graph = p, color = color.red)

for index in range(1, N // 2):
    t, dt = 0, 0.0003
    Unit_K = 2 * pi/(N*d)
    Wavevector = index * Unit_K #單位長度內向位變化
    phase = Wavevector * arange(N) * d
    ball_pos, ball_orig, ball_v, spring_len = np.arange(N)*d + A*np.sin(phase), np.arange(N)*d, np.zeros(N), np.ones(N)*d
    #ball_pos, ball_orig, ball_v, spring_len = np.arange(N)*d, np.arange(N)*d, np.zeros(N), np.ones(N)*d
    while (ball_pos[1] - d > 0):
        #rate(1000)
        t += dt  
        spring_len[:-1] = ball_pos[1:] - ball_pos[:-1]
        spring_len[-1] = ball_pos[0] - ball_pos[-1] + N * d
        ball_v[1:] += (spring_len[1:] - spring_len[:-1]) * k * dt / m
        ball_v[0] += (spring_len[0] - spring_len[-1]) * k * dt / m
        ball_pos += ball_v*dt
        ball_disp = ball_pos - ball_orig
        
        #for i in range(N):
        #    c.modify(i, y = ball_disp[i]*4+1)
    pl.plot(pos = (Wavevector, pi / t / 2))
    po.plot(pos = (Wavevector, pi / t / 2))