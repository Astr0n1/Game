from OpenGL.GL import *
from OpenGL.GLUT import*
from OpenGL.GLU import *
from numpy import *
from random import randrange
#########################################################################
X,Z=0,0
obstacles=[]
#########################################################################
def init_my_scene(Width, Height):
    glClearColor(0.2, 0.2, 0.3, 1) # set the background to blue-grey
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(50, float(Width) / float(Height), 1.0, 30.0)
    glMatrixMode(GL_MODELVIEW)

#########################################################################
def Draw_vehicle():
    glutWireTeapot(1)

#########################################################################
def init_obstacle(X,Z):
    global obstacles
    glPushMatrix()
    glTranslate(X,0,Z+20)
    choice=randrange(3)
    
    obstacles.append([X,Z+20,choice])
    glPopMatrix()

#########################################################################
def draw_old_obstacles():
    global obstacles
    glPushMatrix()
    for obstacle in obstacles:
        glTranslate(obstacle[0],0,obstacle[1])
        if(obstacle[2]==0):
            glutWireCube(1)
        elif(obstacle[2]==1):
            glutWireSphere(1,100,100)
        else:
            glPushMatrix()
            glRotate(-90,1,0,0)
            glutWireCone(1,3,20,20)
            glPopMatrix()
    glPopMatrix()

#########################################################################
def Draw():
    
    global X,Z,obstacles   # variables
    
    # initializing
    glClear(GL_COLOR_BUFFER_BIT)  
    glLoadIdentity()
    gluLookAt(X,8,Z-9, 0,4,Z, 0,1,0)
    
    # generating obstacles
    generate=randrange(7)
    if(generate==1):
        init_obstacle(X,Z)
    
    # all obstacles
    draw_old_obstacles()
    
    # vehicle
    glPushMatrix()
    glTranslate(X,0,Z) 
    Draw_vehicle()
    glPopMatrix()
    
    
    Z+=.1
    
    glutSwapBuffers()

#########################################################################
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(1200, 900)
    glutInitWindowPosition(300,0)
    window = glutCreateWindow(b"Race The Sun !")
    glutDisplayFunc(Draw)
    glutIdleFunc(Draw)
    init_my_scene(1200, 900)
    glutMainLoop()

main()