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
import shutil

'''54-90-60010-8192G_REV44_T
   54-90-60010-8192G_REV45_T
   54-90-60010-8192G_REV46_T
   54-90-60010-8192G_REV47_T
   54-90-60012-0768G_REV17_B
   54-90-60019-3072G_REV16_B
   OMAHA_4TB_RWK_MB_DB_TOP'''


def get_sku_availability(dir_path: str) -> list:
    return os.listdir(dir_path)


def save_image(number: str, sku: str, location: str, color: str, original_image_path: str, ext: str = ".jpg",
               output_file: str = r'C:\Users\63641\Box Sync\AOI Images\Images\20190114\SKU_Based_Faked_Images'):
    """SKU
        ->  Location
          ->        Color"""
    sku_path = os.path.join(output_file, sku)
    location_path = os.path.join(sku_path, location)
    color_path = os.path.join(location_path, color)

    if not os.path.exists(sku_path):
        os.mkdir(sku_path)
    if not os.path.exists(location_path):
        os.mkdir(location_path)
    if not os.path.exists(color_path):
        os.mkdir(color_path)

    new_image_name = location + "_" + sku + "_" + number +ext
    new_image_path = os.path.join(color_path, new_image_name)
    shutil.copyfile(original_image_path, new_image_path)


if __name__ == '__main__':
    main_starting_path = r'C:\Users\63641\Box Sync\AOI Images\Images\20190114\Filtered_GOOD_BADimages'
    list_of_sku = get_sku_availability(
        dir_path=r'C:\Users\63641\Box Sync\AOI Images\Images\20190114\TANTAL (54-64-60047)')
    list_of_location = os.listdir(main_starting_path)
    for location in list_of_location:
        location_path = os.path.join(main_starting_path, location)
        list_of_color = os.listdir(location_path)
        for color in list_of_color:
            color_path = os.path.join(location_path, color)
            list_of_images = os.listdir(color_path)
            count = 1
            for image_name in list_of_images:
                sku = ""
                for checking_sku in list_of_sku:
                    if checking_sku in image_name:
                        sku = checking_sku

                image_path = os.path.join(color_path, image_name)
                count_str = str(count)
                save_image(count_str, sku, location, color, image_path)
                count += 1
