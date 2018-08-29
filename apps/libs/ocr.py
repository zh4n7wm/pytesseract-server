import io

import pytesseract
from PIL import Image


def image_to_string(image, lang=None):
    """
    :param image: bytes data or PIL.Image
    """

    if isinstance(image, bytes):
        image = Image.open(io.BytesIO(image))

    return pytesseract.image_to_string(image, lang=lang)


def image_path_to_string(path, lang=None):
    """
    返回识别出的字符串

    :param path: image path
    :return: str
    """

    image = Image.open(path)
    return image_to_string(image, lang=lang)
