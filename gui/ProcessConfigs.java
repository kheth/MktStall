
package mktstall;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;


public class ProcessConfigs {
    
    private final String inputDir;
    private final File summaryConfig;
    private final File summaryConfigRenamed;
    
    public ProcessConfigs(String inputDir){
        this.inputDir = inputDir;
        summaryConfig = new File(this.inputDir+"/"+"summary_output.config_output.config");
        summaryConfigRenamed = new File(this.inputDir+"/"+"summary_output.config_output.configR");
    }
    
    public void processSummaryConfig(){
        
        if(this.containsSummaryConfig() && !this.containsRenamedSummaryConfig()){
            this.renameSummaryConfig();
            ArrayList<File> configs = this.getConfigFilesList();
            configs.stream().forEach((config) -> {
                this.catConfigsWithRenamedSummaryConfig(config);
            });
        }else if(this.containsSummaryConfig() && this.containsRenamedSummaryConfig()){
            this.removeRenamedSummaryConfig();
            this.renameSummaryConfig();
            ArrayList<File> configs = this.getConfigFilesList();
            configs.stream().forEach((config) -> {
                this.catConfigsWithRenamedSummaryConfig(config);
            });
        }  
    }
    
    private void renameSummaryConfig(){
        try {
            
            Process p = Runtime.getRuntime().exec("mv "+this.summaryConfig.getAbsolutePath()+" "+this.summaryConfigRenamed.getAbsolutePath());
            p.waitFor();
            BufferedReader reader = new BufferedReader(new InputStreamReader(p.getInputStream()));
            StringBuilder b = new StringBuilder();
            String line;			
            while ((line = reader.readLine())!= null) {
               b.append(line);
               b.append("\n");
               System.err.println(line+"\n");
            }
        } catch (IOException | InterruptedException ex) {
            Logger.getLogger(ProcessConfigs.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    
    private void catConfigsWithRenamedSummaryConfig(File config){
        
        try {
            // File location.
            String filePath = config.getAbsolutePath();
	
            StringBuilder sb = new StringBuilder();
            // Content to append.
            BufferedReader r;
            r = new BufferedReader(new FileReader(this.summaryConfigRenamed));
            String line = r.readLine();
            while(line != null){
                sb.append(line);
                sb.append("\n");
                line = r.readLine();
            }
            r.close();
            
            String contentToAppend = sb.toString();
            Files.write(Paths.get(filePath), contentToAppend.getBytes(), StandardOpenOption.APPEND);
            
        } catch (FileNotFoundException ex) {
            Logger.getLogger(ProcessConfigs.class.getName()).log(Level.SEVERE, null, ex);
        } catch (IOException ex) {
            Logger.getLogger(ProcessConfigs.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        
	
	
	
    }
        
    private void removeRenamedSummaryConfig(){
        try {
            Process p = Runtime.getRuntime().exec("rm -rf "+this.summaryConfigRenamed.getAbsolutePath());
            p.waitFor();
            BufferedReader reader = new BufferedReader(new InputStreamReader(p.getInputStream()));
            StringBuilder b = new StringBuilder();
            String line;			
            while ((line = reader.readLine())!= null) {
               b.append(line);
               b.append("\n");
               System.err.println(line+"\n");
            }
        } catch (IOException | InterruptedException ex) {
            Logger.getLogger(ProcessConfigs.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    
    private ArrayList<File> getConfigFilesList(){
        ArrayList<File> list = new ArrayList<>();
        File dir = new File(this.inputDir);
        for (final File f : dir.listFiles()) {
            if(f.getName().endsWith(".config")){
                list.add(f);
            }
        }
        return list;
    }
    

    private boolean containsSummaryConfig(){
        return this.summaryConfig.exists();
    }
    
    private boolean containsRenamedSummaryConfig(){
        return this.summaryConfigRenamed.exists();
    }
    
}
