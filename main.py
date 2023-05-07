from random import randrange
from math import *

import pygame.mixer
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
from objloader import *


#########################################################################

# التاسك بتاعنا عبارة عن powerup الي هو الطيارة تاخد بنزين في الطريق و كمان تاخد قلوب
# البار الي بيعبر عن مستوي البنزين هيكون لوتة بيتغير علي حسب الكمية من الاخضر للاحمر
def create_fuel_bar():
    # todo create a function for create life bar
    # life bar It is a variable width rectangle
    pass


def create_gas():
    # todo create  gas
    ## في التاسك دي حد هيدور علي صورة جركن البنزين و يلزقة علي بوليجون يعني
    
    fuel_z=obstacles.Z[-1]
    if state =="3":
        while True :
            fuel_x=(randrange(3)-1)*8
            
            if fuel_x != obstacles.X[-1]:
                break

    pass


def create_heart():
    # todo create heart
    pass


class obstacle:
    def __init__(self):
        self.X = []
        self.Z = []
        self.PHASE = []

    def generate_new_obstacle(self):
        global counter, speed
        counter += 1
        if counter % 5==0 and speed <= 4:
            speed += 3/(7*speed)
            
            print(speed)
        if state == '3':
            rail = randrange(3)  # rail={0,1,2}
            self.X.append((rail - 1) * 8)
        else:
            rail1 = randrange(5)
            self.X.append((rail1 - 2) * 8)
            rail2 = randrange(5)
            while rail1 == rail2:
                rail2 = randrange(5)

            self.X.append((rail2 - 2) * 8)
            self.Z.append(200)
            self.PHASE.append(randrange(360))

        self.PHASE.append(randrange(360))
        self.Z.append(200)

    def draw_old_obstacles(self):
        global speed
        glPushMatrix()
        for i in range(len(self.X)):
            glPushMatrix()
            glColor3d(1, 1, 0)

            glTranslate(self.X[i], 0, self.Z[i])
            glRotate(self.PHASE[i], 1, 0, 1)
            self.Z[i] -= speed
            glScale(2.5, 2.5, 2.5)
            obstacles.make_obstacle()

            glBindTexture(GL_TEXTURE_2D, -1)
            # glutSolidCube(5)
            self.PHASE[i] += 3
            glPopMatrix()

        glPopMatrix()

    def delete_obstacle(self, n):
        for i in range(n):
            self.Z.pop(0)
            self.X.pop(0)
            self.PHASE.pop(0)

    def make_obstacle(self):
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


class Fuel:
    def __init__(self):
        self.X = []
        self.Z = []

    def generate_new_fuel(self):
        if state == '3':
            rail = randrange(3)  # rail={0,1,2}
            self.X.append((rail - 1) * 8)
        else:
            rail1 = randrange(5)
            self.X.append((rail1 - 2) * 8)
        self.Z.append(200)

    def draw_old_fuel(self):
        global speed
        glPushMatrix()
        for i in range(len(self.X)):
            glPushMatrix()
            glColor3d(1, 1, 0)
            glTranslate(self.X[i], 0, self.Z[i])
            self.Z[i] -= speed
            glScale(2.5, 3, 0)
            fuel.draw_fuel()
            glBindTexture(GL_TEXTURE_2D, -1)
            glPopMatrix()
        glPopMatrix()

    def delete_fuel(self, n):
        for i in range(n):
            self.Z.pop(0)
            self.X.pop(0)

    def draw_fuel(self):
        glBindTexture(GL_TEXTURE_2D, TEXTURE_NAMES[5])
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex(-1, -1)

        glTexCoord2f(1, 0)
        glVertex(1, -1)

        glTexCoord2f(1, 1)
        glVertex(1, 1)

        glTexCoord2f(0, 1)
        glVertex(-1, 1)
        glEnd()

    def fuel_level_bar(self , fuel_level):
        glColor3d(1-fuel_level/100, fuel_level/100, 0.0)
        print('data')
        print(fuel_level)
        glLoadIdentity()
        glBegin(GL_POLYGON)
        glVertex2d(-0.9, 0.7*fuel_level/100)
        glVertex2d(-0.92, 0.7*fuel_level/100)
        glVertex2d(-0.92, -0.1)
        glVertex2d(-0.9, -0.1)

        glEnd()


#########################################################################
obstacles = obstacle()
fuel = Fuel()
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
fuel_level=100
TEXTURE_NAMES = [0, 1, 2, 3, 4, 5]
MILLISECONDS = 15
factory = {}


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
    images = [pygame.image.load("background.jpg"),
              pygame.image.load("GameOver.jpg"),
              pygame.image.load("obstacle.jpeg"),
              pygame.image.load("heart.png"),
              pygame.image.load("Start.jpg"),
              pygame.image.load("fuel.png")
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
    global background_sound
    glPushMatrix()
    glColor(1, 1, 1)
    projection_ortho(-220)

    if state == "start":
        glBindTexture(GL_TEXTURE_2D, TEXTURE_NAMES[4])
    elif state == "gameOver":
        glBindTexture(GL_TEXTURE_2D, TEXTURE_NAMES[1])
        background_sound.stop()
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
        fuel.fuel_level_bar(fuel_level)


    init_my_scene(1000, 900)
    glPopMatrix()


#########################################################################
def lighting():
    LightPos=[0, 10, 5, 1]
    LightAmb=[0, 0, 0, 0]
    LightDiff=[1, 1, 1, 1.0]
    LightSpec=[0.03, 0.03, 0.04, 1.0]

    MatAmbF=[1, 1, 1, 1]
    MatDifF=[1, 1, 1, 1]
    MatSpecF=[0.1, 0.1, 0.1, 1]
    MatShnF=[30]
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
    Nx = (0)*cos(X*pi/180) + (0)-sin(X*pi/180)
    Ny = (0)*sin(X*pi/180) + (0)*cos(X*pi/180)             #Normal vector
    Nz = 1
    glNormal(Nx,Ny,Nz)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    glColor3d(0, 0, 0)
    glPushMatrix()
    glTranslate(X, 0, abs(X / 6))
    glRotate(5*X, 0, 0, 1)
    glScale(.6, .6, .7)
    getModel("models/Jet_01.obj").render()
    glPopMatrix()
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)


#########################################################################
def draw_text(string, x=0, y=0, size=5):
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
def sound_crash(life):
    if life != 0:
        crash_sound = pygame.mixer.Sound("crash.wav")
        crash_sound.play()
    else:
        gameover_sound = pygame.mixer.Sound("gameover.mp3")
        gameover_sound.play()

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
        # print("game")
        game()
    if not pause:
        glutSwapBuffers()



#########################################################################

def game():
    global generate, fuel_generate,fuel_level, speed, state, camera_coords  # variables

    draw_text("SCORE: " + str((generate // 100) * 100), -.9, .7)
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
        obstacles.generate_new_obstacle()

    if counter % 12 == 0:
        
        create_gas()

    obstacles.draw_old_obstacles()
    # draw_text("Hello Word")
    draw_vehicle()

    collision_detection()

    if speed < 3:
        STEP = 3
    else:
        STEP = 4
    if generate >= 4000 and state == "3":
        generate = 0
        state = "5"
    generate += STEP
    fuel_generate += STEP
    fuel_level -=0.2


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
def collision_detection():
    global X, obstacles, life, state, crash
    if len(obstacles.X) and state == '3' and obstacles.Z[0] <= speed and abs(X - obstacles.X[0]) <= 6:
        life -= 1
        sound_crash(life)
        obstacles.delete_obstacle(1)
        print('crash ' * 15 + '\n' + '#' * 50)
        return

    elif len(obstacles.X) > 1 and state == '5':
        if obstacles.Z[0] <= speed and abs(X - obstacles.X[0]) <= 6 or obstacles.Z[1] <= speed and abs(
                X - obstacles.X[1]) <= 6:

            life -= 1
            sound_crash(life)
            if obstacles.Z[0] == obstacles.Z[1]:
                obstacles.delete_obstacle(1)
            obstacles.delete_obstacle(1)
            print('crash ' * 15 + '\n' + '#' * 50)
            return

    if len(obstacles.X) and obstacles.Z[0] < -6:
        if state == "5" and obstacles.Z[1] < -6:
            obstacles.delete_obstacle(2)
        else:
            obstacles.delete_obstacle(1)


#########################################################################
def anim_timer(v):
    switch()
    glutTimerFunc(MILLISECONDS, anim_timer, v + 1)


def main():
    global background_sound
    glutInit(sys.argv)
    pygame.init()
    background_sound = pygame.mixer.Sound("gameplay.mp3")
    background_sound.play(-1)
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
