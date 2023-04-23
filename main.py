from OpenGL.GL import *
from OpenGL.GLUT import*
from OpenGL.GLU import *
from numpy import *
from random import randrange
#########################################################################
X=0
speed=0
obstacle_X=[]
obstacle_Z=[]
generate=0
#########################################################################
def init_my_scene(Width, Height):
    glClearColor(0.2, 0.2, 0.3, 1) # set the background to blue-grey
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, float(Width) / float(Height), 20, 200.0)
    glMatrixMode(GL_MODELVIEW)
#########################################################################
def Draw_vehicle():
    global X,speed
    glColor3d(1,0,1)
    glPushMatrix()
    glTranslate(X,0,0)
    glRotate(speed,1,0,0)
    glutWireSphere(1.8,20,20)
    glPopMatrix()
    speed+=3
#########################################################################
def generate_obstacle():
    rail=randrange(3)  # rail={0,1,2}
    obstacle_X.append((rail-1)*4.5) # X = {-5,0,5}
    obstacle_Z.append(100)
#########################################################################
def draw_old_obstacles():
    global obstacle_X,obstacle_Z
    
    glPushMatrix()
    for i in range (len(obstacle_X)):
        glPushMatrix()
        glColor3d(1,1,0)
        
        glScale(1.5,2,1.5)
        glTranslate(obstacle_X[i],0,obstacle_Z[i])
        obstacle_Z[i]-=1
        glutSolidCube(4)
        
        glPopMatrix()
        # glTranslate(-obstacle_X[i],0,-obstacle_Z[i])
        
    glPopMatrix()
#########################################################################
def Game():
    
    global generate   # variables
    
    # initializing
    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )  
    glEnable(GL_DEPTH_TEST)
    glLoadIdentity()
    #          center     Look at   Up
    gluLookAt(0,20,-20,  0,10,0,  0,1,0)
    
    if(generate%50==0):
        generate_obstacle()
        
    
    
    draw_old_obstacles()
    
    crash_detector()
    
    Draw_vehicle()
    
    generate+=1
    
    glutSwapBuffers()

#########################################################################
def keyboard_callback(key, x, y):
    global X,Z
    if key == GLUT_KEY_LEFT and X<6:
        X+=6
    elif key == GLUT_KEY_RIGHT and X>-6:
        X-=6
#########################################################################
def crash_detector():
    global X,Z,obstacle_X,obstacle_Z
    if (obstacle_Z[0]==0):
        if(obstacle_X[0]==0 and X==0):
            print ('$'*1000)
            
        obstacle_Z.pop(0)
        obstacle_X.pop(0)
        
    
    

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(1000, 900)
    glutInitWindowPosition(300,0)
    window = glutCreateWindow(b"Race The Sun !")
    glutDisplayFunc(Game)
    glutIdleFunc(Game)
    glutSpecialFunc(keyboard_callback)
    init_my_scene(1000, 900)
    glutMainLoop()

main()