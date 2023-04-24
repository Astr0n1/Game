from OpenGL.GL import *
from OpenGL.GLUT import*
from OpenGL.GLU import *
from numpy import *
from constants import *
import pygame
from random import randrange
#########################################################################
X=0
SPEED=2
LIFE=1
FONT_DOWNSCALE = 0.13
OBSTACLE_X=[]
OBSTACLE_Z=[]
PHASE=[]
COUNTER=0
GENERATE=0
TEXTURE_NAMES = [0]
MILLISECONDS = 1
#########################################################################
def projection_ortho():
    glLoadIdentity()
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1, 1, -1, 1, -100, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
#########################################################################
def init_textures():
    loadTextures()

#########################################################################
def texture_setup(texture_image_binary, texture_name, width, height):
    glBindTexture(GL_TEXTURE_2D, texture_name)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T,
                    GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

    glTexImage2D(GL_TEXTURE_2D,
                 0,
                 3,
                 width, height,
                 0,
                 GL_RGBA,
                 GL_UNSIGNED_BYTE,
                 texture_image_binary)
#########################################################################
def loadTextures():
    glEnable(GL_TEXTURE_2D)
    images = [pygame.image.load("background.jpg")]
    textures = [pygame.image.tostring(image, "RGBA", True)
                for image in images]

    glGenTextures(len(images), TEXTURE_NAMES)

    for i in range(len(images)):
        texture_setup(textures[i],
                      TEXTURE_NAMES[i],
                      images[i].get_width(),
                      images[i].get_height())
#########################################################################
def init_my_scene(Width, Height):
    glClearColor(0, 0, 0, 1) # set the background to blue-grey
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, float(Width) / float(Height), 20, 200.0)
    glMatrixMode(GL_MODELVIEW)
#########################################################################
def background_draw():
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex(-1, 1)

    glTexCoord2f(0, 0)
    glVertex(-1, -1)

    glTexCoord2f(1, 0)
    glVertex(1, -1)

    glTexCoord2f(1, 1)
    glVertex(1, 1)
    glEnd()
#########################################################################
def draw_screen():
    glPushMatrix()
    glColor(1, 1, 1)
    projection_ortho()
    glBindTexture(GL_TEXTURE_2D, TEXTURE_NAMES[0])
    background_draw()
    glBindTexture(GL_TEXTURE_2D, -1)
    init_my_scene(1000, 900)
    glPopMatrix()
#########################################################################
def Draw_vehicle():
    global X
    glColor3d(0,0.5,1)
    glPushMatrix()
    glTranslate(X,0,abs(X/6))
    glRotate(3*X,0,0,1)
    glScale(.6, .6, .7)
    glBegin(GL_LINES)
    for edge in spaceship_edges_vector2:
        for vertex in edge:
            glVertex3fv(spaceship_verticies_vector3[vertex])
    glEnd()
    glPopMatrix()
#########################################################################
def generate_obstacle():
    global OBSTACLE_X,OBSTACLE_Z,PHASE,COUNTER,SPEED
    COUNTER+=1
    if(COUNTER==5 and SPEED<=3):
        SPEED+=0.3
        COUNTER=0
        print(SPEED)
    rail=randrange(3)  # rail={0,1,2}
    PHASE.append(randrange(360))
    OBSTACLE_X.append((rail-1)*8) # X = {-8,0,8}
    OBSTACLE_Z.append(100)
#########################################################################
def draw_old_obstacles():
    global OBSTACLE_X, OBSTACLE_Z, SPEED
    
    glPushMatrix()
    for i in range(len(OBSTACLE_X)):
        glPushMatrix()
        glColor3d(1, 1, 0)
        
        glTranslate(OBSTACLE_X[i], 0, OBSTACLE_Z[i])
        glRotate(PHASE[i], 1, 0, 1)
        OBSTACLE_Z[i] -= SPEED
        glutSolidCube(5)
        PHASE[i] += 3
        glPopMatrix()
    
    glPopMatrix()
#########################################################################
def draw_text(string, x, y):
    glLineWidth(2)
    glColor(1, 1, 0)  # Yellow Color
    glPushMatrix()  # remove the previous transformations
    # glScale(0.13,0.13,1)  # TODO: Try this line
    glTranslate(x, y, 0)
    glScale(FONT_DOWNSCALE, FONT_DOWNSCALE, 1) # when writing text and see nothing downscale it to a very small value .001 and draw at center
    string = string.encode()  # conversion from Unicode string to byte string
    for c in string:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, c)
    print(string)
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
        Game_over()
        draw_text("SCORE :", 500,500)
    else:
    
        if(GENERATE%120==0):
            generate_obstacle()
        
        draw_screen()
        
        draw_old_obstacles()
        
        Draw_vehicle()
        
        crash_detector()
        
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
    if (OBSTACLE_Z[0]<5 and  OBSTACLE_Z[0]>4-SPEED and abs(X-OBSTACLE_X[0])<=6):
        
        LIFE-=1
        print ('crash '*15)
    
    
    if(len(OBSTACLE_X) and OBSTACLE_Z[0]<=-10  ):
        OBSTACLE_Z.pop(0)
        OBSTACLE_X.pop(0)
        PHASE.pop(0)
#########################################################################
def Game_over():
    global X

#########################################################################
def anim_timer(v):
    Game()
    glutTimerFunc(MILLISECONDS, anim_timer, v + 1)
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(1000, 900)
    glutInitWindowPosition(400,0)
    glutCreateWindow(b"Race The Sun !")
    glutDisplayFunc(Game)
    glutTimerFunc(MILLISECONDS, anim_timer, 1)
    init_textures()
    # glutSpecialFunc(keyboard_callback)
    glutPassiveMotionFunc(mouse_callback)
    init_my_scene(1000, 900)
    glutMainLoop()

main()