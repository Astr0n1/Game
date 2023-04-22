from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
##########################################################################
Width=1200
Height=1000
##########################################################################
def init_my_scene(Width, Height):
    glClearColor(0.2, 0.2, 0.3, 1) # set the background to blue-grey
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(50, float(Width) / float(Height), 1.0, 100.0)
    glMatrixMode(GL_MODELVIEW)
##########################################################################




##########################################################################
# main
glutInit()
glutInitDisplayMode(GL_DOUBLE | GL_RGB)
glutInitWindowSize(Width,Height)
glutInitWindowPosition(300,200)
glutCreateWindow("Race The Sun")
init_my_scene(Width, Height)
glutDisplayFunc(b"game")
glutIdleFunc(b"game")
glutMainLoop()