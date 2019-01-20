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

import src.Automated_Method.RGBARules as RGB_Rules
from PIL import Image


class ImageColorBasedSegregation:

    def __init__(self, rgb_rules: RGB_Rules,
                 color_name: str,
                 output_image_path: str,
                 percentage=25,
                 negative_category_name: str = "Unknown",
                 dev_mode: bool = True,split_regex="/"):
        self.class_name = "Image Color Based Segregation for " + color_name
        self.image_path = ""
        self.split_regex = split_regex
        self.negative_category_name = negative_category_name
        self.output_path = output_image_path
        self.Display_All_Print_Out = True
        self.dev_mode = dev_mode
        self.rgb_rules = rgb_rules
        self.color = color_name
        self.percentage = percentage

    def set_output_dir(self, output_path):
        self.output_path = output_path

    def get_color_name(self) -> str:
        return self.color

    def set_limit_to_identify_pic_fall_in_this_category(self, percentage: int):
        self.percentage = percentage

    def image_input(self, original_image_path):
        self.image_path = original_image_path

    def run(self) -> str:
        image = Image.open(self.image_path)
        if self.dev_mode:
            print('Working on picture : ' + str(self.image_path))
            # time.sleep(0.5)

        image_name_plus_ext = self.image_path.split(self.split_regex).pop()
        image_name = image_name_plus_ext.split(".")[0]
        ext = image_name_plus_ext.split(".")[1]
        image_height = image.size[1]
        image_width = image.size[0]

        '''Calculate the total pixel in the picture.'''
        total_pixel = image_height * image_width

        list_of_pixel_with_obey_rgb_rules: list = []

        for height in range(image_height):
            for width in range(image_width):
                lookup_pixel_point = (width, height)
                rgb_at_lookup_pixel = image.getpixel(lookup_pixel_point)
                # 1. is pixel color within the rgb_rules of component color.
                is_accept_pixel_of_component = self.rgb_rules.is_pixel_within_rgb_range(rgb_at_lookup_pixel)
                if is_accept_pixel_of_component:
                    if self.dev_mode:
                        print()
                        print(
                            '____________________' + self.class_name + " " + image_name +
                            '_________________________________')
                        print("Adding Pixel : " + str(lookup_pixel_point))
                        print()
                        print("RGB value at this pixel is ->  R :" + str(rgb_at_lookup_pixel[0]) +
                              " G : " + str(rgb_at_lookup_pixel[1]) +
                              " B : " + str(rgb_at_lookup_pixel[2]))
                        print()
                        print('________________________________________________________________________')
                    list_of_pixel_with_obey_rgb_rules.append(lookup_pixel_point)
                else:
                    if self.dev_mode and self.Display_All_Print_Out:
                        print()
                        print(
                            '_____________________' + self.class_name + " " + image_name +
                            '________________________________')
                        print('Pixel : ' + str(lookup_pixel_point) + " is not within the range "
                                                                     "of acceptance pixel color.")
                        print("RGB value at this pixel is ->  R :" + str(rgb_at_lookup_pixel[0]) +
                              " G : " + str(rgb_at_lookup_pixel[1]) +
                              " B : " + str(rgb_at_lookup_pixel[2]))
                        print()
                        print('________________________________________________________________________')

        category_confident = (len(list_of_pixel_with_obey_rgb_rules) / total_pixel) * 100
        if self.dev_mode:
            print()
            print('________________ Picture Category Log ' + self.class_name + '_________________________________')
            print("Picture " + image_name +
                  " has category confident level : " +
                  str(category_confident) + "for color " +
                  self.get_color_name())
            print('__________________________________________________________________________________________')

        if category_confident >= self.percentage:
            self._save_image(self.color, image_name_plus_ext)
            return self.color
        else:
            print()

            print('________________ Picture Category Log ' + self.class_name + '_________________________________')
            print("Picture : " +
                  image_name +
                  " is does not belong to category " +
                  self.get_color_name())
            print('__________________________________________________________________________________________')
            self._save_image(self.negative_category_name, image_name_plus_ext)
            return self.negative_category_name

    def _save_image(self, category, save_as: str):
        image = Image.open(self.image_path)
        if self.dev_mode:
            print("Image saved as : " + save_as)
        category_output_path = os.path.join(self.output_path, category)
        if not os.path.exists(category_output_path):
            os.mkdir(category_output_path)

        save_image_in_path = os.path.join(category_output_path, save_as)
        image.save(save_image_in_path)
