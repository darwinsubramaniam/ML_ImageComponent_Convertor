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
import time

import src.Automated_Method.RGBARules as RGB_Rules
from PIL import Image


class Image_Color_Based_Segregator:

    def __init__(self, rgb_rules: RGB_Rules,
                 input_main_path,
                 color_name: str,
                 output_path: str,
                 percentage=50,
                 negative_category_name:str = "Unkown"):
        self.negative_category_name = negative_category_name
        self.input_main_path = input_main_path
        self.output_path = output_path
        self.Display_All_Print_Out = True
        self.DevMode = True
        self.rgb_rules = rgb_rules
        self.color = color_name
        self.percentage = percentage

    def get_color_name(self) -> str:
        return self.color

    def set_limit_to_identify_pic_fall_in_this_category(self, percentage: int):
        self.percentage = percentage

    def get_list_of_image_input_dir(self)->list:
        list_of_images: list = []
        for each_file in os.listdir(self.input_main_path):
            file_extension = each_file.split('.')[1]
            pic_format = ('png', 'jpg', 'jpeg')
            if file_extension in pic_format:
                print(each_file + " is a picture format")
                list_of_images.append(os.path.join(self.input_main_path, each_file))
        return list_of_images

    def run(self):
        for each_image_path in self.get_list_of_image_input_dir():
            image = Image.open(each_image_path)
            if self.DevMode:
                print('Working on picture : ' + str(each_image_path))
                time.sleep(0.5)

            image_name = each_image_path.split("\\").pop().split(".")[0]
            image_size = image.size
            image_height = image_size[1]
            image_width = image_size[0]

            total_pixel = image_height * image_width

            pixels_with_accepted_color_range: list = []

            for height in range(image_height):
                for width in range(image_width):
                    lookup_pixel_point = (width, height)
                    rgb_at_lookup_pixel = image.getpixel(lookup_pixel_point)
                    # 1. is pixel color within the rgb_rules of component color.
                    is_accept_pixel_of_component = self.rgb_rules.is_pixel_within_rgb_range(rgb_at_lookup_pixel)
                    if is_accept_pixel_of_component:
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

            category_confident = (len(pixels_with_accepted_color_range) / total_pixel) * 100

            if category_confident >= self.percentage:
                self._save_image(image, image_name)
            else:
                print("Picture : " + image_name + " is does not belong to category " + self.get_color_name())

    def _save_image(self, image: Image, save_as: str):
        category_output_path = os.path.join(self.output_path, self.get_color_name())
        if not os.path.exists(category_output_path):
            os.mkdir(category_output_path)

        save_image_in_path = os.path.join(category_output_path, save_as)
        image.save(save_image_in_path)




