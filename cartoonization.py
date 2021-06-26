import io

from cartooner import cartoonize
import cv2
from PIL import Image
import numpy as np


def load_img(bytes_io):
    return Image.open(bytes_io).convert('RGB')


def save_img(pil_image, format_str='PNG'):
    with io.BytesIO() as bytes_io:
        pil_image.save(bytes_io, format=format_str)
        return bytes_io.getvalue()


class Cartoonizer:

    @classmethod
    def pil2cv(cls, image):
        ''' PIL型 -> OpenCV型 '''
        new_image = np.array(image, dtype=np.uint8)
        if new_image.ndim == 2:  # モノクロ
            pass
        elif new_image.shape[2] == 3:  # カラー
            new_image = cv2.cvtColor(new_image, cv2.COLOR_RGB2BGR)
        elif new_image.shape[2] == 4:  # 透過
            new_image = cv2.cvtColor(new_image, cv2.COLOR_RGBA2BGRA)
        return new_image

    @classmethod
    def cv2pil(cls, image):
        ''' OpenCV型 -> PIL型 '''
        new_image = image.copy()
        if new_image.ndim == 2:  # モノクロ
            pass
        elif new_image.shape[2] == 3:  # カラー
            new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB)
        elif new_image.shape[2] == 4:  # 透過
            new_image = cv2.cvtColor(new_image, cv2.COLOR_BGRA2RGBA)
        new_image = Image.fromarray(new_image)
        return new_image

    @classmethod
    def cartoonize(cls, pil_image):
        cv_image = cls.pil2cv(pil_image)
        return cls.cv2pil(cartoonize(cv_image))
