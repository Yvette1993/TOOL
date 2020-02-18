import os, random, shutil

def moveFile(fileDir,tarDir):
        pathDir = os.listdir(fileDir)    # 读取fileDir文件夹下的所有子文件夹

        for path in pathDir:
   
            path2=os.listdir(fileDir+'/'+path) # 读取到每个path文件夹的所有子文件记为path2

            filenumber=len(path2)   # 计算单个path的文件总数

            rate=0.2   

            picknumber=int(filenumber*rate) 

            sample = random.sample(path2, picknumber)  # 随机选取picknumber数量的样本图片
            
            #print (sample)
            
            for name in sample:
                
                if not os.path.exists(tarDir+'/'+path): # 如果目标文件夹的子文件夹不存在，就在目标文件夹中建立子文件夹
                    os.mkdir(tarDir+'/'+path) 
                    print(tarDir+'/'+path)
                shutil.move(fileDir+'/'+path+'/'+name, tarDir+'/'+path+'/'+name)
       
        return pathDir,path,filenumber,path2
        
if __name__ == '__main__':
    ROOT_PATH = os.getcwd() 
    fileDir = os.path.join(ROOT_PATH,'train')      # raw image path  
    print(fileDir)
    tarDir = os.path.join(ROOT_PATH,'test')      # new image path    
    print(tarDir)
    p,p2,l,y=moveFile(fileDir,tarDir)
