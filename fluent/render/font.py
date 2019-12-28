from sdl2.ext import FontManager

from os.path import join


path = __file__.replace('/render/font.py', '/assets/')
manager = FontManager(font_path=join(path, 'bold.ttf'), size=14)

for font in ['bold_italic.ttf', 'extra_bold.ttf',
             'extra_bold_italic.ttf', 'italic.ttf', 'light.ttf',
             'light_italic.ttf', 'regular.ttf', 'semi_bold.ttf',
             'semi_bold_italic.ttf']:
    manager.add(font_path=join(path, font), size=14)
