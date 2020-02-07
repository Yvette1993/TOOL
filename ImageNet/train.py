import dataload
from sklearn.model_selection import train_test_split

train_path = "./cfg/train.txt"
label_path = "./cfg/train_label.txt"
label_name = "./cfg/train_label_name.txt"

train,label = dataload.dataload(train_path,label_path)
train = train/255.
print(label.shape)
print(train.shape)

x_train, x_test, y_train, y_test = train_test_split(train, label, test_size=0.3)
print(x_train[0].shape)