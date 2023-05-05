from random import randrange

from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *

from objloader import *


#########################################################################

# التاسك بتاعنا عبارة عن powerup الي هو الطيارة تاخد بنزين في الطريق و كمان تاخد قلوب
# البار الي بيعبر عن مستوي البنزين هيكون لوتة بيتغير علي حسب الكمية من الاخضر للاحمر
def create_life_bar():
    # todo create a function for create life bar
    # life bar It is a variable width rectangle
    pass


def create_gas():
    # todo create  gas
    ## في التاسك دي حد هيدور علي صورة جركن البنزين و يلزقة علي بوليجون يعني

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
        if counter == 5 and speed <= 5:
            speed += 0.3
            counter = 0
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


#########################################################################
obstacles = obstacle()
X = 0
speed = 2
life = 3
state = "start"
pause=False
camera_coords = {'x_c': 0, 'y_c': 25, 'z_c': -25,
                 'x_l': 0, 'y_l': 11, 'z_l': 0}
FONT_DOWNSCALE = 0.13
counter = 0
generate = 0
TEXTURE_NAMES = [0, 1, 2, 3,4]
MILLISECONDS = 5
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
              pygame.image.load("Start.jpg")]
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
    glPushMatrix()
    glColor(1, 1, 1)
    projection_ortho(-220)
    
    if state == "start":
        glBindTexture(GL_TEXTURE_2D, TEXTURE_NAMES[4])
    elif state == "gameOver":
        glBindTexture(GL_TEXTURE_2D, TEXTURE_NAMES[1])
    else :
        glBindTexture(GL_TEXTURE_2D, TEXTURE_NAMES[0])
    background_draw()
    projection_ortho()
    glBindTexture(GL_TEXTURE_2D, TEXTURE_NAMES[3])
    
    if state=="3" or state=="5":
        for i in range(life):
            glPushMatrix()
            glTranslate(i * .15, 0, 0)
            heart_draw()
            glPopMatrix()
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
    getModel("models/Jet_01.obj").render()
    # glBegin(GL_LINES)
    # for edge in spaceship_edges_vector2:
    #     for vertex in edge:
    #         glVertex3fv(spaceship_verticies_vector3[vertex])
    # glEnd()
    glPopMatrix()


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
def switch():
    global state
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glLoadIdentity()
    draw_screen()
    
    if not life:
        state="gameOver"
    
    if (state == "3" or state =="5") and pause == False:
        # print("game")
        game()
    if not pause :
        glutSwapBuffers()



#########################################################################

def game():
    global generate, speed, state, camera_coords  # variables

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

    draw_screen()

    obstacles.draw_old_obstacles()

    draw_vehicle()

    collision_detector()

    if speed < 3:
        STEP = 3
    elif speed < 4:
        state = "5"
        STEP = 4

    else:

        STEP = 5

    generate += STEP


#########################################################################
def keyboard_callback(key, x, y):
    global state,pause
    if key == b's' and state == "start":
        print(state)
        state="3"
    if key == b'p':
        print ("pause")
        if pause ==True:
            pause = False
        else:
            pause=True


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
def collision_detector():
    global X, obstacles, life, state
    if len(obstacles.X) and state == '3' and obstacles.Z[0] <= speed and abs(X - obstacles.X[0]) <= 6:
        life -= 1
        obstacles.delete_obstacle(1)
        print('crash ' * 15 + '\n' + '#'*50)
        return

    elif len(obstacles.X) > 1 and state == '5':
        if obstacles.Z[0] <= speed and abs(X - obstacles.X[0]) <= 6 or obstacles.Z[1] <= speed and abs(
                X - obstacles.X[1]) <= 6:

            life -= 1
            obstacles.delete_obstacle(2)
            print('crash ' * 15 + '\n' + '#'*50)
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
