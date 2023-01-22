

from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkestamp import tkestamp
from tkestamp_batch import tkestamp_batch
from fitz import *

### GUI User interface that calls tkestamp (single .PDF) and tkestamp_batch (Batch folder) in order to stamp .PDF files with the new TKE logo ###


root = Tk()
root.geometry("400x250")
root.title('TKE Stamp Tool')
root.iconbitmap('./tke_icon.ico')



### Section to select a single .PDF File ###
def open_file():
    #global 
    root.filename = filedialog.askopenfilename(initialdir=".\source_files", title ="Select A .PDF File", filetypes=[(".pdf files","*.pdf"),("all files","*")])
    #print(root.filename)  

    ## Measure .PDF File and preset template ###
    file_m = fitz.open(root.filename)
    page_file = file_m[0]
    page_w = page_file.rect.width
    page_h = page_file.rect.height
    ####print(page_w,page_h) Measure file
    if 2405 <= page_w <= 2415 and 1675 <= page_h <= 1690:
        textVar.set(options[0])
    elif 1670 <= page_w <= 1690 and 1185 <= page_h <= 1200:
        textVar.set(options[1])
    elif 1180 <= page_w <= 1200 and 830 <= page_h <= 850:
        textVar.set(options[2])
    elif 540 <= page_w <= 565 and 805 <= page_h <= 820:
        textVar.set(options[3])
    elif 540 <= page_w <= 565 and 805 <= page_h <= 810:
        textVar.set(options[4])
    # elif (page_w,page_h) == (1680,2409):        
    #     page_file.set_rotation(90)
    #     rotated = root.filename.replace(".pdf" or ".PDF","_rotated.pdf")
    #     file_m.save(rotated, incremental=False,encryption = 0)
    #     root.filename = rotated
    #     textVar.set(options[0])
    # Area originally thought for rotating files that are in the orientation position. It does not work for some reason, even though the software is able to rotate the .pdf file.
          
        
        
        
### Place file selection Button ###
btn_fileSel = Button(root,text="Select .PDF", command = open_file, padx= 40, pady=4)

### Section to select a .PDF folder ###
def open_folder():
    #global 
    root.attributes('-topmost', True)
    root.foldername = filedialog.askdirectory(initialdir=".\batch")
    #print(root.foldername)

### Place folder selection Button ###
btn_folderSel = Button(root,text="Select .PDF Folder", command = open_folder, padx= 22, pady=4)



### Drop-down menu with templates ###

n = DoubleVar()
def comboclick(index=None, value=None, op=None):
    
    global n
    if cmb_template.get() == 'CATIA_V4_DINA1':        
        n = 1                
    if cmb_template.get() == 'CATIA_V4_DINA2':        
        n = 2        
    if cmb_template.get() == 'CATIA_V4_DINA3':        
        n = 3        
    if cmb_template.get() == 'CATIA_V4_DINA4_1':        
        n = 4        
    if cmb_template.get() == 'CATIA_V4_DINA4_2':        
        n = 5
#print(n)
      
### List of possible template options ###
options = [
    'CATIA_V4_DINA1',
    'CATIA_V4_DINA2',
    'CATIA_V4_DINA3',
    'CATIA_V4_DINA4_1',
    'CATIA_V4_DINA4_2']

### ComboBox definition area ###
textVar = StringVar(value='Choose a Template')
textVar.trace('w',comboclick)
#n.trace('w',comboclick)

cmb_template = ttk.Combobox(root, value=options, textvariable = textVar,state='readonly', justify = 'center')
cmb_template.bind("<<ComboboxSelected>>", comboclick)
cmb_template['state'] = 'readonly'

### Function that shows button depending on radio button ###
def show_btn():
    global x
    x = mB.get()
    if x == 1:
        cmb_template.place(x= 130 ,y=108)
        btn_folderSel.place_forget()               
        btn_fileSel.place(x=200, y=20)        

    elif x == 2:
        btn_fileSel.place_forget()
        cmb_template.place_forget()              
        btn_folderSel.place(x=200, y=60)



### Radio Buttons for either Single or Batch Mode ###
mB= IntVar()
r1 = Radiobutton(root, text="Single PDF mode",variable=mB, value=1, command=show_btn)

r2 = Radiobutton(root, text="Batch PDF mode",variable=mB, value=2,command=show_btn)

### Call the previously defined tkestamp and tkestamp_batch functions ###
def call_stamp():   
    
    if x == 1:
        print(root.filename)
        tkestamp(n,root.filename)
    elif x == 2:
        tkestamp_batch(root.foldername)


### Place buttons on GUI ###
btn_stamp = Button(root, text="Stamp .PDF", padx= 36, pady=5, command=call_stamp)
btn_quit = Button(root,text="Exit Program", command = root.quit, padx= 33, pady=5)
r1.place (x=25, y =20)
r2.place (x =25, y = 60)
cmb_template.place(x= 130 ,y=108)
btn_stamp.place(x=130, y=150)
btn_quit.place(x=130, y=200)


root.mainloop()