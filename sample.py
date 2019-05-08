import pytesseract
import sys
import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image

root = Tk()
root.withdraw()
try:
    filename = filedialog.askopenfilename(parent=root,
                                          initialdir=os.path.join(os.getcwd(),'images'), 
                                          title="Select file",
                                          filetypes=[("All Files","*.*")])
    if filename!= "":
        image= Image.open(filename)
        ocr = pytesseract.image_to_string(image, 
                                        lang='eng', 
                                        config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
        messagebox.showinfo("Image to Text",ocr)
    else :
        raise ValueError("Invalid filename")
except FileNotFoundError as fileError:
    messagebox.showinfo("Some error occurred","File not found. Please specify correct file name.")
except ValueError as verr:
    messagebox.showinfo("Some error occurred",verr)    
    sys.exit()
except Exception as e:
    messagebox.showinfo("Some error occurred",e)
    sys.exit()

           