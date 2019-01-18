#  Copyright (c) 2019.
#  Author UD@DarwinSubramaniam
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import src.Segregator.Color_Based_Category_Segregator as colorsegregator
import src.Automated_Method.RGBARules as rgbManager

if __name__ == '__main__':

    orange_range = rgbManager.RGBARules(r_value=252, low_range_r=38, high_range_r=3,
                                                              g_value=108, low_range_g=22, high_range_g=61,
                                                              b_value=60, low_range_b=5, high_range_b=31)

    location_tantalum_path = r'C:\Users\63641\Box Sync\AOI Images\Images\20190114\Location_Segregated_Tantalum'
    output_color_tantalum_path=r'C:\Users\63641\Box Sync\AOI Images\Images\20190114\Location_Color_Segregated_Tantalum'

    colorsegregator = colorsegregator.Image_Color_Based_Segregator(rgb_rules=orange_range,
                                                                   input_main_path=location_tantalum_path,
                                                                   color_name='Orange',
                                                                   percentage=50,
                                                                   negative_category_name="Black")

