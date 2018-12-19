from PIL import Image
import cv2
import numpy as np
from scipy.stats import mode
from collections import Counter
from imageutils import ImageUtils

class RulerMeasure:
    def __init__(self, image_path, config):
        self.pixels_per_cm = ""
        self.horizontal_boundary_coordinates_tuples = []
        self.horizontal_boundary_x = ""
        self.horizontal_boundary_y = ""
        self.black_tuple = (0, 0, 0)
        self.background_tuple = ""
        self.green_tuple = (0, 255, 0)
        self.image_width_pixels = ""
        self.image_height_pixels = ""
        self.image_path = image_path
        self.static_feature_masked_image_path = ""
        self.line_segmented_ruler_image = ""
        self.colour_boundaries = ""
        self.DEBUG = True
        self.config_file = config

    def process_ruler(self):
        self.get_horizontal_ruler_boundary_x()
        print "########## BOUNDARY x ########", self.horizontal_boundary_x
        self.get_boundary_y()
        print "########## BOUNDARY y ########", self.horizontal_boundary_y
        self.line_segmenter()

    @staticmethod
    def upper_bound(number):
        """
        Function: Bounds input number to a max of 255
        :return: number or 255 (whatever is lower)
        """
        if number > 255:
            return 255
        else:
            return number

    @staticmethod
    def lower_bound(number):
        """
        Function: Bounds input number to min of 0
        :return: 0 or number (whatever is greater)
        """
        if number < 0:
            return 0
        else:
            return number

    def get_image_dimensions(self):
        """
        Function: Get dimension of image
        :return: img_width, img_height
        """
        if self.image_width_pixels == "":
            img = Image.open(self.image_path)
            img_dimension = img.size
            self.image_width_pixels = img_dimension[0]
            self.image_height_pixels = img_dimension[1]
        return self.image_width_pixels, self.image_height_pixels

    def get_background_colour_tuple(self):
        """
        Function: Obtains background colour tuple
        :return:
        """
        if self.background_tuple == "":
            img = Image.open(self.image_path)
            img_width = self.get_image_dimensions()[0]
            img_height = self.get_image_dimensions()[1]
            colours = []
            count = 0
            for y in range(img_height):
                count += 1
                for x in range(img_width):
                    c = img.getpixel((x, y))
                    colours.append(c)
            data = Counter(colours)
            most_common_list = data.most_common(2)
            background_colour_tuple = most_common_list[1]
            self.background_tuple = background_colour_tuple[0]
        return self.background_tuple

    def get_background_colour_r(self):
        return self.get_background_colour_tuple()[0]

    def get_background_colour_g(self):
        return self.get_background_colour_tuple()[1]

    def get_background_colour_b(self):
        return self.get_background_colour_tuple()[2]

    def get_colour_boundaries(self):
        """
        Function: Creates upper and lower colours for each RGB channel
        :return: self.colour_boundaries
        """
        if self.colour_boundaries == "":
            ur = self.get_background_colour_r() + 10
            ug = self.get_background_colour_g() + 10
            ub = self.get_background_colour_b() + 10
            lr = self.get_background_colour_r() - 10
            lg = self.get_background_colour_g() - 10
            lb = self.get_background_colour_b() - 10
            upper_blue_r = self.upper_bound(ur)
            upper_blue_g = self.upper_bound(ug)
            upper_blue_b = self.upper_bound(ub)
            lower_blue_r = self.lower_bound(lr)
            lower_blue_g = self.lower_bound(lg)
            lower_blue_b = self.lower_bound(lb)

            self.colour_boundaries = [ ([240, 227, 160], [255, 247, 190]) ]
            #self.colour_boundaries = [
            #    ([lower_blue_b, lower_blue_g, lower_blue_r], [upper_blue_b, upper_blue_g, upper_blue_r])
            #]
        return self.colour_boundaries

    def get_static_feature_masked_image(self):
        """
        Function: Makes masked image using colour boundaries and saves it.
        """
        #############################################
        #frame = cv2.imread(self.image_path)
        ## Convert BGR to HSV
        #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        ## define range of blue color in HSV
        #lower_blue = np.array([100, 150, 0])
        #upper_blue = np.array([140, 255, 255])
        ## Threshold the HSV image to get only blue colors
        #mask = cv2.inRange(hsv, lower_blue, upper_blue)
        #cv2.imwrite(self.image_path + ".BLUE_MASK.jpg", mask)
        ## Bitwise-AND mask and original image
        #res = cv2.bitwise_and(frame, frame, mask=mask)

        if self.static_feature_masked_image_path == "":
            img_imread = cv2.imread(self.image_path)
            for (lower, upper) in self.get_colour_boundaries():
                # create NumPy arrays from the boundaries
                lower = np.array(lower, dtype="uint8")
                upper = np.array(upper, dtype="uint8")
                # find the colors within the specified boundaries and apply
                # the mask
                mask = cv2.inRange(img_imread, lower, upper)
                output = cv2.bitwise_and(img_imread, img_imread, mask=mask)
                # show the images
                self.static_feature_masked_image_path = self.image_path + ".masked.jpg"
                cv2.imwrite(self.static_feature_masked_image_path, output)
        return self.static_feature_masked_image_path

    def get_horizontal_ruler_boundary_x(self):
        """
        Function: Find the boundary of the x axis
        :return:
        """
        if self.horizontal_boundary_x == "":
            #img = Image.open(self.get_static_feature_masked_image())
            ## find the boundary of the ruler on the x axis
            #start_y = 100
            #end_y = 200
            #count_y = 0
            #ruler_x_boundary = []
            ## this loop travels across
            #for y in range(0, self.get_image_dimensions()[0]-1):
            #    count_y += 1
            #    # noinspection PyChainedComparisons
            #    if count_y > start_y and count_y < end_y:
            #        buffer_line = 10
            #        for x in range(0, self.get_image_dimensions()[1]-1):
            #            c = img.getpixel((x, y))
            #            if c == self.black_tuple:
            #                pass
            #            else:
            #                buffer_line -= 1
            #                img.putpixel((x, y), self.green_tuple)
            #                if buffer_line == 0:
            #                    ruler_x_boundary.append(x)
            #                    # here is our end of line coordinates. for the x
            #                    break
            ##self.horizontal_boundary_x = max(ruler_x_boundary)
        #return self.horizontal_boundary_x
            self.horizontal_boundary_x = 670
        return self.horizontal_boundary_x

    def get_boundary_y(self):
        """
        Function: Find y boundary
        :return:
        """
        if self.horizontal_boundary_y == "":
            img = Image.open(self.get_static_feature_masked_image())
            # find the boundary of the ruler on the y axis
            start_y = 50
            start_x = self.get_horizontal_ruler_boundary_x()/2
            end_x = start_x+100
            count_x = 0
            ruler_y_boundary = []
            # this loop travels across
            for x in range(self.get_image_dimensions()[0]):
                count_x += 1
                # noinspection PyChainedComparisons
                if count_x > start_x and count_x < end_x:
                    buffer_line = 10
                    count_y = 0
                    for y in range(self.get_image_dimensions()[1]):
                        count_y += 1
                        if count_y > start_y:
                            c = img.getpixel((x, y))
                            if c == self.black_tuple:
                                pass
                            else:
                                buffer_line -= 1
                                img.putpixel((x, y), self.green_tuple)
                                if buffer_line == 0:
                                    ruler_y_boundary.append(y)
                                    # here is our end of line coordinates. for the x
                                    break

            #self.horizontal_boundary_y = max(ruler_y_boundary)
            self.horizontal_boundary_y = 170
            img.save(self.image_path + ".masked.ruler_segmented.testing.jpg")
        return self.horizontal_boundary_y

    def line_segmenter(self):
        assert isinstance(self.image_path, object)
        original_image = Image.open(self.image_path)
        # TODO: circular dependancy with pea image
        greyscale_gaussian_otsus_image = ImageUtils.get_grayscale_gaussian_otsus_image_copy(self.image_path, self.config_file)
        img = Image.open(greyscale_gaussian_otsus_image.path)
        img_width = self.get_image_dimensions()[0]
        img_height = self.get_image_dimensions()[1]
        # this loop travels across
        line_segments = []
        line_segment_length_list = []
        put_pixel_green = True
        short_line_segment_length_list = []
        short_line_segments = []
        for y in range(img_height):
            if y > int(self.horizontal_boundary_y):
                break
            start_line_segment_pixel_colour = img.getpixel((0, y))
            start_line_segment_pixel_coord = (0, y)
            for x in range(img_width):
                current_line_segment_pixel_colour = img.getpixel((x, y))
                if not current_line_segment_pixel_colour == start_line_segment_pixel_colour:
                    length_segment = x - start_line_segment_pixel_coord[0]
                    # TODO: change magic number to a parameter, the magic number is the minimum length of line segment
                    if length_segment > 25:
                        line_segment_length_list.append(length_segment)
                        line_segments.append(
                            ([start_line_segment_pixel_coord[0], start_line_segment_pixel_coord[1]], [x, y]))
                    else:
                        short_line_segment_length_list.append(length_segment)
                        short_line_segments.append(
                            ([start_line_segment_pixel_coord[0], start_line_segment_pixel_coord[1]], [x, y]))
                    start_line_segment_pixel_colour = img.getpixel((x, y))
                    start_line_segment_pixel_coord = (x, y)
                    if put_pixel_green:
                        put_pixel_green = False
                    else:
                        put_pixel_green = True
                if put_pixel_green:
                    original_image.putpixel((x, y), self.green_tuple)
                else:
                    original_image.putpixel((x, y), self.black_tuple)
                if x > int(self.horizontal_boundary_x):
                    break
        self.pixels_per_cm = (mode(line_segment_length_list)[0][0] * 2) + 2 # multiplied by 2 to account for rescale and +2pix for cm tick mark allowance
        print "Pixels per cm: ", self.pixels_per_cm
        original_image.save(self.image_path + ".masked.ruler_segmented.jpg")
