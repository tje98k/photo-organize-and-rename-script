
from PIL import Image
import os
import shutil


folders=[]
print('Enter dir of photos')
dir = input()
os.chdir(dir)
print('Changing dir to' + (os.getcwd()))

for img in os.listdir():
        if str((Image.open(img)._getexif()[36867]))[0:10] in img:
           pass
        else:
            if '.jpg' in img:
                os.rename(img,str(Image.open(img)._getexif()[36867]).replace(':', '-')+'.jpg')
print('Renamed photos')
for img in os.listdir():
    if img[0:10] in os.listdir():
            pass
    else:
            os.mkdir(img[0:10])
for img in os.listdir():
    if '.jpg' in img:
        pass
    else:
        folders.append(img)
print('created folder(s)' + str(folders))
for img in os.listdir():
    if '.jpg' in img:
        shutil.move(img, str(img[0:10] + '/' + img))
print('moved images to folders')
