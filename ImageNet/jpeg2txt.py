import os
import re

ROOT_PATH = os.getcwd() 
###root_path = '/media/lisali/7d00416d-8275-4263-979a-70ae47372950/ImageNet2012'
print("root path:" + ROOT_PATH)

####jpeg to txt

train = open("{}/train.txt".format(ROOT_PATH),"w")
train_label =  open("{}/train_label.txt".format(ROOT_PATH),"w")
label_list = open("{}/label_list.txt".format(ROOT_PATH),"w")

test  = open("{}/test.txt".format(ROOT_PATH),"w")
test_label =  open("{}/test_label.txt".format(ROOT_PATH),"w")

#val   = open("{}/val.txt".format(ROOT_PATH),"w")
#val_label =  open("{}/val_label.txt".format(ROOT_PATH),"w")



for root,dirs,files in os.walk(ROOT_PATH):
    #print("root",root)
    pattern = re.compile(r'n([0-9]+)')
    if 'train' in root:
        m = pattern.search(root)
        if m != None:
            #print(m.group())
            label_list.write(m.group()+'\n')
        for name in files: 
            m = pattern.search(root)
            if m != None:
                #print(m.group())
                train_label.write(m.group()+'\n')
            if os.path.splitext(name)[-1] == '.JPEG':
                img_path = os.path.join(root,name)
                #print("img_path",img_path)
                train.write(img_path+'\n')
            else:
                print("No JPEG image")
          
    elif 'test' in root:
        m = pattern.search(root)
        if m != None:
            #print(m.group())
            test_label.write(m.group()+'\n')
        for name in files:
            if os.path.splitext(name)[-1] == '.JPEG':
                img_path = os.path.join(root,name)
                test.write(img_path+'\n')
            else: 
                print("No JPEG image")
    """  
    elif 'val' in root:
        m = pattern.search(root)
        if m != None:
            #print(m.group())
            val_label.write(m.group()+'\n')
        for name in files:
            if os.path.splitext(name)[-1] == '.JPEG':
                img_path = os.path.join(root,name)
                val.write(img_path+'\n')
            else:
                print("No JPEG image")
"""
train.close()
train_label.close()
label_list.close()
test.close()
test_label.close()
#val.close()


####### build label_name.txt
     









