import img2pdf
from PIL import Image
import os

#storing img path
img_path="C:\Users\WELCOME\Desktop\Charusat\Result\sem 3 result.png"

#storing pdf path
pdf_path="C:\Users\WELCOME\Desktop\Charusat\Result\sem 3 result.pdf"

#opening image
image=Image.open(img_path)

#converting into chunks
pdf_bytes=img2pdf.convert(image.filename)

#opening file
file=open(pdf_path,"wb")

#writing pdf file with chunks
file.write(pdf_bytes)

#closing image and file
image.close()
file.close()