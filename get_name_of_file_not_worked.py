from PIL import Image, ImageDraw, ImageFont
import json
import os


json_path = 'final_data.json'
path_file = './01/'

#json파일을 연다.
with open(json_path) as data_file:
    data = json.loads(data_file.read())
    #get number of files in json
    lenth_data = len(data)
    intForCount = 0
    listForFilename = []
    #get every file name in json
    while intForCount < lenth_data :
        file = data[intForCount]['Filename']
        filename, filename_Extension = os.path.splitext(file)
        listForFilename.append(filename)
        intForCount += 1

    listForFilename.sort()

    #get every file name in raw data folder
    raw_file_list = os.listdir(path_file)
    raw_file_list.sort()
    raw_file_name_list = []
    for raw_file in raw_file_list:
        raw_filename, raw_fileExtension = os.path.splitext(raw_file)
        raw_file_name_list.append(raw_filename)
    
    raw_file_name_list.sort()

#get number of files that not been worked       

#compare 2 lists's values
def Diff(li1, li2): 
    result_list = []
    result_list = list(set(li1) - set(li2))
    result_list.sort()
    return (result_list)

print(Diff(raw_file_name_list, listForFilename))
# print(len(Diff(raw_file_name_list, listForFilename)))
