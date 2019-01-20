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


from src.Segregator.ColorBasedCategorySegregator import ImageColorBasedSegregation
from src.Automated_Method.RGBARules import RGBARules as rgbManager
import pytest


def initiation():
    orange_range = rgbManager(r_value=252, low_range_r=38, high_range_r=3,
                              g_value=108, low_range_g=22, high_range_g=61,
                              b_value=60, low_range_b=5, high_range_b=31)
    color_name = "Orange"
    negative_color_name = "Black"
    image_color_based_segregation = ImageColorBasedSegregation(rgb_rules=orange_range,
                                                               color_name=color_name,
                                                               output_image_path='../test/resources'
                                                                                 '/ColorBasedTestingOutput',
                                                               percentage=20,
                                                               negative_category_name=negative_color_name,
                                                               dev_mode=True)
    return image_color_based_segregation


def test_color_black_component():
    image_color_based_segregation = initiation()
    negative_color_name = "Black"
    image_color_based_segregation.image_input('../test/resources/ColorBasedTestingInput/Black_Tantalum_1.jpg')
    color_category = image_color_based_segregation.run()
    assert color_category == negative_color_name
    image_color_based_segregation.image_input('../test/resources/ColorBasedTestingInput/Black_Tantalum_4.jpg')
    color_category = image_color_based_segregation.run()
    assert color_category == negative_color_name


def test_color_orange_component():
    image_color_based_segregation = initiation()
    color_name = "Orange"
    image_color_based_segregation.image_input('../test/resources/ColorBasedTestingInput/Orange_Tantalum_2.jpg')
    color_category = image_color_based_segregation.run()
    assert color_category == color_name

    image_color_based_segregation.image_input('../test/resources/ColorBasedTestingInput/Orange_Tantalum_3.jpg')
    color_category = image_color_based_segregation.run()
    assert color_category == color_name
