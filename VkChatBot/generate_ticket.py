from io import BytesIO

import requests
from PIL import Image, ImageDraw, ImageFont

TEMPLATE_PATH = "ticket_template.png"
FONT_PATH = "Roboto-Regular.ttf"
FONT_SIZE = 20

COLOR_WHITE = 255, 255, 255, 255

NAME_OFFSET = (65, 290)
EMAIL_OFFSET = (65, 320)

AVATAR_SIZE = 100
AVATAR_OFFSET = (65, 130)


def generate_ticket(name, email):
    base = Image.open(TEMPLATE_PATH).convert('RGBA')
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    draw = ImageDraw.Draw(base)

    draw.text(NAME_OFFSET, name, font=font, fill=COLOR_WHITE)
    draw.text(EMAIL_OFFSET, email, font=font, fill=COLOR_WHITE)

    response = requests.get(url=f'https://i.pravatar.cc/{AVATAR_SIZE}?u={email}')

    avatar_file_like = BytesIO(response.content)
    avatar = Image.open(avatar_file_like)

    base.paste(avatar, AVATAR_OFFSET)

    temp_file = BytesIO()
    base.save(temp_file, 'png')

    temp_file.seek(0)

    return temp_file
