"""
The use of matplotlib animated plots here is adapted from the following tutorial:
https://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/

This animation is a first attempt at producing a visual tool to make spider plots from bar graphs.
It is very much a work in progress; but why let perfect be the enemy of the just about passable.

"""

%matplotlib notebook
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib

NUM_OF_BARS = 5
FPS=10
duration = 5
steps=duration*FPS
#------------------------------------------------------------
# set up figure and animation
fig = plt.figure()

ax = fig.add_subplot(111, aspect='equal', autoscale_on=False, frameon=False,
                     xlim=(-2.1, 2.1), ylim=(-1.5, 2))
ax.grid()
ax.set_xticklabels([])
ax.set_yticklabels([])
lines = [ax.plot([], [], '-', lw=2)[0] for n in range(NUM_OF_BARS)]
matplotlib.rcParams['savefig.pad_inches'] = 0


x=[n-2 for n in range(5)]
y=[0.6,1.3,0.7,0.5,1.6]
    
def init():
    for a in range(NUM_OF_BARS):
        lines[a].set_data([x[a]-0.25,x[a]+0.25,x[a]+0.25,x[a]-0.25,x[a]-0.25],[0,0,y[a],y[a],0])
    return lines

def animate(k): 
    x0= [x[a]*((steps-k)/steps) for a in range(len(x))]
    x1= [(math.sin(2*math.pi*x[a]/5*k/steps))+x[a]*((steps-k)/steps) for a in range(len(x))]
    y1= [y[a]*math.cos(2*math.pi*x[a]/5*k/steps) for a in range(len(x))]
    if(k==steps):
        ax.fill(x1+[x1[0]],y1+[y1[0]],"0.5")
    for a in range(NUM_OF_BARS):
        lines[a].set_data([x0[a]-1/(k+10),x0[a]+1/(k+10),x1[a]+1/(k+10),x1[a]-1/(k+10),x0[a]-1/(k+10)],[0,0,y1[a],y1[a],0])
    return lines

ani = animation.FuncAnimation(fig, animate, frames=steps+1, interval=math.floor(1000/FPS), blit=True, init_func=init, repeat=False) 

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
ani.save('spider.mp4', fps=FPS, dpi=200 , extra_args=['-vcodec', 'libx264'])

plt.show()
