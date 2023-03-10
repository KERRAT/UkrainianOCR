import os
from PIL import Image, ImageDraw, ImageFont, ImageOps

letters = [
    'А', 'Б', 'В', 'Г', 'Ґ', 'Д', 'Е', 'Є', 'Ж', 'З', 'И', 'І', 'Ї', 'Й', 'К', 'Л',
    'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ю', 'Я',
    'а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м',
    'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я'
]

# Replace the following list with a function to automatically get
# installed fonts that support Ukrainian letters on any system


fon1ts = [ 'Lato-Black-Italic', 'Symbola',
    'Trebuchet-MS', 'Georgia', 'Century-Schoolbook-L-Bold', 'FreeSerif-Italic',
     'Nimbus-Sans-L-Bold-Italic', 'Liberation-Sans',
    'Nimbus-Mono-L-Bold', 'Nimbus-Mono-L', 'DejaVu-Sans-Condensed', 'Bookman-DemiItalic',
    'Lato-Semibold', 'URW-Palladio-L-Italic', 'Nimbus-Roman-No9-L-Regular-Italic',
    'Ubuntu-Light-Italic', 'Lato-Semibold-Italic', 'Nimbus-Sans-L-Bold',
     'Nimbus-Roman-No9-L-Medium-Italic', 'Georgia-Italic',
    'URW-Bookman-L-Light', 'FreeSans', 'Lato-Heavy-Italic', 'Ubuntu-Italic',
    'URW-Palladio-L-Roman', 'Times-New-Roman-Bold-Italic', 'FreeMono-Bold',
    'Liberation-Sans-Bold', 'FreeSans-Bold', 'Lato-Light-Italic', 'Bookman-Demi',
     'FreeMono', 'DejaVu-Sans', 'Century-Schoolbook-L-Roman',
    'Ubuntu-Condensed', 'Nimbus-Sans-L-Regular-Italic', 'FreeSerif', 'Times-New-Roman-Italic',
    'Arial', 'URW-Palladio-L-Bold-Italic', 'Verdana-Italic', 'Ubuntu-Light',
    'Liberation-Serif-Italic', 'Ubuntu-Mono-Bold', 'Liberation-Sans-Narrow-Italic',
    'Liberation-Sans-Narrow', 'DejaVu-Sans-Condensed-Bold-Oblique', 'Nimbus-Sans-L',
    'Ubuntu-Medium', 'Liberation-Serif-Bold', 'DejaVu-Sans-Mono', 'Liberation-Sans-Narrow-Bold-Italic',
    'Lato-Thin', 'Ubuntu-Medium-Italic', 'Century-Schoolbook-L-Bold-Italic',
    'Nimbus-Sans-L-Regular-Condensed-Italic', 'DejaVu-Sans-Bold', 'Ume-Mincho-S3',
    'Liberation-Serif', 'Liberation-Serif-Bold-Italic', 'Liberation-Sans-Bold-Italic',
    'Ume-P-Mincho-S3', 'URW-Gothic-L-Book-Oblique', 'DejaVu-Sans-Condensed-Oblique',
    'URW-Gothic-L-Demi', 'Liberation-Sans-Italic', 'Arial-Bold-Italic', 'Courier-BoldOblique',
     'Ubuntu-Bold', 'WenQuanYi-Micro-Hei', 'Nimbus-Roman-No9-L-Medium',
    'Verdana-Bold-Italic', 'Lato-Italic', 'Lato-Bold', 'Verdana', 'Palatino-Italic',
    'Liberation-Mono', 'Ubuntu-Bold-Italic', 'Liberation-Mono-Bold-Italic',
    'URW-Bookman-L-Demi-Bold', 'Lato-Bold-Italic', 'Andale-Mono',
    'Nimbus-Mono-L-Bold-Oblique', 'Lato-Thin-Italic', 'FreeSans-Oblique',
    'FreeMono-Bold-Oblique', 'Nimbus-Sans-L-Regular-Condensed', 'Liberation-Mono-Italic',
    'DejaVu-Sans-ExtraLight', 'Georgia-Bold', 'Nimbus-Mono-L-Regular-Oblique', 'Ubuntu-Mono',
    'Times-New-Roman', 'FreeSerif-Bold-Italic', 'Nimbus-Roman-No9-L', 'Trebuchet-MS-Bold-Italic',
    'Lato-Medium-Italic', 'FreeSans-Bold-Oblique', 'URW-Bookman-L-Light-Italic',
    'Comic-Sans-MS', 'URW-Gothic-L-Demi-Oblique', 'URW-Bookman-L-Demi-Bold-Italic',
     'Lato-Regular', 'Arial-Black', 'Lato-Light',
    'FreeMono-Oblique', 'DejaVu-Sans-Condensed-Bold', 'Nimbus-Sans-L-Bold-Condensed', 'Lato-Medium',
    'DejaVu-Sans-Mono-Bold', 'Courier-Oblique', 'DejaVu-Sans-Oblique', 'Lato-Hairline-Italic',
    'FreeSerif-Bold', 'Verdana-Bold', 'Lato-Hairline', 'Trebuchet-MS-Italic', 'Georgia-Bold-Italic',
    'Liberation-Sans-Narrow-Bold', 'Times-New-Roman-Bold', 'Trebuchet-MS-Bold',
    'Century-Schoolbook-L-Italic', 'DejaVu-Sans-Bold-Oblique', 'URW-Palladio-L-Bold', 'Lato-Black',
    'Ubuntu', 'Impact', 'Comic-Sans-MS-Bold', 'Lato-Heavy', 'Arial-Bold', 'DejaVu-Sans-Mono-Bold-Oblique',
    'URW-Gothic-L-Book', 'Courier-New-Bold-Italic', 'Courier-New-Italic', 'Courier-New','Ubuntu-Mono-Italic', 'Ubuntu-Mono-Bold-Italic',
    'DejaVu-Sans-Mono-Oblique', 'Ume-P-Mincho', 'Arial-Italic','Courier-New-Bold']

len_letters = len(letters)
directory = 'generate\\fonts'

for i in range(len_letters):
    for file_name in os.listdir(directory):
      font = os.path.join(directory, file_name)
      if os.path.isfile(font):
            # Создаем изображение
            img = Image.new('L', (28, 28), color='black')

            # Создаем объекты ImageDraw и ImageFont
            draw = ImageDraw.Draw(img)
            font_obj = ImageFont.truetype(font, size=20)

            # Рисуем букву по центру изображения
            textbbox = draw.textbbox((0, 0), letters[i], font=font_obj)
            text_width, text_height = textbbox[2] - textbbox[0], textbbox[3] - textbbox[1]

            x = (28 - text_width) / 2
            y = (28 - text_height) / 2 + 5
            draw.text((x, y), letters[i], fill='white', font=font_obj)

            img.save(f'img/{i}.{file_name}.png')
            print(f'{i}.{font}.png')
