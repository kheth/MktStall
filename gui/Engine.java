
package mktstall;

import java.awt.event.ActionListener;
import java.io.File;
import javax.swing.JTextArea;

public class Engine {
    
    
    private Settings settings;
    private LeafRunner leafRunner;
    private ActionListener listener;
    private JTextArea userInfo;
    private ProcessPDFS pdfs;
    private SeedRunner seedRunner;
    
    /**
     * Constructs a new instance of Engine.
     */
    public Engine(){
    
    }
    
    public void setSettings(Settings settings){
        this.settings = settings;
    }
    
    public void setProcessPDFS(ProcessPDFS pdfs){
        this.pdfs = pdfs;
    }
    public void setActionListener(ActionListener listener){
        this.listener = listener;
    }
    
    public void setUserInfoArea(JTextArea userInfo){
        this.userInfo = userInfo;
    }
    
    public Settings getSettings(){
        return this.settings;
    }
    public void killSignal(){
        if(this.leafRunner != null){
            this.leafRunner.killSignal();
        }
        
    }
    
    /**
     * Set the directory containing all of the images to be analyzed.
     * @param path File containing the path to the image directory.
     */
    public void setImageDirectory(File path){
        this.settings.setINPUT_DIR(path.getAbsolutePath());
        
    }
    

    public void runLeaf(){
                                                                                       //do all = true
        this.leafRunner =  new LeafRunner(settings, listener, this.userInfo, this.pdfs, true);
        this.leafRunner.execute();     
    }
    
    public void runSeed(){
        this.seedRunner = new SeedRunner(settings, listener, this.userInfo, this.pdfs, true);
        this.seedRunner.execute();
    }
    
    /**
     * Set the path to python.
     * @param path File containing the path to python executable.
     */
    public void setPythonPath(File path){
        this.settings.setPYTHON_PATH(path.getAbsolutePath());
    }
    
    public String getSettingsString(){
        return this.settings.toString();
    }
    
}
