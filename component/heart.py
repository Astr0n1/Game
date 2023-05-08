from random import randrange

from OpenGL.GL import *
from numpy import *


class Heart:
    def __init__(self):
        self.heart_x_axis = []
        self.heart_z_axis = []
        self.texture_name = -1

    def generate_new_heart(self, num_of_rail, obstacles_x_axis, fuel_x_axis):

        if num_of_rail == 3:
            factor = 1
        else:
            factor = 2

        rail = randrange(num_of_rail)  # rail={0,1,2}
        while (rail - factor) * 8 == obstacles_x_axis or (len(fuel_x_axis) and (rail - factor) * 8 == fuel_x_axis[0]):
            rail = randrange(num_of_rail)
        self.heart_x_axis.append((rail - factor) * 8)

        self.heart_z_axis.append(200)

    def draw_old_heart(self, speed):
        glPushMatrix()
        for i in range(len(self.heart_x_axis)):
            glPushMatrix()
            glColor3d(1, 1, 0)
            glTranslate(self.heart_x_axis[i], 0, self.heart_z_axis[i])
            self.heart_z_axis[i] -= speed
            glScale(5, 5, 0)
            self.draw_heart()
            glBindTexture(GL_TEXTURE_2D, -1)
            glPopMatrix()
        glPopMatrix()

    def delete_heart(self):
        self.heart_x_axis.pop(0)
        self.heart_z_axis.pop(0)

    def draw_heart(self):
        glBindTexture(GL_TEXTURE_2D, self.texture_name)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex(-.6, -.6)

        glTexCoord2f(1, 0)
        glVertex(.6, -0.6)

        glTexCoord2f(1, 1)
        glVertex(.8, .8)

        glTexCoord2f(0, 1)
        glVertex(-.8, .8)
        glEnd()

    def heart_collision_detection(self, space_ship_position, num_of_heart, speed):
        if len(self.heart_x_axis) and self.heart_z_axis[0] <= speed and abs(
                space_ship_position - self.heart_x_axis[0]) <= 6:
            if num_of_heart < 3:
                num_of_heart += 1
            self.delete_heart()
            return num_of_heart
        if len(self.heart_x_axis) and self.heart_z_axis[0] < -6:
            self.delete_heart()
        return num_of_heart
