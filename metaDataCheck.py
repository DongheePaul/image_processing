from PIL import Image
from PIL.ExifTags import TAGS
import os

path = "/home/donghee/Downloads/forRemovingMetadata/removedMetadata/test/hong/nometa/"

for x in os.listdir(path):
    if '.png' in x:
        print(x)
        imgFile = Image.open(path+x)
        info = imgFile._getexif()

        try:
            for tag, value in info.items():
                decoded = TAGS.get(tag, tag)
                print(decoded, value)
        
        except AttributeError as e:
            print(e)