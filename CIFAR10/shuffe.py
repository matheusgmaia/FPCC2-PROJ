import os
import random
import shutil


files_list = []

for root, dirs, files in os.walk("/home/maia/Documents/Universidade/Universidade/UNIVERSIDADE/EXPERIMENTO/0DATASETS/XRAY/train"):
    for file in files:
        #all 
        if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
            files_list.append(os.path.join(root, file))


#print images
#lets me count and print the amount of jpeg,jpg,pmg 
file_count = len(files_list)
print(file_count)

random.shuffle(files_list)


destPathN = "/home/maia/Documents/Universidade/Universidade/UNIVERSIDADE/EXPERIMENTO/0DATASETS/XRAY_RANDOM/train/NORMAL/"
destPathP = "/home/maia/Documents/Universidade/Universidade/UNIVERSIDADE/EXPERIMENTO/0DATASETS/XRAY_RANDOM/train/PNEUMONIA/"

for i in range(len(files_list)):
    if(i < 1349):
        shutil.copy(files_list[i], destPathN)
    else:
        shutil.copy(files_list[i], destPathP)