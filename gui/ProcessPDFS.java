
package mktstall;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.util.HashMap;
import java.util.Iterator;
import java.util.concurrent.CountDownLatch;
import javax.swing.SwingWorker;


public class ProcessPDFS extends SwingWorker<String,String> {

    private final File imageDir;
    private final File holdingDir;
    private final ActionListener listener;
    private CountDownLatch _latch;
    private final HashMap<String,File> pdfMap;
    private final HashMap<String,File> imgMap;
    private final Settings settings;
    
    public ProcessPDFS(Settings settings, ActionListener listener){
        this.imageDir = new File(settings.getIMAGE_DIR());
        this.holdingDir = new File(settings.getHOLDING_DIR());
        this.listener = listener;
        this.pdfMap = new HashMap<>();
        this.settings = settings;
        this.imgMap = new HashMap<>();
    }
    
    public void setCountDownLatch(CountDownLatch latch){
        this._latch = latch;
    }
    
    
    private void populateImageMap(){
        File directory = this.holdingDir;
        String[] filesInDir = directory.list();
        for (String fileInDir : filesInDir) {
            if(fileInDir.endsWith(".jpg")){
                this.imgMap.put(fileInDir, new File(directory+"/"+fileInDir));
            }
        }
    } 
    
    public HashMap<String, File> getImageMap(){
        return this.imgMap;
    }
    
    public void populatePDFMap(){
        File directory = this.imageDir;
        String[] filesInDir = directory.list();
        for (String fileInDir : filesInDir) {
            if(fileInDir.endsWith(".pdf")){
                this.pdfMap.put(fileInDir, new File(directory+"/"+fileInDir));
            }
        }
        PdfConverter convert = new PdfConverter();
        Iterator<String> itr = this.pdfMap.keySet().iterator();
        while(itr.hasNext()){
            String next = itr.next();
            File currentPDF = this.pdfMap.get(next);
            System.out.println("Processing PDF: "+currentPDF);
            //TURN PDF INTO IMAGES AND PLACE INTO HOLDING DIR
            CountDownLatch local_latch = new CountDownLatch(1);
            convert.pdfConvertToJpg(local_latch, settings, currentPDF.getAbsolutePath(), this.holdingDir.getAbsolutePath());
        }
        //POPULATE IMAGES MAP!
        this.populateImageMap();  
    }
    
    @Override
    protected String doInBackground() throws Exception {
        this.populatePDFMap();
        return "process_pdf_doInBackgroundDone";
    }
    
    @Override
    protected void done(){
        this.listener.actionPerformed(new ActionEvent(this, 1, "PDF_DONE"));
        System.out.println("done_methods_for_process_pdf_called");
        if(this._latch != null){
            this._latch.countDown();
        }
    }
    
}
