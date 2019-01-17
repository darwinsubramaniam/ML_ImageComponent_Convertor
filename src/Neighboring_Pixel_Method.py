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
import src.DataModels.NeighbourRelationship as pixelRelationship


class NeighboringPixelValidationMethod:
    original_selected_pixels: list
    clean_up_pixel_list: list = []

    def __init__(self, selected_pixel: list):
        self.original_selected_pixels = selected_pixel
        for each_pixel in self.original_selected_pixels:
            print("Currently looking at Pixel : " + str(each_pixel))
            list_of_pixel_relationship_pixels = self._find_neighboring_pixels(each_pixel)
            for each_relationship in list_of_pixel_relationship_pixels:
                print("Cleaning the point at "+  str(each_relationship.pixel_location))
                print("List of relationship points are : ")
                for each_neighbor in each_relationship.list_of_neighbour:
                    print(each_neighbor)
                    print()
                if each_relationship.get_size_of_relationship() <= 3:
                    print("Clearing up data")
                    list_of_pixel_relationship_pixels.remove(each_relationship)
                    print("number of points : " + str(len(list_of_pixel_relationship_pixels)))
                else:
                    self.clean_up_pixel_list.append(each_relationship)

    def _find_neighboring_pixels(self, pixel: tuple) -> list:
        list_of_pixels_with_neighbor_pixel_info: list = []
        if pixel in self.original_selected_pixels:
            pixel_neighbour = pixelRelationship.Pixel_Neighbour(pixel, [])
            x_axis_of_pix = pixel[0]
            y_axis_of_pix = pixel[1]

            # 1st. condition check left pixel is exist
            x_axis = x_axis_of_pix - 1
            y_axis = y_axis_of_pix
            current_checking_pix = (y_axis, x_axis)
            if current_checking_pix in self.original_selected_pixels:
                pixel_neighbour.add_neighbour(current_checking_pix)
                # 2nd. condition check upper left pixel is exist
                x_axis = x_axis_of_pix - 1
                y_axis = y_axis_of_pix + 1
                current_checking_pix = (y_axis, x_axis)
                if current_checking_pix in self.original_selected_pixels:
                    pixel_neighbour.add_neighbour(current_checking_pix)
            # 3rd. condition check lower left pixel is exist
            x_axis = x_axis_of_pix - 1
            y_axis = y_axis_of_pix - 1
            current_checking_pix = (y_axis, x_axis)
            if current_checking_pix in self.original_selected_pixels:
                pixel_neighbour.add_neighbour(current_checking_pix)
            # 4th. condition check down pixel is exist
            x_axis = x_axis_of_pix
            y_axis = y_axis_of_pix - 1
            current_checking_pix = (y_axis, x_axis)
            if current_checking_pix in self.original_selected_pixels:
                pixel_neighbour.add_neighbour(current_checking_pix)
            # 5th. condition check upper pixel is exist
            x_axis = x_axis_of_pix
            y_axis = y_axis_of_pix + 1
            current_checking_pix = (y_axis, x_axis)
            if current_checking_pix in self.original_selected_pixels:
                pixel_neighbour.add_neighbour(current_checking_pix)
            # 6th. condition check upper right pixel is exist
            x_axis = x_axis_of_pix + 1
            y_axis = y_axis_of_pix + 1
            current_checking_pix = (y_axis, x_axis)
            if current_checking_pix in self.original_selected_pixels:
                pixel_neighbour.add_neighbour(current_checking_pix)
            # 7th. condition check lower right pixel is exist
            x_axis = x_axis_of_pix + 1
            y_axis = y_axis_of_pix - 1
            current_checking_pix = (y_axis, x_axis)
            if current_checking_pix in self.original_selected_pixels:
                pixel_neighbour.add_neighbour(current_checking_pix)
            # 8th. condition check right pixel is exist
            x_axis = x_axis_of_pix + 1
            y_axis = y_axis_of_pix
            current_checking_pix = (y_axis, x_axis)
            if current_checking_pix in self.original_selected_pixels:
                pixel_neighbour.add_neighbour(current_checking_pix)

        list_of_pixels_with_neighbor_pixel_info.append(pixel_neighbour)

        return list_of_pixels_with_neighbor_pixel_info
