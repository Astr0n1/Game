import pygame

from OpenGL.GL import *
gameover_index = 0
gamestart_index = 0
gameplay_index = 0
image_name = [
    'heart.png',
    'fuel.png',
    'start/' +'1 ('+ str(gamestart_index % 20) + ').png', 
    'background/2 (1).png',
    'gameover/' +'3 ('+ str(gameover_index % 42) + ').png'
]
textureList = [i for i in range( 42 + 2 + 20 + 1)]

class Texture:

    def init_textures(self):
        self.load_texture()
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    def load_texture(self):
        glEnable(GL_TEXTURE_2D)
        image_list = [pygame.image.load(f"assets/images/{image_name[i]}") for i in range(2)]
        gamestart_list = [pygame.image.load(f"assets/images/start/1 ({i}).png") for i in range(1,20)]
        gameplay_list = [pygame.image.load(f"assets/images/background/2 (1).png")]
        gameOver_list = [pygame.image.load(f"assets/images/gameover/3 ({i}).png") for i in range(1,42)]
        image_list.extend(gamestart_list)
        image_list.extend(gameplay_list)
        image_list.extend(gameOver_list)
        textures = [pygame.image.tostring(image, "RGBA", True) for image in image_list]
        glGenTextures(len(image_list), textureList)
        for i in range(len(image_list)):
            self.texture_setup(textures[i],
                               i,
                               image_list[i].get_width(),
                               image_list[i].get_height())

    @staticmethod
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
                     texture_image_binary, )
        glBindTexture(GL_TEXTURE_2D, -1)

def pass_index(index, state):
    global gameover_index, gamestart_index, gameplay_index
    if state == "gameover":
        gameover_index = index
    elif state == "gamestart":
        gamestart_index = index
    elif state == "gameplay":
        gameplay_index = index