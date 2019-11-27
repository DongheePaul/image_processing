from PIL import Image, ImageDraw, ImageFont
import json
import os


#visualization data in json file on imagefile
json_path = 'final_data.json'
path_file = './01/'
font = ImageFont.truetype('NotoSansCJKkr-Thin.otf', 30)

#지정된 경로에 있는 모든 파일들을 담는다.
jpgfile_list = os.listdir(path_file)
jpgfile_list.sort()

#json파일을 연다.
with open(json_path) as data_file:
    data = json.loads(data_file.read())

#사진파일리스트에서 사진파일명을 꺼낸다.
for jpg_file in jpgfile_list:
    #제이슨에서 파일명을 꺼낸다.
    jpg_file_name, jpg_filename_Extension = os.path.splitext(jpg_file)

    for item in data:
        file = item["Filename"]
        file_name, filename_Extension = os.path.splitext(file)

        if jpg_file_name == file_name:
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

            jpg_Image_file.save("./visual_thin/"+jpg_file)


