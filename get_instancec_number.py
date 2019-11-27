from PIL import Image, ImageDraw, ImageFont
import json
import os


#get instances number in json file. and compare 2 lists.
json_path = 'final_data.json'
path_file = './01/'

#json파일을 연다.
with open(json_path) as data_file:
    data = json.loads(data_file.read())
    #get number of files that have worked in json
    lenth_data = len(data)
    intForCount = 0
    listForInstance = []
    numberOfInstance = 0
    #get every file in json
    while intForCount < lenth_data :
        #get every instance that each image file have. 'Contents' list have information of every text in an imagefile.
        contents = data[intForCount]['Contents']
        numberOfInstance += len(contents)
        intForCount += 1


    print(numberOfInstance)    



#get number of files that not been worked       

#compare 2 lists's values
def Diff(li1, li2): 
    result_list = []
    result_list = list(set(li1) - set(li2))
    result_list.sort()
    return (result_list)

#print(Diff(raw_file_name_list, listForFilename))
# print(len(Diff(raw_file_name_list, listForFilename)))
