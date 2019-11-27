import os
import shutil
import random


#copy file in one directory to another directory ramdomly
path_dir = './visual_thin/'
outputdir = './random_file/'

files = [file for file in os.listdir(path_dir) if os.path.isfile(os.path.join(path_dir, file))]

    # Amount of random files you'd like to select
random_amount = 130
for x in range(random_amount):
    file = random.choice(files)
    shutil.copyfile(os.path.join(path_dir, file), os.path.join(outputdir, file))