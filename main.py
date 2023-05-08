from math import *

from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *

from component.fuel import Fuel
from component.heart import Heart
from component.objloader import *
from component.obstacle import Obstacle

X = 0
speed = 2
life = 3
state = "start"
pause = False
camera_coords = {'x_c': 0, 'y_c': 25, 'z_c': -25,
                 'x_l': 0, 'y_l': 11, 'z_l': 0}
FONT_DOWNSCALE = 0.13
counter = 0
generate = 0

fuel_generate = 0
fuel_level = 100
TEXTURE_NAMES = [0, 1, 2, 3, 4, 5]
MILLISECONDS = 15
factory = {}

obstacles = Obstacle(texture_name=TEXTURE_NAMES[2])
fuel = Fuel()
heart = Heart()
heart.texture_name = TEXTURE_NAMES[3]
fuel.texture_name = TEXTURE_NAMES[5]


#########################################################################
def getModel(path):
    if path not in factory:
        factory[path] = OBJ(path)
        factory[path].generate()

    return factory[path]


#########################################################################
def projection_ortho(z_near=-200):
    glLoadIdentity()
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1, 1, -1, 1, z_near, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


#########################################################################
def init_textures():
    load_texture()
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)


#########################################################################
def texture_setup(texture_image_binary, texture_name, width, height):
    glBindTexture(GL_TEXTURE_2D, texture_name)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

    glTexImage2D(GL_TEXTURE_2D,
                 0,
                 GL_RGBA,
                 width, height,
                 0,
                 GL_RGBA,
                 GL_UNSIGNED_BYTE,
                 texture_image_binary)
    glBindTexture(GL_TEXTURE_2D, -1)


#########################################################################
def load_texture():
    glEnable(GL_TEXTURE_2D)
    images = [pygame.image.load("assets/images/background.jpg"),
              pygame.image.load("assets/images/GameOver.jpg"),
              pygame.image.load("assets/images/obstacle.jpeg"),
              pygame.image.load("assets/images/heart.png"),
              pygame.image.load("assets/images/Start.jpg"),
              pygame.image.load("assets/images/fuel.png")
              ]
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
    lighting()
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
def heart_draw():
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex(-.9, .9)

    glTexCoord2f(0, 0)
    glVertex(-.9, .8)

    glTexCoord2f(1, 0)
    glVertex(-.8, .8)

    glTexCoord2f(1, 1)
    glVertex(-.8, .9)
    glEnd()


#########################################################################
def draw_screen():
    global state
    glPushMatrix()
    glColor(1, 1, 1)
    projection_ortho(-220)

    if state == "start":
        glBindTexture(GL_TEXTURE_2D, TEXTURE_NAMES[4])
    elif state == "gameOver":
        glBindTexture(GL_TEXTURE_2D, TEXTURE_NAMES[1])
    else:
        glBindTexture(GL_TEXTURE_2D, TEXTURE_NAMES[0])
    background_draw()

    projection_ortho()
    glBindTexture(GL_TEXTURE_2D, TEXTURE_NAMES[3])

    if state == "3" or state == "5":
        for i in range(life):
            glPushMatrix()
            glTranslate(i * .15, 0, 0)
            heart_draw()
            glPopMatrix()
        glBindTexture(GL_TEXTURE_2D, -1)

        state = fuel.fuel_level_bar(fuel_level, state)

    init_my_scene(1000, 900)
    glPopMatrix()


#########################################################################
def lighting():
    LightPos = [0, 10, 5, 1]
    LightAmb = [0, 0, 0, 0]
    LightDiff = [0.2, 0.2, 0.2, 1.0]
    LightSpec = [0.03, 0.03, 0.04, 1.0]

    MatAmbF = [1, 1, 1, 1]
    MatDifF = [1, 1, 1, 1]
    MatSpecF = [0.1, 0.1, 0.1, 1]
    MatShnF = [30]
    #####################################################################################
    glLightfv(GL_LIGHT0, GL_POSITION, LightPos)
    glLightfv(GL_LIGHT0, GL_AMBIENT, LightAmb)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, LightDiff)
    glLightfv(GL_LIGHT0, GL_SPECULAR, LightSpec)

    glLightModeli(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)

    glMaterialfv(GL_FRONT, GL_AMBIENT, MatAmbF)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, MatDifF)
    glMaterialfv(GL_FRONT, GL_SPECULAR, MatSpecF)
    glMaterialfv(GL_FRONT, GL_SHININESS, MatShnF)


#########################################################################
def draw_vehicle():
    global X
    Nx = (0) * cos(X * pi / 180) + (0) - sin(X * pi / 180)
    Ny = (0) * sin(X * pi / 180) + (0) * cos(X * pi / 180)  # Normal vector
    Nz = 1
    glNormal(Nx, Ny, Nz)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glColor3d(0, 0, 0)
    glPushMatrix()
    glTranslate(X, 0, abs(X / 6))
    glRotate(5 * X, 0, 0, 1)
    glScale(.6, .6, .7)
    getModel("models/Jet_01.obj").render()
    glPopMatrix()
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)


#########################################################################
def draw_text(string, x=0.0, y=0.0, size=5.0):
    glPushMatrix()
    projection_ortho()
    glLineWidth(2)
    glColor(1, 1, 0)
    glTranslate(x, y, 0)
    glScale(size / 10000, size / 10000, 1)
    string = string.encode()
    for c in string:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, c)
    init_my_scene(1000, 900)
    glPopMatrix()


#########################################################################
def switch():
    global state
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glLoadIdentity()
    draw_screen()

    if not life:
        state = "gameOver"

    if (state == "3" or state == "5") and pause == False:
        game()
    if not pause:
        glutSwapBuffers()


#########################################################################

def game():
    global generate, fuel_generate, fuel_level, speed, state, camera_coords, life  # variables

    draw_text("SCORE: " + str((generate // 100) * 100), -0.9, 0.7)

    if state == "5":
        if camera_coords['y_c'] < 50:
            camera_coords['y_c'] += 0.5
            camera_coords['z_c'] -= 0.5
            camera_coords['y_l'] -= 3 / 50
            camera_coords['z_l'] += 0.7

    gluLookAt(camera_coords['x_c'], camera_coords['y_c'], camera_coords['z_c'],
              camera_coords['x_l'], camera_coords['y_l'], camera_coords['z_l'],
              0, 1, 0)

    if generate % 120 == 0:
        speed = obstacles.generate_obstacle(num_of_rail=int(state), speed=speed)

    if generate % 1440 == 0:
        heart.generate_new_heart(num_of_rail=int(state), obstacles_x=obstacles.obstacle_x[-1], fuel_x=fuel.fuel_x)

    if fuel_level <= 50 and not len(fuel.fuel_x):
        fuel.generate_new_fuel(num_of_rail=int(state), obstacles_x=obstacles.obstacle_x[-1])
    obstacles.draw_obstacles(speed=speed)
    heart.draw_old_heart(speed)
    fuel.draw_old_fuel(speed=speed)
    draw_vehicle()
    life = obstacles.collision_detection(space_ship_position=X,num_of_heart=life,speed=speed ,state=state)
    fuel_level = fuel.collision_detection(space_ship_position=X, fuel_level=fuel_level, speed=speed)
    life = heart.collision_detection(space_ship_position=X, num_of_heart=life, speed=speed, )
    if speed < 3:
        STEP = 3
    else:
        STEP = 4
    if generate >= 4000 and state == "3":
        generate = 0
        state = "5"
    generate += STEP
    fuel_generate += STEP
    fuel_level -= 0.2


#########################################################################
def keyboard_callback(key, x, y):
    global state, pause
    if key == b's' and state == "start":
        print(state)
        state = "3"
    if key == b'p':
        print("pause")
        if pause == True:
            pause = False
        else:
            pause = True


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
def anim_timer(v):
    switch()
    glutTimerFunc(MILLISECONDS, anim_timer, v + 1)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(1000, 900)
    glutInitWindowPosition(400, 0)
    glutCreateWindow(b"Race The Sun !")
    glutDisplayFunc(switch)
    glutTimerFunc(MILLISECONDS, anim_timer, 1)
    init_textures()
    glutKeyboardFunc(keyboard_callback)
    glutPassiveMotionFunc(mouse_callback)
    init_my_scene(1000, 900)
    glutMainLoop()


main()
