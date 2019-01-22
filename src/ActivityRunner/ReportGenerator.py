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

import csv
import os


def write_into_csv():
    pass


if __name__ == '__main__':
    main_path = r'C:\Users\63641\Box Sync\AOI Images\Images\20190114\SKU_Based_Faked_Images'
    list_of_sku = os.listdir(main_path)
    sku: str
    with open('Report.csv', 'a', newline='') as csvfile:
        fieldnames = ['SKU', 'Location', 'Color', 'Total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
    for sku in list_of_sku:
        sku_path = os.path.join(main_path, sku)
        list_of_location = os.listdir(sku_path)
        for location in list_of_location:
            location_path = os.path.join(sku_path, location)
            list_color = os.listdir(location_path)
            for color in list_color:
                color_path = os.path.join(location_path, color)
                list_images = os.listdir(color_path)
                total_image_in_color = len(list_images)
                with open('Report.csv', 'a', newline='') as csvfile:
                    fieldnames = ['SKU', 'Location', 'Color', 'Total']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    content = ({'SKU': sku, 'Location': location, 'Color': color, 'Total': total_image_in_color})
                    writer.writerow(content)
