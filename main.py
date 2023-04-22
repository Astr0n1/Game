from OpenGL.GL import *
from OpenGL.GLUT import*
from OpenGL.GLU import *
from numpy import *
from random import randrange
#########################################################################
X,Z=0,0
generate=0
obstacles=[]
#########################################################################
def init_my_scene(Width, Height):
    glClearColor(0.2,0.2, 0.3, 1) # set the background to blue-grey
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(30, float(Width) / float(Height), 1.0, 100.0)
    glMatrixMode(GL_MODELVIEW)
#########################################################################
def draw_ground(Z):
    glPushMatrix()
    glColor3d(1,1,1,1)
    glScale(3,0.5,40)
    glTranslate(0,0,Z+10)
    glutSolidCube(1)
    glPopMatrix()
#########################################################################
def Draw_vehicle():
    glColor3d(1,1,1)
    glutWireTeapot(1)
#########################################################################
def init_obstacle(X,Z):
    
    Shape=randrange(3)
    X_axis=randrange(3)
    obstacles.append([X_axis,Z+40,Shape])
#########################################################################
def draw_old_obstacles():
    global obstacles
    
    glPushMatrix()
    for obstacle in obstacles:
        
        glTranslate(0,0,obstacle[1])
        
        if(obstacle[2]==0):
            glPushMatrix()
            glTranslate((obstacle[0]-1)*5,0,0)
            glColor3d(1,1,0)
            
            glScale(1.1,1.5,1)
            glutSolidCube(4)
            
            glPopMatrix()
            
        elif(obstacle[2]==1):
            glPushMatrix()
            glTranslate((obstacle[0]-1)*5,0,0)
            glColor3d(1,0,1)
            
            glScale(0.75,1,0.8)
            glutSolidSphere(3,100,100)
            
            glPopMatrix()
            
        else:
            glPushMatrix()
            glTranslate((obstacle[0]-1)*5,0,0)
            glColor3d(0,1,0)
            
            glRotate(-90,1,0,0)
            glutSolidCone(1.85,5,20,20)
            
            glPopMatrix()
            
    glPopMatrix()
#########################################################################
def Game():
    
    global X,Z,obstacles,generate   # variables
    
    # initializing
    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )  
    glEnable(GL_DEPTH_TEST)
    glLoadIdentity()
    #         center   Look at   Up
    gluLookAt(X,25,Z-25,  0,5,Z+5,  0,1,0)
    
    # draw ground
    draw_ground(Z)
    
    # generating obstacles
    if(generate%7==0):
        init_obstacle(X,Z)
    
    # all obstacles
    draw_old_obstacles()
    
    # vehicle
    glPushMatrix()
    glTranslate(X,0,Z) 
    Draw_vehicle()
    glPopMatrix()
    
    
    Z+=0.4
    generate+=1
    
    glutSwapBuffers()

#########################################################################
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(1000, 900)
    glutInitWindowPosition(300,0)
    window = glutCreateWindow(b"Race The Sun !")
    glutDisplayFunc(Game)
    glutIdleFunc(Game)
    init_my_scene(1000, 900)
    glutMainLoop()

main()