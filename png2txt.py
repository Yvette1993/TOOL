import os
import cv2
#import h5py
import numpy as np






### png 2 txt

def data(path,dir_name):
    data = []
    #print(path)
    path_name= path+dir_name
    #print(path_name)
    filenames=os.listdir(path_name)
    filenames.sort()
    for f in filenames:
        if os.path.splitext(f)[-1] == '.png':
            path = path_name + f 
              
            print('{}'.format(path))         
                
            data.append(path)
    return data


def png2txt(path,file_dir,depth_dir):
    rgb = data(path,file_dir)
    print(len(rgb))
    depth=data(path,depth_dir)
    print(len(depth))

  

    if len(rgb) != len(depth):
        try:
            raise ValueError("len(rgb) != len(depth")
        except ValueError :
            print("the number between data and label is not equal")

    return rgb,depth
    
        

def golden(dir):
    #f = open('/home/lisa/data/kitti/train.txt','wt') 
    f = open('/home/lisa/data/kitti/val.txt','wt') 
    cmd = ("cd {}".format(dir))
    os.system(cmd)
    for i in os.listdir(dir):
        path_dir = os.path.join(dir,i)
        print(path_dir)
        #cmd = ("cd {}".format(path))
        #os.system(cmd)
        file_dir = '/image_02/data/'
        depth_dir = '/proj_depth/groundtruth/image_02/'
        rgb,depth = png2txt(path_dir,file_dir,depth_dir)
        for j,k in zip(rgb,depth):
            f.write('{} {}\n\t'.format(j,k))
    f.close()

if __name__ =='__main__':
    train_dir = '/home/lisa/data/kitti/train/'
    val_dir = '/home/lisa/data/kitti/val/'

    

    #train = golden(train_dir)
    val = golden(val_dir) 
