
package mktstall;

import java.io.IOException;
import java.util.concurrent.CountDownLatch;
import java.util.logging.Level;
import java.util.logging.Logger;


public class PdfConverter {

    private int lastExitStatus;
    
    public void pdfConvertToJpg(CountDownLatch latch, Settings settings, String pdfPath, String outputDir){
        try {
            String[] tokens = pdfPath.split("/");
            String prefix = outputDir + "/" +tokens[tokens.length-1] +".toJpg";
            String pdfconvertcommand = "java -jar "+settings.getRESOURCES_DIR()+"/pdfbox/pdfbox-app-2.0.7.jar " +
                "PDFToImage -imageType jpg -outputPrefix " +
             prefix + " -dpi 300 " + pdfPath;
            Process p = Runtime.getRuntime().exec(pdfconvertcommand);
            int waitFor = p.waitFor();
            this.lastExitStatus = waitFor;
            latch.countDown();
        } catch (InterruptedException | IOException ex) {
            Logger.getLogger(PdfConverter.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    
    public int getLastExitStatus(){
        return this.lastExitStatus;
    }
}
