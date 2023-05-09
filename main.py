import glfw
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *

from component.fuel import Fuel
from component.heart import Heart
from component.objloader import *
from component.obstacle import Obstacle

spaceship_position = 0
flash = 0
speed = 3
num_of_heart = 3
state = "start"
pause = False
camera_coordinates = {
    'x-eye': 0,
    'y-eye': 25,
    'z-eye': -25,
    'x_center': 0,
    'y_center': 11,
    'z_center': 0
}

generate = 0
fuel_generate = 0
fuel_level = 100
textureList = [0, 1, 2, 3, 4, 5]
TEXTURE_NAMES = {
    'Start': 0,
    'background': 1,
    'obstacle': 2,
    'heart': 3,
    'fuel': 4,
    'gameOver': 5
}
IMAGE_NAME = {
    0: 'start.jpg',
    1: 'background.jpg',
    2: 'obstacle.jpeg',
    3: 'heart.png',
    4: 'fuel.png',
    5: 'gameOver.jpg'
}
MILLISECONDS = 15
factory = {}

obstacles = Obstacle(texture_name=TEXTURE_NAMES['obstacle'])
fuel = Fuel(texture_name=TEXTURE_NAMES['fuel'])
heart = Heart(texture_name=TEXTURE_NAMES['heart'])

background_sound = pygame.mixer.Sound("assets/sound/gameplay.mp3")
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
def load_texture():
    glEnable(GL_TEXTURE_2D)
    images = [pygame.image.load(f"assets/images/{IMAGE_NAME[i]}") for i in range(len(IMAGE_NAME))]
    textures = [pygame.image.tostring(image, "RGBA", True) for image in images]
    glGenTextures(len(images), textureList)
    for i in range(len(images)):
        texture_setup(textures[i],
                      i,
                      images[i].get_width(),
                      images[i].get_height())


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
def init_my_scene(width, height):
    lighting()
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

def draw_screen():
    global state
    glPushMatrix()
    glColor(1, 1, 1)
    projection_ortho(-220)

    if state == "start":
        glBindTexture(GL_TEXTURE_2D, TEXTURE_NAMES['Start'])
    elif state == "gameOver":
        glBindTexture(GL_TEXTURE_2D, TEXTURE_NAMES['gameOver'])
    else:
        glBindTexture(GL_TEXTURE_2D, TEXTURE_NAMES['background'])
    background_draw()

    projection_ortho()
    if state == "3" or state == "5":
        for i in range(num_of_heart):
            glPushMatrix()
            glTranslate(-0.85, 0.85, 0)
            glTranslate(i * .15, 0, 0)
            glScale(0.08, 0.08, 0)
            heart.heart_draw()
            glPopMatrix()
        glBindTexture(GL_TEXTURE_2D, -1)

        state = fuel.fuel_level_bar(fuel_level, state)

    init_my_scene(1000, 900)
    glPopMatrix()


#########################################################################

#########################################################################

def lighting():
    LightPos = [0, 10, 5, 1]
    LightAmb = [0, 0, 0, 0]
    LightDiff = [0.3, 0.3, 0.3, 1]
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
    global spaceship_position
    # fire tail outer oval
    glPushMatrix() 
    glColor3d(0,0.3,0.8)
    glTranslate(spaceship_position-0.5, -0.1, abs(spaceship_position / 6)-5.5)
    glRotate(5 * spaceship_position, 0, 0, 1)
    glScale(0.5, 0.5, 2)
    glutSolidSphere(0.8,30,30)
    glTranslate(2,0,0)
    glutSolidSphere(0.8,30,30)
    glPopMatrix()
    # fire tail inner oval
    glPushMatrix() 
    glColor3d(0.5,0.75,0.85)
    glTranslate(spaceship_position-0.5, 0.1, abs(spaceship_position / 6)-5.5)
    glRotate(5 * spaceship_position, 0, 0, 1)
    glScale(0.2, 0.5, 1.7)
    glutSolidSphere(0.8,30,30)
    glTranslate(5,0,0)
    glutSolidSphere(0.8,30,30)
    glPopMatrix()
    #spaceship body
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glPushMatrix()
    glTranslate(spaceship_position, 0, abs(spaceship_position / 6))
    glRotate(5 * spaceship_position, 0, 0, 1)
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

# def draw_fire():
#     glBegin(GL_QUADS)
#     gluSphere(0.2,10,10)
#     glEnd()
#########################################################################
def switch():
    global state
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glLoadIdentity()
    draw_screen()

    if not num_of_heart:
        state = "gameOver"
        background_sound.stop()
    if pause:
        draw_text("press R to continue ", -.3, 0, 6)
        glutSwapBuffers()
    if (state == "3" or state == "5") and pause == False:
        game()
    if not pause:
        glutSwapBuffers()


#########################################################################
def camera_setup():
    global camera_coordinates
    if state == 'intro':
        pass
    if state == "5":
        if camera_coordinates['y-eye'] < 50:
            camera_coordinates['y-eye'] += 0.5
            camera_coordinates['z-eye'] -= 0.5
            camera_coordinates['y_center'] -= 3 / 50
            camera_coordinates['z_center'] += 0.7

    gluLookAt(camera_coordinates['x-eye'], camera_coordinates['y-eye'], camera_coordinates['z-eye'],
              camera_coordinates['x_center'], camera_coordinates['y_center'], camera_coordinates['z_center'],
              0, 1, 0)


def game():
    global generate, fuel_generate, fuel_level, speed, state, camera_coordinates, num_of_heart, flash  # variables

    camera_setup()

    score = (generate // 100) * 100
    draw_text(f"SCORE: {score}", -.9, .7)
    draw_text("press P to pause ", -.9, .6, 4)

    if generate % 120 == 0:
        speed = obstacles.generate_obstacle(num_of_rail=int(state), speed=speed)
    obstacles.draw_obstacles(speed=speed)
    num_of_heart, flash = obstacles.collision_detection(space_ship_position=spaceship_position,
                                                        num_of_heart=num_of_heart, speed=speed,
                                                        state=state, flash=flash)

    if generate % 1440 == 0:
        heart.generate_new_heart(num_of_rail=int(state), obstacles_x=obstacles.obstacle_x[-1], fuel_x=fuel.fuel_x)
    heart.draw_old_heart(speed)
    num_of_heart = heart.collision_detection(space_ship_position=spaceship_position, num_of_heart=num_of_heart,
                                             speed=speed, )

    if 50 >= fuel_level >= 20 and not len(fuel.fuel_x):
        fuel.generate_new_fuel(num_of_rail=int(state), obstacles_x=obstacles.obstacle_x[-1])
    fuel.draw_old_fuel(speed=speed)
    fuel_level = fuel.collision_detection(space_ship_position=spaceship_position, fuel_level=fuel_level, speed=speed)

    if flash:
        flash -= 1
    if flash % 15 == 0:
        draw_vehicle()

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
        pause = True
    if key == b'r':
        print("resume")
        pause = False


def mouse_callback(x, y):
    global spaceship_position, state
    spaceship_position = (-x + 500) / 30
    if spaceship_position > 8 and state == '3':
        spaceship_position = 8
    elif spaceship_position < -8 and state == '3':
        spaceship_position = -8

    if spaceship_position > 16 and state == '5':
        spaceship_position = 16
    elif spaceship_position < -16 and state == '5':
        spaceship_position = -16


#########################################################################
def anim_timer(v):
    switch()
    glutTimerFunc(MILLISECONDS, anim_timer, v + 1)


def main():
    global background_sound
    glutInit(sys.argv)
    pygame.init()
    glfw.init()
    monitor = glfw.get_primary_monitor()
    mode = glfw.get_video_mode(monitor)

    background_sound.play(-1)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(mode.size.width, mode.size.height)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Race The Sun !")
    glutDisplayFunc(switch)
    glutTimerFunc(MILLISECONDS, anim_timer, 1)
    init_textures()
    glutKeyboardFunc(keyboard_callback)
    glutPassiveMotionFunc(mouse_callback)
    init_my_scene(mode.size.width, mode.size.height)
    glutMainLoop()


main()
