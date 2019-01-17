#  Copyright (c) 2019.
#  Author UD@DarwinSubramaniam
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of
# the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import sys
import time

from PIL import Image, ImageDraw
import src.RGBARules as rgbManager

import src.FolderRules as folderManager
from src.Neighboring_Pixel_Method import NeighboringPixelValidationMethod


class ImageColorManipulator:
    DevMode = True
    Display_All_Print_Out = False
    pic_format = ('png', 'jpg', 'jpeg')

    def __init__(self, original_image_folder_path=r'C:\Users\63641\Box Sync\Work\Software Development '
                                                  r'Team\GoodToBad\resources\dev_resources\good_images',
                 output_image_folder_path=r'C:\Users\63641\Box Sync\Work\Software Development '
                                          r'Team\GoodToBad\resources\Output\dev_output\good_images',
                 list_of_rgba_color_monitor: list = []):
        self.list_of_rgba_color_monitor: list = list_of_rgba_color_monitor
        if os.path.exists(original_image_folder_path):
            if os.path.isdir(original_image_folder_path):
                print("Original Image Folder " + original_image_folder_path + "--> Valid.")
                self.original_image_folder_path = original_image_folder_path
            else:
                print("Image Folder path : " + original_image_folder_path + " is not a folder.")
                exit(0)
        else:
            print("Given image folder path : " + original_image_folder_path + " - X doesn'dev_output exist.")
            exit(0)

        if os.path.exists(output_image_folder_path) and len(os.listdir(output_image_folder_path)) > 0:
            print("The Output Folder is not empty -> please rename or delete the folder : " + output_image_folder_path)
            exit(0)
        else:
            os.mkdir(output_image_folder_path)
            self.output_image_folder_path = output_image_folder_path

    def run(self):
        list_of_images = self._find_all_images_in_folder(self.original_image_folder_path)
        for image_path in list_of_images:
            # 1. open the image -> loaded to the RAM
            image = Image.open(image_path)
            if self.DevMode:
                print('Working on picture : ' + str(image_path))
                time.sleep(0.5)

            image_name = image_path.split("\\").pop().split(".")[0]

            # 2. color of component
            searching_for_rgb = {'red': 252, 'green': 108, 'blue': 60}

            rgb_rules = rgbManager.RGBARules(r_value=searching_for_rgb['red'], low_range_r=38, high_range_r=3,
                                             g_value=searching_for_rgb['green'], low_range_g=22, high_range_g=61,
                                             b_value=searching_for_rgb['blue'], low_range_b=5, high_range_b=31)

            image_size = image.size
            image_height = image_size[1]
            image_width = image_size[0]

            pixels_with_accepted_color_range: list = []

            for height in range(image_height):
                for width in range(image_width):
                    lookup_pixel_point = (width, height)
                    rgb_at_lookup_pixel = image.getpixel(lookup_pixel_point)
                    is_accept_pixel_of_shape = rgb_rules.is_pixel_within_rgb_range(rgb_at_lookup_pixel)
                    if is_accept_pixel_of_shape:

                        if self.DevMode:
                            print()
                            print("Adding Pixel : " + str(lookup_pixel_point))
                            print()
                            print("RGB value at this pixel is ->  R :" + str(rgb_at_lookup_pixel[0]) +
                                  " G : " + str(rgb_at_lookup_pixel[1]) +
                                  " B : " + str(rgb_at_lookup_pixel[2]))
                            print()

                        pixels_with_accepted_color_range.append(lookup_pixel_point)

                    else:
                        if self.DevMode and self.Display_All_Print_Out:
                            print()
                            print('_____________________________________________________')
                            print('Pixel : ' + str(lookup_pixel_point) + " is not within the range "
                                                                         "of acceptance pixel color.")
                            print("RGB value at this pixel is ->  R :" + str(rgb_at_lookup_pixel[0]) +
                                  " G : " + str(rgb_at_lookup_pixel[1]) +
                                  " B : " + str(rgb_at_lookup_pixel[2]))
                            print()
                            print('______________________________________________________')

            draw = ImageDraw.Draw(image)
            count = 0
            data_clean_up_list = NeighboringPixelValidationMethod(pixels_with_accepted_color_range).clean_up_pixel_list
            #data_clean_up_list_second = NeighboringPixelValidationMethod(pixels_with_accepted_color_range).clean_up_pixel_list

            for each_pixel in data_clean_up_list:
                count += 1
                draw.point(xy=each_pixel.pixel_location, fill=(255, 0, 0))
            fp = os.path.join(self.output_image_folder_path, image_name+"_"+str(count) + ".png")
            image.save(fp)

    def _find_all_images_in_folder(self, folder_path: str) -> list:
        list_of_images: list = []
        for each_file in os.listdir(folder_path):
            file_extension = each_file.split('.')[1]
            if file_extension in self.pic_format:
                print(each_file + " is a picture format")
                list_of_images.append(os.path.join(folder_path, each_file))

        return list_of_images

    def add_new_format(self, format_name):
        self.pic_format = self.pic_format.__add__(format_name)

    def clean_up_pixel(self,list_of_pixels):
        pass

    def set_color(self, rgb_value):
        pass

    def display_crop_image(self):
        pass

    def display_image_after_manipulation(self):
        pass

    def manipulate_good_image_to_bad(self):
        pass
