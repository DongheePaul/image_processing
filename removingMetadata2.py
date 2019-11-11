from PIL import Image
from PIL.ExifTags import TAGS
import os

path = "/home/donghee/Downloads/forRemovingMetadata/removedMetadata/test/hong/"

for x in os.listdir(path):
    if '.png' in x:
        print(x)
        imgFile = Image.open(path+x)
        
        data = list(imgFile.getdata())
        image_without_exif = Image.new(imgFile.mode, imgFile.size)
        image_without_exif.putdata(data)

        image_without_exif.save('/home/donghee/Downloads/forRemovingMetadata/removedMetadata/test/hong/nometa/no_'+x)


        # imgFile.save('/home/donghee/Downloads/forRemovingMetadata/removedMetadata/test/hong copy/noemta/no_'+x)