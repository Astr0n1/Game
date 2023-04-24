from OpenGL.GL import *
from OpenGL.GLUT import*
from OpenGL.GLU import *
from numpy import *
from random import randrange
#########################################################################
X=0
SPEED=1
BALL_ROTATE=0
LIFE=1
OBSTACLE_X=[]
OBSTACLE_Z=[]
PHASE=[]
COUNTER=0
GENERATE=0
#########################################################################
def init_my_scene(Width, Height):
    glClearColor(0, 0, 0, 1) # set the background to blue-grey
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, float(Width) / float(Height), 20, 200.0)
    glMatrixMode(GL_MODELVIEW)
#########################################################################
def Draw_vehicle():
    global X,BALL_ROTATE
    X
    glColor3d(0,0.8,1)
    glPushMatrix()
    glTranslate(X,0,abs(X/4))
    glRotate(BALL_ROTATE,1,0,0)
    glutWireSphere(2,20,20)
    glPopMatrix()
    BALL_ROTATE+=3
#########################################################################
def generate_obstacle():
    global OBSTACLE_X,OBSTACLE_Z,PHASE,COUNTER,SPEED
    COUNTER+=1
    if(COUNTER==10 and SPEED<=2):
        SPEED+=0.2
        COUNTER=0
        print(SPEED)
    rail=randrange(3)  # rail={0,1,2}
    PHASE.append(randrange(360))
    OBSTACLE_X.append((rail-1)*8) # X = {-8,0,8}
    OBSTACLE_Z.append(100)
#########################################################################
def draw_old_obstacles():
    global OBSTACLE_X,OBSTACLE_Z,SPEED
    
    glPushMatrix()
    for i in range (len(OBSTACLE_X)):
        glPushMatrix()
        glColor3d(1,1,0)
        
        glTranslate(OBSTACLE_X[i],0,OBSTACLE_Z[i])
        glRotate(PHASE[i],1,0,1)
        OBSTACLE_Z[i]-=SPEED
        glutSolidCube(5)
        PHASE[i]+=3
        glPopMatrix()
        # glTranslate(-OBSTACLE_X[i],0,-OBSTACLE_Z[i])
        
    glPopMatrix()
#########################################################################
def Game():
    
    global GENERATE,SPEED   # variables
    
    # initializing
    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )  
    glEnable(GL_DEPTH_TEST)
    glLoadIdentity()
    #          center     Look at   Up
    gluLookAt(0,25,-25,  0,10,0,  0,1,0)
    
    if not LIFE:
        Game_over
    else:
    
        if(GENERATE%180==0):
            generate_obstacle()
        
        
        draw_old_obstacles()
        
        crash_detector()
        
        Draw_vehicle()
        
        if(SPEED <1.5):
            STEP=3
        elif(SPEED<1.7):
            STEP=4
        else:
            STEP=5
        GENERATE+=STEP
    
    glutSwapBuffers()

#########################################################################
def keyboard_callback(key, x, y):
    global X
    if key == GLUT_KEY_LEFT and X<8:
        X+=1
    elif key == GLUT_KEY_RIGHT and X>-8:
        X-=1

def mouse_callback(x, y):
    global X
    X = (-x+500)/30
    if (X>8):
        X=8
    elif(X<-8):
        X=-8
#########################################################################
def crash_detector():
    global X,OBSTACLE_X,OBSTACLE_Z,LIFE,SPEED,PHASE
    if (len(OBSTACLE_X) and OBSTACLE_Z[0]<5 and  OBSTACLE_Z[0]>4.9-SPEED):
        
        if (X>1 and OBSTACLE_X[0]==8 or X<-1 and OBSTACLE_X[0]==-8 or X<5 and X>-5 and OBSTACLE_X[0]==0):
            LIFE-=1
            print ('crash '*15)
    
    
    if(len(OBSTACLE_X) and OBSTACLE_Z[0]<=-10  ):
        OBSTACLE_Z.pop(0)
        OBSTACLE_X.pop(0)
        PHASE.pop(0)
#########################################################################
def Game_over():
    global X
    

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(1000, 900)
    glutInitWindowPosition(400,0)
    window = glutCreateWindow(b"Race The Sun !")
    glutDisplayFunc(Game)
    glutIdleFunc(Game)
    # glutSpecialFunc(keyboard_callback)
    glutPassiveMotionFunc(mouse_callback)
    init_my_scene(1000, 900)
    glutMainLoop()

main()