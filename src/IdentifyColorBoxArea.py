
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
from PIL import Image
import src.RGBARules as rgbManager
import src.FolderRules as folderManager


class ImageColorManipulator:

    def __init__(self, original_image_folder_path=r'C:\Users\63641\Box Sync\Work\Software Development '
                                                  r'Team\GoodToBad\resources\GoodImages',
                 output_image_folder_path=r'C:\Users\63641\Box Sync\Work\Software Development '
                                          r'Team\GoodToBad\resources\Output', list_of_rgba_color_monitor: list = []):
        self.list_of_rgba_color_monitor: list = list_of_rgba_color_monitor
        if os.path.exists(original_image_folder_path):
            if os.path.isdir(original_image_folder_path):
                print("Original Image Folder " + original_image_folder_path + "--> Valid.")
                self.original_image_folder_path = original_image_folder_path
            else:
                print("Image Folder path : " + original_image_folder_path + " is not a folder.")
                exit(0)
        else:
            print("Given image folder path : " + original_image_folder_path + " - X doesn't exist.")
            exit(0)

        if os.path.exists(output_image_folder_path) and len(os.listdir(output_image_folder_path)) > 0:
            print("The Output Folder is not empty -> please rename or delete the folder : " + output_image_folder_path)
        else:
            os.mkdir(output_image_folder_path)
            self.output_image_folder_path = output_image_folder_path

    def run(self):
        list_of_images = self.find_all_images_in_folder(self.original_image_folder_path)
        for image_path in list_of_images:
            image = Image.open(image_path)
            searching_for_rgb = {'red': 252, 'green': 138, 'blue': 68}
            rgb_rules = rgbManager.RGBARules(r_value=searching_for_rgb['red'], low_range_r=4, high_range_r=3,
                                             g_value=searching_for_rgb['green'], low_range_g=20, high_range_g=20,
                                             b_value=searching_for_rgb['blue'], low_range_b=80, high_range_b=50)



    def find_pixel_color(self, image_path) -> list:
        image = Image.open(image_path)
        pix = image.load()
        print("Image Size : " + str(image.size))
        pixel_point = (120, 180)
        print(image.getpixel(pixel_point))

    def find_all_images_in_folder(self, folder_path: str) -> list:
        list_of_images: list = []
        for each_file in os.listdir(folder_path):
            file_extension = each_file.split('.')[1]
            if file_extension in 'png' or 'jpeg' or 'jpg':
                print(each_file + " is a picture format")
                list_of_images.append(os.path.join(folder_path, each_file))

    def set_color(self, rgb_value):
        pass

    def display_crop_image(self):
        pass

    def display_image_after_manipulation(self):
        pass

    def manipulate_good_image_to_bad(self):
        pass
