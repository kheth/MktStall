from parameters import Parameters
import os.path
class ConfigMaker:
    def __init__(self, input_image_path):
        self.label = ""
        self.status = ""
        self.path = input_image_path  # path to original image
        image_path_list = self.path.split("/")
        image_name = image_path_list[-1]
        self.config_file_path = Parameters.results + "/" + image_name + "_output.config"  # path to config file
        #
        self.crop_image_path = "" # path to crop1 image
        self.rotate_image_path = "" # path to rotated image
        self.crop2_image_path = "" # path to crop2 image
        self.dilated_skinny_path = "" # path to dilated image
        self.contours_path = "" # path to contours image
        self.contours_skinny_path = "" # path to contours skinny image
        self.centroid_path = "" # path to centroid image
        self.centroid_skinny_path = "" # path to centroid skinny
        self.length_path = "" # path to length
        self.width_path = "" # path to width
        self.area_path = "" # path to area
        self.aspect_ratio_path = "" # path to aspect ratio
        self.roundness_path = "" # path to roundness
        self.compactness_path = "" # path to compactness
        self.rectangularity_path = "" # path to rectangularity
        self.perimeterratiolength = "" # path to perimeterratiolength
        self.perimeterratiolengthwidth_path = "" # path to perimeterratiolengthwidth
        self.perimeterconvexity_path = "" # path to perimeterconvexity_path
        self.areaconvexity_path = "" # path to areaconvexity_path
        self.arearatioconvexity_path = "" # path to arearatioconvexity
        self.equivalentdiameter_path = "" # path to equivalentdiameter_path
        self.area_teeth_2sd_path = "" # path to area teeth 2sd
        self.area_teeth_path = "" # path to area teeth 2sd
        self.area_teeth_2sd_sinusPointsLength = "" # path to area_teeth_2sd_sinusPointsLength
        self.area_teeth_2sd_sinusPointsLength_height = ""
        self.area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_ID_key_a_path = ""
        self.area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_path = ""
        self.area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_apexF_path = ""
        self.area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_lobeF_path = ""
        self.resizedforruler_path = ""
        self.A_path = ""
        self.B_path = ""
        self.C_path = ""
        self.D_path = ""
        self.E_path = ""
        self.F_path = ""
        self.G_path = ""
        self.H_path = ""
        self.R_path = "" # path to resize
        self.H_hsv_path = "" # path to hsv
        # HTMLs
        self.html_summary_plot_leaf_eqd_cm_path = ""
        self.html_summary_plot_leaf_compactness_path = ""
        self.html_summary_plot_leaf_shape2_path = ""
        self.html_summary_plot_leaf_shape_path = ""
        self.html_summary_plot_leaf_teeth_path = ""
        self.html_summary_plot_leaf_morphological_cm_output_config_file_path = ""
        self.html_summary_plot_pixels_eqs_path = ""
        self.html_plot_pixels_morphological_path = ""
        self.html_summary_table_path = ""
        self.html_method_path = ""
        self.html_margin_path = ""
        self.html_shape_path = ""
        self.html_morphological_path = ""
        # PCA
        self.pca_output_config_file = ""
        # boxplots
        self.length_pixels_boxplot_path = ""
        self.width_pixels_boxplot_path = ""
        self.area_pixels_boxplot_path = ""
        self.perimeter_pixels_boxplot_path = ""
        self.eqd_pixels_boxplot_path = ""
        self.length_cm_boxplot_path = ""
        self.width_cm_boxplot_path = ""
        self.area_cm_boxplot_path = ""
        self.perimeter_cm_boxplot_path = ""
        self.number_of_teeth_boxplot_path = ""
        self.aspect_ratio_boxplot_path = ""
        self.perimeter_ratio_of_length_boxplot_path = ""
        self.perimeter_ratio_of_length_and_width_boxplot_path = ""
        self.roundness_boxplot_path = ""
        self.rectangularity_boxplot_path = ""
        self.perimeter_convexity_boxplot_path = ""
        self.area_convexity_boxplot_path = ""
        self.area_ratio_of_convexity_boxplot_path = ""
        self.compactness_boxplot_path = ""
        self.eqd_cm_boxplot_path = ""
        # html boxplots
        self.html_cm_boxplot_path = ""
        self.html_pixels_boxplot_path = ""


    def status_check(self, input_path, process):
        if os.path.exists(input_path):
            self.status = "#status_" + process + "=SUCCESS"
        else:
            self.status = "#status_" + process + "=FAIL"

    def status_check_label(self, label_accepted, process):
        if label_accepted:
            self.status = "#status_" + process + "=SUCCESS"
        else:
            self.status = "#status_" + process + "=FAIL"

    def label_string_output_config_file(self, label, label_accepted):
        self.label = label
        self.status_check_label(label_accepted, "label_string")
        print "Writing label string to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to label string\n")
        config.write(self.status + "\n")
        config.write("#PATH="+label+"\n")

    def original_image_output_config_file(self, input_image_path):
        print "input image path", input_image_path
        self.status_check(input_image_path, "initial_image")
        config = open(self.config_file_path, "w")
        print "Writing initial image to config file."
        config.write("#CONFIG FILE\n")
        config.write("\n#Path to initial image\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + input_image_path + "\n")
        config.close()

    def crop1_image_output_config_file(self, crop1_image_path):
        self.crop_image_path = crop1_image_path
        self.status_check(crop1_image_path, "crop1_image")
        print "Writing crop1 image to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to crop1 image\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + crop1_image_path + "\n")
        config.close()

    def rotate_image_output_config_file(self, rotate_image_path):
        self.rotate_image_path = rotate_image_path
        self.status_check(rotate_image_path, "rotate_image")
        print "Writing rotated image to config file."
        config = open(self.config_file_path , "a")
        config.write("\n#Path to rotated image\n")
        config.write(self.status + "\n")
        config.write("#PATH="+ rotate_image_path + "\n")
        config.close()

    def crop2_image_output_config_file(self, crop2_image_path):
        self.crop2_image_path = crop2_image_path
        self.status_check(crop2_image_path, "crop2_image")
        print "Writing crop2 image to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to crop2 image\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + crop2_image_path + "\n")
        config.close()

    def dilated_skinny_output_config_file(self, dilated_skinny_path):
        self.dilated_skinny_path = dilated_skinny_path
        self.status_check(dilated_skinny_path, "dilated_skinny_path")
        print "Writing dilated skinny image to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to dilated skinny image\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + dilated_skinny_path + "\n")
        config.close()

    def contours_output_config_file(self, contours_path):
        self.contours_path = contours_path
        self.status_check(contours_path, "contours_path")
        print "Writing contours image to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to contours image\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + contours_path + "\n")
        config.close()

    def contours_skinny_output_config_file(self, contours_skinny_path):
        self.contours_skinny_path = contours_skinny_path
        self.status_check(contours_skinny_path, "contours_skinny_path")
        print "Writing contours skinny image to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to contours skinny image\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + contours_skinny_path + "\n")
        config.close()

    def centroid_output_config_file(self, centroid_path):
        self.centroid_path = centroid_path
        self.status_check(centroid_path, "centroid_path")
        print "Writing centroid image to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to centroid image\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + centroid_path + "\n")
        config.close()

    def centroid_skinny_output_config_file(self, centroid_skinny_path):
        self.centroid_skinny_path = centroid_skinny_path
        self.status_check(centroid_skinny_path, "centroid_skinny_path")
        print "Writing centroid skinny image to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to centroid skinny image\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + centroid_skinny_path + "\n")
        config.close()

    def length_output_config_file(self, length_path):
        self.length_path = length_path
        self.status_check(length_path, "length_path")
        print "Writing length image to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to length image\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + length_path + "\n")
        config.close()

    def width_output_config_file(self, width_path):
        self.width_path = width_path
        self.status_check(width_path, "width_path")
        print "Writing width image to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to width image\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + width_path + "\n")
        config.close()

    def area_output_config_file(self, area_path):
        self.area_path = area_path
        self.status_check(area_path, "area_path")
        print "Writing area image to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to area image\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + area_path + "\n")
        config.close()

    def aspectratio_output_config_file(self, aspect_ratio_path):
        self.aspect_ratio_path = aspect_ratio_path
        self.status_check(aspect_ratio_path, "aspect_ratio_path")
        print "Writing aspect ratio image to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to aspect ratio image\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + aspect_ratio_path + "\n")
        config.close()

    def roundness_output_config_file(self, roundness_path):
        self.roundness_path = roundness_path
        self.status_check(roundness_path, "roundness_path")
        print "Writing roundness image to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to roundness image\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + roundness_path + "\n")
        config.close()

    def compactness_output_config_file(self, compactness_path):
        self.compactness_path = compactness_path
        self.status_check(compactness_path, "compactness_path")
        print "Writing compactness image to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to compactness image\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + compactness_path + "\n")
        config.close()

    def rectangularity_output_config_file(self, rectangularity_path):
        self.rectangularity_path = rectangularity_path
        self.status_check(rectangularity_path, "rectangularity_path")
        print "Writing rectangularity image to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to rectangularity image\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + rectangularity_path + "\n")
        config.close()

    def perimeterratiolength_output_config_file(self, perimeterratiolength_path):
        self.perimeterratiolength_path = perimeterratiolength_path
        self.status_check(perimeterratiolength_path, "perimeterratiolength_path")
        print "Writing perimeterratiolength image to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to perimeterratiolength image\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + perimeterratiolength_path + "\n")
        config.close()

    def perimeterratiolengthwidth_output_config_file(self, perimeterratiolengthwidth_path):
        self.perimeterratiolengthwidth_path = perimeterratiolengthwidth_path
        self.status_check(perimeterratiolengthwidth_path, "perimeterratiolengthwidth_path")
        print "Writing perimeterratiolengthwidth image to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to perimeterratiolengthwidth image\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + perimeterratiolengthwidth_path + "\n")
        config.close()

    def perimeterconvexity_output_config_file(self, perimeterconvexity_path):
        self.perimeterconvexity_path = perimeterconvexity_path
        self.status_check(perimeterconvexity_path, "perimeterconvexity_path")
        print "Writing perimeterconvexity image to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to perimeterconvexity image\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + perimeterconvexity_path + "\n")
        config.close()

    def areaconvexity_output_config_file(self, areaconvexity_path):
        self.areaconvexity_path = areaconvexity_path
        self.status_check(areaconvexity_path, "areaconvexity_path")
        print "Writing area convexity image to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to area convexity image\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + areaconvexity_path + "\n")
        config.close()

    def arearatioconvexity_output_config_file(self, arearatioconvexity_path):
        self.arearatioconvexity_path = arearatioconvexity_path
        self.status_check(arearatioconvexity_path, "arearatioconvexity_path")
        print "Writing area ratio convexity image to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to area ratio convexity image\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + arearatioconvexity_path + "\n")
        config.close()

    def equivalentdiameter_output_config_file(self, equivalentdiameter_path):
        self.equivalentdiameter_path = equivalentdiameter_path
        self.status_check(equivalentdiameter_path, "equivalentdiameter_path")
        print "Writing equivalent diameter image to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to equivalent diameter image\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + equivalentdiameter_path + "\n")
        config.close()

    def area_teeth_output_config_file(self, area_teeth_path):
        self.area_teeth_path = area_teeth_path
        self.status_check(area_teeth_path, "area_teeth_path")
        print "Writing area teeth image to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to area teeth image\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + area_teeth_path + "\n")
        config.close()

    def area_teeth_2sd_output_config_file(self, area_teeth_2sd_path):
        self.area_teeth_2sd_path = area_teeth_2sd_path
        self.status_check(area_teeth_2sd_path, "area_teeth_2sd_path")
        print "Writing area teeth 2sd image to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to area teeth 2sd image\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + area_teeth_2sd_path + "\n")
        config.close()

    def area_teeth_2sd_sinusPointsLength_output_config_file(self, area_teeth_2sd_sinusPointsLength_path):
        self.area_teeth_2sd_sinusPointsLength = area_teeth_2sd_sinusPointsLength_path
        self.status_check(area_teeth_2sd_sinusPointsLength_path, "area_teeth_2sd_sinusPointsLength_path")
        print "Writing area_teeth_2sd_sinusPointsLength image to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to area_teeth_2sd_sinusPointsLength image\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + area_teeth_2sd_sinusPointsLength_path + "\n")
        config.close()

    def area_teeth_2sd_sinusPointsLength_height_output_config_file(self, area_teeth_2sd_sinusPointsLength_height_path):
        self.area_teeth_2sd_sinusPointsLength_height = area_teeth_2sd_sinusPointsLength_height_path
        self.status_check(area_teeth_2sd_sinusPointsLength_height_path, "area_teeth_2sd_sinusPointsLength_height_path")
        print "Writing area_teeth_2sd_sinusPointsLength_height_path image to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to area_teeth_2sd_sinusPointsLength_height_pathimage\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + area_teeth_2sd_sinusPointsLength_height_path + "\n")
        config.close()

    def area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_ID_key_a_output_config_file(self, area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_ID_key_a_path):
        self.area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_ID_key_a_path = area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_ID_key_a_path
        self.status_check(area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_ID_key_a_path, "area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_ID_key_a_path")
        print "Writing area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_ID_key_a_path image to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_ID_key_a_path\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_ID_key_a_path + "\n")
        config.close()
    def area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_output_config_file(self, area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_path):
        self.area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_path = area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_path
        self.status_check(area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_path, "area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_path")
        print "Writing area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_ID_key_a_path image to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to area_teeth_2sd_sinusPointsLength_height_overlapsFiltered\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_path + "\n")
        config.close()

    def area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_apexF_output_config_file(self, area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_apexF_path):
        self.area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_apexF_path = area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_apexF_path
        self.status_check(area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_apexF_path, "area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_apexF_path")
        print "Writing area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_apexF_path image to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_apexF_path\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_apexF_path + "\n")
        config.close()

    def area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_lobeF_output_config_file(self, area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_lobeF_path):
        self.area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_lobeF_path = area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_lobeF_path
        self.status_check(area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_lobeF_path, "area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_lobeF_path")
        print "Writing area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_lobeF_path image to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_lobeF_path\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_lobeF_path + "\n")
        config.close()
    def resizedforruler_output_config_file(self,resizedforruler_path):
        self.resizedforruler_path = resizedforruler_path
        self.status_check(resizedforruler_path, "resizedforruler_path")
        print "Writing resizedforruler_path image to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to resizedforruler_path\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + resizedforruler_path + "\n")
        config.close()
    def A_output_config_file(self, A_path):
        self.A_path = A_path
        self.status_check(A_path, "A_path")
        print "Writing rotated transformation (A) image to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to rotated transformation (A)\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + A_path + "\n")
        config.close()

    def B_output_config_file(self, B_path):
        self.B_path = B_path
        self.status_check(B_path, "B_path")
        print "Writing greyscale transformation (B) image to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to greyscale transformation (B)\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + B_path + "\n")
        config.close()

    def C_output_config_file(self, C_path):
        self.C_path = C_path
        self.status_check(C_path, "C_path")
        print "Writing adaptive threshold transformation (C) image to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to adaptive threshold transformation (C) \n")
        config.write(self.status + "\n")
        config.write("#PATH=" + C_path + "\n")
        config.close()

    def D_output_config_file(self, D_path):
        self.D_path = D_path
        self.status_check(D_path, "D_path")
        print "Writing crop transformation image to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to crop transformation (D)\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + D_path + "\n")
        config.close()

    def E_output_config_file(self, E_path):
        self.E_path = E_path
        self.status_check(E_path, "E_path")
        print "Writing denoise the image(E) image to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to denoise the image (E)\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + E_path + "\n")
        config.close()

    def F_output_config_file(self, F_path):
        self.F_path = F_path
        self.status_check(F_path, "F_path")
        print "Writing global_thresholding F_path image to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to global_thresholding (F)\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + F_path + "\n")
        config.close()

    def G_output_config_file(self, G_path):
        self.G_path = G_path
        self.status_check(G_path, "G_path")
        print "Writing otsus_thresholding (G) image to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to otsus_thresholding (G)\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + G_path + "\n")
        config.close()

    def H_output_config_file(self, H_path):
        self.H_path = H_path
        self.status_check(H_path, "H_path")
        print "Writing gaussian_filtering_otsus_thresholding (H) image to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to gaussian_filtering_otsus_thresholding (H)\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + H_path + "\n")
        config.close()

    def H_hsv_output_config_file(self, H_hsv_path):
        self.H_hsv_path = H_hsv_path
        self.status_check(H_hsv_path, "H_hsv_path")
        print "Writing H_hsv_path image to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to H_hsv_path\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + H_hsv_path + "\n")
        config.close()

    def R_resize_output_config_file(self, R_path):
        self.R_path = R_path
        self.status_check(R_path, "R_path")
        print "Writing R_path image to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to resized image (R_path)\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + R_path + "\n")
        config.close()
    ############# HTML##############
    def html_morphological_output_config_file(self, html_morphological_path):
        self.html_morphological_path = html_morphological_path
        self.status_check(html_morphological_path, "html_morphological_path")
        print "Writing html morphological descriptors to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to html morphological descriptors \n")
        config.write(self.status + "\n")
        config.write("#PATH=" + html_morphological_path + "\n")
        config.close()

    def html_shape_output_config_file(self, html_shape_path):
        self.html_shape_path = html_shape_path
        self.status_check(html_shape_path, "html_shape_path")
        print "Writing html shape descriptors to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to html shape descriptors \n")
        config.write(self.status + "\n")
        config.write("#PATH=" + html_shape_path + "\n")
        config.close()


    def html_margin_output_config_file(self, html_margin_path):
        self.html_margin_path = html_margin_path
        self.status_check(html_margin_path, "html_margin_path")
        print "Writing html leaf margin to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to html leaf margin \n")
        config.write(self.status + "\n")
        config.write("#PATH=" + html_margin_path + "\n")
        config.close()

    def html_method_output_config_file(self, html_method_path):
        self.html_method_path = html_method_path
        self.status_check(html_method_path, "html_method_path")
        print "Writing html method to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to html method\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + html_method_path + "\n")
        config.close()

    def html_summary_output_config_file(self, html_summary_table_path):
        self.html_summary_table_path = html_summary_table_path
        self.status_check(html_summary_table_path, "html_summary_table_path")
        print "Writing html summary table to config file.", html_summary_table_path
        config = open(self.config_file_path, "w")
        config.write("#SUMMARY CONFIG FILE\n")
        config.write("\n#Path to html summary table\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + html_summary_table_path + "\n")
        config.close()

    def html_plot_pixels_morphological_output_config_file(self, html_plot_pixels_morphological_path):
        self.html_plot_pixels_morphological_path = html_plot_pixels_morphological_path
        self.status_check(html_plot_pixels_morphological_path, "html_plot_pixels_morphological_path")
        print "Writing html plot in pixels of morphological descriptors to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to html plot in pixels of morphological descriptors \n")
        config.write(self.status + "\n")
        config.write("#PATH=" + html_plot_pixels_morphological_path + "\n")
        config.close()

    def html_summary_plot_pixels_eqs_output_config_file(self, html_summary_plot_pixels_eqs_path):
        self.html_summary_plot_pixels_eqs_path = html_summary_plot_pixels_eqs_path
        self.status_check(html_summary_plot_pixels_eqs_path, "html_summary_plot_pixels_eqs_path")
        print "Writing html summary plot in pixels of Equivalent Diameter to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to html plot in pixels of Equivalent Diameter\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + html_summary_plot_pixels_eqs_path + "\n")
        config.close()

    def html_summary_plot_leaf_morphological_cm_output_config_file(self, html_summary_plot_leaf_morphological_cm_output_config_file_path):
        self.html_summary_plot_leaf_morphological_cm_output_config_file_path = html_summary_plot_leaf_morphological_cm_output_config_file_path
        self.status_check(html_summary_plot_leaf_morphological_cm_output_config_file_path, "html_summary_plot_leaf_morphological_cm_output_config_file_path")
        print "Writing html summary plot in cm of Morphological Descriptors to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to html plot in pixels of Morphological Descriptors\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + html_summary_plot_leaf_morphological_cm_output_config_file_path + "\n")
        config.close()

    def html_summary_plot_leaf_teeth_output_config_file(self, html_summary_plot_leaf_teeth_path):
        self.html_summary_plot_leaf_teeth_path = html_summary_plot_leaf_teeth_path
        self.status_check(html_summary_plot_leaf_teeth_path, "html_summary_plot_leaf_teeth_path")
        print "Writing html summary plot of Leaf Teeth to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to html plot of Leaf teeth\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + html_summary_plot_leaf_teeth_path + "\n")
        config.close()

    def html_summary_plot_leaf_shape_output_config_file(self, html_summary_plot_leaf_shape_path):
        self.html_summary_plot_leaf_shape_path = html_summary_plot_leaf_shape_path
        self.status_check(html_summary_plot_leaf_shape_path, "html_summary_plot_leaf_shape_path")
        print "Writing html summary plot of Leaf Shape 1 to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to html plot of Leaf Shape1\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + html_summary_plot_leaf_shape_path + "\n")
        config.close()

    def html_summary_plot_leaf_shape2_output_config_file(self, html_summary_plot_leaf_shape2_path):
        self.html_summary_plot_leaf_shape2_path = html_summary_plot_leaf_shape2_path
        self.status_check(html_summary_plot_leaf_shape2_path, "html_summary_plot_leaf_shape2_path")
        print "Writing html summary plot of Leaf Shape 2 to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to html plot of Leaf Shape2\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + html_summary_plot_leaf_shape2_path + "\n")
        config.close()

    def html_summary_plot_leaf_compactness_output_config_file(self, html_summary_plot_leaf_compactness_path):
        self.html_summary_plot_leaf_compactness_path = html_summary_plot_leaf_compactness_path
        self.status_check(html_summary_plot_leaf_compactness_path, "html_summary_plot_leaf_compactness_path")
        print "Writing html summary plot of Leaf compactness to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to html plot of Leaf compactness\n")
        config.write(self.status + "\n")
        config.write("#PATH=" + html_summary_plot_leaf_compactness_path + "\n")
        config.close()

    def html_summary_plot_leaf_eqd_cm_output_config_file(self, html_summary_plot_leaf_eqd_cm_path):
        self.html_summary_plot_leaf_eqd_cm_path = html_summary_plot_leaf_eqd_cm_path
        self.status_check(html_summary_plot_leaf_eqd_cm_path, "html_summary_plot_leaf_eqd_cm_path")
        print "Writing html summary plot of Leaf Equivalent diameter in cm to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to html plot of Leaf Equivalent diameter in cm \n")
        config.write(self.status + "\n")
        config.write("#PATH=" + html_summary_plot_leaf_eqd_cm_path + "\n")
        config.close()

    def pca_output_config_file(self, pca_path):
        self.pca_output_config_file = pca_path
        self.status_check(pca_path, "pca_path")
        print "Writing PCA plots to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to PCA plots \n")
        config.write(self.status + "\n")
        config.write("#PATH=" + pca_path + "\n")
        config.close()

    def length_pixels_boxplot_output_config_file(self, length_pixels_boxplot_path):
        self.length_pixels_boxplot_path = length_pixels_boxplot_path
        self.status_check(length_pixels_boxplot_path, "length_pixels_boxplot_path")
        print "Writing length_pixels_boxplot_path to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to length_pixels_boxplot_path \n")
        config.write(self.status + "\n")
        config.write("#PATH=" + length_pixels_boxplot_path + "\n")
        config.close()

    def width_pixels_boxplot_output_config_file(self, width_pixels_boxplot_path):
        self.width_pixels_boxplot_path = width_pixels_boxplot_path
        self.status_check(width_pixels_boxplot_path, "width_pixels_boxplot_path")
        print "Writing width_pixels_boxplot_path to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to width_pixels_boxplot_path \n")
        config.write(self.status + "\n")
        config.write("#PATH=" + width_pixels_boxplot_path + "\n")
        config.close()

    def area_pixels_boxplot_output_config_file(self, area_pixels_boxplot_path):
        self.area_pixels_boxplot_path = area_pixels_boxplot_path
        self.status_check(area_pixels_boxplot_path, "area_pixels_boxplot_path")
        print "Writing area_pixels_boxplot_path to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to area_pixels_boxplot_path \n")
        config.write(self.status + "\n")
        config.write("#PATH=" + area_pixels_boxplot_path + "\n")
        config.close()

    def perimeter_pixels_boxplot_output_config_file(self, perimeter_pixels_boxplot_path):
        self.perimeter_pixels_boxplot_path = perimeter_pixels_boxplot_path
        self.status_check(perimeter_pixels_boxplot_path, "perimeter_pixels_boxplot_path")
        print "Writing perimeter_pixels_boxplot_path to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to perimeter_pixels_boxplot_path \n")
        config.write(self.status + "\n")
        config.write("#PATH=" + perimeter_pixels_boxplot_path + "\n")
        config.close()

    def eqd_pixels_boxplot_output_config_file(self, eqd_pixels_boxplot_path):
        self.eqd_pixels_boxplot_path = eqd_pixels_boxplot_path
        self.status_check(eqd_pixels_boxplot_path, "eqd_pixels_boxplot_path")
        print "Writing eqd_pixels_boxplot_path to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to eqd_pixels_boxplot_path \n")
        config.write(self.status + "\n")
        config.write("#PATH=" + eqd_pixels_boxplot_path + "\n")
        config.close()

    def length_cm_boxplot_output_config_file(self, length_cm_boxplot_path):
        self.length_cm_boxplot_path = length_cm_boxplot_path
        self.status_check(length_cm_boxplot_path, "length_cm_boxplot_path")
        print "Writing length_cm_boxplot_path to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to length_cm_boxplot_path \n")
        config.write(self.status + "\n")
        config.write("#PATH=" + length_cm_boxplot_path + "\n")
        config.close()

    def width_cm_boxplot_output_config_file(self, width_cm_boxplot_path):
        self.width_cm_boxplot_path = width_cm_boxplot_path
        self.status_check(width_cm_boxplot_path, "width_cm_boxplot_path")
        print "Writing width_cm_boxplot_path to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to width_cm_boxplot_path \n")
        config.write(self.status + "\n")
        config.write("#PATH=" + width_cm_boxplot_path + "\n")
        config.close()

    def area_cm_boxplot_output_config_file(self, area_cm_boxplot_path):
        self.area_cm_boxplot_path = area_cm_boxplot_path
        self.status_check(area_cm_boxplot_path, "area_cm_boxplot_path")
        print "Writing area_cm_boxplot_path to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to area_cm_boxplot_path \n")
        config.write(self.status + "\n")
        config.write("#PATH=" + area_cm_boxplot_path + "\n")
        config.close()

    def perimeter_cm_boxplot_output_config_file(self, perimeter_cm_boxplot_path):
        self.perimeter_cm_boxplot_path = perimeter_cm_boxplot_path
        self.status_check(perimeter_cm_boxplot_path, "perimeter_cm_boxplot_path")
        print "Writing perimeter_cm_boxplot_path to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to perimeter_cm_boxplot_path \n")
        config.write(self.status + "\n")
        config.write("#PATH=" + perimeter_cm_boxplot_path + "\n")
        config.close()

    def number_of_teeth_boxplot_output_config_file(self, number_of_teeth_boxplot_path):
        self.number_of_teeth_boxplot_path = number_of_teeth_boxplot_path
        self.status_check(number_of_teeth_boxplot_path, "number_of_teeth_boxplot_path")
        print "Writing number_of_teeth_boxplot_path to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to number_of_teeth_boxplot_path \n")
        config.write(self.status + "\n")
        config.write("#PATH=" + number_of_teeth_boxplot_path + "\n")
        config.close()

    def aspect_ratio_boxplot_output_config_file(self, aspect_ratio_boxplot_path):
        self.aspect_ratio_boxplot_path = aspect_ratio_boxplot_path
        self.status_check(aspect_ratio_boxplot_path, "aspect_ratio_boxplot_path")
        print "Writing aspect_ratio_boxplot_path to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to aspect_ratio_boxplot_path \n")
        config.write(self.status + "\n")
        config.write("#PATH=" + aspect_ratio_boxplot_path + "\n")
        config.close()

    def perimeter_ratio_of_length_boxplot_output_config_file(self, perimeter_ratio_of_length_boxplot_path):
        self.perimeter_ratio_of_length_boxplot_path = perimeter_ratio_of_length_boxplot_path
        self.status_check(perimeter_ratio_of_length_boxplot_path, "perimeter_ratio_of_length_boxplot_path")
        print "Writing perimeter_ratio_of_length_boxplot_path to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to perimeter_ratio_of_length_boxplot_path \n")
        config.write(self.status + "\n")
        config.write("#PATH=" + perimeter_ratio_of_length_boxplot_path + "\n")
        config.close()

    def perimeter_ratio_of_length_and_width_boxplot_output_config_file(self, perimeter_ratio_of_length_and_width_boxplot_path):
        self.perimeter_ratio_of_length_and_width_boxplot_path = perimeter_ratio_of_length_and_width_boxplot_path
        self.status_check(perimeter_ratio_of_length_and_width_boxplot_path, "perimeter_ratio_of_length_and_width_boxplot_path")
        print "Writing perimeter_ratio_of_length_and_width_boxplot_path to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to perimeter_ratio_of_length_and_width_boxplot_path \n")
        config.write(self.status + "\n")
        config.write("#PATH=" + perimeter_ratio_of_length_and_width_boxplot_path + "\n")
        config.close()

    def roundness_boxplot_output_config_file(self, roundness_boxplot_path):
        self.roundness_boxplot_path = roundness_boxplot_path
        self.status_check(roundness_boxplot_path, "roundness_boxplot_path")
        print "Writing roundness_boxplot_path to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to roundness_boxplot_path \n")
        config.write(self.status + "\n")
        config.write("#PATH=" + roundness_boxplot_path + "\n")
        config.close()

    def rectangularity_boxplot_output_config_file(self, rectangularity_boxplot_path):
        self.rectangularity_boxplot_path = rectangularity_boxplot_path
        self.status_check(rectangularity_boxplot_path, "rectangularity_boxplot_path")
        print "Writing rectangularity_boxplot_path to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to rectangularity_boxplot_path \n")
        config.write(self.status + "\n")
        config.write("#PATH=" + rectangularity_boxplot_path + "\n")
        config.close()


    def perimeter_convexity_boxplot_output_config_file(self, perimeter_convexity_boxplot_path):
        self.perimeter_convexity_boxplot_path = perimeter_convexity_boxplot_path
        self.status_check(perimeter_convexity_boxplot_path, "perimeter_convexity_boxplot_path")
        print "Writing perimeter_convexity_boxplot_path to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to perimeter_convexity_boxplot_path \n")
        config.write(self.status + "\n")
        config.write("#PATH=" + perimeter_convexity_boxplot_path + "\n")
        config.close()


    def area_convexity_boxplot_output_config_file(self, area_convexity_boxplot_path):
        self.area_convexity_boxplot_path = area_convexity_boxplot_path
        self.status_check(area_convexity_boxplot_path, "area_convexity_boxplot_path")
        print "Writing area_convexity_boxplot_path to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to area_convexity_boxplot_path \n")
        config.write(self.status + "\n")
        config.write("#PATH=" + area_convexity_boxplot_path + "\n")
        config.close()


    def area_ratio_of_convexity_boxplot_output_config_file(self, area_ratio_of_convexity_boxplot_path):
        self.area_ratio_of_convexity_boxplot_path = area_ratio_of_convexity_boxplot_path
        self.status_check(area_ratio_of_convexity_boxplot_path, "area_ratio_of_convexity_boxplot_path")
        print "Writing area_ratio_of_convexity_boxplot_path to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to area_ratio_of_convexity_boxplot_path \n")
        config.write(self.status + "\n")
        config.write("#PATH=" + area_ratio_of_convexity_boxplot_path + "\n")
        config.close()


    def compactness_boxplot_output_config_file(self, compactness_boxplot_path):
        self.compactness_boxplot_path = compactness_boxplot_path
        self.status_check(compactness_boxplot_path, "compactness_boxplot_path")
        print "Writing compactness_boxplot_path to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to compactness_boxplot_path \n")
        config.write(self.status + "\n")
        config.write("#PATH=" + compactness_boxplot_path + "\n")
        config.close()


    def eqd_cm_boxplot_output_config_file(self, eqd_cm_boxplot_path):
        self.eqd_cm_boxplot_path = eqd_cm_boxplot_path
        self.status_check(eqd_cm_boxplot_path, "eqd_cm_boxplot_path")
        print "Writing eqd_cm_boxplot_path to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to eqd_cm_boxplot_path \n")
        config.write(self.status + "\n")
        config.write("#PATH=" + eqd_cm_boxplot_path + "\n")
        config.close()

    def html_boxplot_pixels_output_config_file(self, html_pixels_boxplot_path):
        self.html_pixels_boxplot_path = html_pixels_boxplot_path
        self.status_check(html_pixels_boxplot_path, "html_pixels_boxplot_path")
        print "Writing html_pixels_boxplot_path to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to html_pixels_boxplot_path \n")
        config.write(self.status + "\n")
        config.write("#PATH=" + html_pixels_boxplot_path + "\n")
        config.close()

    def html_boxplot_cm_output_config_file(self, html_cm_boxplot_path):
        self.html_cm_boxplot_path = html_cm_boxplot_path
        self.status_check(html_cm_boxplot_path, "html_cm_boxplot_path")
        print "Writing html_cm_boxplot_path to config file."
        config = open(self.config_file_path, "a")
        config.write("\n#Path to html_cm_boxplot_path \n")
        config.write(self.status + "\n")
        config.write("#PATH=" + html_cm_boxplot_path + "\n")
        config.close()
