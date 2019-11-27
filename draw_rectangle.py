from PIL import Image, ImageDraw, ImageFont
import json
import os

#Draw rectangle using xywh on image file. And save it.
json_path = 'final_data_prac.json'
path_file = './01/'
jpg_Image_file_path = './01/01_0001.jpg'
font = ImageFont.truetype('NotoSansCJKkr-Medium.otf', 40)



#json파일을 연다.
with open(json_path) as data_file:
    data = json.loads(data_file.read())
    #get number of files that have worked in json
    lenth_data = len(data)

    checkint = 0
    checki = 9000
    jpg_Image_file = Image.open(jpg_Image_file_path)

    draw = ImageDraw.Draw(jpg_Image_file)

    for item in data:
        for contents in item['Contents']:
            x = contents["Geometry"]["LocValue"][0]
            y = contents["Geometry"]["LocValue"][1]
            w = contents["Geometry"]["LocValue"][2]
            h = contents["Geometry"]["LocValue"][3]

            shpae = [(x, y), (x+w, y+h)]
            draw.rectangle(shpae, outline="red")

            text = contents["Text"]
            labelpoint_tuple = (x-5, y-37)
            draw.text(labelpoint_tuple, text, font=font, fill=(255,0,0,255), align='left')


    jpg_Image_file.save("./test.jpg")
