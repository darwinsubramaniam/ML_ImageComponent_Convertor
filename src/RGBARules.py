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

class RGBARules:
    def __init__(self, r_value: int, low_range_r: int,
                 high_range_r: int, g_value: int,
                 low_range_g: int, high_range_g,
                 b_value: int, low_range_b: int, high_range_b: int):
        self.r_value = r_value
        self.low_range_r = low_range_r
        self.high_range_r = high_range_r
        self.g_value = g_value
        self.low_range_g = low_range_g
        self.high_range_g = high_range_g
        self.b_value = b_value
        self.low_range_b = low_range_b
        self.high_range_b = high_range_b
        self.min_r = r_value - low_range_r
        self.max_r = r_value + high_range_r
        self.min_g = g_value - low_range_g
        self.max_g = g_value + high_range_g
        self.min_b = b_value - low_range_b
        self.max_b = b_value + high_range_b
        self.display_rule()

    def is_red_value_within_range(self, r_value):
        if r_value <= self.high_range_r:
            if r_value >= self.low_range_r:
                return True
            else:
                return True
        else:
            return False

    def is_green_value_within_range(self, g_value):
        if g_value <= self.high_range_g:
            if g_value >= self.low_range_g:
                return True
            else:
                return True
        else:
            return False

    def is_blue_value_within_range(self, b_value):
        if b_value <= self.high_range_b:
            if b_value >= self.low_range_b:
                return True
            else:
                return True
        else:
            return False

    def display_rule(self):
        print()
        print("Current RGB Rule is : ")
        print("Red value : " + str(self.r_value))
        print("Min red value :" + str(self.min_r))
        print("Max red value :" + str(self.max_r))
        print('----------------------------------------')
        print("Green value : " + str(self.g_value))
        print("Min green value :" + str(self.min_g))
        print("Max red value :" + str(self.max_g))
        print('----------------------------------------')
        print("Blue value : " + str(self.b_value))
        print("Min blue value :" + str(self.min_b))
        print("Max blue value :" + str(self.max_b))
        print()
