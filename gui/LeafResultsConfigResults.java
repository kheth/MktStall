package mktstall;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.concurrent.CountDownLatch;

public class LeafResultsConfigResults implements ConfigResults {
    
    String ID;
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
    // summary new
    boolean status_html_boxplot_pixels_path;
    boolean status_html_boxplot_cm_path;
    boolean status_html_pca_path;
    boolean status_html_links_path;
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
    String html_boxplot_pixels_path;
    String html_boxplot_cm_path;
    String html_pca_path;
    String html_links_path; 
    // read in config
    
    public String getID(){
        return this.ID;
    }
    
    /**
     * Read in config file and populate field.
     *
     * @param filepathToConfig
     * @param latch
     * @throws java.io.FileNotFoundException
     */
    public void readLeafConfig(String filepathToConfig, CountDownLatch latch) throws FileNotFoundException, IOException {
        ArrayList<String> configStrings;
        try (Scanner configScanner = new Scanner(new File(filepathToConfig))) {
            configStrings = new ArrayList<>();
            while (configScanner.hasNext()) {
                configStrings.add(configScanner.next());
            }
        }
        // for each in the array list
        for(String c :configStrings){
            // CHECKING STATUS
            if (c.startsWith("#status_")){
                //System.out.println("print c: " + c);
                String[] statusString;
                String[] status;
                statusString = c.split("#status_");
                //System.out.println("statusString[0]: " + statusString[0]);
                //System.out.println("statusString[1]: " + statusString[1]);
                status = statusString[1].split("=");
                //System.out.println("status: " + status[0]);
                if(status[0].matches("initial_image")){
                    status_initial_image = status[1].matches("SUCCESS");
                } else if(status[0].matches("crop1_image")){
                    status_crop1_image = status[1].matches("SUCCESS");
                } else if(status[0].matches("rotate_image")){
                    status_rotate_image = status[1].matches("SUCCESS");
                } else if(status[0].matches("crop2_image")){
                    status_crop2_image = status[1].matches("SUCCESS");
                } else if(status[0].matches("dilated_skinny_path")){
                    status_dilated_skinny_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("contours_path")){
                    status_contours_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("contours_skinny_path")){
                    status_contours_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("centroid_path")){
                    status_centroid_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("centroid_skinny_path")){
                    status_centroid_skinny_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("length_path")){
                    status_length_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("width_path")){
                    status_width_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("area_path")){
                    status_area_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("roundness_path")){
                    status_roundness_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("compactness_path")){
                    status_compactness_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("rectangularity_path")){
                    status_rectangularity_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("perimeterratiolength_path")){
                    status_perimeterratiolength_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("perimeterratiolengthwidth_path")){
                    status_perimeterratiolengthwidth_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("perimeterconvexity_path")){
                    status_perimeterconvexity_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("areaconvexity_path")){
                    status_areaconvexity_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("arearatioconvexity_path")){
                    status_arearatioconvexity_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("equivalentdiameter_path")){
                    status_equivalentdiameter_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("area_teeth_2sd_path")){
                    status_area_teeth_2sd_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("area_teeth_2sd_sinusPointsLength_path")){
                    status_area_teeth_2sd_sinusPointsLength_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("area_teeth_2sd_sinusPointsLength_height_path")){
                    status_area_teeth_2sd_sinusPointsLength_height_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_apexF_path")){
                    status_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_apexF_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_lobeF_path")){
                    status_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_lobeF_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_ID_key_a_path")){
                    status_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_ID_key_a_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_path")){
                    status_area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("html_morphological_path")){
                    status_html_morphological_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("html_shape_path")){
                    status_html_shape_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("html_margin_path")){
                    status_html_margin_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("html_method_path")){
                    status_html_method_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("html_summary_table_path")){
                    status_html_summary_table_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("html_plot_pixels_morphological_path")){
                    status_html_plot_pixels_morphological_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("html_summary_plot_pixels_eqs_path")){
                    status_html_summary_plot_pixels_eqs_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("html_summary_plot_leaf_morphological_cm_output_config_file_path")){
                    status_html_summary_plot_leaf_morphological_cm_output_config_file_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("html_summary_plot_leaf_teeth_path")){
                    status_html_summary_plot_leaf_teeth_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("html_summary_plot_leaf_shape2_path")){
                    status_html_summary_plot_leaf_shape2_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("html_summary_plot_leaf_compactness_path")){
                    status_html_summary_plot_leaf_compactness_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("html_summary_plot_leaf_eqd_cm_path")){
                    status_html_summary_plot_leaf_eqd_cm_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("html_pixels_boxplot_path")){
                    status_html_boxplot_pixels_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("html_cm_boxplot_path")){
                    status_html_boxplot_cm_path = status[1].matches("SUCCESS");
                } else if(status[0].matches("html_pca_path")){
                    status_html_pca_path = status[1].matches("SUCCESS");
                }else {
                    System.out.println("no status found");
                }   
            }
        }
        for(String p : configStrings){
            // CHECKING STATUS
            if (p.startsWith("#PATH=")){

                String[] pathString;
                String[] fileTokens;
                pathString = p.split("PATH=");
                //System.out.println("path:" + pathString[1]);
                fileTokens = pathString[1].split("/");
                //System.out.println("last file token"+ fileTokens[fileTokens.length-1] );
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
                    rectangularity_path =pathString[1];
                }else if (fileTokens[fileTokens.length-1].endsWith(".jpg.ro.jpg.c2.jpg.perimeterratiolength.jpg")){
                    perimeterratiolength_path = pathString[1];
                }else if (fileTokens[fileTokens.length-1].endsWith(".cr.jpg.ro.jpg.c2.jpg.perimeterratiolengthwidth.jpg")){
                    perimeterratiolengthwidth_path= pathString[1];
                }else if (fileTokens[fileTokens.length-1].endsWith(".cr.jpg.ro.jpg.c2.jpg.perimeterconvexity.jpg")){
                    perimeterconvexity_path = pathString[1];
                }else if (fileTokens[fileTokens.length-1].endsWith(".cr.jpg.ro.jpg.c2.jpg.areaconvexity.jpg")){
                    areaconvexity_path= pathString[1];
                }else if (fileTokens[fileTokens.length-1].endsWith(".cr.jpg.ro.jpg.c2.jpg.arearatioconvexity.jpg")){
                    arearatioconvexity_path= pathString[1];
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
                    area_teeth_2sd_sinusPointsLength_height_path= pathString[1];
                }else if (fileTokens[fileTokens.length-1].endsWith(".cr.jpg.ro.jpg.c2.jpg.centroid.jpg.area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_apexF.jpg")){
                    area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_apexF_path = pathString[1];
                }else if (fileTokens[fileTokens.length-1].endsWith(".cr.jpg.ro.jpg.c2.jpg.centroid.jpg.area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_lobeF.jpg")){
                    area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_lobeF_path = pathString[1];
                }else if (fileTokens[fileTokens.length-1].endsWith(".cr.jpg.ro.jpg.c2.jpg.centroid.jpg.area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_ID_key_a.jpg")){
                    area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_ID_key_a_path = pathString[1];
                }else if (fileTokens[fileTokens.length-1].endsWith(".centroid.jpg.area_teeth_2sd_sinusPointsLength_height_overlapsFiltered.jpg")){
                    area_teeth_2sd_sinusPointsLength_height_overlapsFiltered_path = pathString[1];
                }else if (fileTokens[fileTokens.length-1].startsWith("html_shape_descriptors")){
                    html_shape_path = pathString[1];
                }else if (fileTokens[fileTokens.length-1].startsWith("html_morphological_descriptors")){
                    html_morphological_path= pathString[1];
                }else if (fileTokens[fileTokens.length-1].startsWith("html_morphological_descriptors")){
                    html_morphological_path= pathString[1];
                }else if (fileTokens[fileTokens.length-1].startsWith("html_leaf_margin_chart")){
                    html_margin_path = pathString[1];
                }else if (fileTokens[fileTokens.length-1].startsWith("html_method")){
                    html_method_path= pathString[1];
                }else if (fileTokens[fileTokens.length-1].endsWith("html_summary_table.html")){
                    html_summary_table_path = pathString[1];
                }else if (fileTokens[fileTokens.length-1].endsWith("html_summary_plot_pixels_morphological.html")){
                    html_plot_pixels_morphological_path= pathString[1];
                }else if (fileTokens[fileTokens.length-1].endsWith("html_summary_plot_pixels_eqs.html")){
                    html_plot_pixels_morphological_path =pathString[1];
                }else if (fileTokens[fileTokens.length-1].endsWith("html_summary_plot_leaf_morphological_cm.html")){
                    html_summary_plot_leaf_morphological_cm_output_config_file_path =pathString[1];
                }else if (fileTokens[fileTokens.length-1].endsWith("html_summary_plot_leaf_teeth.html")){
                    html_summary_plot_leaf_teeth_path =pathString[1];
                }else if (fileTokens[fileTokens.length-1].endsWith("html_summary_plot_leaf_shape.html")){
                    html_summary_plot_leaf_shape_path =pathString[1];
                }else if (fileTokens[fileTokens.length-1].endsWith("html_summary_plot_leaf_shape2.html")){
                    html_summary_plot_leaf_shape2_path =pathString[1];
                }else if (fileTokens[fileTokens.length-1].endsWith("html_summary_plot_leaf_compactness.html")){
                    html_summary_plot_leaf_compactness_path =pathString[1];
                }else if (fileTokens[fileTokens.length-1].endsWith("html_summary_plot_leaf_eqd_cm.html")){
                    html_summary_plot_leaf_eqd_cm_path =pathString[1];
                }else if (fileTokens[fileTokens.length-1].endsWith("html_boxplot_cm.html")){
                    html_boxplot_cm_path =pathString[1];
                }else if (fileTokens[fileTokens.length-1].endsWith("html_boxplot_pixels.html")){
                    html_boxplot_pixels_path =pathString[1];
                }else if (fileTokens[fileTokens.length-1].endsWith("pca.html")){
                    html_pca_path =pathString[1]; 
                }else if(fileTokens[fileTokens.length-1].endsWith("_")){
                    this.ID = pathString[1]; 
                }
                else{
                    initial_image =pathString[1];
                }
            }    
        }
        latch.countDown();
    }
    
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
        System.err.println("requested summary table path: "+html_summary_table_path);
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

    public boolean isStatus_html_boxplot_pixels_path() {
        return status_html_boxplot_pixels_path;
    }

    public boolean isStatus_html_boxplot_cm_path() {
        return status_html_boxplot_cm_path;
    }

    public boolean isStatus_html_pca_path() {
        return status_html_pca_path;
    }

    public boolean isStatus_html_links_path() {
        return status_html_links_path;
    }

    public void setStatus_html_boxplot_pixels_path(boolean status_html_boxplot_pixels_path) {
        this.status_html_boxplot_pixels_path = status_html_boxplot_pixels_path;
    }

    public void setStatus_html_boxplot_cm_path(boolean status_html_boxplot_cm_path) {
        this.status_html_boxplot_cm_path = status_html_boxplot_cm_path;
    }

    public void setStatus_html_pca_path(boolean status_html_pca_path) {
        this.status_html_pca_path = status_html_pca_path;
    }

    public void setStatus_html_links_path(boolean status_html_links_path) {
        this.status_html_links_path = status_html_links_path;
    }

    public String getHtml_boxplot_pixels_path() {
        return html_boxplot_pixels_path;
    }

    public String getHtml_boxplot_cm_path() {
        return html_boxplot_cm_path;
    }

    public String getHtml_pca_path() {
        return html_pca_path;
    }

    public String getHtml_links_path() {
        return html_links_path;
    }

    public void setHtml_boxplot_pixels_path(String html_boxplot_pixels_path) {
        this.html_boxplot_pixels_path = html_boxplot_pixels_path;
    }

    public void setHtml_boxplot_cm_path(String html_boxplot_cm_path) {
        this.html_boxplot_cm_path = html_boxplot_cm_path;
    }

    public void setHtml_pca_path(String html_pca_path) {
        this.html_pca_path = html_pca_path;
    }

    public void setHtml_links_path(String html_links_path) {
        this.html_links_path = html_links_path;
    }

    @Override
    public String I_AM_A() {
        return "LEAF_CONFIG";
    }
    
    
}
