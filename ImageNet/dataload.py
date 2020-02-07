import os
from PIL import Image
import numpy as np

def get_name(path):
    with open(path) as lines:
        array = lines.readlines()
        get_list = []
        for i in array:
            i = i.strip('\n')
            get_list.append(i)
    #print(len(get_list))
    return get_list

def load_img(path):
    n = len(path)
    img_list = []
    for i in range(n):
        img = Image.open(path[i]).convert('RGB')
        img = np.array(img .resize((224,224),Image.ANTIALIAS))
        img = img/255.
        img = img.transpose((1,0,2))
        #print(img)
        #print("img.shape:",img.shape)
        #print("img.type:",type(img))
        img_list.append(img)
    return img_list

def dataload(train_path, label_path):
    train_list = get_name(train_path)
    label_list = get_name(label_path)
    train_img = load_img(train_list)
    return np.array(train_img), np.array(label_list)







