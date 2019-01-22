import os
import pygame
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
    dir_path = r'C:\Users\63641\Box Sync\AOI Images\Images\20190114\Location_Color_Segregated_Tantalum'
    output_path = r'C:\Users\63641\Box Sync\AOI Images\Images\20190114\Fake_NG_Manipulation_Output'

    list_of_location_dir = os.listdir(dir_path)

    for each_location_dir in list_of_location_dir:

        component_location = each_location_dir
        output_component_location_path = os.path.join(output_path, component_location)

        if not os.listdir(output_path).__contains__(component_location):
            os.mkdir(output_component_location_path)

        color_folder_path = os.path.join(dir_path, each_location_dir)
        list_color_folder = os.listdir(color_folder_path)

        for each_color in list_color_folder:
            output_component_orientation_path_with_color = os.path.join(output_component_location_path, each_color)
            if not os.listdir(output_component_location_path).__contains__(each_color):
                os.mkdir(os.path.join(output_component_orientation_path_with_color))
                orientation_color_folder_path = os.path.join(color_folder_path, each_color)
                list_of_images = os.listdir(orientation_color_folder_path)
                left = 0
                upper = 0
                right = 0
                lower = 0
                count = 0
                for each_image in list_of_images:
                    original_image_path = os.path.join(orientation_color_folder_path, each_image)
                    if count == 0:
                        # obtain the coordinate of the selected box
                        screen, px = setup(original_image_path)
                        next = False
                        while not next:
                            left, upper, right, lower = mainLoop(screen, px)
                            x = input("All Good? y/n ")
                            if x == "y":
                                next = True
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
                    if count == 0:
                        im.show()

                    # append the file name with fake_NG
                    # if the original filename contain word "good", may need to write some code to remove the Good
                    name, ext = os.path.splitext(each_image)
                    new_name = name + "_fake_NG" + ext
                    absolute_new_name = output_path + '\\' + component_location + '\\' + each_color + '\\' + new_name

                    pygame.display.quit()
                    im.save(absolute_new_name)
