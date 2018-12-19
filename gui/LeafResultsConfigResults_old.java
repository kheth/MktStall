package mktstall;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;


public class LeafResultsConfigResults_old {

    //TODO : add summary config stuff
    //individual status
    boolean status_initial_image;
    boolean status_crop1_image;
    boolean status_rotate_image;
    boolean status_crop2_image;
    boolean status_dilated_skinny_path;
    boolean status_contours_path;
    boolean status_contours_skinny_path;
    boolean status_centroid_path;
    boolean status_centroid_skinny_path;
    boolean status_length_path;
    boolean status_width_path;
    boolean status_area_path;
    boolean status_aspect_ratio_path;
    boolean status_roundness_path;
    boolean status_compactness_path;
    boolean status_rectangularity_path;
    boolean status_perimeterratiolength_path;
    boolean status_perimeterratiolengthwidth_path;
    boolean status_perimeterconvexity_path;
    boolean status_areaconvexity_path;
    boolean status_arearatioconvexity_path;
    boolean status_equivalentdiameter_path;
    boolean status_area_teeth_path;
    boolean status_area_teeth_2sd_path;
    boolean status_area_teeth_2sd_sinusPointsLength_path;
    boolean status_area_teeth_2sd_sinusPointsLength_height_path;
    boolean status_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_apexF_path;
    boolean status_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_lobeF_path;
    boolean status_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_ID_key_a_path;
    boolean status_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_path;
    boolean status_html_morphological_path;
    boolean status_html_shape_path;
    boolean status_html_margin_path;
    boolean status_html_method_path;
    //summary status
    boolean status_html_summary_table_path;
    boolean status_html_plot_pixels_morphological_path;
    boolean status_html_summary_plot_pixels_eqs_path;
    boolean status_html_summary_plot_leaf_morphological_cm_output_config_file_path;
    boolean status_html_summary_plot_leaf_teeth_path;
    boolean status_html_summary_plot_leaf_shape_path;
    boolean status_html_summary_plot_leaf_shape2_path;
    boolean status_html_summary_plot_leaf_compactness_path;
    boolean status_html_summary_plot_leaf_eqd_cm_path;
    //individual image paths
    String initial_image;
    String crop1_image;
    String rotate_image;
    String crop2_image;
    String dilated_skinny_path;
    String contours_path;
    String contours_skinny_path;
    String centroid_path;
    String centroid_skinny_path;
    String length_path;
    String width_path;
    String area_path;
    String aspect_ratio_path;
    String roundness_path;
    String compactness_path;
    String rectangularity_path;
    String perimeterratiolength_path;
    String perimeterratiolengthwidth_path;
    String perimeterconvexity_path;
    String areaconvexity_path;
    String arearatioconvexity_path;
    String equivalentdiameter_path;
    String area_teeth_path;
    String area_teeth_2sd_path;
    String area_teeth_2sd_sinusPointsLength_path;
    String area_teeth_2sd_sinusPointsLength_height_path;
    String area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_apexF_path;
    String area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_lobeF_path;
    String area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_ID_key_a_path;
    String area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_path;
    String html_morphological_path;
    String html_shape_path;
    String html_margin_path;
    String html_method_path;
    //summary image paths
    String html_summary_table_path;
    String html_plot_pixels_morphological_path;
    String html_summary_plot_pixels_eqs_path;
    String html_summary_plot_leaf_morphological_cm_output_config_file_path;
    String html_summary_plot_leaf_teeth_path;
    String html_summary_plot_leaf_shape_path;
    String html_summary_plot_leaf_shape2_path;
    String html_summary_plot_leaf_compactness_path;
    String html_summary_plot_leaf_eqd_cm_path;

    // read in config
    
    /**
     * Read in config file and populate field.
     *
     * @param filepathToConfig
     */
    String filepathToConfig= "~/mktstall/mktstall_py/results/summary_output.config_output.config";
    public void ReadLeafConfig(String filepathToConfig) throws FileNotFoundException, IOException {
        Scanner configScanner = new Scanner(new File(filepathToConfig));
        ArrayList<String> configStrings = new ArrayList<String>();
        while (configScanner.hasNext()) {
            configStrings.add(configScanner.next());
        }
        configScanner.close();
        // for each in the array list
        for(String c :configStrings){
            // CHECKING STATUS
            if (c.startsWith("#status_")){
                String[] statusString;
                String[] status;
                statusString = c.split("#status_");
                status = statusString[0].split("=");
                if(status[0].matches("initial_image")){
                    if (status[1].matches("SUCCESS")){
                      status_initial_image = true;
                    } else{
                      status_initial_image = false;
                    }
                } else if(status[0].matches("crop1_image")){
                    if (status[1].matches("SUCCESS")){
                      status_crop1_image = true;
                    } else{
                      status_crop1_image = false;
                    }
                } else if(status[0].matches("rotate_image")){
                    if (status[1].matches("SUCCESS")){
                      status_rotate_image = true;
                    } else{
                      status_rotate_image = false;
                    }
                } else if(status[0].matches("crop2_image")){
                    if (status[1].matches("SUCCESS")){
                      status_crop2_image = true;
                    } else{
                      status_crop2_image = false;
                    }
                } else if(status[0].matches("dilated_skinny_path")){
                    if (status[1].matches("SUCCESS")){
                      status_dilated_skinny_path = true;
                    } else{
                      status_dilated_skinny_path = false;
                    }
                } else if(status[0].matches("contours_path")){
                    if (status[1].matches("SUCCESS")){
                      status_contours_path = true;
                    } else{
                      status_contours_path = false;
                    }
                } else if(status[0].matches("contours_skinny_path")){
                    if (status[1].matches("SUCCESS")){
                      status_contours_path = true;
                    } else{
                      status_contours_path = false;
                    }
                } else if(status[0].matches("centroid_path")){
                    if (status[1].matches("SUCCESS")){
                      status_centroid_path = true;
                    } else{
                      status_centroid_path = false;
                    }
                } else if(status[0].matches("centroid_skinny_path")){
                    if (status[1].matches("SUCCESS")){
                      status_centroid_skinny_path = true;
                    } else{
                      status_centroid_skinny_path = false;
                    }
                } else if(status[0].matches("length_path")){
                    if (status[1].matches("SUCCESS")){
                      status_length_path = true;
                    } else{
                      status_length_path = false;
                    }
                } else if(status[0].matches("width_path")){
                    if (status[1].matches("SUCCESS")){
                      status_width_path = true;
                    } else{
                      status_width_path = false;
                    }
                } else if(status[0].matches("area_path")){
                    if (status[1].matches("SUCCESS")){
                      status_area_path = true;
                    } else{
                      status_area_path = false;
                    }
                } else if(status[0].matches("roundness_path")){
                    if (status[1].matches("SUCCESS")){
                      status_roundness_path = true;
                    } else{
                      status_roundness_path = false;
                    }
                } else if(status[0].matches("compactness_path")){
                    if (status[1].matches("SUCCESS")){
                      status_compactness_path = true;
                    } else{
                      status_compactness_path = false;
                    }
                } else if(status[0].matches("rectangularity_path")){
                    if (status[1].matches("SUCCESS")){
                      status_rectangularity_path = true;
                    } else{
                      status_rectangularity_path = false;
                    }
                } else if(status[0].matches("perimeterratiolength_path")){
                    if (status[1].matches("SUCCESS")){
                      status_perimeterratiolength_path = true;
                    } else{
                      status_perimeterratiolength_path = false;
                    }
                } else if(status[0].matches("perimeterratiolengthwidth_path")){
                    if (status[1].matches("SUCCESS")){
                      status_perimeterratiolengthwidth_path = true;
                    } else{
                      status_perimeterratiolengthwidth_path = false;
                    }
                } else if(status[0].matches("perimeterconvexity_path")){
                    if (status[1].matches("SUCCESS")){
                      status_perimeterconvexity_path= true;
                    } else{
                      status_perimeterconvexity_path = false;
                    }
                } else if(status[0].matches("areaconvexity_path")){
                    if (status[1].matches("SUCCESS")){
                      status_areaconvexity_path= true;
                    } else{
                      status_areaconvexity_path = false;
                    }
                } else if(status[0].matches("arearatioconvexity_path")){
                    if (status[1].matches("SUCCESS")){
                      status_arearatioconvexity_path= true;
                    } else{
                      status_arearatioconvexity_path = false;
                    }
                } else if(status[0].matches("equivalentdiameter_path")){
                    if (status[1].matches("SUCCESS")){
                      status_equivalentdiameter_path= true;
                    } else{
                      status_equivalentdiameter_path = false;
                    }
                } else if(status[0].matches("area_teeth_2sd_path")){
                    if (status[1].matches("SUCCESS")){
                      status_area_teeth_2sd_path= true;
                    } else{
                      status_area_teeth_2sd_path = false;
                    }
                } else if(status[0].matches("area_teeth_2sd_sinusPointsLength_path")){
                    if (status[1].matches("SUCCESS")){
                      status_area_teeth_2sd_sinusPointsLength_path= true;
                    } else{
                      status_area_teeth_2sd_sinusPointsLength_path = false;
                    }
                } else if(status[0].matches("area_teeth_2sd_sinusPointsLength_height_path")){
                    if (status[1].matches("SUCCESS")){
                      status_area_teeth_2sd_sinusPointsLength_height_path= true;
                    } else{
                      status_area_teeth_2sd_sinusPointsLength_height_path = false;
                    }
                } else if(status[0].matches("area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_apexF_path")){
                    if (status[1].matches("SUCCESS")){
                      status_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_apexF_path= true;
                    } else{
                      status_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_apexF_path = false;
                    }
                } else if(status[0].matches("area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_lobeF_path")){
                    if (status[1].matches("SUCCESS")){
                      status_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_lobeF_path= true;
                    } else{
                      status_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_lobeF_path = false;
                    }
                } else if(status[0].matches("area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_ID_key_a_path")){
                    if (status[1].matches("SUCCESS")){
                      status_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_ID_key_a_path= true;
                    } else{
                      status_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_ID_key_a_path = false;
                    }
                } else if(status[0].matches("area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_path")){
                    if (status[1].matches("SUCCESS")){
                      status_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_path= true;
                    } else{
                      status_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_path = false;
                    }
                } else if(status[0].matches("html_morphological_path")){
                    if (status[1].matches("SUCCESS")){
                      status_html_morphological_path= true;
                    } else{
                      status_html_morphological_path = false;
                    }
                } else if(status[0].matches("html_shape_path")){
                    if (status[1].matches("SUCCESS")){
                      status_html_shape_path= true;
                    } else{
                      status_html_shape_path = false;
                    }
                } else if(status[0].matches("html_margin_path")){
                    if (status[1].matches("SUCCESS")){
                      status_html_margin_path= true;
                    } else{
                      status_html_margin_path = false;
                    }
                } else if(status[0].matches("html_method_path")){
                    if (status[1].matches("SUCCESS")){
                      status_html_method_path = true;
                    } else{
                      status_html_method_path = false;
                    }
                } else if(status[0].matches("html_summary_table_path")){
                    if (status[1].matches("SUCCESS")){
                      status_html_summary_table_path = true;
                    } else{
                      status_html_summary_table_path = false;
                    }
                } else if(status[0].matches("html_plot_pixels_morphological_path")){
                    if (status[1].matches("SUCCESS")){
                      status_html_plot_pixels_morphological_path = true;
                    } else{
                      status_html_plot_pixels_morphological_path = false;
                    }
                } else if(status[0].matches("html_summary_plot_pixels_eqs_path")){
                    if (status[1].matches("SUCCESS")){
                      status_html_summary_plot_pixels_eqs_path = true;
                    } else{
                      status_html_summary_plot_pixels_eqs_path = false;
                    }
                } else if(status[0].matches("html_summary_plot_leaf_morphological_cm_output_config_file_path")){
                    if (status[1].matches("SUCCESS")){
                      status_html_summary_plot_leaf_morphological_cm_output_config_file_path = true;
                    } else{
                      status_html_summary_plot_leaf_morphological_cm_output_config_file_path = false;
                    }
                } else if(status[0].matches("html_summary_plot_leaf_teeth_path")){
                    status_html_summary_plot_leaf_teeth_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("html_summary_plot_leaf_shape2_path")){
                    status_html_summary_plot_leaf_shape2_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("html_summary_plot_leaf_compactness_path")){
                    status_html_summary_plot_leaf_compactness_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("html_summary_plot_leaf_eqd_cm_path")){
                    status_html_summary_plot_leaf_eqd_cm_path = status[1].matches("SUCCESS");
                }else {
                    System.out.println("no status found");
                }   
            }
            for(String p : configStrings){
                // CHECKING STATUS
                if (p.startsWith("#PATH=")){
                    String[] pathString;
                    
                    String[] fileTokens;
                    pathString = p.split("PATH=");
                    System.out.println("#PATH STRING:::::: 0  "+pathString[0]);
                    System.out.println("#PATH STRING:::::: 1  "+pathString[1]);
                    fileTokens = pathString[1].split("/");
                    if(fileTokens[fileTokens.length-1].endsWith(".cr.jpg")){
                        crop1_image = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].endsWith(".cr.jpg.ro.jpg")){
                        rotate_image = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].endsWith(".cr.jpg.ro.jpg.c2.jpg")){
                        crop2_image = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].endsWith(".cr.jpg.ro.jpg.c2.jpgdilated_skinny.jpg")){
                        dilated_skinny_path = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].endsWith(".cr.jpg.ro.jpg.c2.jpg.contours.jpg")){
                        contours_path = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].endsWith(".cr.jpg.ro.jpg.c2.jpg.contours_skinny.jpg")){
                        contours_skinny_path = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].endsWith(".cr.jpg.ro.jpg.c2.jpg.centroid.jpg")){
                        centroid_path = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].endsWith(".cr.jpg.ro.jpg.c2.jpg.centroid_skinny.jpg")){
                        centroid_skinny_path = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].endsWith(".cr.jpg.ro.jpg.c2.jpg.length.jpg")){
                        length_path = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].endsWith(".cr.jpg.ro.jpg.c2.jpg.width.jpg")){
                        width_path = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].endsWith(".cr.jpg.ro.jpg.c2.jpg.area.jpg")){
                        area_path = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].endsWith(".cr.jpg.ro.jpg.c2.jpg.aspectratio.jpg")){
                        aspect_ratio_path = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].endsWith(".cr.jpg.ro.jpg.c2.jpg.roundness.jpg")){
                        roundness_path = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].endsWith(".cr.jpg.ro.jpg.c2.jpg.compactness.jpg")){
                        compactness_path = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].endsWith(".cr.jpg.ro.jpg.c2.jpg.rectangularity.jpg")){
                        rectangularity_path = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].endsWith(".jpg.ro.jpg.c2.jpg.perimeterratiolength.jpg")){
                        perimeterratiolength_path = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].endsWith(".cr.jpg.ro.jpg.c2.jpg.perimeterratiolengthwidth.jpg")){
                        perimeterratiolengthwidth_path = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].endsWith(".cr.jpg.ro.jpg.c2.jpg.perimeterconvexity.jpg")){
                        perimeterconvexity_path = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].endsWith(".cr.jpg.ro.jpg.c2.jpg.areaconvexity.jpg")){
                        areaconvexity_path = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].endsWith(".cr.jpg.ro.jpg.c2.jpg.arearatioconvexity.jpg")){
                        arearatioconvexity_path = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].endsWith(".cr.jpg.ro.jpg.c2.jpg.arearatioconvexity.jpg")){
                        arearatioconvexity_path = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].endsWith(".cr.jpg.ro.jpg.c2.jpg.equivalentdiameter.jpg")){
                        equivalentdiameter_path = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].endsWith(".cr.jpg.ro.jpg.c2.jpg.centroid.jpg.area_teeth.jpg")){
                        area_teeth_path = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].endsWith(".cr.jpg.ro.jpg.c2.jpg.centroid.jpg.area_teeth_2sd.jpg")){
                        area_teeth_2sd_path = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].endsWith(".cr.jpg.ro.jpg.c2.jpg.centroid.jpg.area_teeth_2sd_sinusPointsLength.jpg")){
                        area_teeth_2sd_sinusPointsLength_path = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].endsWith(".cr.jpg.ro.jpg.c2.jpg.centroid.jpg.area_teeth_2sd_sinusPointsLength_height.jpg")){
                        area_teeth_2sd_sinusPointsLength_height_path = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].endsWith(".cr.jpg.ro.jpg.c2.jpg.centroid.jpg.area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_apexF.jpg")){
                        area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_apexF_path = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].endsWith(".cr.jpg.ro.jpg.c2.jpg.centroid.jpg.area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_lobeF.jpg")){
                        area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_lobeF_path = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].endsWith(".cr.jpg.ro.jpg.c2.jpg.centroid.jpg.area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_ID_key_a.jpg")){
                        area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_ID_key_a_path = pathString[1];
                    }
                    else if (fileTokens[fileTokens.length-1].endsWith(".centroid.jpg.area_teeth_2sd_sinusPointsLength_height_overlapsFiltered.jpg")){
                        area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_path = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].startsWith("html_shape_descriptors")){
                        html_shape_path = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].startsWith("html_morphological_descriptors")){
                        html_morphological_path = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].startsWith("html_morphological_descriptors")){
                        html_morphological_path = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].startsWith("html_leaf_margin_chart")){
                        html_margin_path = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].startsWith("html_method")){
                        html_method_path = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].endsWith("html_summary_table.html")){
                        html_summary_table_path = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].endsWith("html_summary_plot_pixels_morphological.html")){
                        html_plot_pixels_morphological_path = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].endsWith("html_summary_plot_pixels_eqs.html")){
                        html_plot_pixels_morphological_path = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].endsWith("html_summary_plot_leaf_morphological_cm.html")){
                        html_summary_plot_leaf_morphological_cm_output_config_file_path = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].endsWith("html_summary_plot_leaf_teeth.html")){
                        html_summary_plot_leaf_teeth_path = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].endsWith("html_summary_plot_leaf_shape.html")){
                        html_summary_plot_leaf_shape_path = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].endsWith("html_summary_plot_leaf_shape2.html")){
                        html_summary_plot_leaf_shape2_path = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].endsWith("html_summary_plot_leaf_compactness.html")){
                        html_summary_plot_leaf_compactness_path = pathString[1];
                    }else if (fileTokens[fileTokens.length-1].endsWith("html_summary_plot_leaf_eqd_cm.html")){
                        html_summary_plot_leaf_eqd_cm_path = pathString[1];
                    } else{
                        initial_image = pathString[1]; 
                        System.err.println("########## INITIAL IMAGE: "+this.initial_image);
                    }
                }
            }
        }
    }
    

    
    // getters for status  
    public boolean get_status_initial_image() {
        return status_initial_image;
    }

    public boolean get_status_crop1_image() {
        return status_crop1_image;
    }

    public boolean get_status_rotate_image() {
        return status_rotate_image;
    }

    public boolean get_status_crop2_image() {
        return status_crop2_image;
    }

    public boolean get_status_dilated_skinny_path() {
        return status_dilated_skinny_path;
    }

    public boolean get_status_contours_path() {
        return status_contours_path;
    }

    public boolean get_status_contours_skinny_path() {
        return status_contours_skinny_path;
    }

    public boolean get_status_centroid_path() {
        return status_centroid_path;
    }

    public boolean get_status_centroid_skinny_path() {
        return status_centroid_skinny_path;
    }

    public boolean get_status_length_path() {
        return status_length_path;
    }

    public boolean get_status_width_path() {
        return status_width_path;
    }

    public boolean get_status_area_path() {
        return status_area_path;
    }

    public boolean get_status_aspect_ratio_path() {
        return status_aspect_ratio_path;
    }

    public boolean get_status_roundness_path() {
        return status_roundness_path;
    }

    public boolean get_status_compactness_path() {
        return status_compactness_path;
    }

    public boolean get_status_rectangularity_path() {
        return status_rectangularity_path;
    }

    public boolean get_status_perimeterratiolength_path() {
        return status_perimeterratiolength_path;
    }

    public boolean get_status_perimeterratiolengthwidth_path() {
        return status_perimeterratiolengthwidth_path;
    }

    public boolean get_status_perimeterconvexity_path() {
        return status_perimeterconvexity_path;
    }

    public boolean get_status_areaconvexity_path() {
        return status_areaconvexity_path;
    }

    public boolean get_status_arearatioconvexity_path() {
        return status_arearatioconvexity_path;
    }

    public boolean get_status_equivalentdiameter_path() {
        return status_equivalentdiameter_path;
    }

    public boolean get_status_area_teeth_path() {
        return status_area_teeth_path;
    }

    public boolean get_status_area_teeth_2sd_path() {
        return status_area_teeth_2sd_path;
    }

    public boolean get_status_area_teeth_2sd_sinusPointsLength_path() {
        return status_area_teeth_2sd_sinusPointsLength_path;
    }

    public boolean get_status_area_teeth_2sd_sinusPointsLength_height_path() {
        return status_area_teeth_2sd_sinusPointsLength_height_path;
    }

    public boolean get_status_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_apexF_path() {
        return status_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_apexF_path;
    }

    public boolean get_status_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_lobeF_path() {
        return status_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_lobeF_path;
    }

    public boolean get_status_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_ID_key_a_path() {
        return status_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_ID_key_a_path;
    }

    public boolean get_status_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_path() {
        return status_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_path;
    }

    public boolean get_status_html_morphological_path() {
        return status_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_path;
    }

    public boolean get_status_html_shape_path() {
        return status_html_shape_path;
    }

    public boolean get_status_html_margin_path() {
        return status_html_margin_path;
    }

    public boolean get_status_html_method_path() {
        return status_html_method_path;
    }
    
    // get status for summary 

    public boolean get_status_html_summary_table_path() {
        return status_html_summary_table_path;
    }

    public boolean get_status_html_plot_pixels_morphological_path() {
        return status_html_plot_pixels_morphological_path;
    }

    public boolean get_status_html_summary_plot_pixels_eqs_path() {
        return status_html_summary_plot_pixels_eqs_path;
    }

    public boolean get_status_html_summary_plot_leaf_morphological_cm_output_config_file_path() {
        return status_html_summary_plot_leaf_morphological_cm_output_config_file_path;
    }

    public boolean get_status_html_summary_plot_leaf_teeth_path() {
        return status_html_summary_plot_leaf_teeth_path;
    }

    public boolean get_status_html_summary_plot_leaf_shape_path() {
        return status_html_summary_plot_leaf_shape_path;
    }

    public boolean get_status_html_summary_plot_leaf_shape2_path() {
        return status_html_summary_plot_leaf_shape2_path;
    }

    public boolean get_status_html_summary_plot_leaf_compactness_path() {
        return status_html_summary_plot_leaf_compactness_path;
    }

    public boolean get_status_html_summary_plot_leaf_eqd_cm_path() {
        return status_html_summary_plot_leaf_eqd_cm_path;
    }
    // set status
    public void set_status_initial_image(boolean newStatus){
        status_initial_image = newStatus;
    }
    public void set_status_crop1_image(boolean newStatus){
        status_crop1_image = newStatus;
    }
    public void set_status_rotate_image(boolean newStatus){
        status_rotate_image = newStatus;
    }
    public void set_status_crop2_image(boolean newStatus){
        status_crop2_image = newStatus;
    }
    public void set_status_dilated_skinny_path(boolean newStatus){
        status_dilated_skinny_path = newStatus;
    }
    public void set_status_contours_path(boolean newStatus){
        status_contours_path = newStatus;
    }
    public void set_status_contours_skinny_path(boolean newStatus){
        status_contours_skinny_path = newStatus;
    }
    public void set_status_centroid_path(boolean newStatus){
        status_centroid_path = newStatus;
    }
    public void set_status_centroid_skinny_path(boolean newStatus){
        status_centroid_skinny_path = newStatus;
    }
    public void set_status_length_path(boolean newStatus){
        status_length_path = newStatus;
    }
    public void set_status_width_path(boolean newStatus){
        status_width_path = newStatus;
    }
    public void set_status_area_path(boolean newStatus){
        status_area_path = newStatus;
    }
    public void set_status_aspect_ratio_path(boolean newStatus){
        status_aspect_ratio_path = newStatus;
    }
    public void set_status_roundness_path(boolean newStatus){
        status_roundness_path = newStatus;
    }
    public void set_status_compactness_path(boolean newStatus){
        status_compactness_path = newStatus;
    }
    public void set_status_rectangularity_path(boolean newStatus){
        status_rectangularity_path = newStatus;
    }
    public void set_status_perimeterratiolength_path(boolean newStatus){
        status_perimeterratiolength_path = newStatus;
    }
    public void set_status_perimeterratiolengthwidth_path(boolean newStatus){
        status_perimeterratiolengthwidth_path = newStatus;
    }
    public void set_status_perimeterconvexity_path(boolean newStatus){
        status_perimeterconvexity_path = newStatus;
    }
    public void set_status_areaconvexity_path(boolean newStatus){
        status_areaconvexity_path = newStatus;
    }
    public void set_status_arearatioconvexity_path(boolean newStatus){
        status_arearatioconvexity_path = newStatus;
    }
    public void set_status_equivalentdiameter_path(boolean newStatus){
        status_equivalentdiameter_path = newStatus;
    }
    public void set_status_area_teeth_path(boolean newStatus){
        status_area_teeth_path = newStatus;
    }
    public void set_status_area_teeth_2sd_path(boolean newStatus){
        status_area_teeth_2sd_path = newStatus;
    }
    public void set_status_area_teeth_2sd_sinusPointsLength_path(boolean newStatus){
        status_area_teeth_2sd_sinusPointsLength_path = newStatus;
    }
    public void set_status_area_teeth_2sd_sinusPointsLength_height_path(boolean newStatus){
        status_area_teeth_2sd_sinusPointsLength_height_path = newStatus;
    }
    public void set_status_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_apexF_path(boolean newStatus){
        status_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_apexF_path = newStatus;
    }
    public void set_status_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_lobeF_path(boolean newStatus){
        status_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_lobeF_path = newStatus;
    }
    public void set_status_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_ID_key_a_path(boolean newStatus){
        status_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_ID_key_a_path = newStatus;
    }
    public void set_status_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_path(boolean newStatus){
        status_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_path = newStatus;
    }
    public void set_status_html_morphological_path(boolean newStatus){
        status_html_morphological_path = newStatus;
    }
    public void set_status_html_shape_path(boolean newStatus){
        status_html_shape_path = newStatus;
    }
    public void set_status_html_margin_path(boolean newStatus){
        status_html_margin_path = newStatus;
    }
    public void set_status_html_method_path(boolean newStatus){
        status_html_method_path = newStatus;
    }
    // set summary status
    public void set_status_html_summary_table_path(boolean newStatus){
        status_html_summary_table_path = newStatus;
    }
    public void set_status_html_plot_pixels_morphological_path(boolean newStatus){
        status_html_plot_pixels_morphological_path = newStatus;
    }
    public void set_status_html_summary_plot_pixels_eqs_path(boolean newStatus){
        status_html_summary_plot_pixels_eqs_path = newStatus;
    }
    public void set_status_html_summary_plot_leaf_morphological_cm_output_config_file_path(boolean newStatus){
        status_html_summary_plot_leaf_morphological_cm_output_config_file_path = newStatus;
    }
    public void set_status_html_summary_plot_leaf_teeth_path(boolean newStatus){
        status_html_summary_plot_leaf_teeth_path = newStatus;
    }
    public void set_status_html_summary_plot_leaf_shape_path(boolean newStatus){
        status_html_summary_plot_leaf_shape_path = newStatus;
    }
    public void set_status_html_summary_plot_leaf_shape2_path(boolean newStatus){
        status_html_summary_plot_leaf_shape2_path = newStatus;
    }
    public void set_status_html_summary_plot_leaf_compactness_path(boolean newStatus){
        status_html_summary_plot_leaf_compactness_path = newStatus;
    }
    public void set_status_html_summary_plot_leaf_eqd_cm_path(boolean newStatus){
        status_html_summary_plot_leaf_eqd_cm_path = newStatus;
    }
    
    // GETTERS FOR PATHS
        //individual image paths
    public String get_initial_image(){
        return initial_image;
    }
    public String get_crop1_image(){
        return crop1_image;
    }
    public String get_rotate_image(){
        return rotate_image;
    }
    public String get_crop2_image(){
        return crop2_image;
    }
    public String get_dilated_skinny_path(){
        return dilated_skinny_path;
    }
    public String get_contours_path(){
        return contours_path;
    }
    public String get_contours_skinny_path(){
        return contours_skinny_path;
    }
    public String get_centroid_path(){
        return centroid_path;
    }
    public String get_centroid_skinny_path(){
        return centroid_skinny_path;
    }
    public String get_length_path(){
        return length_path;
    }
    public String get_width_path(){
        return width_path;
    }
    public String get_area_path(){
        return area_path;
    }
    public String get_aspect_ratio_path(){
        return aspect_ratio_path;
    }
    public String get_roundness_path(){
        return roundness_path;
    }
    public String get_compactness_path(){
        return compactness_path;
    }
    public String get_rectangularity_path(){
        return rectangularity_path;
    }
    public String get_perimeterratiolength_path(){
        return perimeterratiolength_path;
    }
    public String get_perimeterratiolengthwidth_path(){
        return perimeterratiolengthwidth_path;
    }
    public String get_perimeterconvexity_path(){
        return perimeterconvexity_path;
    }
    public String get_areaconvexity_path(){
        return areaconvexity_path;
    }
    public String get_arearatioconvexity_path(){
        return arearatioconvexity_path;
    }
    public String get_equivalentdiameter_path(){
        return equivalentdiameter_path;
    }
    public String get_area_teeth_path(){
        return area_teeth_path;
    }
    public String get_area_teeth_2sd_path(){
        return area_teeth_2sd_path;
    }
    public String get_area_teeth_2sd_sinusPointsLength_path(){
        return area_teeth_2sd_sinusPointsLength_path;
    }
    public String get_area_teeth_2sd_sinusPointsLength_height_path(){
        return area_teeth_2sd_sinusPointsLength_height_path;
    }
    public String get_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_apexF_path(){
        return area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_apexF_path;
    }
    public String get_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_lobeF_path(){
        return area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_lobeF_path;
    }
    public String get_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_ID_key_a_path(){
        return area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_ID_key_a_path;
    }
    public String get_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_path(){
        return area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_path;
    }
    public String get_html_morphological_path(){
        return html_morphological_path;
    }
    public String get_html_shape_path(){
        return html_shape_path;
    }
    public String get_html_margin_path(){
        return html_margin_path;
    }
    public String get_html_method_path(){
        return html_method_path;
    }
 
    public String get_html_summary_table_path(){
        return html_summary_table_path;
    }
    public String get_html_plot_pixels_morphological_path(){
        return html_plot_pixels_morphological_path;
    }
    public String get_html_summary_plot_pixels_eqs_path(){
        return html_summary_plot_pixels_eqs_path;
    }
    public String get_html_summary_plot_leaf_morphological_cm_output_config_file_path(){
        return html_summary_plot_leaf_morphological_cm_output_config_file_path;
    }
    public String get_html_summary_plot_leaf_teeth_path(){
        return html_summary_plot_leaf_teeth_path;
    }
    public String get_html_summary_plot_leaf_shape_path(){
        return html_summary_plot_leaf_shape_path;
    }
    public String get_html_summary_plot_leaf_shape2_path(){
        return html_summary_plot_leaf_shape2_path;
    }
    public String get_html_summary_plot_leaf_compactness_path(){
        return html_summary_plot_leaf_compactness_path;
    }
    public String get_html_summary_plot_leaf_eqd_cm_path(){
        return html_summary_plot_leaf_eqd_cm_path;
    }

    //setters FOR PATHS

    public void set_initial_image(String newpath) {
        initial_image = newpath;
    }

    public void set_crop1_image(String newpath) {
        crop1_image = newpath;
    }

    public void set_rotate_image(String newpath) {
        rotate_image = newpath;
    }

    public void set_crop2_image(String newpath) {
        crop2_image = newpath;
    }

    public void set_dilated_skinny_path(String newpath) {
        dilated_skinny_path = newpath;
    }

    public void set_contours_path(String newpath) {
        contours_path = newpath;
    }

    public void set_contours_skinny_path(String newpath) {
        contours_skinny_path = newpath;
    }

    public void set_centroid_path(String newpath) {
        centroid_path = newpath;
    }

    public void set_centroid_skinny_path(String newpath) {
        centroid_skinny_path = newpath;
    }

    public void set_length_path(String newpath) {
        length_path = newpath;
    }

    public void set_width_path(String newpath) {
        width_path = newpath;
    }

    public void set_area_path(String newpath) {
        area_path = newpath;
    }

    public void set_aspect_ratio_path(String newpath) {
        aspect_ratio_path = newpath;
    }

    public void set_roundness_path(String newpath) {
        roundness_path = newpath;
    }

    public void set_compactness_path(String newpath) {
        compactness_path = newpath;
    }

    public void set_rectangularity_path(String newpath) {
        rectangularity_path = newpath;
    }

    public void set_perimeterratiolength_path(String newpath) {
        perimeterratiolength_path = newpath;
    }

    public void set_perimeterratiolengthwidth_path(String newpath) {
        perimeterratiolengthwidth_path = newpath;
    }

    public void set_perimeterconvexity_path(String newpath) {
        perimeterconvexity_path = newpath;
    }

    public void set_areaconvexity_path(String newpath) {
        areaconvexity_path = newpath;
    }

    public void set_arearatioconvexity_path(String newpath) {
        arearatioconvexity_path = newpath;
    }

    public void set_equivalentdiameter_path(String newpath) {
        equivalentdiameter_path = newpath;
    }

    public void set_area_teeth_path(String newpath) {
        area_path = newpath;
    }

    public void set_area_teeth_2sd_path(String newpath) {
        area_teeth_2sd_path = newpath;
    }

    public void set_area_teeth_2sd_sinusPointsLength_path(String newpath) {
        area_teeth_2sd_sinusPointsLength_path = newpath;
    }

    public void set_area_teeth_2sd_sinusPointsLength_height_path(String newpath) {
        area_teeth_2sd_sinusPointsLength_height_path = newpath;
    }

    public void set_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_apexF_path(String newpath) {
        area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_apexF_path = newpath;
    }

    public void set_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_lobeF_path(String newpath) {
        area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_lobeF_path = newpath;
    }

    public void set_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_ID_key_a_path(String newpath) {
        area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_ID_key_a_path = newpath;
    }

    public void set_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_path(String newpath) {
        area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_path = newpath;
    }

    public void set_html_morphological_path(String newpath) {
        html_morphological_path = newpath;
    }

    public void set_html_shape_path(String newpath) {
        html_shape_path = newpath;
    }

    public void set_html_margin_path(String newpath) {
        html_margin_path = newpath;
    }

    public void set_html_method_path(String newpath) {
        html_method_path = newpath;
    }

    //setters for summary

    public void set_html_summary_table_path(String newpath) {
        html_summary_table_path = newpath;
    }

    public void set_html_plot_pixels_morphological_path(String newpath) {
        html_plot_pixels_morphological_path = newpath;
    }

    public void set_html_summary_plot_pixels_eqs_path(String newpath) {
        html_summary_plot_pixels_eqs_path = newpath;
    }

    public void set_html_summary_plot_leaf_morphological_cm_output_config_file_path(String newpath) {
        html_summary_plot_leaf_morphological_cm_output_config_file_path = newpath;
    }

    public void set_html_summary_plot_leaf_teeth_path(String newpath) {
        html_summary_plot_leaf_teeth_path = newpath;
    }

    public void set_html_summary_plot_leaf_shape_path(String newpath) {
        html_summary_plot_leaf_shape_path = newpath;
    }

    public void set_html_summary_plot_leaf_shape2_path(String newpath) {
        html_summary_plot_leaf_shape2_path = newpath;
    }

    public void set_html_summary_plot_leaf_compactness_path(String newpath) {
        html_summary_plot_leaf_compactness_path = newpath;
    }

    public void set_html_summary_plot_leaf_eqd_cm_path(String newpath) {
        html_summary_plot_leaf_eqd_cm_path = newpath;
    }
}
