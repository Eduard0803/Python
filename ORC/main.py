from PIL import Image
import pytesseract
import cv2
import sys

args = sys.argv
if len(args) < 2:
    args.append('example.jpg')

image = Image.open('images/' + args[1])
image = image.convert('L') # converte em preto e branco

text = pytesseract.image_to_string(image) # extrai o texto da imagem
print(text)
