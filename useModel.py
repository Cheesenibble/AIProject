import tensorflow as tf, keras, numpy as np
import sys
from PIL import Image
model = keras.saving.load_model('ScienceFair.keras')
def resize_final(path):

def parse_image(image_path:str):
    img = np.array(Image.open(resize_final(image_path))).ravel() / 255.0
    return np.argmax(model(img).numpy(), axis=-1)

def resize_final(path:str, w:int=720, h:int=480) -> str:
    image = Image.open(path)
    save_path = "received_images_cleaned/" + path.split("/")[-1]
    if image.mode in ("RGBA", "P"):
        image = image.convert("RGB")
    image.resize((w, h)).save(save_path)
    return save_path

#Make a method to test with a folder