# Stamptool

Stamptool is a python project that automatically stamps PDF files using PyMuPDF.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install PyMuPDF, if you wish to run this code locally.

```bash
python -m pip install --upgrade pip
python -m pip install --upgrade pymupdf
```

## Usage
This code revolves around the insert_image function. It inserts an image in a PDF file using (X1X2, Y1Y2) coordinates.
In the tke_stamp.py file, it is done as follows.

```python
import fitz

## import stamp 
tke = open("./stamps/LogoTKE_reveal.png", "rb").read()

## define coordinates
mage_rectangle1 = fitz.Rect(1854,1524,2154,1564)

## insert image (stamp)
first_page.insert_image(image_rectangle1, stream=tke)

## save outputpdf

file_handle.save(output)

```

The tkestamp_batch.py file identifies the width and height of the file, recognizes it per size, i.A. A4 size, and then stamps automatically the whole folder were the PDF files are.

```python

## measure page width
page_w = page_file.rect.width

## measure page height
page_h = page_file.rect.height
        
## identify each page
if 2405 <= page_w <= 2415 and 1675 <= page_h <= 1690:
  n = 1

## apply function from the tke_stamp.py file.
tkestamp(n, file)


```

The user_interface.py file simply generates a usabel UI for this application. It uses TKinter, that can be installed as follows.

```bash
python -m pip install --upgrade pip
python -m pip install --upgrade pymupdf
```

Import inside python file.
```python
from tkinter import *

```


