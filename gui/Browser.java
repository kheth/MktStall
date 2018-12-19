package mktstall;

import java.awt.Dimension;
import java.awt.Point;
import java.io.File;
import java.net.MalformedURLException;
import java.util.concurrent.CountDownLatch;
import java.util.logging.Level;
import java.util.logging.Logger;
import javafx.application.Platform;
import javafx.embed.swing.JFXPanel;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.web.WebEngine;
import javafx.scene.web.WebView;
import javax.swing.JPanel;

public class Browser {
    
    private final JFXPanel fxPanel;
    private WebView webView;
    
    public Browser(){
        fxPanel = new JFXPanel();
    }
    
    public void init(JPanel parent) throws InterruptedException{
        
        CountDownLatch latch = new CountDownLatch(1);
        fxPanel.setSize(new Dimension(parent.getWidth(), parent.getHeight()));
        fxPanel.setLocation(new Point(0, 27));
        Platform.runLater(new Runnable() { // this will run initFX as JavaFX-Thread
            @Override
            public void run() {
                try {
                    initFX(fxPanel, latch);
                } catch (MalformedURLException ex) {
                    Logger.getLogger(Browser.class.getName()).log(Level.SEVERE, null, ex);
                }
            }
        });
        latch.await();   
    }
    
    public void resizeBrowser(JPanel parent){
        int width = parent.getWidth();
        int height = parent.getHeight();
        Dimension d = new Dimension(width, height);
        this.fxPanel.setSize(d);
        this.fxPanel.setPreferredSize(d);
        this.webView.setPrefSize(d.getWidth(), d.getHeight());
    }
    
    private void initFX(final JFXPanel fxPanel, CountDownLatch latch) throws MalformedURLException {
        Group group = new Group();
        Scene scene = new Scene(group);
        fxPanel.setScene(scene);
        webView = new WebView();
       
        group.getChildren().add(webView);
        webView.setMinSize(fxPanel.getWidth(),fxPanel.getHeight());
        WebEngine webEngine = webView.getEngine();
        File f = new File("~/mktstall/mktstall_py/java_transfer/testing.html");
        webEngine.load(f.toURI().toURL().toString()); 
        latch.countDown();
       
    }
    
    public void setPage(String pageAddress){
        // Obtain the webEngine to navigate
        WebEngine webEngine = webView.getEngine();
        webEngine.load(pageAddress);
    }
    
    public JFXPanel getFXPanel(){
        return this.fxPanel;
    }
    
}
