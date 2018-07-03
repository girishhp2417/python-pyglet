import pyglet
from pyglet.gl import *
 
win = pyglet.window.Window()
 
@win.event
def on_draw():
 
        # Clear buffers
        glClear(GL_COLOR_BUFFER_BIT)
 
        # Draw outlines only
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
 
        # Draw some stuff
        glBegin(GL_TRIANGLE_STRIP) #[(50,50),(75,100),(200,200)]and[(75,100),(200,200),(50,250)]
        glVertex2i(50, 50)
        glVertex2i(75, 100)
        glVertex2i(200, 200)
        glVertex2i(50, 250)
        glEnd()
 
pyglet.app.run()
