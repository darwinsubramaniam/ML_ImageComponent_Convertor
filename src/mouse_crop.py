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

    # eliminate redundant drawing cycles (when mouse isn't moving)
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

    dir_path = r'C:\Users\63641\Box Sync\Work\Software Development Team\GoodToBad\resources\GoodImages'
    output_path = r'C:\Users\63641\Box Sync\Work\Software Development Team\GoodToBad\resources\Output'
    input_filename = 'C132_DB_SDM0002FF8D_Good.png'
    absolute_input_filename = os.path.join(dir_path, input_filename)

    # obtain the coordinate of the selected box
    screen, px = setup(absolute_input_filename)
    left, upper, right, lower = mainLoop(screen, px)

    # ensure output rect always has positive width, height
    if right < left:
        left, right = right, left
    if lower < upper:
        lower, upper = upper, lower

    # using the coordinate, cropped the image, perform rotation and paste it back to the original image
    print(left, upper, right, lower)
    im = Image.open(absolute_input_filename)
    cropped = im.crop((left, upper, right, lower))
    new_img = cropped.rotate(180)
    im.paste(new_img, box=(left, upper, right, lower))
    im.show()

    # append the file name with fake_NG
    # if the original filename contain word "good", may need to write some code to remove the Good
    name, ext = os.path.splitext(input_filename)
    new_name = name + "_fake_NG" + ext
    absolute_new_name = output_path + '\\' + new_name

    pygame.display.quit()
    im.save(absolute_new_name)
