import io
from skimage import io
from skimage.transform import rescale
from skimage import color
from skimage import measure
from skimage.measure import regionprops
from skimage import feature
from skimage.morphology import disk, dilation
import os
import math
import cv2
from operator import attrgetter
import errno
import datetime
import shutil
import numpy as np
from matplotlib import pyplot as plt
from parameters import Parameters


class PeaUtils:

    def __init__(self):
        print('PeaUtils Created.')

    @staticmethod
    def get_unique(seq):
        seen = set()
        seen_add = seen.add
        return [x for x in seq if not (x in seen or seen_add(x))]

    @staticmethod
    def output_image_points_for_leaf_teeth(input_image, contour_tuples, index_list_a, index_list_b, output_suffix):
        """
        Outputs an image to file with points highlighted
        :param input_image: the input image to draw on.
        :param contour_tuples: the contour tuples giving xy coords.
        :param index_list_a: list a that indexes contour tuples.
        :param index_list_b: list b that indexes contour tuples.
        :param output_suffix: the suffix for the output (not including .jpg)
        :return: None
        """
        # open the input image.
        img = io.imread(input_image)
        # iterate through the indexes and add a circle point for each tuple.
        for i in index_list_a:
            cv2.circle(img, contour_tuples[i], 3, thickness=-1, color=(255, 0, 0))
        # iterate though the indexes and add a circle point for each tuple.
        for i in index_list_b:
            cv2.circle(img, contour_tuples[i], 3, thickness=-1, color=(0, 255, 0))
        # save the image.
        io.imsave(input_image + "." + output_suffix+".jpg", img)

    @staticmethod
    def show_leaf_teeth_distance_plot(title, x_label, y_label, distances, index_list_a, index_list_a_label,
                                      index_list_b, index_list_b_label):
        """
        Function to show a distance/position plot for leafteeth.
        :param index_list_b_label:
        :param index_list_a_label:
        :param title: the title of the plot.
        :param x_label: the label for the x axis.
        :param y_label: the label for the y axis.
        :param distances: the list of distances.
        :param index_list_a: a list of indexes into distances to plot points.
        :param index_list_b: a list of indexes into distances to plot points.
        :return: None
        """
        ###################################
        # Make calculations for the plot.
        ###################################
        # calculate the mean from distances.
        mean = np.mean(distances)
        # calculate the std deviation.
        stddev = np.std(distances)
        # calculate one std deviation above the mean.
        one_std_above = mean + stddev
        # calculate two std deviation above the mean.
        two_std_above = mean + (2 * stddev)
        # calculate one std deviation below the mean.
        one_std_below = mean - stddev
        # calculate two std deviation below the mean.
        two_std_below = mean - (2 * stddev)

        ###################################
        # Set up the plot graphic.
        ###################################
        fig1 = plt.figure(figsize=(15, 15))
        # add the sub plot to the figure.
        ax1 = fig1.add_subplot(111)
        # add the title and lables to the sub plot.
        ax1.set_title(title)
        ax1.set_ylabel(y_label)
        ax1.set_xlabel(x_label)

        ###################################
        # plot the data to the graphic.
        ###################################
        # plot the distances
        ax1.plot(distances)
        # plot the mean, one std dev and two std dev
        ax1.plot((0, len(distances) - 1), (mean, mean), linestyle='--', color='b', linewidth=1, label="mean")
        ax1.plot((0, len(distances) - 1), (one_std_above, one_std_above), linestyle=':', color='r', linewidth=1,
                 label="one std deviation")
        ax1.plot((0, len(distances) - 1), (two_std_above, two_std_above), linestyle=':', color='g', linewidth=1,
                 label="two std deviation")
        ax1.plot((0, len(distances) - 1), (one_std_below, one_std_below), linestyle=':', color='r', linewidth=1,
                 label="one std deviation")
        ax1.plot((0, len(distances) - 1), (two_std_below, two_std_below), linestyle=':', color='g', linewidth=1,
                 label="two std deviation")
        # plot the distances data points indexed by list_a.
        for i in index_list_a:
            ax1.plot(i, distances[i], 'b^', label=index_list_a_label)
        # plot the distances data points indexed by list_b.
        for i in index_list_b:
            ax1.plot(i, distances[i], 'r^', label=index_list_b_label)
        # add the legend
        handles, labels = fig1.gca().get_legend_handles_labels()
        new_labels, new_handles = [], []
        for handle, label in zip(handles, labels):
            if label not in new_labels:
                new_labels.append(label)
                new_handles.append(handle)
        fig1.legend(new_handles, new_labels)
        # ax1.legend(loc='upper right', shadow=True)
        # show the figure.
        fig1.show()

    @staticmethod
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    @staticmethod
    def point_within_bounding_box(min_row, min_col, max_row, max_col):
        if min_row > 100 and min_col > 100 and max_row < 600 and max_col < 380:
            return "true"

    @staticmethod
    def point_within_hardcode_bounding_box(width, height, min_x, min_y, max_x, max_y):

        min_x_percent_boundary = 14.1
        min_y_percent_boundary = 9.977
        max_x_percent_boundary = 74.957
        max_y_percent_boundary = 70.81
        min_x_boundary = (width/100.0)*min_x_percent_boundary
        min_y_boundary = (height/100.0)*min_y_percent_boundary
        max_x_boundary = (width/100.0)*max_x_percent_boundary
        max_y_boundary = (width/100.0)*max_y_percent_boundary

        if min_x > min_x_boundary and min_y > min_y_boundary and max_x < max_x_boundary and max_y < max_y_boundary:
            return "true"

        # if min_x > 175 and min_y > 175 and max_x < 925 and max_y < 1242:
        #    return "true"

    @staticmethod
    def copy_directory_structure(verbose, input_dir, temp_dir):
        """
        Function: copy contents of the input dir to a temp dir
        """
        if verbose:
            print "Copying directory structure to temp."
        input_top_level_directory = input_dir  # this variable needs to be assigned at runtime on cmd line
        directory_prefix = temp_dir  # this variable needs to be assigned at runtime via cmd line.
        top_dir = os.path.basename(input_top_level_directory)
        time_stamp = '{:_%m%d_%h%m%s}'.format(datetime.datetime.now())
        tmp_working_directory = directory_prefix + "/" + top_dir + "_" + time_stamp
        try:
            # shutil.copytree(src, dest, symlinks=false,
            # ignore=none, copy_function=shutil.copy2, ignore_dangling_symlinks=false)
            shutil.copytree(input_dir, tmp_working_directory)
        except OSError as e:  # if the error was caused because the source wasn't a directory
            if e.errno == errno.ENOTDIR:
                shutil.copy(input_dir, tmp_working_directory)
            else:
                print('directory not copied. error: %s' % e)
        return tmp_working_directory

    @staticmethod
    def get_file_path(in_suffix, in_path, extension):
        """
        Function: Makes a file path using the given inputs
        :param in_suffix: the suffix to the existing name e.g. L or A or B
        :param in_path: The full path to the file e.g. DIR/DIR/SOMETHING.A.B.C.jpg
        :param extension: e.g. .jpg or .pdf or .txt
        :return: e.g. DIR/DIR/SOMETHING.A.B.C.L.jpg
        """
        base_name = os.path.basename(in_path)
        base_path = os.path.dirname(in_path)
        file_name_without_extension = os.path.splitext(base_name)[0]
        name_out = file_name_without_extension + "." + in_suffix + extension
        path_out = base_path + "/" + name_out
        return name_out, path_out

    @staticmethod
    def show_two_images(image_object_a_title, image_object_b_title, image_object_a, image_object_b):
        """
        Function: Plot images before and after transformation. This must be a cv2 image (we think).
        :param image_object_a_title: The title for image a.
        :param image_object_b_title: The title for image b.
        :param image_object_a: the first image to be shown.
        :param image_object_b: the second image to be shown.
        """
        title_a = ""
        count = 0
        for c in image_object_a_title:
            title_a += c
            count += 1
            if count % 30 == 0:
                title_a += "\n"
        title_b = ""
        count = 0
        for c in image_object_b_title:
            title_b += c
            count += 1
            if count % 30 == 0:
                title_b += "\n"

        plt.subplot(121), plt.imshow(image_object_a.get_loaded_image()), plt.title(title_a)
        plt.subplot(122), plt.imshow(image_object_b.get_loaded_image()), plt.title(title_b)
        # TODO: move this to single image tmp
        img_path = Parameters.results + '/images/' + image_object_a_title + '_' + image_object_b_title + '.png'
        plt.savefig(Parameters.results + '/images/' + image_object_a_title + '_' + image_object_b_title + '.png')
        print "############# outputting lable image to: ", img_path

    @staticmethod
    def show_single_image(image_object_a_title, image_object_a):
        title_a = ""
        count = 0
        for c in image_object_a_title:
            title_a += c
            count += 1
            if count % 30 == 0:
                title_a += "\n"

        plt.subplot(111), plt.imshow(image_object_a.get_loaded_image()), plt.title(title_a)
        plt.show()

    @staticmethod
    def show_single_loaded_image(image_title, loaded_image):
        title_a = ""
        count = 0
        for c in image_title:
            title_a += c
            count += 1
            if count % 30 == 0:
                title_a += "\n"
        # 8 to 6 ratio
        plt.figure(figsize=(24, 18)), plt.imshow(loaded_image), plt.title(title_a)
        # plt.subplot(111), plt.imshow(loaded_image), plt.title(title_a)
        plt.show()

    # https://stackoverflow.com/questions/26690932/opencv-rectangle-with-dotted-or-dashed-lines
    @staticmethod
    def drawline(img, pt1, pt2, line_color, thickness=1, style='dotted', gap=8):
        dist = ((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2) ** .5
        pts = []
        for i in np.arange(0, dist, gap):
            r = i / dist
            x = int((pt1[0] * (1 - r) + pt2[0] * r) + .5)
            y = int((pt1[1] * (1 - r) + pt2[1] * r) + .5)
            p = (x, y)
            pts.append(p)

        if style == 'dotted':
            for p in pts:
                cv2.circle(img, p, thickness, line_color, -1)
        else:
            e = pts[0]
            i = 0
            for p in pts:
                s = e
                e = p
                if i % 2 == 1:
                    cv2.line(img, s, e, line_color, thickness)
                i += 1

    @staticmethod
    def draw_perpendicular_line(image, p1x, p1y, p2x, p2y, length, colour=(255, 0, 0), linesize=1):
        """
        Draws a line perpendicular to the line specified by the two points of p
        :param image: the image to draw the line on
        :param p1x: x coord of p1
        :param p1y: y coord of p1
        :param p2x: x coord of p2
        :param p2y: y coord of p2
        :param length: the length of the line to be drawn
        :param colour: the colour of the line to be drawn
        :param linesize: the width(size) of the line to be drawn
        """
        bx = p1x
        by = p1y
        ax = p2x
        ay = p2y
        # v.x = B.x - A.x;v.y = B.y - A.y
        vx = bx - ax
        vy = by - ay
        mag = math.sqrt(vx * vx + vy * vy)
        vx = vx / mag
        vy = vy / mag
        # temp = v.x; v.x = -v.y; v.y = temp;
        temp = vx
        vx = -vy
        vy = temp
        # C.x = B.x + v.x * length; C.y = B.y + v.y * length;
        cx = int(round(bx + vx * length))
        cy = int(round(by + vy * length))
        cv2.line(image, (bx, by), (cx, cy), colour, linesize)

    @staticmethod
    def get_extreme_points(contour):
        """
        Calculates the top,bottom,left and right extreme points
        :param contour: the contour to extract the extreme points from
        :return: 4 (x,y) tuples for top,bottom,left and right points
        """
        # find extreme left, right, top and bottom points.
        leftmost = tuple(contour[contour[:, :, 0].argmin()][0])
        rightmost = tuple(contour[contour[:, :, 0].argmax()][0])
        topmost = tuple(contour[contour[:, :, 1].argmin()][0])
        bottommost = tuple(contour[contour[:, :, 1].argmax()][0])
        return leftmost, rightmost, topmost, bottommost

    @staticmethod
    def draw_extreme_points(image, contour, circle_size=4, colour=(255, 0, 0)):
        """
        Calculates and draws the top,bottom,left and right extreme points
        :param image: the image to draw on.
        :param contour: the contour to extract the points from.
        :param colour: the colour of the points to be drawn
        :param circle_size: the size of the circle to be drawn
        """
        # leftmost = tuple(contour[contour[:, :, 0].argmin()][0])
        # rightmost = tuple(contour[contour[:, :, 0].argmax()][0])
        topmost = tuple(contour[contour[:, :, 1].argmin()][0])
        bottommost = tuple(contour[contour[:, :, 1].argmax()][0])
        cv2.circle(image, topmost, circle_size, colour)
        cv2.circle(image, bottommost, circle_size, colour)

    @staticmethod
    def get_static_region_convex_hulls(self):
        """
        work in progress for convex hulls - Note: may not work.
        :return:
        """
        path = self.path+".masked.jpg"
        img = io.imread(path)
        resized_img = rescale(img, 0.5)
        img_hsv = color.rgb2hsv(resized_img)
        img_hue = img_hsv[:, :, 0]
        edges_detection = feature.canny(color.rgb2gray(img_hue), sigma=3)
        dilation(edges_detection, disk(3))
        boolean_matrix_of_hue_values_above_median = img_hue > np.median(img_hue) * 0.925
        boolean_matrix_of_hue_values_above_median_not = np.logical_not(boolean_matrix_of_hue_values_above_median)
        regions = measure.label(boolean_matrix_of_hue_values_above_median_not, connectivity=2)
        regions_measured = regionprops(regions, intensity_image=img_hsv[:, :, 2])
        regions_measured_sorted = sorted(regions_measured, key=attrgetter('area'), reverse=True)
        # plt.subplot(111), plt.imshow(np.logical_xor(boolean_matrix_of_hue_values_above_median,
        #       dilated_edges)), "Edges"
        # plt.show()
        region = regions_measured_sorted[0]
        print region.convex_area
        print region.coords
        print region.perimeter
        blank_img = np.zeros((img_hue.shape[0], img_hue.shape[1]), dtype=np.uint8)
        tmp_img = blank_img.copy()
        ref_coord = region.coords.astype(int)
        tmp_img[ref_coord[:, 0], ref_coord[:, 1]] = 1
        # contours = measure.find_contours(tmp_img, 0.9)
        fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(15, 15))
        ax.imshow(resized_img)
        ax.plot(region.perimeter[:, 1], region.perimeter[:, 0], linewidth=3)
        plt.show()
