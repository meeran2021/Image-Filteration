from PIL import Image
import os, shutil

# srcPath = r"A:\Learning Materials\Coding\VS Code\images"
# destPath = r"A:\Learning Materials\Coding\VS Code\Dest"

srcPath = input("Enter the path of the source directory: ")
destPath = input("Enter the path of the destination directory: ")
slash = "\ "

# Getting the list of files(file name) present in the source directory
listOfFiles = os.listdir(srcPath) 
# print(listOfFiles)

count = 0           # For counting number of images
for file in listOfFiles:
    src = srcPath + slash[:-1] + file 
    dest = destPath + slash[:-1] + file 
    # print(src)
    # Opening source image 
    img = Image.open(src)

    size = round(os.stat(src).st_size/1024,3)       # size in kb
    width, height = img.size                        # Img width and height
    imgFormat = img.format                          # Getting format of image
    
    # Filtering based on requirement
    if size>25 and width>400 and height>400 and imgFormat == 'JPEG':
        # Copying image into destination directory 
        shutil.copy(src,dest)
        count+=1
print("Successfully copied %s files"%(count))
