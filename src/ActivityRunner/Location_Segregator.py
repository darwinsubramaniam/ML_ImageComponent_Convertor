#  Copyright (c) 2019.
#  Author UD@DarwinSubramaniam
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import os

import src.Segregator.ColorBasedCategorySegregator as colorSegregator
import src.Automated_Method.RGBARules as rgbManager
import  shutil

if __name__ == '__main__':

    Tantalum_path = r'C:\Users\63641\Box Sync\AOI Images\Images\20190114\TANTAL (54-64-60047)'
    Tantalum_output_path = r'C:\Users\63641\Box Sync\AOI Images\Images\20190114\Location_Segregated_Tantalum'

    list_dir = os.listdir(Tantalum_path)
    list_sku_path = []


    for each_dir in list_dir:
        sku_path = os.path.join(Tantalum_path, each_dir)
        list_sku_path.append(sku_path)

    count = 0
    for each_sku in list_sku_path:
        list_result_path_in_each_sku = os.listdir(each_sku)
        for each_result_path in list_result_path_in_each_sku:
            result_path = os.path.join(each_sku,each_result_path)
            list_component_path = os.listdir(result_path)
            for each_component_path in list_component_path:
                component_location = each_component_path.split('-')[0].strip()
                component_folder_output_path = os.path.join(Tantalum_output_path, component_location)
                if not os.path.exists(component_folder_output_path):
                    os.mkdir(component_folder_output_path)
                count += 1
                component_dir_path = os.path.join(result_path, each_component_path)
                list_image = os.listdir(component_dir_path)
                for each_image in list_image:
                    original_image_path = os.path.join(component_dir_path,each_image)
                    copy_image_path = os.path.join(component_folder_output_path, str(count)+"_"+each_image)
                    shutil.copyfile(original_image_path,copy_image_path)






    #segregate = colorSegregator.Image_Color_Based_Segregator(rgb_rules=orange_range,)


