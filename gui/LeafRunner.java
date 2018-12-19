
package mktstall;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.concurrent.CountDownLatch;
import javax.swing.JTextArea;
import javax.swing.SwingWorker;


public class LeafRunner extends SwingWorker<String,String> {

    private final Settings settings;
    private final ActionListener listener;
    private Process running_process;
    private final JTextArea userInfo;
    private final ProcessPDFS pdfs;
    private final boolean all;
    
    public LeafRunner(Settings settings, ActionListener listener, JTextArea userInfo, ProcessPDFS pdfs, boolean all){
        this.settings = settings;
        this.listener = listener;
        this.userInfo = userInfo;
        this.pdfs = pdfs;
        this.all = all;
    }
    
    /**
     * Kills a leafRunner if it has started processing.
     */
    public void killSignal(){
        if(this.running_process != null && this.running_process.isAlive()){
            this.running_process.destroyForcibly();    
        }
    }
    
    public void doAll() throws IOException, InterruptedException{
        this.userInfo.append("Running leaf analysis.\n");
        //RUN THE MKTSTALL SCRIPT
        ProcessBuilder builder = new ProcessBuilder(settings.getRUN_LEAF_ANALYSIS_SCRIPT());
        builder.directory(new File(settings.getMKTSTALL_PYTHON()));
        final Process process = builder.inheritIO().start();
        this.running_process = process;
        InputStream is = process.getInputStream();
        InputStreamReader isr = new InputStreamReader(is);
        BufferedReader br = new BufferedReader(isr);
        String line;
        while ((line = br.readLine()) != null) {
            System.out.println(line);
            publish(line);
        }
        process.waitFor();
        this.userInfo.append("done.\n");
    }
    
    public void doIndividual() throws InterruptedException, IOException{
        this.userInfo.append("Organising images.\n");
        CountDownLatch _latch = new CountDownLatch(1);
        this.pdfs.setCountDownLatch(_latch);
        this.pdfs.execute();
        _latch.await();
        this.userInfo.append("done.");
        
        this.userInfo.append("Running leaf analysis.\n");
        HashMap<String, File> imageMap = this.pdfs.getImageMap();
        Iterator<String> itr = imageMap.keySet().iterator();
        //LOOP OVER THE IMAGES IN THE IMAGE MAP
        while(itr.hasNext()){
            String fileName = itr.next();
            this.userInfo.append("Processing image: "+fileName);
            //COPY A SINGLE IMAGE INTO THE RUN_DIR
            CountDownLatch copy_latch = new CountDownLatch(1);
            File holdingLocation = imageMap.get(fileName);
            File input_dir_location = new File(this.settings.getINPUT_DIR()+"/"+holdingLocation.getName());
            Utils.copyFile(holdingLocation, input_dir_location, copy_latch);
            copy_latch.await();
            
            //RUN THE MKTSTALL SCRIPT
            ProcessBuilder builder = new ProcessBuilder(settings.getRUN_LEAF_ANALYSIS_SCRIPT());
            builder.directory(new File(settings.getMKTSTALL_PYTHON()));
            final Process process = builder.inheritIO().start();
            this.running_process = process;
            InputStream is = process.getInputStream();
            InputStreamReader isr = new InputStreamReader(is);
            BufferedReader br = new BufferedReader(isr);
            String line;
            while ((line = br.readLine()) != null) {
                System.out.println(line);
                publish(line);
            }
            process.waitFor();
            
            //REMOVE THE IMAGE IN THE INPUT_DIR
            input_dir_location.delete();
            this.userInfo.append("... done.\n");
        }
        this.userInfo.append("done.");
    }
    
    @Override
    protected String doInBackground() throws Exception {
        if(this.all){
            this.doAll();
        }else{
            this.doIndividual();
        }
        return "done";
    }
    
    
    @Override
    protected void process(List<String> chunks){
        if(chunks.size() > 0){
            for(int i = 0; i < chunks.size(); i++){
                System.out.println("HELLOOOOOOOOOOOOOO");
                this.userInfo.append(chunks.get(i));
                this.userInfo.append("\n");
                this.userInfo.repaint();
            }
        }
    }
        
     
    @Override
    protected void done(){
        this.listener.actionPerformed(new ActionEvent(this, 1, "LEAF_DONE"));
        System.out.println("is done!");
    }
   
}
