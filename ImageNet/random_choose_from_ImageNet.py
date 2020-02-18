import os, random, shutil
def moveFile(fileDir):
        pathDir = os.listdir(fileDir)    # 取图片的原始路径
        sample = random.sample(pathDir, 200)  # 随机选取picknumber数量的样本图片, picknumber=200
        print (sample)
        for name in sample:
                shutil.move(fileDir+name, tarDir+name)
        return
if __name__ == '__main__':
	fileDir = "./train "    # 源图片文件夹路径
	tarDir = './later'      # 移动到新的文件夹路径
	moveFile(fileDir)
