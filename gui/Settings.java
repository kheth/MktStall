
package mktstall;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;


public class Settings {

    public static enum Setting  { 
        EMPTY, MAX_THREADS, PYTHON_PATH, MKTSTALL_PYTHON, TEMP_DIR, INPUT_DIR, OUTPUT_DIR, RESOURCES_DIR, RUN_LEAF_ANALYSIS_SCRIPT, IMAGE_DIR, HOLDING_DIR, RUN_SEED_ANALYSIS_SCRIPT
    }
   
    private int MAX_THREADS;
    private String PYTHON_PATH;
    private String MKTSTALL_PYTHON;
    private String TEMP_DIR;
    private String INPUT_DIR;
    private String OUTPUT_DIR;
    private String RESOURCES_DIR;
    private String RUN_LEAF_ANALYSIS_SCRIPT;
    private String RUN_SEED_ANALYSIS_SCRIPT;
    private String IMAGE_DIR;
    private String HOLDING_DIR;
    
    private String organ = "LEAF";
    
    /**
     * Construct Settings.
     */
    public Settings(){
        this.loadSettingsConfig();
        this.getMaxThreads();
        this.makeLeafRunnerScript();  
    }

    public String getOrgan() {
        return organ;
    }

    public void setOrgan(String organ) {
        this.organ = organ;
    }
    
    /**
     * Load a settings configuration file. 
     */
    public final void loadSettingsConfig() {
        String path = new File("").getAbsolutePath();
        if(this.organ.equalsIgnoreCase("LEAF")){
            path = path.concat("/settingsLeaf.config");
        }else if(this.organ.equalsIgnoreCase("SEED")){
            path = path.concat("/settingsSeed.config");
        }
        try (BufferedReader r = new BufferedReader(new FileReader(new File(path)))) {
            String line = r.readLine();
            while(line!= null){
                if(!line.startsWith("#")){
                    String[] toks = line.split("=");
                    if(toks[0].startsWith("IMAGE_DIR")){
                        this.IMAGE_DIR = toks[1];
                    }
                    if(toks[0].startsWith("HOLDING_DIR")){
                        this.HOLDING_DIR = toks[1];
                    }
                    if(toks[0].startsWith("MAX_THREADS")){
                        this.MAX_THREADS = Integer.parseInt(toks[1]);
                    }
                    if(toks[0].startsWith("PYTHON_PATH")){
                        this.PYTHON_PATH = toks[1];
                    }
                    if(toks[0].startsWith("MKTSTALL_PYTHON")){
                        this.MKTSTALL_PYTHON = toks[1];
                    }
                    if(toks[0].startsWith("TEMP_DIR")){
                        this.TEMP_DIR = toks[1];
                    }
                    if(toks[0].startsWith("INPUT_DIR")){
                        this.INPUT_DIR = toks[1];
                    }
                    if(toks[0].startsWith("OUTPUT_DIR")){
                        this.OUTPUT_DIR = toks[1];
                    }
                    if(toks[0].startsWith("RESOURCES_DIR")){
                        this.RESOURCES_DIR = toks[1];
                    }
                }
                line = r.readLine();
            }
            
        } catch (FileNotFoundException ex) {
            Logger.getLogger(Settings.class.getName()).log(Level.SEVERE, null, ex);
        } catch (IOException ex) {
            Logger.getLogger(Settings.class.getName()).log(Level.SEVERE, null, ex);
        } 
        this.updateSettings(Setting.EMPTY, "");
    }
    
    /**
     * Set a setting to a new value.
     * @param setting the setting to be set.
     * @param newValue the new value of the setting.
     */
    public void updateSettings(Setting setting, Object newValue){
        switch(setting) {
            case MAX_THREADS        : {this.MAX_THREADS=(Integer)newValue; break;}
            case PYTHON_PATH        : {this.PYTHON_PATH=(String)newValue; break;} 
            case MKTSTALL_PYTHON    : {this.MKTSTALL_PYTHON=(String)newValue; break;}
            case TEMP_DIR           : {this.TEMP_DIR=(String)newValue; break;}
            case INPUT_DIR          : {this.INPUT_DIR=(String)newValue; break;}
            case OUTPUT_DIR         : {this.OUTPUT_DIR=(String)newValue; break;}
            case RESOURCES_DIR      : {this.RESOURCES_DIR=(String)newValue; break;}
            case RUN_LEAF_ANALYSIS_SCRIPT : {this.RUN_LEAF_ANALYSIS_SCRIPT=(String)newValue; break;}
            case RUN_SEED_ANALYSIS_SCRIPT : {this.RUN_SEED_ANALYSIS_SCRIPT=(String)newValue; break;}
            case IMAGE_DIR          : {this.IMAGE_DIR=(String)newValue; break;}
            case HOLDING_DIR        : {this.HOLDING_DIR=(String)newValue; break;}
        }
        if(this.organ.equalsIgnoreCase("LEAF")){
            this.makeLeafRunnerScript();
        }else if(this.organ.equalsIgnoreCase("SEED")){
            this.makeSeedRunnerScript();
        }
    }
    
    /**
     * Makes a script that will run the leaf python mktstall.
     */
    private void makeLeafRunnerScript(){
        String path = new File("").getAbsolutePath();
        path = path.concat("/runLeaf.sh");
        try (BufferedWriter w = new BufferedWriter(new FileWriter(new File(path)))) {
            StringBuilder sb = new StringBuilder();
            sb.append("#!/bin/bash --login");//note important to keep --login so that ~/.bash_profile is loaded.
            sb.append("\n");
            sb.append("source ~/.bash_profile");
            sb.append("\n");
            sb.append("cd ");
            sb.append(this.MKTSTALL_PYTHON);
            sb.append("\n");
            sb.append("python ");
            sb.append(this.MKTSTALL_PYTHON);
            sb.append("/mktstall.py");
            w.write(sb.toString());
            this.RUN_LEAF_ANALYSIS_SCRIPT = path;
            File f = new File(this.RUN_LEAF_ANALYSIS_SCRIPT);
            //set application user permissions to 455
            f.setExecutable(true);
            f.setReadable(true);
            f.setWritable(true);
        } catch (IOException ex) {
            Logger.getLogger(Settings.class.getName()).log(Level.SEVERE, null, ex);
        }    
    }
    
    /**
     * Makes a script that will run the leaf python mktstall.
     */
    private void makeSeedRunnerScript(){
        String path = new File("").getAbsolutePath();
        path = path.concat("/runSeed.sh");
        try (BufferedWriter w = new BufferedWriter(new FileWriter(new File(path)))) {
            StringBuilder sb = new StringBuilder();
            sb.append("#!/bin/bash --login");//note important to keep --login so that ~/.bash_profile is loaded.
            sb.append("\n");
            sb.append("source ~/.bash_profile");
            sb.append("\n");
            sb.append("cd ");
            sb.append(this.MKTSTALL_PYTHON);
            sb.append("\n");
            sb.append("python ");
            sb.append(this.MKTSTALL_PYTHON);
            sb.append("/mktstall.py");
            w.write(sb.toString());
            this.RUN_SEED_ANALYSIS_SCRIPT = path;
            File f = new File(this.RUN_SEED_ANALYSIS_SCRIPT);
            System.out.println(this.RUN_SEED_ANALYSIS_SCRIPT);
            //set application user permissions to 455
            f.setExecutable(true);
            f.setReadable(true);
            f.setWritable(true);
        } catch (IOException ex) {
            Logger.getLogger(Settings.class.getName()).log(Level.SEVERE, null, ex);
        }    
    }
    
    
    /**
     * Gets a string describing the settings.
     * @return description of settings.
     */
    @Override
    public String toString(){
        StringBuilder sb = new StringBuilder();
        sb.append("MAX_THREADS: ");
        sb.append(this.MAX_THREADS);
        sb.append("\n");
        sb.append("PYTHON_PATH: ");
        sb.append(this.PYTHON_PATH);
        sb.append("\n");
        sb.append("MKTSTALL_PYTHON: ");
        sb.append(this.MKTSTALL_PYTHON);
        sb.append("\n");
        sb.append("TEMP_DIR: ");
        sb.append(this.TEMP_DIR);
        sb.append("\n");
        sb.append("INPUT_DIR: ");
        sb.append(this.INPUT_DIR);
        sb.append("\n");
        sb.append("OUTPUT_DIR: ");
        sb.append(this.OUTPUT_DIR);
        sb.append("\n");
        sb.append("RESOURCES_DIR: ");
        sb.append(this.RESOURCES_DIR);
        sb.append("\n");
        sb.append("IMAGE_DIR: ");
        sb.append(this.IMAGE_DIR);
        sb.append("\n");
        sb.append("HOLDING_DIR: ");
        sb.append(this.HOLDING_DIR);
        sb.append("\n");
        return sb.toString();
    }
    
    /**
     * Get the number of cores from the system and set the maximum number
     * of threads (1 per core).
     */
    private void getMaxThreads(){
        this.MAX_THREADS = Runtime.getRuntime().availableProcessors();
    }

    public int getMAX_THREADS() {
        return MAX_THREADS;
    }

    public void setMAX_THREADS(int MAX_THREADS) {
        this.MAX_THREADS = MAX_THREADS;
    }

    public String getPYTHON_PATH() {
        return PYTHON_PATH;
    }

    public void setPYTHON_PATH(String PYTHON_PATH) {
        this.PYTHON_PATH = PYTHON_PATH;
    }

    public String getMKTSTALL_PYTHON() {
        return MKTSTALL_PYTHON;
    }

    public void setMKTSTALL_PYTHON(String MKTSTALL_PYTHON) {
        this.MKTSTALL_PYTHON = MKTSTALL_PYTHON;
    }

    public String getTEMP_DIR() {
        return TEMP_DIR;
    }

    public void setTEMP_DIR(String TEMP_DIR) {
        this.TEMP_DIR = TEMP_DIR;
    }

    public String getINPUT_DIR() {
        return INPUT_DIR;
    }

    public void setINPUT_DIR(String INPUT_DIR) {
        this.INPUT_DIR = INPUT_DIR;
    }

    public String getOUTPUT_DIR() {
        return OUTPUT_DIR;
    }

    public void setOUTPUT_DIR(String OUTPUT_DIR) {
        this.OUTPUT_DIR = OUTPUT_DIR;
    }

    public String getRESOURCES_DIR() {
        return RESOURCES_DIR;
    }

    public void setRESOURCES_DIR(String RESOURCES_DIR) {
        this.RESOURCES_DIR = RESOURCES_DIR;
    }

    public String getRUN_LEAF_ANALYSIS_SCRIPT() {
        return RUN_LEAF_ANALYSIS_SCRIPT;
    }

    public String getIMAGE_DIR() {
        return IMAGE_DIR;
    }

    public String getRUN_SEED_ANALYSIS_SCRIPT() {
        return RUN_SEED_ANALYSIS_SCRIPT;
    }

    public void setRUN_SEED_ANALYSIS_SCRIPT(String RUN_SEED_ANALYSIS_SCRIPT) {
        this.RUN_SEED_ANALYSIS_SCRIPT = RUN_SEED_ANALYSIS_SCRIPT;
    }

    public void setIMAGE_DIR(String IMAGE_DIR) {
        this.IMAGE_DIR = IMAGE_DIR;
    }

    public String getHOLDING_DIR() {
        return HOLDING_DIR;
    }

    public void setHOLDING_DIR(String HOLDING_DIR) {
        this.HOLDING_DIR = HOLDING_DIR;
    }
    
    
    
}
