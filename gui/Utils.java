
package mktstall;

import java.io.File;
import java.io.IOException;
import java.util.concurrent.CountDownLatch;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Utils {
    
    public static int moveFile(File from, File to, CountDownLatch latch){
        int exitStatus = 1;
        try {
            String cmd = "mv "+from.getAbsolutePath()+" "+to.getAbsolutePath();
            Process p;
            p = Runtime.getRuntime().exec(cmd);
            exitStatus = p.waitFor();
            latch.countDown();
            
            
        } catch (IOException | InterruptedException ex) {
            Logger.getLogger(Utils.class.getName()).log(Level.SEVERE, null, ex);
        }
        return exitStatus;
    }
    
    public static int copyFile(File from, File to, CountDownLatch latch){
        int exitStatus = 1;
        try {
            String cmd = "cp "+from.getAbsolutePath()+" "+to.getAbsolutePath();
            Process p;
            p = Runtime.getRuntime().exec(cmd);
            exitStatus = p.waitFor();
            latch.countDown();
        } catch (IOException | InterruptedException ex) {
            Logger.getLogger(Utils.class.getName()).log(Level.SEVERE, null, ex);
        }
        return exitStatus;
    }
    
}
