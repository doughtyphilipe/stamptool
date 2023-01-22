
from fitz import *
import webbrowser
from pathlib import *
from tkestamp import tkestamp

#path_file = os.sep.join([path_dir, filename])
### Function that calls the tkestamp function in a loop. It calls all files in one give folder. ###

def tkestamp_batch (folder):
       
    input_dir = Path(folder)
    files = list(input_dir.glob("*.pdf*"))    
    
    for path in files:
        file = str(path)
        file_m = fitz.open(file)
        page_file = file_m[0]
        page_w = page_file.rect.width
        page_h = page_file.rect.height
        

        if 2405 <= page_w <= 2415 and 1675 <= page_h <= 1690:
            n = 1
        elif 1670 <= page_w <= 1690 and 1185 <= page_h <= 1200:
            n = 2
        elif 1180 <= page_w <= 1200 and 830 <= page_h <= 850:
            n = 3
        elif 540 <= page_w <= 565 and 805 <= page_h <= 820:
            n = 4
        elif 540 <= page_w <= 565 and 805 <= page_h <= 810:
            n = 5
        # elif 1675 <= page_w <= 1690 and 2405 <= page_h <= 2415:            
        #     page_file.set_rotation(90)
        # Area originally thought for rotating files that are in the wrong orientation. It does not work for some reason, even though the software is able to rotate the .pdf file.
        else:
            n = 1
        tkestamp(n, file)
        
        
        



