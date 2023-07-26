from PIL import Image, ImageDraw


from io import BytesIO
from django.core.files import File
from PIL import Image

# Подготавливает маску, рисуя её в <antialias> раз больше и
# затем уменьшая, чтобы получилось сглаженно.
def prepare_mask(size, antialias = 2):
    mask = Image.new('L', (size[0] * antialias, size[1] * antialias), 0)
    ImageDraw.Draw(mask).ellipse((0, 0) + mask.size, fill=255)
    return mask.resize(size, Image.LANCZOS)

def crop(im, s):
    w, h = im.size
    k = w / s[0] - h / s[1]
    if k > 0: im = im.crop(((w - h) / 2, 0, (w + h) / 2, h))
    elif k < 0: im = im.crop((0, (h - w) / 2, w, (h + w) / 2))
    return im.resize(s, Image.LANCZOS)


def make_thumbnail(image,  name, size=(150, 150),):
    """Создает миниатюры заданного размера"""
    im = Image.open(image)
    im.convert('RGB')
    im.thumbnail(size)
    thumb_io = BytesIO()
    im.save(thumb_io, 'PNG', quality=85)
    thumbnail = File(thumb_io, name=f"{name}.jpeg")
    return thumbnail