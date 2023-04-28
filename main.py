from random import randrange
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
from constants import *

#########################################################################
X = 0
SPEED = 2
LIFE = 3
state = "3"
camera_coords = {'x_c': 0, 'y_c': 25, 'z_c': -25,
                 'x_l': 0, 'y_l': 11, 'z_l': 0}
FONT_DOWNSCALE = 0.13
OBSTACLE_X = []
OBSTACLE_Z = []
PHASE = []
COUNTER = 0
GENERATE = 0
TEXTURE_NAMES = [0, 1, 2]
MILLISECONDS = 1


#########################################################################
def projection_ortho():
    glLoadIdentity()
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1, 1, -1, 1, -200, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


#########################################################################
def init_textures():
    load_texture()


#########################################################################
def texture_setup(texture_image_binary, texture_name, width, height):
    glBindTexture(GL_TEXTURE_2D, texture_name)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
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
def load_texture():
    glEnable(GL_TEXTURE_2D)
    images = [pygame.image.load("background.jpg"),
              pygame.image.load("GameOver.jpg"),
              pygame.image.load("obstacle.jpeg")]
    textures = [pygame.image.tostring(image, "RGBA", True)
                for image in images]

    glGenTextures(len(images), TEXTURE_NAMES)

    for i in range(len(images)):
        texture_setup(textures[i],
                      TEXTURE_NAMES[i],
                      images[i].get_width(),
                      images[i].get_height())


#########################################################################
def init_my_scene(width, height):
    glClearColor(0, 0, 0, 1)  # set the background to blue-grey
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, float(width) / float(height), 20, 300.0)
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
def make_obstacle():
    # Front Face
    glBindTexture(GL_TEXTURE_2D, TEXTURE_NAMES[2])
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0, -1.0, 1.0)  # Bottom Left

    glTexCoord2f(1.0, 0.0)
    glVertex3f(1.0, -1.0, 1.0)  # Bottom Right

    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)  # Top Right

    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)  # Top Left
    glEnd()

    # Back Face
    glBindTexture(GL_TEXTURE_2D, TEXTURE_NAMES[2])
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)  # Bottom Right
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, 1.0, -1.0)  # Top Right
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0, 1.0, -1.0)  # Top Left
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)  # Bottom Left
    glEnd()

    # Top Face
    glBindTexture(GL_TEXTURE_2D, TEXTURE_NAMES[2])
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0, 1.0, -1.0)  # Top Left
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, 1.0, 1.0)  # Bottom Left
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)  # Bottom Right
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0, 1.0, -1.0)  # Top Right
    glEnd()

    # Bottom Face
    glBindTexture(GL_TEXTURE_2D, TEXTURE_NAMES[2])
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)  # Top Right
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)  # Top Left
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)  # Bottom Left
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)  # Bottom Right
    glEnd()

    # Right face
    glBindTexture(GL_TEXTURE_2D, TEXTURE_NAMES[2])
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)  # Bottom Right
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1.0, 1.0, -1.0)  # Top Right
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)  # Top Left
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)  # Bottom Left
    glEnd()

    # Left Face
    glBindTexture(GL_TEXTURE_2D, TEXTURE_NAMES[2])
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)  # Bottom Left
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, -1.0, 1.0)  # Bottom Right
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)  # Top Right
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)  # Top Left
    glEnd()
#########################################################################
def draw_screen(state):
    glPushMatrix()
    glColor(1, 1, 1)
    projection_ortho()
    if state == "start":
        glBindTexture(GL_TEXTURE_2D, TEXTURE_NAMES[0])
    elif state == "end":
        glBindTexture(GL_TEXTURE_2D, TEXTURE_NAMES[1])
    background_draw()
    glBindTexture(GL_TEXTURE_2D, -1)
    init_my_scene(1000, 900)
    glPopMatrix()


#########################################################################
def draw_vehicle():
    global X
    glColor3d(0, 0.5, 1)
    glPushMatrix()
    glTranslate(X, 0, abs(X / 6))
    glRotate(3 * X, 0, 0, 1)
    glScale(.6, .6, .7)
    glBegin(GL_LINES)
    for edge in spaceship_edges_vector2:
        for vertex in edge:
            glVertex3fv(spaceship_verticies_vector3[vertex])
    glEnd()
    glPopMatrix()


#########################################################################
def generate_obstacle():
    global OBSTACLE_X, OBSTACLE_Z, PHASE, COUNTER, SPEED
    COUNTER += 1
    if COUNTER == 5 and SPEED <= 5:
        SPEED += 0.3
        COUNTER = 0
        print(SPEED)
    if state == '3':
        rail = randrange(3)  # rail={0,1,2}
        OBSTACLE_X.append((rail - 1) * 8)
    else:
        rail1 = randrange(5)
        OBSTACLE_X.append((rail1 - 2) * 8)
        rail2 = randrange(5)
        while rail1 == rail2:
            rail2 = randrange(5)

        OBSTACLE_X.append((rail2 - 2) * 8)
        OBSTACLE_Z.append(200)
        PHASE.append(randrange(360))

    PHASE.append(randrange(360))
    OBSTACLE_Z.append(200)


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
        glScale(2.5, 2.5, 2.5)
        make_obstacle()
        glBindTexture(GL_TEXTURE_2D, -1)
        # glutSolidCube(5)
        PHASE[i] += 3
        glPopMatrix()

    glPopMatrix()

#########################################################################
def delete_obstacle(n):
    global OBSTACLE_X,OBSTACLE_Z,PHASE
    for i in range (n):
        OBSTACLE_Z.pop(0)
        OBSTACLE_X.pop(0)
        PHASE.pop(0)


#########################################################################
def draw_text(string, x, y):
    glLineWidth(2)
    glColor(1, 1, 0)  # Yellow Color
    glPushMatrix()  # remove the previous transformations
    # glScale(0.13,0.13,1)  # TODO: Try this line
    glTranslate(x, y, 0)
    glScale(FONT_DOWNSCALE, FONT_DOWNSCALE,
            1)  # when writing text and see nothing downscale it to a very small value .001 and draw at center
    string = string.encode()  # conversion from Unicode string to byte string
    # for c in string:
    # glutStrokeCharacter(GLUT_STROKE_ROMAN, c)
    # print(string)
    glPopMatrix()


#########################################################################
def game():
    global GENERATE, SPEED, state, camera_coords  # variables

    # initializing
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glLoadIdentity()

    if state == "5":
        if camera_coords['y_c'] < 50:
            camera_coords['y_c'] += 0.5
            camera_coords['z_c'] -= 0.5
            camera_coords['y_l'] -= 3 / 50
            camera_coords['z_l'] += 0.7

    gluLookAt(camera_coords['x_c'], camera_coords['y_c'], camera_coords['z_c'],
              camera_coords['x_l'], camera_coords['y_l'], camera_coords['z_l'],
              0, 1, 0)

    if not LIFE:
        game_over()
        draw_text("SCORE :", 500, 500)
    else:

        if GENERATE % 120 == 0:
            generate_obstacle()

        draw_screen("start")

        draw_old_obstacles()

        draw_vehicle()

        crash_detector()

        if SPEED < 3:
            STEP = 3
        elif SPEED < 4:
            state = "5"
            STEP = 4

        else:

            STEP = 5

        GENERATE += STEP

    glutSwapBuffers()


#########################################################################
def keyboard_callback(key, x, y):
    global X
    if key == GLUT_KEY_LEFT and X < 8:
        X += 1
    elif key == GLUT_KEY_RIGHT and X > -8:
        X -= 1


def mouse_callback(x, y):
    global X, state
    X = (-x + 500) / 30
    if X > 8 and state == '3':
        X = 8
    elif X < -8 and state == '3':
        X = -8

    if X > 16 and state == '5':
        X = 16
    elif X < -16 and state == '5':
        X = -16


#########################################################################
def crash_detector():
    global X, OBSTACLE_X, OBSTACLE_Z, LIFE, PHASE
    if  len(OBSTACLE_X) and state == '3' and OBSTACLE_Z[0] <= SPEED and abs(X - OBSTACLE_X[0]) <= 6 :
        LIFE -= 1
        delete_obstacle(1)
        print('crash ' * 15 + '\n' + '#'*50)
        return

    elif len(OBSTACLE_X)>1 and state == '5' and OBSTACLE_Z[1] <= SPEED and abs(X - OBSTACLE_X[1]) <= 6:
        LIFE -= 1
        delete_obstacle(1)
        print('crash ' * 15 + '\n' + '#'*50)
        return

    if len(OBSTACLE_X) and OBSTACLE_Z[0] < -6 :
        if state == "5" and OBSTACLE_Z[1] < -6:
            delete_obstacle(2)
        else :
            delete_obstacle(1)


#########################################################################
def game_over():
    draw_screen("end")


#########################################################################
def anim_timer(v):
    game()
    glutTimerFunc(MILLISECONDS, anim_timer, v + 1)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(1000, 900)
    glutInitWindowPosition(400, 0)
    glutCreateWindow(b"Race The Sun !")
    glutDisplayFunc(game)
    glutTimerFunc(MILLISECONDS, anim_timer, 1)
    init_textures()
    # glutSpecialFunc(keyboard_callback)
    glutPassiveMotionFunc(mouse_callback)
    init_my_scene(1000, 900)
    glutMainLoop()


main()
