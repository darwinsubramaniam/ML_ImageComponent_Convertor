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


def scanning_dir(path: str) -> list:
    list_dir_file = []
    for each_dir_or_file in os.listdir(path):
        image_path = os.path.join(path, each_dir_or_file)
        list_dir_file.append(image_path)

    return list_dir_file


def remove_images_which_are_duplicated(list_of_image_path):
    number_before = 0
    is_start = True
    for each_image_path in list_of_image_path:
        print(each_image_path)
        image_path_ext = each_image_path.split('\\').pop()
        image_name = image_path_ext.split('.')[0]
        print(image_name)
        image_number = image_name.split('_')[0]
        print(image_number)

        def minus_one(first_number, next_number):
            return next_number - first_number

        if is_start is True:
            number_before = int(image_number)
            is_start = False
        else:
            if minus_one(number_before, int(image_number)) is 0:
                pass
            else:
                os.remove(each_image_path)


if __name__ == '__main__':
    main_path = r'C:\Users\63641\Box Sync\AOI Images\Images\20190114\Fake_NG_Manipulation_Output'
    list_of_location = scanning_dir(main_path)

    for each_location in list_of_location:
        list_of_color_path = scanning_dir(each_location)
        for each_color_path in list_of_color_path:
            print(each_color_path)
            list_of_image_path = scanning_dir(each_color_path)
            remove_images_which_are_duplicated(list_of_image_path)