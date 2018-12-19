import matplotlib.pyplot as plt
import cv2
import numpy as np
import skimage as skimg
import plotly.plotly as py
import plotly.graph_objs as go
from skimage import io  # image I/O
from skimage.transform import rescale  # hsv converting
from rulermeasure import RulerMeasure
import seaborn as sns
import re
from matplotlib.pyplot import savefig
from shutil import copyfile
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import pandas as pd
import webbrowser
from parameters import Parameters
from configmaker import ConfigMaker
from htmlmaker import HtmlMaker
from skimage import color
from PIL import Image
from PIL import ImageDraw
import math
from scipy import signal
from scipy.signal import savgol_filter


class seed:
    def __init__(self, path):
        self.path = path
        self.config_file = ConfigMaker(self.path)
        self.hsv_jpg_file = ""
        self.mask_png_file = ""
        self.seed_labels_jpg_file = ""
        self.imposed_annotation_jpg_file = ""
        self.original_image_jpg_file = ""
        self.html_file = HtmlMaker(self.path)
        self.image_name = ""
        self.csv_string = ""
        # imagename,NumberofPeas,MeanAreaPixels,EqdMeanPixels,meanperimeterPixels
        self.numberofseeds = 0
        self.area_sum = 0
        self.area_mean = 0
        self.eqd_sum = 0
        self.eqd_mean = 0
        self.perimeter_sum = 0
        self.perimeter_mean = 0
        self.sum_max_mins = 0
        self.mean_max_mins = 0
        self.csv_file = Parameters.results + "/tables/workfile.csv"
        self.accession_workfile = ""
        self.csv_string_list = []
        self.pixels_per_cm = 0.0

    def seed_analyse(self):
        self.extract_image_ruler()
        self.pixels_per_cm = self.image_ruler.pixels_per_cm
        image_path_list = self.path.split("/")
        self.image_name = image_path_list[-1]
        self.csv_string = self.image_name + "\t"
        self.accession_workfile = Parameters.results + "/tables/" + self.image_name + "_workfile.csv"

        img = cv2.imread(self.path)

        # figure(figsize=(15,15))
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        print "Making hsv image."
        self.hsv_jpg_file = Parameters.results + "/images/"+self.image_name+"_hsv.jpg"
        cv2.imwrite(self.hsv_jpg_file, hsv)
        self.config_file.hsv_output_config_file(self.hsv_jpg_file)
        upper_green = np.array([35, 255, 255])
        lower_green = np.array([10, 100, 20])
        mask = cv2.inRange(hsv, lower_green, upper_green)

        res = cv2.bitwise_and(hsv, hsv, mask=mask)

        mask = cv2.bilateralFilter(mask, 15, 75, 75)
        print "Applying green mask_png_file."
        self.mask_png_file = Parameters.results + "/images/"+self.image_name+"_imagemask.png"
        cv2.imwrite(self.mask_png_file, mask)
        self.config_file.mask_output_config_file(self.mask_png_file)

        labels = skimg.measure.label(mask)
        len(labels)
        print "Creating labels for seeds."
        self.seed_labels_jpg_file = Parameters.results + "/images/"+self.image_name+"_labels.png"
        cv2.imwrite(self.seed_labels_jpg_file, labels)
        self.config_file.seed_labels_output_config_file(self.seed_labels_jpg_file)

        properties = skimg.measure.regionprops(labels)
        print len(properties)
        print "Showing original image."
        self.original_image_jpg_file = Parameters.results + "/images/"+self.image_name+"_img.png"
        cv2.imwrite(self.original_image_jpg_file, img)
        plt.figure(figsize=(10, 10))
        plt.imshow(img)
        self.config_file.original_image_jpg_output_config_file(self.original_image_jpg_file)
        clean_obj = []
        clean_obj_contours = [] #not used, but gives the contour for each of the seeds and could be useful later.
        max_mins_list = []
        eccentricity_list = []
        eccentricity_sum = 0.0
        counter = 0
        sum_max_min = 0
        im = Image.open(self.path)
        draw = ImageDraw.Draw(im)

        for p in properties:
            if p.area > 1000:
                if p.perimeter / p.equivalent_diameter < 5 and p.perimeter / p.equivalent_diameter > 3:
                    eccentricity_list.append(p.eccentricity)
                    eccentricity_sum += p.eccentricity
                    plt.annotate("%d" % (p.area,), xy=(p.centroid[1], p.centroid[0]))
                    plt.plot(p.centroid[1], p.centroid[0], 'o')
                    clean_obj.append(p)
                    reference_image = io.imread(self.path)
                    pea_hsv = color.rgb2hsv(reference_image)
                    pea_hue = pea_hsv[:, :, 0]
                    blank_img = np.zeros((pea_hue.shape[0], pea_hue.shape[1]), dtype=np.uint8)
                    leaf_tmp = blank_img.copy()  # also another array of zeros
                    ###########################################
                    #TESTING - ADDING CONTOURS
                    ref_coord = p.coords.astype(int)
                    for count, value in enumerate(p.coords):
                        leaf_tmp[value[0]][value[1]] = 255
                    #leaf_tmp[ref_coord[:, 0], ref_coord[:, 1]] = 255
                    tmp_path = Parameters.tmp_dir+"/"+self.image_name+".__" + str(counter) + ".jpg"
                    io.imsave(tmp_path, leaf_tmp)
                    counter += 1
                    contours = skimg.measure.find_contours(leaf_tmp, 0.8, fully_connected='high')
                    contours.sort(lambda x, y: cmp(len(x), len(y)))
                    #print "AREA: ", p.area
                    #for n, contour in enumerate(contours):
                    #    print "length Contour: ", len(contour)
                        #if len(contour) > 200:
                    contour = contours[-1]
                    clean_obj_contours.append(contour)
                    #print "length Contour: ", len(contour)
                    distances = []
                    for m, point in enumerate(contour):
                        tuple = (int(point[1]),int(point[0]))
                        im.putpixel(tuple, (0,255,0,255))
                        distance = math.sqrt(math.pow(tuple[0] - p.centroid[0], 2) + math.pow(tuple[1] - p.centroid[1], 2))
                        distances.append(distance)
                    #maximums = seed.get_maximum_points_on_contour(distances, 10)
                    #minimus = seed.get_minimum_points_on_contour(distances, 10)
                    position = []
                    for i, value in enumerate(contour):
                        position.append(i)
                    yhat = savgol_filter(distances, 67, 8, mode="nearest")  # window size 51, polynomial order 3
                    maximums = signal.argrelmax(np.asarray(yhat))
                    minimums = signal.argrelmin(np.asarray(yhat))
                    max_min = (len(maximums) + len(minimums))
                    sum_max_min += max_min
                    max_mins_list.append(max_min)
                    #print "len max: ", len(maximums)
                    #print "len max: ", len(minimums)
                    plt.figure(num=None, figsize=(18, 18), dpi=80, facecolor='w', edgecolor='k')
                    plt.subplot(211)
                    plt.plot(position, distances, 'y-')
                    plt.plot(position, yhat, 'g-')
                    plt.xlabel("position on contour")
                    plt.ylabel("distance from centroid")
                    plt.title("pea contour plot")
                    for m, value in enumerate(maximums[0]):
                        #print "value:",value
                        plt.plot(position[value], distances[value], 'ro')
                        x = int(contour[value][1])
                        y = int(contour[value][0])
                        r = 2
                        #im.putpixel(max, (0, 0, 255, 255))
                        draw.ellipse((x - r, y - r, x + r, y + r), fill=(255, 0, 0, 255))
                    for m, value in enumerate(minimums[0]):
                        #print "value: ", value
                        plt.plot(position[value], distances[value], 'bo')
                        x = int(contour[value][1])
                        y = int(contour[value][0])
                        r = 2
                        #im.putpixel(max, (0, 0, 255, 255))
                        draw.ellipse((x - r, y - r, x + r, y + r), fill=(0, 0, 255, 255))
                    plt.savefig(Parameters.tmp_dir +"/"+self.image_name+".pea_plot."+str(counter)+".png", bbox_inches='tight')
                    draw.ellipse((p.centroid[1] - r, p.centroid[0] - r, p.centroid[1] + r, p.centroid[0] + r), fill=(255, 0, 0, 255))

        if counter == 0:
            return self.image_name + ",empty,,,,,,,,,\n"
        self.mean_max_mins = sum_max_min / counter
        im.save(Parameters.tmp_dir+"/"+self.image_name+".with_contours.jpg")
        plt.xlim((0, img.shape[1]))
        plt.ylim((img.shape[0], 0))
        print "Imposing annotation onto image."
        self.imposed_annotation_jpg_file = Parameters.results + "/images/"+self.image_name+"_imposed.png"
        plt.savefig(self.imposed_annotation_jpg_file, bbox_inches=None)
        self.config_file.imposed_annotation_output_config_file(self.imposed_annotation_jpg_file)
        # Descriptive stats
        self.numberofseeds = str(len(clean_obj))

        # print "Number of peas found: \t%d" %(len(clean_obj), )
        # print "Mean pea size: \t\t%.2f" %(np.array([p.area for p in clean_obj]).mean(), )
        # print "Sd for mean pea size: \t%.2f" %(np.array([p.area for p in clean_obj]).std(), )
        #
        # print "The median is %f" % (np.median(np.array([p.area for p in clean_obj])))
        # print "The maximum is %f" % (np.max(np.array([p.area for p in clean_obj])))
        # print "The minimum is %f" % (np.min(np.array([p.area for p in clean_obj])))
        # draw violin plot
        rep_area = [p.area for p in clean_obj]
        rep_eqd = [p.equivalent_diameter for p in clean_obj]
        rep_perimeter = [p.perimeter for p in clean_obj]
        rep_centroid = [p.centroid for p in clean_obj]
        #####
        self.html_file.accession_area_pixel_maker(rep_area, self.image_name)
        self.html_file.accession_eqd_pixel_maker(rep_eqd,self.image_name)
        self.html_file.accession_perimeter_pixel_maker(rep_perimeter, self.image_name)
        #####################
        # Create averages for each
        #####################
        for i in rep_area:
            self.area_sum = float(self.area_sum) + float(i)
        self.area_mean = self.area_sum / float(self.numberofseeds)
        self.area_mean = str(self.area_mean)

        for i in rep_eqd:
            self.eqd_sum = float(self.eqd_sum) + float(i)
        self.eqd_mean = self.eqd_sum / float(self.numberofseeds)
        self.eqd_mean = str(self.eqd_mean)

        for i in rep_perimeter:
            self.perimeter_sum = float(self.perimeter_sum) + float(i)
        self.perimeter_mean = self.perimeter_sum / float(self.numberofseeds)
        self.perimeter_mean = str(self.perimeter_mean)
        #####################
        # create a table (1 accession, all seeds)
        #####################
        workfile = open(self.accession_workfile, "w")

        workfile.write("Perimeter,Area,Equivalent Diameter,max_mins, eccentricity\n")
        for i in range(len(clean_obj)):
            seed_string = str(rep_perimeter[i]) + "," + str(rep_area[i]) + "," + str(rep_eqd[i]) + "," + str(max_mins_list[i]) + "," + str(eccentricity_list[i])
            workfile.write(seed_string)
            workfile.write("\n")
        workfile.close()
        df = pd.read_csv(self.accession_workfile, sep=",")
        df.index = np.arange(1, len(df) + 1)
        seed_table = df.to_html(justify='left')
        list_seed_table = seed_table.split('\n')
        del list_seed_table[0]
        del list_seed_table[-1]
        seed_table = "\n".join(list_seed_table)

        self.html_file.accession_seed_table_file_maker(seed_table, self.image_name)

        self.html_file.accession_method_html_maker(self.original_image_jpg_file, self.hsv_jpg_file, self.mask_png_file,
                                                   self.seed_labels_jpg_file, self.imposed_annotation_jpg_file,self.image_name)
        print "Printing csv string for this accession: ", self.image_name

        one_over_pix_per_cm = float(1.0 / float(self.pixels_per_cm))
        area_mean_cm = float(self.area_mean) * one_over_pix_per_cm * one_over_pix_per_cm
        eqd_mean_cm = float(self.eqd_mean) / float(self.pixels_per_cm)
        perimeter_mean_cm = float(self.perimeter_mean) / float(self.pixels_per_cm)
        ecc_mean = float(eccentricity_sum) / counter
        self.csv_string = self.image_name + "," + \
                          self.numberofseeds + "," + \
                          self.area_mean + "," + \
                          self.eqd_mean + "," + \
                          self.perimeter_mean + "," + \
                          str(self.mean_max_mins) + "," + \
                          str(self.pixels_per_cm) + "," + \
                          str(area_mean_cm) + "," + \
                          str(eqd_mean_cm) + "," + \
                          str(perimeter_mean_cm) + "," + \
                          str(ecc_mean) + "\n"
        return self.csv_string

    def extract_image_ruler(self):
        print "extract_image_ruler: ", self.path
        reference_image = io.imread(self.path)
        resized_image_ruler = rescale(reference_image, 0.5, mode='constant')  # 50% more pixels
        image_path_list = self.path.split("/")
        image_name = image_path_list[-1]
        dst = Parameters.tmp_dir + "/" + image_name
        io.imsave(dst, resized_image_ruler)
        self.image_ruler = RulerMeasure(dst, self.config_file)
        # add success for this process to the config
        #self.config_file.resizedforruler_output_config_file(self.path + ".resizedforruler.jpg")
        self.image_ruler.process_ruler()

