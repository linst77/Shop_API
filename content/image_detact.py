import PIL.Image
from io import BytesIO
from django.core.files import File
import os


def de_alpha(file):
    files = file
    img = PIL.Image.open(file)

    if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
        file_name = os.path.splitext(files.name)[0] + ".jpg"
        th_img = PIL.Image.new("RGB", img.size, (255, 255, 255))
        th_img.paste(img, mask=img.split()[3])
        img = th_img
        image_file = BytesIO()
        img.save(image_file, "JPEG", quality=100)
        file = File(image_file, name=file_name)
        return file
    else:
        return files


def de_thumb(file):
    size_wh = (110, 62)
    files = file
    img = PIL.Image.open(file)
    file_name = os.path.splitext(files.name)[0] + ".jpg"

    img.thumbnail((size_wh[0], size_wh[0] * 3))

    # if image is bigger then 122
    if img.size[1] > size_wh[1]:
        img = img.crop((0, 0, size_wh[0], size_wh[1]))

    # if image is smaller then 122
    elif img.size[1] < size_wh[1]:
        img = img.resize((size_wh))

    if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
        th_img = PIL.Image.new("RGB", img.size, (255, 255, 255))
        th_img.paste(img, mask=img.split()[3])
        img = th_img

    image_file = BytesIO()
    img.save(image_file, "JPEG", quality=60)
    thumbnail = File(image_file, name=file_name)

    return thumbnail
