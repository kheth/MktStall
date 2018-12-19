
package mktstall;

import java.awt.Color;
import javax.swing.UIManager;
import javax.swing.plaf.ColorUIResource;
import javax.swing.plaf.metal.DefaultMetalTheme;

public class MarineGreenMetal extends DefaultMetalTheme {
    
    @Override
    public String getName() { return "MarineGreenMetal"; }
    
    //FONT COLOURS
                  Color ivory = new Color(253,246,228);
                  Color cyan = new Color(1,218,162);
                  Color offBlack = new Color(32,32,32);
                  Color gunMetal = new Color(101,123,132);
                  //BUTTON COLOURS
    
    public void setUIManagerProperties(){
        UIManager.put("Button.foreground",gunMetal);
        UIManager.put("Button.background", cyan);
        UIManager.put("Menu.foreground", ivory);
        UIManager.put("MenuItem.foreground", ivory);
        UIManager.put("ComboBox.foreground", ivory);
        UIManager.put("TabbedPane.foreground", ivory);
        UIManager.put("Label.foreground", ivory);
        UIManager.put("OptionPane.foreground", ivory);
        UIManager.put("OptionPane.messageForeground",ivory);
        UIManager.put("TableHeader.foreground", ivory);
    }
    
    private final ColorUIResource primary1 = new ColorUIResource(0, 255, 0);//GREEN
    private final ColorUIResource primary2 = new ColorUIResource(147, 161, 163);//IVORY // SELECTED MENU CONTROLS AND SCROLL BARS AND PROGRESS BAR INDETERMINANT
    private final ColorUIResource primary3 = new ColorUIResource(38, 139, 211);//BLUE //SELECTED TABLE ELEMENTS
    private final ColorUIResource secondary1 = new ColorUIResource(147, 161, 162);//YELLOW//HIGHTLIGHTS AND BORDERS
    private final ColorUIResource secondary2 = new ColorUIResource(101, 123, 132);//MAGENTA//UNSELECTED VISIBLE CONTROLS/TABS
    private final ColorUIResource secondary3 = new ColorUIResource(7, 54,67);//LARGE BACKGROUND
    
    @Override
    protected ColorUIResource getPrimary1() { return primary1; }
    @Override
    protected ColorUIResource getPrimary2() { return primary2; }
    @Override
    protected ColorUIResource getPrimary3() { return primary3; }
    @Override
    protected ColorUIResource getSecondary1() {return secondary1; }
    @Override
    protected ColorUIResource getSecondary2() {return secondary2; }
    @Override
    protected ColorUIResource getSecondary3() {return secondary3; }
}
