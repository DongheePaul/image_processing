from PIL import Image, ImageDraw, ImageFont
import json
import os


json_path = 'final_data.json'
path_file = './01/'
jpg_Image_file_path = './01/01_0001.jpg'
font = ImageFont.truetype('NotoSansCJKkr-Medium.otf', 40)

#지정된 경로에 있는 모든 파일들을 담는다.
jpgfile_list = os.listdir(path_file)
jpgfile_list.sort()

#json파일을 연다.
with open(json_path) as data_file:
    data = json.loads(data_file.read())

#사진파일리스트에서 사진파일명을 꺼낸다.
for jpg_file in jpgfile_list:
    #제이슨에서 파일명을 꺼낸다.
    
    for item in data:
        file_name = item["Filename"]
        if jpg_file == file_name:
            jpg_Image_file_path = path_file+jpg_file   
            jpg_Image_file = Image.open(jpg_Image_file_path)
            draw = ImageDraw.Draw(jpg_Image_file)
 
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

            jpg_Image_file.save("./visual/"+jpg_file)


