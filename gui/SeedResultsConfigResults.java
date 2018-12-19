
package mktstall;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.concurrent.CountDownLatch;

public class SeedResultsConfigResults implements ConfigResults {

    private String ID;
    private String path_method;
    private String path_Accession_table;
    private String path_Accession_Area_Plot;
    private String path_Accession_Perimeter_Plot;
    private String path_Accession_EqD_Plot;
    private String path_Summary_Table;
    private String path_Summary_Area_Plot;
    private String path_Summary_Perimeter_Plot;
    private String path_Summary_EqD_Plot;
    private String path_Summary_Number_of_Seeds;
    
    private boolean status_path_method;
    private boolean status_path_Accession_table;
    private boolean status_path_Accession_Area_Plot;
    private boolean status_path_Accession_Perimeter_Plot;
    private boolean status_path_Accession_EqD_Plot;
    private boolean status_path_Summary_Table;
    private boolean status_path_Summary_Area_Plot;
    private boolean status_path_Summary_Perimeter_Plot;
    private boolean status_path_Summary_EqD_Plot;
    private boolean status_path_Summary_Number_of_Seeds;

    
    @Override
    public String I_AM_A() {
        return "SEED_CONFIG";
    }

    public void readSeedConfig(String absolutePath, CountDownLatch latch) throws IOException {

        this.ID = new File(absolutePath).getName().split("\\.")[0];
        try (BufferedReader r = new BufferedReader(new FileReader(new File(absolutePath)))) {
            String line = r.readLine();
            while(line != null){
                
                if(line.contains("status_accession_area_pixels_boxplot_path")){
                    this.status_path_Accession_Area_Plot = line.split("=")[1].equalsIgnoreCase("SUCCESS");
                }
                if(line.contains("plot_accession_area_pixels.png")){
                    this.path_Accession_Area_Plot = line.split("=")[1];
                }
                if(line.contains("status_accession_eqd_pixels_boxplot_path")){
                    this.status_path_Accession_EqD_Plot = line.split("=")[1].equalsIgnoreCase("SUCCESS");
                }
                if(line.contains("plot_accession_eqd_pixels.png")){
                    this.path_Accession_EqD_Plot = line.split("=")[1];
                }
                if(line.contains("status_accession_perimeter_pixels_boxplot_path")){
                    this.status_path_Accession_Perimeter_Plot = line.split("=")[1].equalsIgnoreCase("SUCCESS");
                }
                if(line.contains("plot_accession_perimeter_pixels.png")){
                    this.path_Accession_Perimeter_Plot = line.split("=")[1];
                }
                if(line.contains("status_accession_table_html_path")){
                    this.status_path_Accession_table = line.split("=")[1].equalsIgnoreCase("SUCCESS");
                }
                if(line.contains("accession_seed_table.html")){
                    this.path_Accession_table = line.split("=")[1];
                }
                
                if(line.contains("status_accession_seed_method_file")){
                    this.status_path_method = line.split("=")[1].equalsIgnoreCase("SUCCESS");
                }
                if(line.contains("accession_method_seed.html")){
                    this.path_method = line.split("=")[1];
                }
                if(line.contains("status_summary_table_html_file")){
                    this.status_path_Summary_Table = line.split("=")[1].equalsIgnoreCase("SUCCESS");
                }
                if(line.contains("summary_seed_table.html")){
                    this.path_Summary_Table = line.split("=")[1];
                }
                
                if(line.contains("status_summary_perimeter_boxplot_png_file")){
                    this.status_path_Summary_Perimeter_Plot = line.split("=")[1].equalsIgnoreCase("SUCCESS");
                }
                if(line.contains("plot_summary_perimeter_pixels.png")){
                    this.path_Summary_Perimeter_Plot = line.split("=")[1];
                }
                if(line.contains("status_summary_area_boxplot_png_file")){
                    this.status_path_Summary_Area_Plot = line.split("=")[1].equalsIgnoreCase("SUCCESS");
                }
                if(line.contains("plot_summary_area_pixels.png")){
                    this.path_Summary_Area_Plot = line.split("=")[1];
                }
                if(line.contains("status_summary_eqd_boxplot_png_file")){
                    this.status_path_Summary_EqD_Plot = line.split("=")[1].equalsIgnoreCase("SUCCESS");
                }
                if(line.contains("plot_summary_eqd_pixels.png")){
                    this.path_Summary_EqD_Plot = line.split("=")[1];
                }
                
                if(line.contains("status_summary_numberofseeds_boxplot_png_file")){
                    this.status_path_Summary_Number_of_Seeds = line.split("=")[1].equalsIgnoreCase("SUCCESS");
                }
                if(line.contains("plot_summary_number_of_seeds.png")){
                    this.path_Summary_Number_of_Seeds = line.split("=")[1];
                }
                line = r.readLine();
            }
        }
        latch.countDown();
    }

    public String getID() {
        return this.ID;
    }

    
    public String getPath_method() {
        return path_method;
    }

    public void setPath_method(String path_method) {
        this.path_method = path_method;
    }

    public String getPath_Accession_table() {
        return path_Accession_table;
    }

    public void setPath_Accession_table(String path_Accession_table) {
        this.path_Accession_table = path_Accession_table;
    }

    public String getPath_Accession_Area_Plot() {
        return path_Accession_Area_Plot;
    }

    public void setPath_Accession_Area_Plot(String path_Accession_Area_Plot) {
        this.path_Accession_Area_Plot = path_Accession_Area_Plot;
    }

    public String getPath_Accession_Perimeter_Plot() {
        return path_Accession_Perimeter_Plot;
    }

    public void setPath_Accession_Perimeter_Plot(String path_Accession_Perimeter_Plot) {
        this.path_Accession_Perimeter_Plot = path_Accession_Perimeter_Plot;
    }

    public String getPath_Accession_EqD_Plot() {
        return path_Accession_EqD_Plot;
    }

    public void setPath_Accession_EqD_Plot(String path_Accession_EqD_Plot) {
        this.path_Accession_EqD_Plot = path_Accession_EqD_Plot;
    }

    public String getPath_Summary_Table() {
        return path_Summary_Table;
    }

    public void setPath_Summary_Table(String path_Summary_Table) {
        this.path_Summary_Table = path_Summary_Table;
    }

    public String getPath_Summary_Area_Plot() {
        return path_Summary_Area_Plot;
    }

    public void setPath_Summary_Area_Plot(String path_Summary_Area_Plot) {
        this.path_Summary_Area_Plot = path_Summary_Area_Plot;
    }

    public String getPath_Summary_Perimeter_Plot() {
        return path_Summary_Perimeter_Plot;
    }

    public void setPath_Summary_Perimeter_Plot(String path_Summary_Perimeter_Plot) {
        this.path_Summary_Perimeter_Plot = path_Summary_Perimeter_Plot;
    }

    public String getPath_Summary_EqD_Plot() {
        return path_Summary_EqD_Plot;
    }

    public void setPath_Summary_EqD_Plot(String path_Summary_EqD_Plot) {
        this.path_Summary_EqD_Plot = path_Summary_EqD_Plot;
    }

    public String getPath_Summary_Number_of_Seeds() {
        return path_Summary_Number_of_Seeds;
    }

    public void setPath_Summary_Number_of_Seeds(String path_Summary_Number_of_Seeds) {
        this.path_Summary_Number_of_Seeds = path_Summary_Number_of_Seeds;
    }

    public boolean isStatus_path_method() {
        return status_path_method;
    }

    public boolean isStatus_path_Accession_table() {
        return status_path_Accession_table;
    }

    public boolean isStatus_path_Accession_Area_Plot() {
        return status_path_Accession_Area_Plot;
    }

    public boolean isStatus_path_Accession_Perimeter_Plot() {
        return status_path_Accession_Perimeter_Plot;
    }

    public boolean isStatus_path_Accession_EqD_Plot() {
        return status_path_Accession_EqD_Plot;
    }

    public boolean isStatus_path_Summary_Table() {
        return status_path_Summary_Table;
    }

    public boolean isStatus_path_Summary_Area_Plot() {
        return status_path_Summary_Area_Plot;
    }

    public boolean isStatus_path_Summary_Perimeter_Plot() {
        return status_path_Summary_Perimeter_Plot;
    }

    public boolean isStatus_path_Summary_EqD_Plot() {
        return status_path_Summary_EqD_Plot;
    }

    public boolean isStatus_path_Summary_Number_of_Seeds() {
        return status_path_Summary_Number_of_Seeds;
    }
    
    
    
    
    
    
}
