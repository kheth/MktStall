from parameters import Parameters
import pandas as pd
import seaborn as sns
import re
from matplotlib.pyplot import savefig
import matplotlib.pyplot as plt
import numpy as np
from configmaker import ConfigMaker

class HtmlMaker:

    def __init__(self, config):
        self.images = []
        self.config_file = ConfigMaker(Parameters.results + "/summary_output.config")

    def make_html(self, out_dir, images):
        """ Making SUMMARY Table """
        # open tsv file
        f_tsv = open(Parameters.results + '/tables/workfile.tsv', "r")
        # make new html
        f = open(Parameters.results + "/html/html_summary_table.html", 'w')
        # read tsv as thml
        tsv_data_to_html = pd.read_table(f_tsv, "\t")
        html_table = tsv_data_to_html.to_html()

        my_html_table_list = html_table.split("\n")

        # substitute lines in table
        table_index = my_html_table_list.index("<table border=\"1\" class=\"dataframe\">")
        my_html_table_list[table_index] = "<table class=\"table table-striped results\">"

        header_string = "<tr style=\"text-align: right;\">"
        sub_str = [s for s in my_html_table_list if header_string in s]
        new_sub_str = str(sub_str[0])
        table_index = my_html_table_list.index(new_sub_str)
        my_html_table_list[table_index] = "<tr style=\"text-align: left;\">"

        header_string = "<th>Area_cm2</th>"
        sub_str = [s for s in my_html_table_list if header_string in s]
        new_sub_str = str(sub_str[0])
        table_index = my_html_table_list.index(new_sub_str)
        my_html_table_list[table_index] = "<th>Area cm<sup>2</sup></th>"

        header_string = "<th>Length_cm</th>"
        sub_str = [s for s in my_html_table_list if header_string in s]
        new_sub_str = str(sub_str[0])
        table_index = my_html_table_list.index(new_sub_str)
        my_html_table_list[table_index] = "<th>Length cm</th>"

        header_string = "<th>Width_cm</th>"
        sub_str = [s for s in my_html_table_list if header_string in s]
        new_sub_str = str(sub_str[0])
        table_index = my_html_table_list.index(new_sub_str)
        my_html_table_list[table_index] = "<th>Width cm</th>"

        header_string = "<th>Perimeter_cm</th>"
        sub_str = [s for s in my_html_table_list if header_string in s]
        new_sub_str = str(sub_str[0])
        table_index = my_html_table_list.index(new_sub_str)
        my_html_table_list[table_index] = "<th>Perimeter cm</th>"

        joined_table = '\n'.join(my_html_table_list)

        # open index html
        # my_html_test_doc = []
        f2 = open("../resources/html/index_summary.html", "r")
        my_html_test_doc = f2.read().split('\n')
        # substitute lines in html doc
        html_index = my_html_test_doc.index("THIS IS TABLE")
        my_html_test_doc[html_index] = joined_table

        html_index = my_html_test_doc.index("<link href=\"bootstrap.min.css\" rel=\"stylesheet\">")
        bootstrap_string = "<link href=\"" + Parameters.resources + "/css/bootstrap.min.css\" rel=\"stylesheet\">"
        my_html_test_doc[html_index] = bootstrap_string

        html_index = my_html_test_doc.index("<link href=\"dashboard.css\" rel=\"stylesheet\">")
        dashboard_string = "<link href=\"" + Parameters.resources + "/css/dashboard.css\" rel=\"stylesheet\">"
        my_html_test_doc[html_index] = dashboard_string

        str_for_html = "\n".join(my_html_test_doc)
        f.write(str_for_html)

        # close
        f.close()
        f2.close()
        # f_tsv.close()
        # open
        filename = 'file://' + Parameters.results + "/html/html_summary_table.html"

        # add success for this process to the config
        self.config_file.html_summary_output_config_file(Parameters.results + "/html/html_summary_table.html")
        """ Making Summary Plots Pixels """
        # TODO: MAKE PATHS RELEATIVE!!!!!!
        f_plot_pixel = open(Parameters.results + '/html/html_summary_plot_pixels_morphological.html', 'w')
        my_html_test_doc_plot_pixels = []
        f1_p = open('../resources/html/index_plot_leaf_morphological_pixels.html', "r")
        my_html_test_doc_plot_pixels = f1_p.read().split('\n')
        # print tsv_data_to_html
        # violin plot data entry PIXELS
        # length
        length = tsv_data_to_html["Length"].tolist()
        string_length_array = "var x14=[length]"
        html_index = my_html_test_doc_plot_pixels.index(string_length_array)
        my_html_test_doc_plot_pixels[html_index] = "var x14=%s" % length
        #####################
        print "Adding length pixels boxplot to config file."
        pos = [1]
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(20, 20))
        plt.figure()
        plt.xlabel("Major axis length (length) in Pixels")
        plt.boxplot(length, 0, 'rs', 0)
        boxplot_path_length_pixels = Parameters.results + "/images/plot_length_pixels.png"
        savefig(boxplot_path_length_pixels)
        self.config_file.length_pixels_boxplot_output_config_file(boxplot_path_length_pixels)
        #####################
        # width
        width = tsv_data_to_html["Width"].tolist()
        string_width_array = "var x13=[width]"
        html_index = my_html_test_doc_plot_pixels.index(string_width_array)
        my_html_test_doc_plot_pixels[html_index] = "var x13=%s" % width
        #####################
        print "Adding width pixels boxplot to config file."
        pos = [1]
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(20, 20))
        plt.figure()
        plt.xlabel("Minor axis length (width) in Pixels")
        plt.boxplot(width, 0, 'rs', 0)
        boxplot_path_width_pixels = Parameters.results + "/images/plot_width_pixels.png"
        savefig(boxplot_path_width_pixels)
        self.config_file.width_pixels_boxplot_output_config_file(boxplot_path_width_pixels)

        #####################
        # area
        area = tsv_data_to_html["Area"].tolist()
        string_area_array = "var x12=[area]"
        html_index = my_html_test_doc_plot_pixels.index(string_area_array)
        my_html_test_doc_plot_pixels[html_index] = "var x12=%s" % area
        #####################
        print "Adding area pixels boxplot to config file."
        pos = [1]
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(20, 20))
        plt.figure()
        plt.xlabel("Area in Pixels")
        plt.boxplot(area, 0, 'rs', 0)
        boxplot_path_area_pixels = Parameters.results + "/images/plot_area_pixels.png"
        savefig(boxplot_path_area_pixels)
        self.config_file.area_pixels_boxplot_output_config_file(boxplot_path_area_pixels)

        #####################
        # perimeter
        perimeter = tsv_data_to_html["Perimeter"].tolist()
        string_perimeter_array = "var x11=[perimeter]"
        html_index = my_html_test_doc_plot_pixels.index(string_perimeter_array)
        my_html_test_doc_plot_pixels[html_index] = "var x11=%s" % perimeter
        #####################
        print "Adding perimeter pixels boxplot to config file."
        pos = [1]
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(20, 20))
        plt.figure()
        plt.xlabel("Perimeter in Pixels")
        plt.boxplot(perimeter, 0, 'rs', 0)
        boxplot_path_perimeter_pixels = Parameters.results + "/images/plot_perimeter_pixels.png"
        savefig(boxplot_path_perimeter_pixels)
        self.config_file.perimeter_pixels_boxplot_output_config_file(boxplot_path_perimeter_pixels)

        #####################
        html_index = my_html_test_doc_plot_pixels.index("<link href=\"bootstrap.min.css\" rel=\"stylesheet\">")
        bootstrap_string = "<link href=\"" + Parameters.resources + "/css/bootstrap.min.css\" rel=\"stylesheet\">"
        my_html_test_doc_plot_pixels[html_index] = bootstrap_string

        html_index = my_html_test_doc_plot_pixels.index("<link href=\"dashboard.css\" rel=\"stylesheet\">")
        dashboard_string = "<link href=\"" + Parameters.resources + "/css/dashboard.css\" rel=\"stylesheet\">"
        my_html_test_doc_plot_pixels[html_index] = dashboard_string

        str_for_html = "\n".join(my_html_test_doc_plot_pixels)
        f_plot_pixel.write(str_for_html)
        f_plot_pixel.close()
        f1_p.close()
        filename_plot = 'file://' + Parameters.results + '/html/html_summary_plot_pixels_morphological.html'

        # add success for this process to the config
        self.config_file.html_plot_pixels_morphological_output_config_file(Parameters.results + '/html/html_summary_plot_pixels_morphological.html')

        f_plot_pixel = open(Parameters.results + '/html/html_summary_plot_pixels_eqs.html', 'w')
        my_html_test_doc_plot_pixels = []
        f2_p = open('../resources/html/index_plot_leaf_eq_pixels.html', "r")
        my_html_test_doc_plot_pixels = f2_p.read().split('\n')

        equivalent_diameter = tsv_data_to_html["Equivalent Diameter"].tolist()
        string_equivalentdiameter_array = "var x9=[equivalentdiameter]"
        html_index = my_html_test_doc_plot_pixels.index(string_equivalentdiameter_array)
        my_html_test_doc_plot_pixels[html_index] = "var x9=%s" % equivalent_diameter

        html_index = my_html_test_doc_plot_pixels.index("<link href=\"bootstrap.min.css\" rel=\"stylesheet\">")
        bootstrap_string = "<link href=\"" + Parameters.resources + "/css/bootstrap.min.css\" rel=\"stylesheet\">"
        my_html_test_doc_plot_pixels[html_index] = bootstrap_string

        html_index = my_html_test_doc_plot_pixels.index("<link href=\"dashboard.css\" rel=\"stylesheet\">")
        dashboard_string = "<link href=\"" + Parameters.resources + "/css/dashboard.css\" rel=\"stylesheet\">"
        my_html_test_doc_plot_pixels[html_index] = dashboard_string

        str_for_html = "\n".join(my_html_test_doc_plot_pixels)
        f_plot_pixel.write(str_for_html)
        f_plot_pixel.close()
        f2.close()
        filename_plot = 'file://' + Parameters.results + '/html/html_summary_plot_pixels_eqs.html'

        # add success for this process to the config
        self.config_file.html_summary_plot_pixels_eqs_output_config_file(Parameters.results + '/html/html_summary_plot_pixels_eqs.html')
        #####################
        print "Adding equivalent diameter pixels boxplot to config file."
        pos = [1]
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(20, 20))
        plt.figure()
        plt.xlabel("Equivalent Diameter in Pixels")
        plt.boxplot(equivalent_diameter, 0, 'rs', 0)
        boxplot_path_eqd_pixels = Parameters.results + "/images/plot_eqd_pixels.png"
        savefig(boxplot_path_eqd_pixels)
        self.config_file.perimeter_pixels_boxplot_output_config_file(boxplot_path_eqd_pixels)

        #####################

        """ Making Summary plot CM """
        ###########
        # CM PLOTS
        f_plot_leaf_morphological_cm = open(Parameters.results + '/html/html_summary_plot_leaf_morphological_cm.html',
                                            'w')
        f3 = open('../resources/html/index_plot_leaf_morphological_cm.html', "r")
        my_html_test_doc_plot_cm = f3.read().split('\n')
        # violin plot data entry CM
        # length
        length_cm = tsv_data_to_html["Length_cm"].tolist()
        string_length_array = "var x14=[length]"
        html_index = my_html_test_doc_plot_cm.index(string_length_array)
        my_html_test_doc_plot_cm[html_index] = "var x14=%s" % length_cm
        #####################
        print "Adding length cm boxplot to config file."
        pos = [1]
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(20, 20))
        plt.figure()
        plt.xlabel("Major Axis Length (length) in Centimeters")
        plt.boxplot(length_cm, 0, 'rs', 0)
        boxplot_path_length_cm = Parameters.results + "/images/plot_length_cm.png"
        savefig(boxplot_path_length_cm)
        self.config_file.length_cm_boxplot_output_config_file(boxplot_path_length_cm)

        #####################
        # width
        width_cm = tsv_data_to_html["Width_cm"].tolist()
        string_width_array = "var x13=[width]"
        html_index = my_html_test_doc_plot_cm.index(string_width_array)
        my_html_test_doc_plot_cm[html_index] = "var x13=%s" % width_cm
        #####################
        print "Adding width cm boxplot to config file."
        pos = [1]
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(20, 20))
        plt.figure()
        plt.xlabel("Minor Axis Length (Width) in Centimeters")
        plt.boxplot(width_cm, 0, 'rs', 0)
        boxplot_path_width_cm = Parameters.results + "/images/plot_width_cm.png"
        savefig(boxplot_path_width_cm)
        self.config_file.width_cm_boxplot_output_config_file(boxplot_path_width_cm)

        #####################
        # area
        area_cm = tsv_data_to_html["Area_cm2"].tolist()
        string_area_array = "var x12=[area]"
        html_index = my_html_test_doc_plot_cm.index(string_area_array)
        my_html_test_doc_plot_cm[html_index] = "var x12=%s" % area_cm
        #####################
        print "Adding area cm boxplot to config file."
        pos = [1]
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(20, 20))
        plt.figure()
        plt.xlabel("Area in Centimeters")
        plt.boxplot(area_cm, 0, 'rs', 0)
        boxplot_path_area_cm = Parameters.results + "/images/plot_area_cm.png"
        savefig(boxplot_path_area_cm)
        self.config_file.area_cm_boxplot_output_config_file(boxplot_path_area_cm)

        #####################
        # perimeter
        perimeter_cm = tsv_data_to_html["Perimeter_cm"].tolist()
        string_perimeter_array = "var x11=[perimeter]"
        html_index = my_html_test_doc_plot_cm.index(string_perimeter_array)
        my_html_test_doc_plot_cm[html_index] = "var x11=%s" % perimeter_cm
        #####################
        print "Adding perimeter cm boxplot to config file."
        pos = [1]
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(20, 20))
        plt.figure()
        plt.xlabel("Perimeter in Centimeters")
        plt.boxplot(perimeter_cm, 0, 'rs', 0)
        boxplot_path_perimeter_cm = Parameters.results + "/images/plot_perimeter_cm.png"
        savefig(boxplot_path_perimeter_cm)
        self.config_file.perimeter_cm_boxplot_output_config_file(boxplot_path_perimeter_cm)

        #####################
        html_index = my_html_test_doc_plot_cm.index("<link href=\"bootstrap.min.css\" rel=\"stylesheet\">")
        bootstrap_string = "<link href=\"" + Parameters.resources + "/css/bootstrap.min.css\" rel=\"stylesheet\">"
        my_html_test_doc_plot_cm[html_index] = bootstrap_string

        html_index = my_html_test_doc_plot_cm.index("<link href=\"dashboard.css\" rel=\"stylesheet\">")
        dashboard_string = "<link href=\"" + Parameters.resources + "/css/dashboard.css\" rel=\"stylesheet\">"
        my_html_test_doc_plot_cm[html_index] = dashboard_string

        str_for_html = "\n".join(my_html_test_doc_plot_cm)
        f_plot_leaf_morphological_cm.write(str_for_html)
        f_plot_leaf_morphological_cm.close()
        f3.close()

        filename_plot_cm = 'file://' + Parameters.results + '/html/html_summary_plot_leaf_morphological_cm.html'

        # add success for this process to the config
        self.config_file.html_summary_plot_leaf_morphological_cm_output_config_file(Parameters.results + '/html/html_summary_plot_leaf_morphological_cm.html')

        # TODO: make pixel morphological and eqd
        # TODO: add label to the end of this all files
        ##############################
        f_plot_leaf_teeth = open(Parameters.results + '/html/html_summary_plot_leaf_teeth.html', 'w')
        f4 = open('../resources/html/index_plot_leaf_teeth.html', "r")
        my_html_test_doc_plot_cm = f4.read().split('\n')

        number_of_teeth = tsv_data_to_html["NumberofTeeth"].tolist()
        string_number_of_teeth_array = "var x10=[numberofteeth]"
        html_index = my_html_test_doc_plot_cm.index(string_number_of_teeth_array)
        my_html_test_doc_plot_cm[html_index] = "var x10=%s" % number_of_teeth

        html_index = my_html_test_doc_plot_cm.index("<link href=\"bootstrap.min.css\" rel=\"stylesheet\">")
        bootstrap_string = "<link href=\"" + Parameters.resources + "/css/bootstrap.min.css\" rel=\"stylesheet\">"
        my_html_test_doc_plot_cm[html_index] = bootstrap_string

        html_index = my_html_test_doc_plot_cm.index("<link href=\"dashboard.css\" rel=\"stylesheet\">")
        dashboard_string = "<link href=\"" + Parameters.resources + "/css/dashboard.css\" rel=\"stylesheet\">"
        my_html_test_doc_plot_cm[html_index] = dashboard_string

        str_for_html = "\n".join(my_html_test_doc_plot_cm)
        f_plot_leaf_teeth.write(str_for_html)
        f_plot_leaf_teeth.close()
        f4.close()

        filename_plot_cm = 'file://' + Parameters.results + '/html/html_summary_plot_leaf_teeth.html'
        # add success for this process to the config
        self.config_file.html_summary_plot_leaf_teeth_output_config_file(Parameters.results + '/html/html_summary_plot_leaf_teeth.html')
        #####################
        print "Adding number of teeth boxplot to config file."
        pos = [1]
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(20, 20))
        plt.figure()
        plt.xlabel("Number of Teeth")
        plt.boxplot(number_of_teeth, 0, 'rs', 0)
        boxplot_path_number_of_teeth = Parameters.results + "/images/plot_number_of_teeth.png"
        savefig(boxplot_path_number_of_teeth)
        self.config_file.number_of_teeth_boxplot_output_config_file(boxplot_path_number_of_teeth)

        #####################
        # shape descriptors
        f_plot_leaf_shape = open(Parameters.results + '/html/html_summary_plot_leaf_shape.html', 'w')
        f5 = open('../resources/html/index_plot_leaf_shape.html', "r")
        my_html_test_doc_plot_cm = f5.read().split('\n')

        aspect_ratio = tsv_data_to_html["AspectRatio"].tolist()
        string_aspect_ratio_array = "var x0=[aspectratio]"
        html_index = my_html_test_doc_plot_cm.index(string_aspect_ratio_array)
        my_html_test_doc_plot_cm[html_index] = "var x0=%s" % aspect_ratio
        #####################
        print "Adding aspect ratio boxplot to config file."
        pos = [1]
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(20, 20))
        plt.figure()
        plt.xlabel("Aspect Ratio")
        plt.boxplot(aspect_ratio, 0, 'rs', 0)
        boxplot_path_aspect_ratio= Parameters.results + "/images/plot_aspect_ratio.png"
        savefig(boxplot_path_aspect_ratio)
        self.config_file.aspect_ratio_boxplot_output_config_file(boxplot_path_aspect_ratio)

        #####################

        perimeter_ratio_of_length = tsv_data_to_html["Perimeter Ratio of Length"].tolist()
        string_perimeter_ratio_of_length_array = "var x4=[perimeterratiooflength]"
        html_index = my_html_test_doc_plot_cm.index(string_perimeter_ratio_of_length_array)
        my_html_test_doc_plot_cm[html_index] = "var x4=%s" % perimeter_ratio_of_length
        #####################
        print "Adding perimeter_ratio_of_length boxplot to config file."
        pos = [1]
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(20, 20))
        plt.figure()
        plt.xlabel("Perimeter Ratio of Length")
        plt.boxplot(perimeter_ratio_of_length, 0, 'rs', 0)
        boxplot_path_perimeter_ratio_of_length= Parameters.results + "/images/plot_perimeter_ratio_of_length.png"
        savefig(boxplot_path_perimeter_ratio_of_length)
        self.config_file.perimeter_ratio_of_length_boxplot_output_config_file(boxplot_path_perimeter_ratio_of_length)

        #####################

        perimeter_ratio_of_length_and_width = tsv_data_to_html["Perimeter Ratio of Length and Width"].tolist()
        string_perimeter_ratio_of_length_and_width_array = "var x5=[perimeterratiooflengthandwidth]"
        html_index = my_html_test_doc_plot_cm.index(string_perimeter_ratio_of_length_and_width_array)
        my_html_test_doc_plot_cm[html_index] = "var x5=%s" % perimeter_ratio_of_length_and_width
        #####################
        print "Adding perimeter_ratio_of_length_and_width boxplot to config file."
        pos = [1]
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(20, 20))
        plt.figure()
        plt.xlabel("Perimeter Ratio of Length and Width")
        plt.boxplot(perimeter_ratio_of_length_and_width, 0, 'rs', 0)
        boxplot_path_perimeter_ratio_of_length_and_withd= Parameters.results + "/images/plot_perimeter_ratio_of_length_and_width.png"
        savefig(boxplot_path_perimeter_ratio_of_length_and_withd)
        self.config_file.perimeter_ratio_of_length_and_width_boxplot_output_config_file(boxplot_path_perimeter_ratio_of_length_and_withd)

        #####################
        html_index = my_html_test_doc_plot_cm.index("<link href=\"bootstrap.min.css\" rel=\"stylesheet\">")
        bootstrap_string = "<link href=\"" + Parameters.resources + "/css/bootstrap.min.css\" rel=\"stylesheet\">"
        my_html_test_doc_plot_cm[html_index] = bootstrap_string

        html_index = my_html_test_doc_plot_cm.index("<link href=\"dashboard.css\" rel=\"stylesheet\">")
        dashboard_string = "<link href=\"" + Parameters.resources + "/css/dashboard.css\" rel=\"stylesheet\">"
        my_html_test_doc_plot_cm[html_index] = dashboard_string

        str_for_html = "\n".join(my_html_test_doc_plot_cm)
        f_plot_leaf_shape.write(str_for_html)
        f_plot_leaf_shape.close()
        f5.close()

        filename_plot_cm = 'file://' + Parameters.results + '/html/html_summary_plot_leaf_shape.html'

        # add success for this process to the config
        self.config_file.html_summary_plot_leaf_shape_output_config_file(Parameters.results + '/html/html_summary_plot_leaf_shape.html')
        # shapedescriptors2

        f_plot_leaf_shape2 = open(Parameters.results + '/html/html_summary_plot_leaf_shape2.html', 'w')
        f6 = open('../resources/html/index_plot_leaf_shape2.html', "r")
        my_html_test_doc_plot_cm = f6.read().split('\n')

        roundness = tsv_data_to_html["Roundness"].tolist()
        string_roundness_array = "var x1=[roundness]"
        html_index = my_html_test_doc_plot_cm.index(string_roundness_array)
        my_html_test_doc_plot_cm[html_index] = "var x1=%s" % roundness
        #####################
        print "Adding roundness boxplot to config file."
        pos = [1]
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(20, 20))
        plt.figure()
        plt.xlabel("Roundness")
        plt.boxplot(roundness, 0, 'rs', 0)
        boxplot_path_roundness= Parameters.results + "/images/plot_roundness.png"
        savefig(boxplot_path_roundness)
        self.config_file.roundness_boxplot_output_config_file(boxplot_path_roundness)

        #####################
        rectangularity = tsv_data_to_html["Rectangularity"].tolist()
        string_rectangularity_array = "var x3=[rectangularity]"
        html_index = my_html_test_doc_plot_cm.index(string_rectangularity_array)
        my_html_test_doc_plot_cm[html_index] = "var x3=%s" % rectangularity
        #####################
        print "Adding rectangularity boxplot to config file."
        pos = [1]
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(20, 20))
        plt.figure()
        plt.xlabel("Rectangularity")
        plt.boxplot(rectangularity, 0, 'rs', 0)
        boxplot_path_rectangularity= Parameters.results + "/images/plot_rectangularity.png"
        savefig(boxplot_path_rectangularity)
        self.config_file.rectangularity_boxplot_output_config_file(boxplot_path_rectangularity)

        #####################

        perimeter_convexity = tsv_data_to_html["Perimeter Convexity"].tolist()
        string_perimeter_convexity_array = "var x6=[perimeterconvexity]"
        html_index = my_html_test_doc_plot_cm.index(string_perimeter_convexity_array)
        my_html_test_doc_plot_cm[html_index] = "var x6=%s" % perimeter_convexity
        #####################
        print "Adding perimeter convexity boxplot to config file."
        pos = [1]
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(20, 20))
        plt.figure()
        plt.xlabel("Perimeter Convexity")
        plt.boxplot(perimeter_convexity, 0, 'rs', 0)
        boxplot_path_perimeter_convexity = Parameters.results + "/images/plot_perimeter_convexity.png"
        savefig(boxplot_path_perimeter_convexity)
        self.config_file.perimeter_convexity_boxplot_output_config_file(boxplot_path_perimeter_convexity)

        #####################
        area_convexity = tsv_data_to_html["Area Convexity"].tolist()
        string_area_convexity_array = "var x7=[areaconvexity]"
        html_index = my_html_test_doc_plot_cm.index(string_area_convexity_array)
        my_html_test_doc_plot_cm[html_index] = "var x7=%s" % area_convexity
        #####################
        print "Adding area convexity boxplot to config file."
        pos = [1]
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(20, 20))
        plt.figure()
        plt.xlabel("Area Convexity")
        plt.boxplot(area_convexity, 0, 'rs', 0)
        boxplot_path_area_convexity = Parameters.results + "/images/plot_area_convexity.png"
        savefig(boxplot_path_area_convexity)
        self.config_file.area_convexity_boxplot_output_config_file(boxplot_path_area_convexity)

        #####################
        area_ratio_of_convexity = tsv_data_to_html["Area Ratio of Convexity"].tolist()
        string_area_ratio_of_convexity_array = "var x8=[arearatioofconvexity]"
        html_index = my_html_test_doc_plot_cm.index(string_area_ratio_of_convexity_array)
        my_html_test_doc_plot_cm[html_index] = "var x8=%s" % area_ratio_of_convexity
        #####################
        print "Adding area ratio of convexity boxplot to config file."
        pos = [1]
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(20, 20))
        plt.figure()
        plt.xlabel("Area Ratio of Convexity")
        plt.boxplot(area_ratio_of_convexity, 0, 'rs', 0)
        boxplot_path_area_ratio_of_convexity = Parameters.results + "/images/plot_area_ratio_of_convexity.png"
        savefig(boxplot_path_area_ratio_of_convexity)
        self.config_file.area_ratio_of_convexity_boxplot_output_config_file(boxplot_path_area_ratio_of_convexity)

        #####################

        html_index = my_html_test_doc_plot_cm.index("<link href=\"bootstrap.min.css\" rel=\"stylesheet\">")
        bootstrap_string = "<link href=\"" + Parameters.resources + "/css/bootstrap.min.css\" rel=\"stylesheet\">"
        my_html_test_doc_plot_cm[html_index] = bootstrap_string

        html_index = my_html_test_doc_plot_cm.index("<link href=\"dashboard.css\" rel=\"stylesheet\">")
        dashboard_string = "<link href=\"" + Parameters.resources + "/css/dashboard.css\" rel=\"stylesheet\">"
        my_html_test_doc_plot_cm[html_index] = dashboard_string

        str_for_html = "\n".join(my_html_test_doc_plot_cm)
        f_plot_leaf_shape2.write(str_for_html)
        f_plot_leaf_shape2.close()
        f6.close()

        filename_plot_cm = 'file://' + Parameters.results + '/html/html_summary_plot_leaf_shape2.html'

        # add success for this process to the config
        self.config_file.html_summary_plot_leaf_shape2_output_config_file(Parameters.results + '/html/html_summary_plot_leaf_shape2.html')
        # compactness
        f_plot_leaf_compactness = open(Parameters.results + '/html/html_summary_plot_leaf_compactness.html', 'w')
        f7 = open('../resources/html/index_plot_leaf_compactness.html', "r")
        my_html_test_doc_plot_cm = f7.read().split('\n')
        compactness = tsv_data_to_html["Compactness"].tolist()
        string_compactness_array = "var x2=[compactness]"
        html_index = my_html_test_doc_plot_cm.index(string_compactness_array)
        my_html_test_doc_plot_cm[html_index] = "var x2=%s" % compactness
        #####################
        print "Adding compactness boxplot to config file."
        pos = [1]
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(20, 20))
        plt.figure()
        plt.xlabel("Compactness")
        plt.boxplot(compactness, 0, 'rs', 0)
        boxplot_path_compactness = Parameters.results + "/images/plot_compactness.png"
        savefig(boxplot_path_compactness)
        self.config_file.compactness_boxplot_output_config_file(boxplot_path_compactness)

        #####################
        html_index = my_html_test_doc_plot_cm.index("<link href=\"bootstrap.min.css\" rel=\"stylesheet\">")
        bootstrap_string = "<link href=\"" + Parameters.resources + "/css/bootstrap.min.css\" rel=\"stylesheet\">"
        my_html_test_doc[html_index] = bootstrap_string

        html_index = my_html_test_doc_plot_cm.index("<link href=\"dashboard.css\" rel=\"stylesheet\">")
        dashboard_string = "<link href=\"" + Parameters.resources + "/css/dashboard.css\" rel=\"stylesheet\">"
        my_html_test_doc[html_index] = dashboard_string

        str_for_html = "\n".join(my_html_test_doc_plot_cm)
        f_plot_leaf_compactness.write(str_for_html)
        f_plot_leaf_compactness.close()
        f7.close()

        filename_plot_cm = 'file://' + Parameters.results + '/html/html_summary_plot_leaf_compactness.html'

        # add success for this process to the config
        self.config_file.html_summary_plot_leaf_compactness_output_config_file(Parameters.results + '/html/html_summary_plot_leaf_compactness.html')

        # equivalent diameter in cm
        f_plot_leaf_eqd_cm = open(Parameters.results + '/html/html_summary_plot_leaf_eqd_cm.html', 'w')
        f8 = open('../resources/html/index_plot_leaf_eqd_cm.html', "r")
        my_html_test_doc_plot_cm = f8.read().split('\n')
        equivalent_diameter = tsv_data_to_html["Equivalent Diameter cm"].tolist()
        string_equivalent_diameter_array = "var x9=[equivalentdiameter]"
        html_index = my_html_test_doc_plot_cm.index(string_equivalent_diameter_array)
        my_html_test_doc_plot_cm[html_index] = "var x9=%s" % equivalent_diameter
        #####################
        print "Adding equivalent diameter cm boxplot to config file."
        pos = [1]
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(20, 20))
        plt.figure()
        plt.xlabel("Equivalent Diameter in cm")
        plt.boxplot(equivalent_diameter, 0, 'rs', 0)
        boxplot_path_eqd_cm = Parameters.results + "/images/plot_eqd_cm.png"
        savefig(boxplot_path_eqd_cm)
        self.config_file.eqd_cm_boxplot_output_config_file(boxplot_path_eqd_cm)

        #####################
        html_index = my_html_test_doc_plot_cm.index("<link href=\"bootstrap.min.css\" rel=\"stylesheet\">")
        bootstrap_string = "<link href=\"" + Parameters.resources + "/css/bootstrap.min.css\" rel=\"stylesheet\">"
        my_html_test_doc_plot_cm[html_index] = bootstrap_string

        html_index = my_html_test_doc_plot_cm.index("<link href=\"dashboard.css\" rel=\"stylesheet\">")
        dashboard_string = "<link href=\"" + Parameters.resources + "/css/dashboard.css\" rel=\"stylesheet\">"
        my_html_test_doc_plot_cm[html_index] = dashboard_string
        str_for_html = "\n".join(my_html_test_doc_plot_cm)
        f_plot_leaf_eqd_cm.write(str_for_html)
        f_plot_leaf_eqd_cm.close()
        f8.close()

        filename_plot_cm = 'file://' + Parameters.results + '/html/html_summary_plot_leaf_eqd_cm.html'

        # add success for this process to the config
        self.config_file.html_summary_plot_leaf_eqd_cm_output_config_file(Parameters.results + '/html/html_summary_plot_leaf_eqd_cm.html')

        boxplot_pixels = open(Parameters.results + '/html/html_boxplot_pixels.html', 'w')
        boxplot_template = open(Parameters.resources + '/html/boxplot_template.html', "r")
        my_html_boxplot_pixels = boxplot_template.read().split('\n')

        string_to_change = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"1\" width=\"400\" />"
        html_index = my_html_boxplot_pixels.index(string_to_change)
        my_html_boxplot_pixels[html_index] = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"%s\" width=\"400\" />" % (Parameters.results + "/images/plot_length_pixels.png")

        string_to_change = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"2\" width=\"400\" />"
        html_index = my_html_boxplot_pixels.index(string_to_change)
        my_html_boxplot_pixels[html_index] = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"%s\" width=\"400\" />" % (Parameters.results + "/images/plot_width_pixels.png")

        string_to_change = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"3\" width=\"400\" />"
        html_index = my_html_boxplot_pixels.index(string_to_change)
        my_html_boxplot_pixels[html_index] = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"%s\" width=\"400\" />" % (Parameters.results + "/images/plot_area_pixels.png")

        string_to_change = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"4\" width=\"400\" />"
        html_index = my_html_boxplot_pixels.index(string_to_change)
        my_html_boxplot_pixels[html_index] = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"%s\" width=\"400\" />" % (Parameters.results + "/images/plot_perimeter_pixels.png")

        string_to_change = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"5\" width=\"400\" />"
        html_index = my_html_boxplot_pixels.index(string_to_change)
        my_html_boxplot_pixels[html_index] = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"%s\" width=\"400\" />" % (Parameters.results + "/images/plot_eqd_pixels.png")

        string_to_change = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"6\" width=\"400\" />"
        html_index = my_html_boxplot_pixels.index(string_to_change)
        my_html_boxplot_pixels[
            html_index] = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"%s\" width=\"400\" />" % (
                    Parameters.results + "/images/plot_area_convexity.png")

        string_to_change = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"7\" width=\"400\" />"
        html_index = my_html_boxplot_pixels.index(string_to_change)
        my_html_boxplot_pixels[
            html_index] = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"%s\" width=\"400\" />" % (
                    Parameters.results + "/images/plot_area_ratio_of_convexity.png")

        string_to_change = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"8\" width=\"400\" />"
        html_index = my_html_boxplot_pixels.index(string_to_change)
        my_html_boxplot_pixels[
            html_index] = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"%s\" width=\"400\" />" % (
                    Parameters.results + "/images/plot_aspect_ratio.png")

        string_to_change = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"9\" width=\"400\" />"
        html_index = my_html_boxplot_pixels.index(string_to_change)
        my_html_boxplot_pixels[
            html_index] = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"%s\" width=\"400\" />" % (
                    Parameters.results + "/images/plot_compactness.png")

        string_to_change = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"10\" width=\"400\" />"
        html_index = my_html_boxplot_pixels.index(string_to_change)
        my_html_boxplot_pixels[
            html_index] = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"%s\" width=\"400\" />" % (
                    Parameters.results + "/images/plot_number_of_teeth.png")

        string_to_change = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"11\" width=\"400\" />"
        html_index = my_html_boxplot_pixels.index(string_to_change)
        my_html_boxplot_pixels[
            html_index] = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"%s\" width=\"400\" />" % (
                    Parameters.results + "/images/plot_perimeter_convexity.png")

        string_to_change = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"12\" width=\"400\" />"
        html_index = my_html_boxplot_pixels.index(string_to_change)
        my_html_boxplot_pixels[
            html_index] = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"%s\" width=\"400\" />" % (
                    Parameters.results + "/images/plot_perimeter_ratio_of_length.png")

        string_to_change = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"13\" width=\"400\" />"
        html_index = my_html_boxplot_pixels.index(string_to_change)
        my_html_boxplot_pixels[
            html_index] = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"%s\" width=\"400\" />" % (
                    Parameters.results + "/images/plot_perimeter_ratio_of_length_and_width.png")

        string_to_change = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"14\" width=\"400\" />"
        html_index = my_html_boxplot_pixels.index(string_to_change)
        my_html_boxplot_pixels[
            html_index] = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"%s\" width=\"400\" />" % (
                    Parameters.results + "/images/plot_roundness.png")


        str_for_html = "\n".join(my_html_boxplot_pixels)
        boxplot_pixels.write(str_for_html)
        boxplot_pixels.close()
        boxplot_template.close()
        boxplot_pixels_string = Parameters.results + '/html/html_boxplot_pixels.html'
        self.config_file.html_boxplot_pixels_output_config_file(boxplot_pixels_string)
        ### CM ####
        boxplot_cm = open(Parameters.results + '/html/html_boxplot_cm.html', 'w')
        boxplot_template = open(Parameters.resources + '/html/boxplot_template.html', "r")
        my_html_boxplot_cm = boxplot_template.read().split('\n')

        string_to_change = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"1\" width=\"400\" />"
        html_index = my_html_boxplot_cm.index(string_to_change)
        my_html_boxplot_cm[
            html_index] = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"%s\" width=\"400\" />" % (
                    Parameters.results + "/images/plot_length_cm.png")

        string_to_change = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"2\" width=\"400\" />"
        html_index = my_html_boxplot_cm.index(string_to_change)
        my_html_boxplot_cm[
            html_index] = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"%s\" width=\"400\" />" % (
                    Parameters.results + "/images/plot_width_cm.png")

        string_to_change = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"3\" width=\"400\" />"
        html_index = my_html_boxplot_cm.index(string_to_change)
        my_html_boxplot_cm[
            html_index] = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"%s\" width=\"400\" />" % (
                    Parameters.results + "/images/plot_area_cm.png")

        string_to_change = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"4\" width=\"400\" />"
        html_index = my_html_boxplot_cm.index(string_to_change)
        my_html_boxplot_cm[
            html_index] = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"%s\" width=\"400\" />" % (
                    Parameters.results + "/images/plot_perimeter_cm.png")

        string_to_change = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"5\" width=\"400\" />"
        html_index = my_html_boxplot_cm.index(string_to_change)
        my_html_boxplot_cm[
            html_index] = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"%s\" width=\"400\" />" % (
                    Parameters.results + "/images/plot_eqd_cm.png")

        string_to_change = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"6\" width=\"400\" />"
        html_index = my_html_boxplot_cm.index(string_to_change)
        my_html_boxplot_cm[
            html_index] = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"%s\" width=\"400\" />" % (
                Parameters.results + "/images/plot_area_convexity.png")

        string_to_change = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"7\" width=\"400\" />"
        html_index = my_html_boxplot_cm.index(string_to_change)
        my_html_boxplot_cm[
            html_index] = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"%s\" width=\"400\" />" % (
                Parameters.results + "/images/plot_area_ratio_of_convexity.png")

        string_to_change = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"8\" width=\"400\" />"
        html_index = my_html_boxplot_cm.index(string_to_change)
        my_html_boxplot_cm[
            html_index] = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"%s\" width=\"400\" />" % (
                Parameters.results + "/images/plot_aspect_ratio.png")

        string_to_change = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"9\" width=\"400\" />"
        html_index = my_html_boxplot_cm.index(string_to_change)
        my_html_boxplot_cm[
            html_index] = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"%s\" width=\"400\" />" % (
                Parameters.results + "/images/plot_compactness.png")

        string_to_change = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"10\" width=\"400\" />"
        html_index = my_html_boxplot_cm.index(string_to_change)
        my_html_boxplot_cm[
            html_index] = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"%s\" width=\"400\" />" % (
                Parameters.results + "/images/plot_number_of_teeth.png")

        string_to_change = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"11\" width=\"400\" />"
        html_index = my_html_boxplot_cm.index(string_to_change)
        my_html_boxplot_cm[
            html_index] = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"%s\" width=\"400\" />" % (
                Parameters.results + "/images/plot_perimeter_convexity.png")

        string_to_change = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"12\" width=\"400\" />"
        html_index = my_html_boxplot_cm.index(string_to_change)
        my_html_boxplot_cm[
            html_index] = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"%s\" width=\"400\" />" % (
                Parameters.results + "/images/plot_perimeter_ratio_of_length.png")

        string_to_change = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"13\" width=\"400\" />"
        html_index = my_html_boxplot_cm.index(string_to_change)
        my_html_boxplot_cm[
            html_index] = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"%s\" width=\"400\" />" % (
                Parameters.results + "/images/plot_perimeter_ratio_of_length_and_width.png")

        string_to_change = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"14\" width=\"400\" />"
        html_index = my_html_boxplot_cm.index(string_to_change)
        my_html_boxplot_cm[
            html_index] = "<img style=\"float: left; margin: 0px 0px 15px 15px;\" src=\"%s\" width=\"400\" />" % (
                Parameters.results + "/images/plot_roundness.png")

        str_for_html = "\n".join(my_html_boxplot_cm)
        boxplot_cm.write(str_for_html)
        boxplot_cm.close()
        boxplot_template.close()
        boxplot_cm_string = Parameters.results + '/html/html_boxplot_cm.html'
        self.config_file.html_boxplot_cm_output_config_file(boxplot_cm_string)
