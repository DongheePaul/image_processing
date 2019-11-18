from PIL import Image, ImageDraw, ImageFont
import json
import os

#이미지 파일들이 있는 디렉토리를 가르키는 경로
path_jpg = "./01_origin/01"
#제이슨 파일들이 있는 디렉토리를 가르키는 경로
path_json = "./jsondata_origin"


#지정된 경로에 있는 모든 파일들을 담는다.
jpgfile_list = os.listdir(path_jpg)
jsonfile_list = os.listdir(path_json)
#.jpg, .json, tif로 끝나는 모든 파일을 담는다.
file_list_jpg = [file for file in jpgfile_list if file.endswith(".jpg")]
file_list_tif = [file for file in jpgfile_list if file.endswith(".tif")]
file_list_json = [file for file in jsonfile_list if file.endswith(".json")]

file_list_jpg.sort()
file_list_json.sort()
file_list_tif.sort()
fnt = ImageFont.truetype("font1.ttf", 30)


#json, jpg 파일들을 하나씩 뽑아낸다.
for jpg_file in file_list_tif:
    #파일명 추출
    jpg_filename, jpg_fileExtension = os.path.splitext(jpg_file)

    for json_file in file_list_json:
        json_filename, json_fileExtension = os.path.splitext(json_file)

        #json, jpg 파일명이 동일하다면
        if jpg_filename == json_filename:
        #이미지파일을 연다
            jpg_Image_file = Image.open(os.path.join(path_jpg, jpg_filename+jpg_fileExtension))
        #json파일을 연다.
            with open(os.path.join(path_json, json_filename+json_fileExtension), encoding='euc-kr') as data_file:    
                data = json.loads(data_file.read())

            #get number of bbox objects. 
                number_of_shapes_objects = len(data['shapes'])            
                intForshapesNumber = 0
                point_list=[]
                labelpoint_list=[]
                #비박스 갯수만큼 포문을 돌려서 label과 x,y 좌표를 꺼낸다. 그리고 그것을 이미지에 그린다.
                while intForshapesNumber < number_of_shapes_objects:
                    draw = ImageDraw.Draw(jpg_Image_file)
                    #첫번째 점
                    start_point_list = (data['shapes'][intForshapesNumber]['points'][0])
                    #두번째 점
                    end_point_list = (data['shapes'][intForshapesNumber]['points'][1])
                    #라벨 데이터
                    label = (data['shapes'][intForshapesNumber]['label'])
                    #튜플로 바꾼 뒤 리스트에 넣는다.
                    start_point_tuple = tuple(start_point_list)
                    end_point_tuple = tuple(end_point_list)
                    point_list.append(start_point_tuple)
                    point_list.append(end_point_tuple)
                    #직사각형을 그린다.
                    draw.rectangle(point_list, outline="red")

                    #첫번쨰 점의 x좌표, y좌표
                    start_point_xlist = (data['shapes'][intForshapesNumber]['points'][0][0])
                    start_point_ylist = (data['shapes'][intForshapesNumber]['points'][0][1] - 40.00)
                    labelpoint_list.append(start_point_xlist)
                    labelpoint_list.append(start_point_ylist)
                    labelpoint_tuple = tuple(labelpoint_list)
                    #start_point에 글자를 적어야할듯. draw.text의 첫번째 파라미터는 튜플
                    draw.text(labelpoint_tuple, label, font=fnt, fill=(255,0,0,255), align='right')
                    # #라벨
                    # print(data['shapes'][intForshapes]['label'])
                    #다음 비박스의 json object 값을 뺴기 위해 +1을 한다.
                    intForshapesNumber+= 1
                    #다음 비박스의 json obeject 값을 담기 위해 리스트를 비운다.
                    point_list.clear()
                    labelpoint_list.clear()            

            jpg_Image_file.save("./visualization_tif/"+jpg_filename+jpg_fileExtension)
        else:
            print("not match")
            continue

