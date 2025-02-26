# -*- coding: utf-8 -*-

import re
import glob
import os
from PIL import Image

# Methods
def crop(infile, height, width):
    im = Image.open(infile)
    imgwidth, imgheight = im.size
    for i in range(imgheight//height):
        for j in range(imgwidth//width):
            box = (j*width, i*height, (j+1)*width, (i+1)*height)
            yield im.crop(box)

# ---------------------------------------------------

pathImgs = '/home/julianorinaldi/Documentos/Mestrado/Cambissolos'
imageFiles = []
for file in glob.glob(f'{pathImgs}/*.jpg'):
    imageFiles.append(file)

imageFiles = sorted(imageFiles)
# -----------------------------------------------------

height=256
width=256
directoryExtracted = f'{pathImgs}/{height}x{width}'
if not os.path.exists(directoryExtracted):
    os.makedirs(directoryExtracted)

cont = 1
contAll = len(imageFiles)
for img in imageFiles:
  infile = img
  print(f'######## Processando {infile} - {cont} de {contAll}')
  cont = cont + 1
  start_num = 1
  pathDir, file = os.path.split(img)
  for k,piece in enumerate(crop(infile,height,width),start_num):
      img=Image.new('RGB', (height, width), 255)
      img.paste(piece)
      pattern = r"([A-Za-z]\d+[A-Za-z])"
      nameFound = re.search(pattern, file)
      fileName = nameFound.group(1)
      fileImg = f"{fileName}-{k}.png"
      path=os.path.join(directoryExtracted, fileImg)
      img.save(path)
      print(path)

# Outro algorítimo
# Instalando pacote image_slicer
#!pip install image_slicer

# import image_slicer
# for img in imageFiles:
#    image_slicer.slice(img, 50)
#    print(f'Finalizado extração de [{img} - {cont} de {contAll} ]\n')
#    cont = cont + 1