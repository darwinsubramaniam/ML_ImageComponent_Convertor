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
""" BoundingBoxDetector to detect the color pixel which is used as the boundary box. """

from src.Automated_Method.RGBARules import RGBARules


class BoundingBox:

    def __init__(self, image_height: int,
                 image_width: int,
                 frame_percentage_removal: int,
                 rgba_rules: RGBARules = RGBARules(r_value=255, g_value=255, b_value=255,
                                                   low_range_r=146, low_range_g=140,
                                                   low_range_b=163,
                                                   high_range_r=0, high_range_b=0,
                                                   high_range_g=0)):
        self.frame_percentage_removal = frame_percentage_removal
        self.image_width = image_width
        self.image_height = image_height
        self.rgb_rules = rgba_rules

    def is_pixel_part_of_frame(self) -> bool:
        pass

    def is_bounding_box(self) -> bool:
        pass
