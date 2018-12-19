
package mktstall;


public class MktStall {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        /* Create and display the form */
        java.awt.EventQueue.invokeLater(() -> {
            new MktStallGUI(new Engine()).setVisible(true);
        });
    }
    
}
