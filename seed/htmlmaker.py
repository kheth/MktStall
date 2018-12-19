from parameters import Parameters
import pandas as pd
import seaborn as sns
import re
import webbrowser
from matplotlib.pyplot import savefig
import matplotlib.pyplot as plt
import numpy as np
from configmaker import ConfigMaker

class HtmlMaker:

    def __init__(self, path):
        self.images = []
        self.path = path
        self.config_file = ConfigMaker(self.path)
        self.image_name = ""
        #self.config_file = ConfigMaker(Parameters.results + "/summary_output.config")

    def accession_area_pixel_maker(self, rep_area, image_name):
        self.image_name = image_name
        accession_area_plot_html_file = Parameters.results + "/html/"+ self.image_name+"_accession_area_violin.html"
        outF = open(accession_area_plot_html_file, "w")
        inF = open(Parameters.resources + '/html/index_single_area.html', "r")
        my_html_test_doc_plot = inF.read().split('\n')

        string_to_be_substituted = "var x10=[Area]"
        html_index = my_html_test_doc_plot.index(string_to_be_substituted)
        my_html_test_doc_plot[html_index] = "var x10=%s" % rep_area
        str_for_html = "\n".join(my_html_test_doc_plot)
        outF.write(str_for_html)
        outF.close()
        inF.close()

        filename_plot = 'file://' + accession_area_plot_html_file
        #webbrowser.get().open_new_tab(filename_plot)
        self.config_file.accession_area_plot_html_output_config_file(accession_area_plot_html_file)
        #####################
        print "Adding area pixels boxplot to config file."
        pos = [1]
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(20, 20))
        plt.figure()
        plt.xlabel("Area of seeds in accession in Pixels")
        plt.boxplot(rep_area, 0, 'rs', 0)
        boxplot_path_accession_area_pixels = Parameters.results + "/images/"+self.image_name+"_plot_accession_area_pixels.png"
        savefig(boxplot_path_accession_area_pixels)
        self.config_file.accession_area_pixels_boxplot_output_config_file(boxplot_path_accession_area_pixels)

    def accession_eqd_pixel_maker(self, rep_eqd,image_name):
        self.image_name = image_name
        accession_eqd_plot_html_file = Parameters.results + '/html/'+self.image_name+'_accession_eqd_violin.html'
        outF = open(accession_eqd_plot_html_file, "w")
        inF = open(Parameters.resources + '/html/index_single_eqd.html', "r")
        my_html_test_doc_plot = inF.read().split('\n')

        string_to_be_substituted = "var x10=[Eqd]"
        html_index = my_html_test_doc_plot.index(string_to_be_substituted)
        my_html_test_doc_plot[html_index] = "var x10=%s" % rep_eqd
        str_for_html = "\n".join(my_html_test_doc_plot)
        outF.write(str_for_html)
        outF.close()
        inF.close()

        filename_plot = 'file://' + accession_eqd_plot_html_file
        #webbrowser.get().open_new_tab(filename_plot)
        self.config_file.accession_eqd_plot_html_output_config_file(accession_eqd_plot_html_file)
        #####################
        print "Adding equivalent diameter pixels boxplot to config file."
        pos = [1]
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(20, 20))
        plt.figure()
        plt.xlabel("Equivalent Diameter of seeds in accession in Pixels")
        plt.boxplot(rep_eqd, 0, 'rs', 0)
        boxplot_path_accession_eqd_pixels = Parameters.results + "/images/"+self.image_name+"_plot_accession_eqd_pixels.png"
        savefig(boxplot_path_accession_eqd_pixels)
        self.config_file.accession_eqd_pixels_boxplot_output_config_file(boxplot_path_accession_eqd_pixels)

    def accession_perimeter_pixel_maker(self, rep_perimeter, image_name):
        self.image_name = image_name
        accession_perimeter_plot_html_file = Parameters.results + '/html/'+self.image_name+'_accession_perimeter_violin.html'
        outF = open(accession_perimeter_plot_html_file, "w")
        inF = open(Parameters.resources + '/html/index_single_perimeter.html', "r")
        my_html_test_doc_plot = inF.read().split('\n')

        string_to_be_substituted = "var x10=[Perimeter]"
        html_index = my_html_test_doc_plot.index(string_to_be_substituted)
        my_html_test_doc_plot[html_index] = "var x10=%s" % rep_perimeter
        str_for_html = "\n".join(my_html_test_doc_plot)
        outF.write(str_for_html)
        outF.close()
        inF.close()

        filename_plot = 'file://' + accession_perimeter_plot_html_file
        #webbrowser.get().open_new_tab(filename_plot)
        self.config_file.accession_perimeter_plot_html_output_config_file(accession_perimeter_plot_html_file)
        #####################
        print "Adding perimeter pixels boxplot to config file."
        pos = [1]
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(20, 20))
        plt.figure()
        plt.xlabel("Perimeter of seeds in accession in Pixels")
        plt.boxplot(rep_perimeter, 0, 'rs', 0)
        boxplot_path_accession_perimeter_pixels = Parameters.results + "/images/"+self.image_name+"_plot_accession_perimeter_pixels.png"
        savefig(boxplot_path_accession_perimeter_pixels)
        self.config_file.accession_perimeter_pixels_boxplot_output_config_file(boxplot_path_accession_perimeter_pixels)

    def accession_seed_table_file_maker(self,seed_table, image_name):
        self.image_name = image_name
        accession_seed_table_file = Parameters.results + "/html/"+self.image_name+"_accession_seed_table.html"
        outTable = open(accession_seed_table_file, "w")
        inTable = open(Parameters.resources + '/html/index.html', "r")
        my_html_test_doc = inTable.read().split('\n')

        string_to_be_substituted = "THIS IS TABLE"
        html_index = my_html_test_doc.index(string_to_be_substituted)
        my_html_test_doc[html_index] = seed_table
        str_for_html = "\n".join(my_html_test_doc)
        outTable.write(str_for_html)
        outTable.close()
        inTable.close()

        filename_plot = 'file://' + accession_seed_table_file
        #webbrowser.get().open_new_tab(filename_plot)
        self.config_file.accession_table_html_output_config_file(accession_seed_table_file)

    def accession_method_html_maker(self, original_image_jpg_file, hsv_jpg_file,mask_png_file,seed_labels_jpg_file,imposed_annotation_jpg_file, image_name):
        self.image_name = image_name
        seed_method_file = Parameters.results + "/html/"+self.image_name+"_accession_method_seed.html"
        outF = open(seed_method_file, "w")
        inF = open(Parameters.resources + '/html/method_index.html', "r")
        my_html_test_doc_method = inF.read().split('\n')

        string_to_be_substituted = "<img class=\"card-img-top\" data-src=\"PICTURE\" alt=\"Card image cap\">"
        html_index = my_html_test_doc_method.index(string_to_be_substituted)
        method_string = "<img class=\"card-img-top\" src=\"%s\" alt=\"Card image cap\">" % original_image_jpg_file
        my_html_test_doc_method[html_index] = method_string

        string_to_be_substituted = "<img class=\"card-img-top\" data-src=\"PICTURE2\" alt=\"Card image cap\">"
        html_index = my_html_test_doc_method.index(string_to_be_substituted)
        method_string = "<img class=\"card-img-top\" src=\"%s\" alt=\"Card image cap\">" % hsv_jpg_file
        my_html_test_doc_method[html_index] = method_string

        string_to_be_substituted = "<img class=\"card-img-top\" data-src=\"PICTURE3\" alt=\"Card image cap\">"
        html_index = my_html_test_doc_method.index(string_to_be_substituted)
        method_string = "<img class=\"card-img-top\" src=\"%s\" alt=\"Card image cap\">" % mask_png_file
        my_html_test_doc_method[html_index] = method_string

        string_to_be_substituted = "<img class=\"card-img-top\" data-src=\"PICTURE4\" alt=\"Card image cap\">"
        html_index = my_html_test_doc_method.index(string_to_be_substituted)
        method_string = "<img class=\"card-img-top\" src=\"%s\" alt=\"Card image cap\">" % seed_labels_jpg_file
        my_html_test_doc_method[html_index] = method_string

        string_to_be_substituted = "<img class=\"card-img-top\" data-src=\"PICTURE5\" alt=\"Card image cap\">"
        html_index = my_html_test_doc_method.index(string_to_be_substituted)
        method_string = "<img class=\"card-img-top\" src=\"%s\" alt=\"Card image cap\">" % imposed_annotation_jpg_file
        my_html_test_doc_method[html_index] = method_string
        str_for_html = "\n".join(my_html_test_doc_method)
        outF.write(str_for_html)
        outF.close()
        inF.close()

        filename_plot = 'file://' + seed_method_file
        #webbrowser.get().open_new_tab(filename_plot)
        self.config_file.accession_method_html_output_config_file(seed_method_file)

    def summary_table_maker(self, summary_csv_file):
        print "Making html summary."
        summary_file = open(summary_csv_file, "r")
        columns = ['Accession',
                   'Number of Seeds',
                   'Mean Area Pixels',
                   'Mean Equivalent Diameter Pixels',
                   'Mean Perimeter Pixels']
        df = pd.read_csv(summary_file, names=columns)
        html_table = df.to_html(justify='left')
        list_seed_table = html_table.split('\n')
        del list_seed_table[0]
        del list_seed_table[-1]
        seed_table_summary = "\n".join(list_seed_table)
        summary_file.close()
        summary_seed_html_table_file = Parameters.results + "/html/summary_seed_table.html"
        outTable = open(summary_seed_html_table_file, "w")
        inTable = open(Parameters.resources + '/html/index.html', "r")
        my_html_test_doc = inTable.read().split('\n')

        string_to_be_substituted = "THIS IS TABLE"
        html_index = my_html_test_doc.index(string_to_be_substituted)
        my_html_test_doc[html_index] = seed_table_summary
        str_for_html = "\n".join(my_html_test_doc)
        outTable.write(str_for_html)
        outTable.close()
        inTable.close()

        filename_plot = 'file://' + summary_seed_html_table_file
        #webbrowser.get().open_new_tab(filename_plot)
        self.config_file.summary_table_html_output_config_file(summary_seed_html_table_file)
        self.config_file.summary_csv_output_config_file(summary_csv_file)
        summary_file.close()

    def summary_perimeter_pixel_maker(self):
        summaryfile = open(Parameters.results + "/tables/workfile.csv", "r")
        header_names = ["Accession",
                        "Number of Seeds",
                        "Mean Area Pixels",
                        "Mean Equivalent Diameter Pixels",
                        "Mean Perimeter Pixels"]
        df = pd.read_csv(summaryfile, names=header_names)
        summary_perimeter = []
        for i in df["Mean Perimeter Pixels"]:
            summary_perimeter.append(i)

        summary_perimeter_plot_html_file = Parameters.results + '/html/summary_perimeter_violin.html'
        outF = open(summary_perimeter_plot_html_file, "w")
        inF = open(Parameters.resources + '/html/index_single_perimeter.html', "r")
        my_html_test_doc_plot = inF.read().split('\n')

        string_to_be_substituted = "var x10=[Perimeter]"
        html_index = my_html_test_doc_plot.index(string_to_be_substituted)
        my_html_test_doc_plot[html_index] = "var x10=%s" % summary_perimeter
        str_for_html = "\n".join(my_html_test_doc_plot)
        outF.write(str_for_html)
        outF.close()
        inF.close()

        filename_plot = 'file://' + summary_perimeter_plot_html_file
        #webbrowser.get().open_new_tab(filename_plot)
        self.config_file.summary_perimter_pixels_html_output_config_file(summary_perimeter_plot_html_file)
        #####################
        print "Adding summary perimeter pixels boxplot to config file."
        pos = [1]
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(20, 20))
        plt.figure()
        plt.xlabel("Average Perimeter of seeds in summary in Pixels")
        plt.boxplot(summary_perimeter, 0, 'rs', 0)
        boxplot_path_summary_perimeter_pixels = Parameters.results + "/images/plot_summary_perimeter_pixels.png"
        savefig(boxplot_path_summary_perimeter_pixels)
        self.config_file.summary_perimeter_pixels_boxplot_output_config_file(boxplot_path_summary_perimeter_pixels)

    def summary_area_pixel_maker(self):
        summaryfile = open(Parameters.results + "/tables/workfile.csv", "r")
        header_names = ["image_name",
                        "numberofseeds",
                        "area_mean_pix",
                        "eqd_mean_pix",
                        "perimeter_mean_pix",
                        "mean_max_mins",
                        "pix_per_cm",
                        "area_mean_cm",
                        "eqd_mean_cm",
                        "perimeter_mean_cm"]
        df = pd.read_csv(summaryfile, names=header_names)
        summary_area = []
        for i in df["area_mean_pix"]:
            summary_area.append(i)

        summary_area_plot_html_file = Parameters.results + '/html/summary_area_violin.html'
        outF = open(summary_area_plot_html_file, "w")
        inF = open(Parameters.resources + '/html/index_single_area.html', "r")
        my_html_test_doc_plot = inF.read().split('\n')

        string_to_be_substituted = "var x10=[Area]"
        html_index = my_html_test_doc_plot.index(string_to_be_substituted)
        my_html_test_doc_plot[html_index] = "var x10=%s" % summary_area
        str_for_html = "\n".join(my_html_test_doc_plot)
        outF.write(str_for_html)
        outF.close()
        inF.close()

        filename_plot = 'file://' + summary_area_plot_html_file
        #webbrowser.get().open_new_tab(filename_plot)
        self.config_file.summary_area_pixels_html_output_config_file(summary_area_plot_html_file)
        #####################
        print "Adding summary area pixels boxplot to config file."
        pos = [1]
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(20, 20))
        plt.figure()
        plt.xlabel("Average Area of seeds in summary in Pixels")
        plt.boxplot(summary_area, 0, 'rs', 0)
        boxplot_path_summary_area_pixels = Parameters.results + "/images/plot_summary_area_pixels.png"
        savefig(boxplot_path_summary_area_pixels)
        self.config_file.summary_area_pixels_boxplot_output_config_file(boxplot_path_summary_area_pixels)

    def summary_eqd_pixel_maker(self):
        summaryfile = open(Parameters.results + "/tables/workfile.csv", "r")
        header_names = ["image_name",
                        "numberofseeds",
                        "area_mean_pix",
                        "eqd_mean_pix",
                        "perimeter_mean_pix",
                        "mean_max_mins",
                        "pix_per_cm",
                        "area_mean_cm",
                        "eqd_mean_cm",
                        "perimeter_mean_cm"]
        df = pd.read_csv(summaryfile, names=header_names)
        summary_eqd = []
        for i in df["eqd_mean_pix"]:
            summary_eqd.append(i)

        summary_eqd_plot_html_file = Parameters.results + '/html/summary_eqd_violin.html'
        outF = open(summary_eqd_plot_html_file, "w")
        inF = open(Parameters.resources + '/html/index_single_eqd.html', "r")
        my_html_test_doc_plot = inF.read().split('\n')

        string_to_be_substituted = "var x10=[Eqd]"
        html_index = my_html_test_doc_plot.index(string_to_be_substituted)
        my_html_test_doc_plot[html_index] = "var x10=%s" % summary_eqd
        str_for_html = "\n".join(my_html_test_doc_plot)
        outF.write(str_for_html)
        outF.close()
        inF.close()

        filename_plot = 'file://' + summary_eqd_plot_html_file
        #webbrowser.get().open_new_tab(filename_plot)
        self.config_file.summary_eqd_pixels_html_output_config_file(summary_eqd_plot_html_file)
        #####################
        print "Adding summary eqd pixels boxplot to config file."
        pos = [1]
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(20, 20))
        plt.figure()
        plt.xlabel("Average Equivalent Diameter of seeds in summary in Pixels")
        plt.boxplot(summary_eqd, 0, 'rs', 0)
        boxplot_path_summary_eqd_pixels = Parameters.results + "/images/plot_summary_eqd_pixels.png"
        savefig(boxplot_path_summary_eqd_pixels)
        self.config_file.summary_eqd_pixels_boxplot_output_config_file(boxplot_path_summary_eqd_pixels)

    def summary_numberofseeds_pixel_maker(self):
        summaryfile = open(Parameters.results + "/tables/workfile.csv", "r")
        header_names = ["image_name",
                        "numberofseeds",
                        "area_mean_pix",
                        "eqd_mean_pix",
                        "perimeter_mean_pix",
                        "mean_max_mins",
                        "pix_per_cm",
                        "area_mean_cm",
                        "eqd_mean_cm",
                        "perimeter_mean_cm"]
        df = pd.read_csv(summaryfile, names=header_names)
        summary_number_of_seeds = []
        for i in df["numberofseeds"]:
            summary_number_of_seeds.append(i)

        summary_number_of_seeds_plot_html_file = Parameters.results + '/html/summary_numberofseeds_violin.html'
        outF = open(summary_number_of_seeds_plot_html_file, "w")
        inF = open(Parameters.resources + '/html/index_summary_numberofseeds.html', "r")
        my_html_test_doc_plot = inF.read().split('\n')

        string_to_be_substituted = "var x10=[Number]"
        html_index = my_html_test_doc_plot.index(string_to_be_substituted)
        my_html_test_doc_plot[html_index] = "var x10=%s" % summary_number_of_seeds
        str_for_html = "\n".join(my_html_test_doc_plot)
        outF.write(str_for_html)
        outF.close()
        inF.close()

        filename_plot = 'file://' + summary_number_of_seeds_plot_html_file
        #webbrowser.get().open_new_tab(filename_plot)
        self.config_file.summary_numberofseeds_html_output_config_file(summary_number_of_seeds_plot_html_file)
        #####################
        print "Adding summary number of seeds boxplot to config file."
        pos = [1]
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(20, 20))
        plt.figure()
        plt.xlabel("Number of seeds in summary")
        plt.boxplot(summary_number_of_seeds, 0, 'rs', 0)
        boxplot_path_summary_number_of_seeds= Parameters.results + "/images/plot_summary_number_of_seeds.png"
        savefig(boxplot_path_summary_number_of_seeds)
        self.config_file.summary_number_of_seeds_boxplot_output_config_file(boxplot_path_summary_number_of_seeds)

