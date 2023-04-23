import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageOps

letters = [
    'А','Б','В','Г','Ґ','Д','Е','Є','Ж','З','И','І','Ї','Й','К',
    'Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ',
    'Ь','Ю','Я','а','б','в','г','ґ','д','е','є','ж','з','и','і',
    'ї','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц',
    'ч','ш','щ','ь','ю','я','1','2','3','4','5','6','7','8','9',
    '0','№','%','@',',','.','?',':',';','"','!','(',')','-','\''
]

# Replace the following list with a function to automatically get
# installed fonts that support Ukrainian letters on any system


fon1ts = [


    'Ubuntu-Light-Italic',
    'FreeSans', 'Ubuntu-Italic',
    'Times-New-Roman-Bold-Italic', 'FreeMono-Bold',
     'FreeSans-Bold',
     'FreeMono',
    'Ubuntu-Condensed',   'Times-New-Roman-Italic',
    'Arial', 'Verdana-Italic', 'Ubuntu-Light',
     'Ubuntu-Mono-Bold',

    'Ubuntu-Medium',
    'Ubuntu-Medium-Italic',
     'Ume-Mincho-S3',

    'Ume-P-Mincho-S3', 'URW-Gothic-L-Book-Oblique',
    'URW-Gothic-L-Demi', 'Arial-Bold-Italic', 'Courier-BoldOblique',
     'Ubuntu-Bold', 'WenQuanYi-Micro-Hei',
    'Verdana-Bold-Italic', 'Verdana', 'Palatino-Italic',
     'Ubuntu-Bold-Italic',
     'Andale-Mono',
     'FreeSans-Oblique',
    'FreeMono-Bold-Oblique',
      'Ubuntu-Mono',
    'Times-New-Roman',
     'FreeSans-Bold-Oblique',
    'Comic-Sans-MS', 'URW-Gothic-L-Demi-Oblique',
     'Arial-Black',
    'FreeMono-Oblique',
 'Courier-Oblique',
     'Verdana-Bold',
     'Times-New-Roman-Bold',
    'Ubuntu', 'Impact', 'Comic-Sans-MS-Bold', 'Arial-Bold',
    'URW-Gothic-L-Book', 'Courier-New-Bold-Italic', 'Courier-New-Italic', 'Courier-New','Ubuntu-Mono-Italic', 'Ubuntu-Mono-Bold-Italic',
     'Ume-P-Mincho', 'Arial-Italic','Courier-New-Bold']

len_letters = len(letters)
directory = 'generate\\fonts'

for i in range(len_letters):
    for file_name in os.listdir(directory):
      font = os.path.join(directory, file_name)
      if os.path.isfile(font):
            # Створюємо зображення
            img = Image.new('L', (28, 28), color='black')

            # Створюємо об'єкти ImageDraw і ImageFont
            draw = ImageDraw.Draw(img)
            font_obj = ImageFont.truetype(font, size=20)

            # Рисуємо літеру по центру зображення
            textbbox = draw.textbbox((0, 0), letters[i], font=font_obj)
            text_width, text_height = textbbox[2] - textbbox[0], textbbox[3] - textbbox[1]

            x = (28 - text_width) / 2
            y = (28 - text_height) / 2
            draw.text((x, y), letters[i], fill='white', font=font_obj)

            img.save(f'img/{i}.{file_name}.png')

            print(f'{i}.{font}.png')
