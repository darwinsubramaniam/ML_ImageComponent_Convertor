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
from attr import dataclass


@dataclass
class Pixel_Neighbour:
    pixel_location: tuple
    list_of_neighbour: list

    def __init__(self, pixel, list_of_neighbour=[]):
        self.pixel_location = pixel
        self.list_of_neighbour = list_of_neighbour

    def add_neighbour(self, neighbour_pixel):
        print("Adding neighboring pixel :" + str(neighbour_pixel) + " to -> " + str(self.pixel_location))
        self.list_of_neighbour.append(neighbour_pixel)

    def get_size_of_relationship(self) -> int:
        return len(self.list_of_neighbour)
