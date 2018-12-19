from parameters import Parameters
import os.path


class ConfigMaker:
    def __init__(self, input_image_path):
        self.path = input_image_path  # path to original image
        image_path_list = self.path.split("/")
        image_name = image_path_list[-1]
        self.config_file_path = Parameters.results + "/" + image_name + ".config"
        self.status = ""
        self.mask_image_path = ""
        self.seed_labels_jpg_path = ""
        self.original_image_jpg_path = ""
        self.imposed_annotation_png_path = ""
        self.accession_area_plot_html_path = ""
        self.accession_eqd_plot_html_path = ""
        self.accession_perimeter_plot_html_file = ""
        self.accession_table_html_path = ""
        self.accession_area_pixels_boxplot_path = ""
        self.accession_eqd_pixels_boxplot_path = ""
        self.accession_perimeter_pixels_boxplot_path = ""
        self.accession_seed_method_file = ""
        self.summary_table_html_file = ""
        self.summary_csv_file = ""
        self.summary_perimeter_boxplot_png_file = ""
        self.summary_perimeter_plot_html_file = ""
        self.summary_area_boxplot_png_file = ""
        self.summary_area_plot_html_file = ""
        self.summary_eqd_boxplot_png_file = ""
        self.summary_eqd_plot_html_file = ""
        self.summary_number_of_seeds_plot_html_file = ""
        self.summary_numberofseeds_boxplot_png_file = ""
    def status_check(self, input_path, process):
        if os.path.exists(input_path):
            self.status = "#status_" + process + "=SUCCESS"
        else:
            self.status = "#status_" + process + "=FAIL"

    def hsv_output_config_file(self, hsv_image_path):
        print "Input image path: ", hsv_image_path
        self.status_check(hsv_image_path, "hsv_image")
        config = open(self.config_file_path, "w")
        print "Writing hsv image to config file."
        config.write("#CONFIG FILE\n")
        config.write("\n#Path to hsv image\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + hsv_image_path + "\n")
        config.close()

    def mask_output_config_file(self, mask_image_path):
        self.mask_image_path = mask_image_path
        print "Input image path:", mask_image_path
        self.status_check(mask_image_path, "mask_image")
        config = open(self.config_file_path, "a")
        print "Writing mask_png_file image to config file."
        config.write("\n#Path to mask_png_file image\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + mask_image_path + "\n")
        config.close()

    def seed_labels_output_config_file(self, seed_labels_jpg_path):
        self.seed_labels_jpg_path = seed_labels_jpg_path
        print "Input image path:", seed_labels_jpg_path
        self.status_check(seed_labels_jpg_path, "seed_labels_jpg")
        config = open(self.config_file_path, "a")
        print "Writing seed_labels_jpg_path image to config file."
        config.write("\n#Path to seed_labels_jpg image\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + seed_labels_jpg_path + "\n")
        config.close()

    def original_image_jpg_output_config_file(self, original_image_jpg_path):
        self.original_image_jpg_path = original_image_jpg_path
        print "Input image path:", original_image_jpg_path
        self.status_check(original_image_jpg_path, "original_image_jpg")
        config = open(self.config_file_path, "a")
        print "Writing original_image_jpg_path image to config file."
        config.write("\n#Path to original_image_jpg image\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + original_image_jpg_path + "\n")
        config.close()

    def imposed_annotation_output_config_file(self, imposed_annotation_png_path):
        self.imposed_annotation_png_path = imposed_annotation_png_path
        print "Input image path:", imposed_annotation_png_path
        self.status_check(imposed_annotation_png_path, "imposed_annotation_png")
        config = open(self.config_file_path, "a")
        print "Writing imposed_annotation_png_path image to config file."
        config.write("\n#Path to imposed_annotation_png image\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + imposed_annotation_png_path + "\n")
        config.close()

    def accession_method_html_output_config_file(self, accession_seed_method_file):
        self.accession_seed_method_file = accession_seed_method_file
        print "Input image path:", accession_seed_method_file
        self.status_check(accession_seed_method_file, "accession_seed_method_file")
        config = open(self.config_file_path, "a")
        print "Writing accession_seed_method_file image to config file."
        config.write("\n#Path to accession_seed_method_file image\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + accession_seed_method_file + "\n")
        config.close()

    def accession_area_plot_html_output_config_file(self, accession_area_plot_html_path):
        self.accession_area_plot_html_path = accession_area_plot_html_path
        print "Input image path:", accession_area_plot_html_path
        self.status_check(accession_area_plot_html_path, "accession_area_plot_html")
        config = open(self.config_file_path, "a")
        print "Writing accession_area_plot_html image to config file."
        config.write("\n#Path to accession_area_plot_html file\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + accession_area_plot_html_path + "\n")
        config.close()

    def accession_eqd_plot_html_output_config_file(self, accession_eqd_plot_html_path):
        self.accession_eqd_plot_html_path = accession_eqd_plot_html_path
        print "Input image path:", accession_eqd_plot_html_path
        self.status_check(accession_eqd_plot_html_path, "accession_eqd_plot_html_path")
        config = open(self.config_file_path, "a")
        print "Writing accession_eqd_plot_html image to config file."
        config.write("\n#Path to accession_eqd_plot_html file\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + accession_eqd_plot_html_path + "\n")
        config.close()

    def accession_perimeter_plot_html_output_config_file(self, accession_perimeter_plot_html_file):
        self.accession_perimeter_plot_html_file = accession_perimeter_plot_html_file
        print "Input image path:", accession_perimeter_plot_html_file
        self.status_check(accession_perimeter_plot_html_file, "accession_perimeter_plot_html_file")
        config = open(self.config_file_path, "a")
        print "Writing accession_perimeter_plot_html_file image to config file."
        config.write("\n#Path to accession_perimeter_plot_html_file file\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + accession_perimeter_plot_html_file + "\n")
        config.close()

    def accession_table_html_output_config_file(self, accession_table_html_path):
        self.accession_table_html_path = accession_table_html_path
        print "Input image path:", accession_table_html_path
        self.status_check(accession_table_html_path, "accession_table_html_path")
        config = open(self.config_file_path, "a")
        print "Writing accession_table_html_path image to config file."
        config.write("\n#Path to accession_table_html_path file\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + accession_table_html_path + "\n")
        config.close()

    def accession_area_pixels_boxplot_output_config_file(self, accession_area_pixels_boxplot_path):
        self.accession_area_pixels_boxplot_path = accession_area_pixels_boxplot_path
        print "Input image path:", accession_area_pixels_boxplot_path
        self.status_check(accession_area_pixels_boxplot_path, "accession_area_pixels_boxplot_path")
        config = open(self.config_file_path, "a")
        print "Writing accession_area_pixels_boxplot_path image to config file."
        config.write("\n#Path to accession_area_pixels_boxplot_path file\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + accession_area_pixels_boxplot_path + "\n")
        config.close()

    def accession_eqd_pixels_boxplot_output_config_file(self, accession_eqd_pixels_boxplot_path):
        self.accession_eqd_pixels_boxplot_path = accession_eqd_pixels_boxplot_path
        print "Input image path:", accession_eqd_pixels_boxplot_path
        self.status_check(accession_eqd_pixels_boxplot_path, "accession_eqd_pixels_boxplot_path")
        config = open(self.config_file_path, "a")
        print "Writing accession_eqd_pixels_boxplot_path image to config file."
        config.write("\n#Path to accession_eqd_pixels_boxplot_path file\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + accession_eqd_pixels_boxplot_path + "\n")
        config.close()

    def accession_perimeter_pixels_boxplot_output_config_file(self, accession_perimeter_pixels_boxplot_path):
        self.accession_perimeter_pixels_boxplot_path = accession_perimeter_pixels_boxplot_path
        print "Input image path:", accession_perimeter_pixels_boxplot_path
        self.status_check(accession_perimeter_pixels_boxplot_path, "accession_perimeter_pixels_boxplot_path")
        config = open(self.config_file_path, "a")
        print "Writing accession_perimeter_pixels_boxplot_path image to config file."
        config.write("\n#Path to accession_perimeter_pixels_boxplot_path file\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + accession_perimeter_pixels_boxplot_path + "\n")
        config.close()

    def summary_table_html_output_config_file(self, summary_table_html_file):
        self.summary_table_html_file = summary_table_html_file
        print "Input image path:", summary_table_html_file
        self.status_check(summary_table_html_file, "summary_table_html_file")
        config = open(self.config_file_path, "w")
        print "Writing summary_table_html_file image to config file."
        config.write("\n#Path to summary_table_html_file file\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + summary_table_html_file + "\n")
        config.close()

    def summary_csv_output_config_file(self, summary_csv_file):
        self.summary_csv_file = summary_csv_file
        print "Input image path:", summary_csv_file
        self.status_check(summary_csv_file, "summary_csv_file")
        config = open(self.config_file_path, "a")
        print "Writing summary_csv_file image to config file."
        config.write("\n#Path to summary_csv_file file\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + summary_csv_file + "\n")
        config.close()

    def summary_perimter_pixels_html_output_config_file(self, summary_perimeter_plot_html_file):
        self.summary_perimeter_plot_html_file = summary_perimeter_plot_html_file
        print "Input image path:", summary_perimeter_plot_html_file
        self.status_check(summary_perimeter_plot_html_file, "summary_perimeter_plot_html_file")
        config = open(self.config_file_path, "a")
        print "Writing summary_perimeter_plot_html_file image to config file."
        config.write("\n#Path to summary_perimeter_plot_html_file file\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + summary_perimeter_plot_html_file + "\n")
        config.close()

    def summary_perimeter_pixels_boxplot_output_config_file(self, summary_perimeter_boxplot_png_file):
        self.summary_perimeter_boxplot_png_file = summary_perimeter_boxplot_png_file
        print "Input image path:", summary_perimeter_boxplot_png_file
        self.status_check(summary_perimeter_boxplot_png_file, "summary_perimeter_boxplot_png_file")
        config = open(self.config_file_path, "a")
        print "Writing summary_perimeter_boxplot_png_file image to config file."
        config.write("\n#Path to summary_perimeter_boxplot_png_file file\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + summary_perimeter_boxplot_png_file + "\n")
        config.close()

    def summary_area_pixels_html_output_config_file(self, summary_area_plot_html_file):
        self.summary_area_plot_html_file = summary_area_plot_html_file
        print "Input image path:", summary_area_plot_html_file
        self.status_check(summary_area_plot_html_file, "summary_area_plot_html_file")
        config = open(self.config_file_path, "a")
        print "Writing summary_area_plot_html_file image to config file."
        config.write("\n#Path to summary_area_plot_html_file file\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + summary_area_plot_html_file + "\n")
        config.close()

    def summary_area_pixels_boxplot_output_config_file(self, summary_area_boxplot_png_file):
        self.summary_area_boxplot_png_file = summary_area_boxplot_png_file
        print "Input image path:", summary_area_boxplot_png_file
        self.status_check(summary_area_boxplot_png_file, "summary_area_boxplot_png_file")
        config = open(self.config_file_path, "a")
        print "Writing summary_area_boxplot_png_file image to config file."
        config.write("\n#Path to summary_area_boxplot_png_file file\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + summary_area_boxplot_png_file + "\n")
        config.close()

    def summary_eqd_pixels_html_output_config_file(self, summary_eqd_plot_html_file):
        self.summary_eqd_plot_html_file = summary_eqd_plot_html_file
        print "Input image path:", summary_eqd_plot_html_file
        self.status_check(summary_eqd_plot_html_file, "summary_eqd_plot_html_file")
        config = open(self.config_file_path, "a")
        print "Writing summary_eqd_plot_html_file image to config file."
        config.write("\n#Path to summary_eqd_plot_html_file file\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + summary_eqd_plot_html_file + "\n")
        config.close()

    def summary_eqd_pixels_boxplot_output_config_file(self, summary_eqd_boxplot_png_file):
        self.summary_eqd_boxplot_png_file = summary_eqd_boxplot_png_file
        print "Input image path:", summary_eqd_boxplot_png_file
        self.status_check(summary_eqd_boxplot_png_file, "summary_eqd_boxplot_png_file")
        config = open(self.config_file_path, "a")
        print "Writing summary_eqd_boxplot_png_file image to config file."
        config.write("\n#Path to summary_eqd_boxplot_png_file file\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + summary_eqd_boxplot_png_file + "\n")
        config.close()
    def summary_numberofseeds_html_output_config_file(self, summary_number_of_seeds_plot_html_file):
        self.summary_number_of_seeds_plot_html_file = summary_number_of_seeds_plot_html_file
        print "Input image path:", summary_number_of_seeds_plot_html_file
        self.status_check(summary_number_of_seeds_plot_html_file, "summary_number_of_seeds_plot_html_file")
        config = open(self.config_file_path, "a")
        print "Writing summary_number_of_seeds_plot_html_file image to config file."
        config.write("\n#Path to summary_number_of_seeds_plot_html_file file\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + summary_number_of_seeds_plot_html_file + "\n")
        config.close()

    def summary_number_of_seeds_boxplot_output_config_file(self, summary_numberofseeds_boxplot_png_file):
        self.summary_numberofseeds_boxplot_png_file = summary_numberofseeds_boxplot_png_file
        print "Input image path:", summary_numberofseeds_boxplot_png_file
        self.status_check(summary_numberofseeds_boxplot_png_file, "summary_numberofseeds_boxplot_png_file")
        config = open(self.config_file_path, "a")
        print "Writing summary_numberofseeds_boxplot_png_file image to config file."
        config.write("\n#Path to summary_numberofseeds_boxplot_png_file file\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + summary_numberofseeds_boxplot_png_file + "\n")
        config.close()