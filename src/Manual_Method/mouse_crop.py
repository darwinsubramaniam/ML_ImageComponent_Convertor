#  Copyright (c) 2019.
#  Author UD@DarwinSubramaniam
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import pygame, sys
import os
from PIL import Image

pygame.init()


def displayImage(screen, px, topleft, prior):
    # ensure that the rect always has positive width, height
    x, y = topleft
    width = pygame.mouse.get_pos()[0] - topleft[0]
    height = pygame.mouse.get_pos()[1] - topleft[1]
    if width < 0:
        x += width
        width = abs(width)
    if height < 0:
        y += height
        height = abs(height)

    # eliminate redundant drawing cycles (when mouse isn'dev_output moving)
    current = x, y, width, height
    if not (width and height):
        return current
    if current == prior:
        return current

    # draw transparent box and blit it onto canvas
    screen.blit(px, px.get_rect())
    im = pygame.Surface((width, height))
    im.fill((128, 128, 128))
    pygame.draw.rect(im, (32, 32, 32), im.get_rect(), 1)
    im.set_alpha(128)
    screen.blit(im, (x, y))
    pygame.display.flip()

    # return current box extents
    return (x, y, width, height)


def setup(path):
    px = pygame.image.load(path)
    screen = pygame.display.set_mode(px.get_rect()[2:])
    screen.blit(px, px.get_rect())
    pygame.display.flip()
    return screen, px


def mainLoop(screen, px):
    top_left = bottom_right = prior = None
    n = 0
    while n != 1:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if not top_left:
                    top_left = event.pos
                else:
                    bottom_right = event.pos
                    n = 1
        if top_left:
            prior = displayImage(screen, px, top_left, prior)
    return top_left + bottom_right


if __name__ == "__main__":

    dir_path = r'C:\Users\63641\Box Sync\AOI Images\Tantalum_54-64-60047'
    output_path = r'C:\Users\63641\Box Sync\AOI Images\Tantalum_54-64-60047\Fake_NG'

    list_path_of_dir = os.listdir(dir_path)

    for each_dir in list_path_of_dir:

        if each_dir not in "Fake_NG":
            component_orentation = each_dir
            output_component_orentation_path = os.path.join(output_path, component_orentation)

            if not os.listdir(output_path).__contains__(component_orentation):
                os.mkdir(output_component_orentation_path)

            orentation_folder_path = os.path.join(dir_path, each_dir)
            list_color_folder = os.listdir(orentation_folder_path)
            for each_color in list_color_folder:
                output_component_orentation_path_with_color = os.path.join(output_component_orentation_path, each_color)
                if not os.listdir(output_component_orentation_path).__contains__(each_color):
                    os.mkdir(os.path.join(output_component_orentation_path_with_color))
                    orentation_color_folder_path = os.path.join(orentation_folder_path, each_color)
                    list_of_images = os.listdir(orentation_color_folder_path)
                    left = 0
                    upper = 0
                    right = 0
                    lower = 0
                    count = 0
                    for each_image in list_of_images:
                        original_image_path = os.path.join(orentation_color_folder_path, each_image)
                        if count == 0:
                            # obtain the coordinate of the selected box
                            screen, px = setup(original_image_path)
                            left, upper, right, lower = mainLoop(screen, px)
                            count = 1

                        # ensure output rect always has positive width, height
                        if right < left:
                            left, right = right, left
                        if lower < upper:
                            lower, upper = upper, lower

                        # using the coordinate, cropped the image, perform rotation and paste it back to the original image
                        print(left, upper, right, lower)
                        im = Image.open(original_image_path)
                        cropped = im.crop((left, upper, right, lower))
                        new_img = cropped.rotate(180)
                        im.paste(new_img, box=(left, upper, right, lower))
                        im.show()

                        # append the file name with fake_NG
                        # if the original filename contain word "good", may need to write some code to remove the Good
                        name, ext = os.path.splitext(each_image)
                        new_name = name + "_fake_NG" + ext
                        absolute_new_name = output_path + '\\' + component_orentation + '\\' + each_color + '\\' + new_name

                        pygame.display.quit()
                        if  "GOOD" and "FC" and not "NG" in each_image:
                            im.save(absolute_new_name)



