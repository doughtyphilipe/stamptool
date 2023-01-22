# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 17:19:58 2022

@author: P.Doughty
"""
import argparse
import fitz
import webbrowser
from pathlib import *

### Function that adds images (stamps) to .pdf files depending on preset coordinates. Only options 1 until 5 were used in the GUI user_interface ###
def tkestamp (n, file):
    
    #Import stamp files from folder

    tke = open("./stamps/LogoTKE_reveal.png", "rb").read()
    tke90gradGZ = open("./stamps/LogoTKE_reveal_90gradGZ.png", "rb").read()
    tke90gradUZ = open("./stamps/LogoTKE_reveal_90gradUZ.png", "rb").read()
    sRE = open("./stamps/schwarzRE_A4.png", "rb").read()
    sRE_A4 = open("./stamps/schwarzRE.png", "rb").read()
    wRE = open("./stamps/weissRE.png", "rb").read()
    wRE_A3 = open("./stamps/weissRE_A3.png", "rb").read()
    wRE_A4 = open("./stamps/weissRE_A4.png", "rb").read()

    #Import the pdf file from folder   
    if ".pdf" in file:
        output= file.replace(".pdf", "_TKE.pdf")
    if ".PDF" in file:
        output= file.replace(".PDF", "_TKE.pdf")
    
    #output = file.replace(".pdf" or ".PDF","_TKE.pdf")
    
    #print("Filename:",file,"Output:",output,"n:",n)
    if n == 1:              
        

        image_rectangle1 = fitz.Rect(1854,1524,2154,1564)
        image_rectangle2 = fitz.Rect(1870,1518,1886,1663)
        image_rectangle3 = fitz.Rect(0,1662,2412,1690)
        file_handle = fitz.open(file)
        first_page = file_handle[0]

        first_page.insert_image(image_rectangle1, stream=tke)
        first_page.insert_image(image_rectangle2, stream=sRE)
        first_page.insert_image(image_rectangle3, stream=wRE)

        file_handle.save(output)
        #webbrowser.open_new(output)
    if n == 2:
        
        image_rectangle1 = fitz.Rect(1164,1030,1348,1070)
        image_rectangle2 = fitz.Rect(1140,1029,1159,1173)
        image_rectangle3 = fitz.Rect(0,1176,1679,1188)
        file_handle = fitz.open(file)
        first_page = file_handle[0]

        first_page.insert_image(image_rectangle1, stream=tke)
        first_page.insert_image(image_rectangle2, stream=sRE)
        first_page.insert_image(image_rectangle3, stream=wRE)

        file_handle.save(output)
        #webbrowser.open_new(output)
    if n == 3:
        
        image_rectangle1 = fitz.Rect(678,685,858,727)
        image_rectangle2 = fitz.Rect(651,683,667,827)
        image_rectangle3 = fitz.Rect(0,824,1189,849)
        file_handle = fitz.open(file)
        first_page = file_handle[0]

        first_page.insert_image(image_rectangle1, stream=tke)
        first_page.insert_image(image_rectangle2, stream=sRE)
        first_page.insert_image(image_rectangle3, stream=wRE_A3)

        file_handle.save(output)
        #webbrowser.open_new(output)
                               
    if n == 4:
        
        image_rectangle1 = fitz.Rect(44,653,224,690)
        image_rectangle2 = fitz.Rect(18,642,33,793)
        image_rectangle3 = fitz.Rect(0,794,558,812)
        file_handle = fitz.open(file)
        first_page = file_handle[0]

        first_page.insert_image(image_rectangle1, stream=tke)
        first_page.insert_image(image_rectangle2, stream=sRE_A4)
        first_page.insert_image(image_rectangle3, stream=wRE_A4)

        file_handle.save(output)
        #webbrowser.open_new(output)
    if n == 5:
        
        image_rectangle1 = fitz.Rect(43,653,224,688)
        image_rectangle2 = fitz.Rect(18,649,33,793)
        image_rectangle3 = fitz.Rect(0,794,558,812)
        file_handle = fitz.open(file)
        first_page = file_handle[0]

        first_page.insert_image(image_rectangle1, stream=tke)
        first_page.insert_image(image_rectangle2, stream=sRE_A4)
        first_page.insert_image(image_rectangle3, stream=wRE_A4)

        file_handle.save(output)
        #webbrowser.open_new(output)
    if n == 6:
        output = 'Federzeichnung_DINA4_TKE.pdf'
        image_rectangle1 = fitz.Rect(134,743,278,783)
        image_rectangle3 = fitz.Rect(0,824,594,834)
        file_handle = fitz.open(file)
        first_page = file_handle[0]

        first_page.insert_image(image_rectangle1, stream=tke)
        first_page.insert_image(image_rectangle3, stream=wRE)

        file_handle.save(output)
        #webbrowser.open_new(output)
    if n == 7:
        output = 'Handzeichnung_DINA1_TKE.pdf'
        image_rectangle1 = fitz.Rect(2919,2314,3044,2360)
        image_rectangle3 = fitz.Rect(0,2403,3381,2417)
        file_handle = fitz.open(file)
        first_page = file_handle[0]

        first_page.insert_image(image_rectangle1, stream=tke)
        first_page.insert_image(image_rectangle3, stream=wRE)

        file_handle.save(output)
        #webbrowser.open_new(output)
    if n == 8:
        output = 'Handzeichnung_DINA2_1_TKE.pdf'
        image_rectangle1 = fitz.Rect(90,2962,142,3171)
        image_rectangle3 = fitz.Rect(0,3502,2456,3522)
        file_handle = fitz.open(file)
        first_page = file_handle[0]

        first_page.insert_image(image_rectangle1, stream=tke90gradUZ)
        first_page.insert_image(image_rectangle3, stream=wRE)
        #TKE Logo um 90 Grad umdrehen gegenuhrzeigersinn
        file_handle.save(output)
        #webbrowser.open_new(output)
    if n == 9:
        output = 'Handzeichnung_DINA2_2_TKE.pdf'
        image_rectangle1 = fitz.Rect(1262,1146,1363,1186)
        image_rectangle3 = fitz.Rect(0,1207,1721,1224)
        file_handle = fitz.open(file)
        first_page = file_handle[0]

        first_page.insert_image(image_rectangle1, stream=tke)
        first_page.insert_image(image_rectangle3, stream=wRE)

        file_handle.save(output)
        #webbrowser.open_new(output)
    if n == 10:
        output = 'Handzeichnung_DINA3_1_TKE.pdf'
        image_rectangle1 = fitz.Rect(838,796,919,834)
        image_rectangle3 = fitz.Rect(0,856,1224,872)
        file_handle = fitz.open(file)
        first_page = file_handle[0]

        first_page.insert_image(image_rectangle1, stream=tke)
        first_page.insert_image(image_rectangle3, stream=wRE)

        file_handle.save(output)
        #webbrowser.open_new(output)
    if n == 11:
        output = 'Handzeichnung_DINA3_2_TKE.pdf'
        image_rectangle1 = fitz.Rect(773,793,882,824)
        image_rectangle3 = fitz.Rect(0,846,1219,860)
        file_handle = fitz.open(file)
        first_page = file_handle[0]

        first_page.insert_image(image_rectangle1, stream=tke)
        first_page.insert_image(image_rectangle3, stream=wRE)

        file_handle.save(output)
        #webbrowser.open_new(output)
    if n == 12:
        output = 'Handzeichnung_DINA3_3_TKE.pdf'
        image_rectangle1 = fitz.Rect(772,792,884,835)
        image_rectangle3 = fitz.Rect(0,860,1220,872)
        file_handle = fitz.open(file)
        first_page = file_handle[0]

        first_page.insert_image(image_rectangle1, stream=tke)
        first_page.insert_image(image_rectangle3, stream=wRE)

        file_handle.save(output)
        #webbrowser.open_new(output)
    if n == 13:
        output = 'Handzeichnung_DINA3_4_TKE.pdf'
        image_rectangle1 = fitz.Rect(757,787,856,827)
        image_rectangle3 = fitz.Rect(0,853,1222,864)
        file_handle = fitz.open(file)
        first_page = file_handle[0]

        first_page.insert_image(image_rectangle1, stream=tke)
        first_page.insert_image(image_rectangle3, stream=wRE)

        file_handle.save(output)
        #webbrowser.open_new(output)
    if n == 14:
        output = 'Handzeichnung_DINA3_5_TKE.pdf'
        image_rectangle1 = fitz.Rect(1217,1145,1380,1184)
        image_rectangle3 = fitz.Rect(0,1209,1717,1224)
        file_handle = fitz.open(file)
        first_page = file_handle[0]

        first_page.insert_image(image_rectangle1, stream=tke)
        first_page.insert_image(image_rectangle3, stream=wRE)

        file_handle.save(output)
        #webbrowser.open_new(output)
    if n == 15:
        output = 'Handzeichnung_DINA3_6_TKE.pdf'
        image_rectangle1 = fitz.Rect(734,797,875,841)
        image_rectangle3 = fitz.Rect(0,856,1224,875)
        file_handle = fitz.open(file)
        first_page = file_handle[0]

        first_page.insert_image(image_rectangle1, stream=tke)
        first_page.insert_image(image_rectangle3, stream=wRE)

        file_handle.save(output)
        #webbrowser.open_new(output)
    if n == 16:
        output = 'Handzeichnung_DINA4_1_TKE.pdf'
        image_rectangle1 = fitz.Rect(238,788,449,837)
        image_rectangle3 = fitz.Rect(0,841,878,863)
        #### Zertifikatstempel noch überprüfen, TKE Logo um 90 Grad umdrehen gegenzeigersinn
        image_rectangle4 = fitz.Rect(575,484,630,592)

        file_handle = fitz.open(file)
        first_page = file_handle[0]

        first_page.insert_image(image_rectangle1, stream=tke)
        first_page.insert_image(image_rectangle3, stream=wRE)
        first_page.insert_image(image_rectangle4, stream=tke90gradGZ)

        file_handle.save(output)
        #webbrowser.open_new(output)
    if n == 17:
        output = 'Handzeichnung_DINA4_2_TKE.pdf'
        image_rectangle1 = fitz.Rect(142,800,302,840)
        image_rectangle3 = fitz.Rect(0,866,631,883)
        file_handle = fitz.open(file)
        first_page = file_handle[0]

        first_page.insert_image(image_rectangle1, stream=tke)
        first_page.insert_image(image_rectangle3, stream=wRE)

        file_handle.save(output)
        #webbrowser.open_new(output)
    if n == 18:
        output = 'Handzeichnung_DINA4_3_TKE.pdf'
        image_rectangle1 = fitz.Rect(174,806,276,845)
        image_rectangle3 = fitz.Rect(0,872,633,886)
        file_handle = fitz.open(file)
        first_page = file_handle[0]

        first_page.insert_image(image_rectangle1, stream=tke)
        first_page.insert_image(image_rectangle3, stream=wRE)

        file_handle.save(output)
        #webbrowser.open_new(output)
    if n == 19:
        output = 'Handzeichnung_DINA4_4_TKE.pdf'
        image_rectangle1 = fitz.Rect(207,796,320,834)
        image_rectangle3 = fitz.Rect(0,856,627,872)
        file_handle = fitz.open(file)
        first_page = file_handle[0]

        first_page.insert_image(image_rectangle1, stream=tke)
        first_page.insert_image(image_rectangle3, stream=wRE)

        file_handle.save(output)
        #webbrowser.open_new(output)
    if n == 20:
        output = 'Handzeichnung_DINA4_5_RStahl_TKE.pdf'
        image_rectangle1 = fitz.Rect(43,653,224,688)
        image_rectangle2 = fitz.Rect(18,649,32,793)
        image_rectangle3 = fitz.Rect(0,795,554,809)
        file_handle = fitz.open(file)
        first_page = file_handle[0]

        first_page.insert_image(image_rectangle1, stream=tke)
        first_page.insert_image(image_rectangle3, stream=wRE)

        file_handle.save(output)
        #webbrowser.open_new(output)
    if n == 21:
        output = 'Handzeichnung_DINA4_6_TKE.pdf'
        image_rectangle1 = fitz.Rect(133,787,283,830)
        image_rectangle3 = fitz.Rect(0,860,628,872)
        file_handle = fitz.open(file)
        first_page = file_handle[0]

        first_page.insert_image(image_rectangle1, stream=tke)
        first_page.insert_image(image_rectangle3, stream=wRE)

        file_handle.save(output)
        #webbrowser.open_new(output)
        
    if n == 22:
        output = 'Handzeichnung_DINA4_2_TKE.pdf'
        image_rectangle1 = fitz.Rect(104,37,165,63)
        image_rectangle3 = fitz.Rect(0,848,623,863)
        file_handle = fitz.open(file)
        first_page = file_handle[0]

        first_page.insert_image(image_rectangle1, stream=tke)
        first_page.insert_image(image_rectangle3, stream=wRE)

        file_handle.save(output)
        #webbrowser.open_new(output)




### Possible use of parser if needed ###


#########  parser ########


# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('index', type=int, default=1,
#                     help='Input Index')
# parser.add_argument('file_name', type=str, default='CATIA_V4_DINA1.pdf',
#                     help='Input file name and .pdf ')

#args = parser.parse_args()
#tkestamp(args.index, args.file)
