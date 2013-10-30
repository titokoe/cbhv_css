from org.eclipse.swt.widgets import FileDialog
from org.eclipse.jface.window import Window
#from SWTFileDialog import *    
        
    
dialog = FileDialog(display.getCurrent().getActiveShell())
a = dialog.open() 