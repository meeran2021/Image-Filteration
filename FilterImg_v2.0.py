from PIL import Image
import os, shutil

# srcPath = r"A:\Learning Materials\Coding\VS Code\Men Running Shoes Images"
# destPath = r"A:\Learning Materials\Coding\VS Code\Python\Projects\YOLOAutomation\Dest"

def performFilter(srcPath,destPath):
    # print(listOfFiles)
    slash = "\ "
    count = 0           # For counting number of images
    limit = 250         # Setting maximum files to be copied
    
    # Getting the list of files(file name) present in the source directory
    listOfFiles = os.listdir(srcPath) 

    for file in listOfFiles:
        if count>limit:
            break
        
        src = srcPath + slash[:-1] + file 
        dest = destPath + slash[:-1] + file 
        try:
            # Opening source image 
            img = Image.open(src)
        except PermissionError:
            print('Not an image file')

        size = round(os.stat(src).st_size/1024,3)       # size in kb
        width, height = img.size                        # Img width and height
        imgFormat = img.format                          # Getting format of image
        
        # Filtering based on requirement
        if size>25 and width>400 and height>400 and imgFormat == 'JPEG':
            # Copying image into destination directory 
            shutil.copy(src,dest)
            count+=1
    print("Successfully copied %s files"%(count))

def fileRename(filePath, newName):
    # Getting the list of files(file name) present in the directory
    listOfFiles = os.listdir(filePath) 
    # print(listOfFiles)
    slash = "\ "
    i = 1
    for file in listOfFiles:
        src = filePath + slash[:-1] + file 
        dest = filePath + slash[:-1] + newName + str(i) + '.jpg' 
        os.rename(src, dest)    # renaming source file with destination file
        i+=1
    print('Successfully renamed %s files'%(i-1))

def main():
    print('################################ W E L C O M E ################################')
    print('     S. No        Operations')
    print('      1.        Filter images')
    print('      2.        Rename images')
    print('      0.        Exit')
    ans = int(input('Choose any operation: '))
    if ans == 1:
        srcPath = input("Enter path of the source directory: ")
        destPath = input("Enter path of the destination directory: ")
        # slash = "\ "
        performFilter(srcPath,destPath)
        # break
    if ans == 2:
        path = input('Enter path of image directory: ')
        fileName = input('New filename: ')
        fileRename(path,fileName)

main()