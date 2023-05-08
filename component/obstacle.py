
from math import *
from random import randrange
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
class Obstacle:
    def __init__(self):
        self.X = []
        self.Z = []
        self.PHASE = []

    def generate_new_obstacle(self):
        global counter, speed
        counter += 1
        if counter % 5 == 0 and speed <= 4:
            speed += 3 / (7 * speed)

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