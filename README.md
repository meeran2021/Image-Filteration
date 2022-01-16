# Image-Filteration
This repo consists of files which performs filter operation on list of images present in a directory based on some criteria.
The criterias we are applying here are:- 
1. Image should be greater thean 25kb of size.
2. Image should have a resolution greater than 400x400
3. Image should be in .jpg/.JPEG format
Note: We will be comparing with JPEG format since PIL library of python doesn't support JPG format.


Installation-Required
Python version > 3.0
Pillow for PIL liberary

**Windows**<br />
Type the command in the terminal:<br />
      pip install Pillow

for detailed information on installation of PIL module, <br /> refer to the link:
https://www.geeksforgeeks.org/how-to-install-pil-on-windows/

**Working**<br />
**If you are going through the first version i.e. 'FilterImg.py',  then you will need to follow the following steps:-**
1. Open the 'FilterImg.py' file in your IDE.
2. Go to line 4. You will find this piece of code <br />
    srcPath = r"A:\Learning Materials\Coding\VS Code\Python\Projects\YOLOAutomation\TestImg"
3. replace the path string(inside the double quotes) with the path of your source file directory.
4. Go to line 6. You will find this piece of code <br />
    destPath = r"A:\Learning Materials\Coding\VS Code\Python\Projects\YOLOAutomation\Dest"
5. replace the path string(inside the double quotes) with the path of your destination file directory.
6. Now save the file and run.



**If you are going through the second version i.e. 'FilterImg1.0.py',  then you will need to follow the following steps:-**
1. Open the 'FilterImg1.0.py' file in your IDE.
2. Run the file.
3. Now it would probably be asking for source file path, So, just paste or type the source file path(not including source file name) and hit enter.
4. Now it would probably be asking for destination file path, So, just paste or type the destination file path(not including destination file name) and hit enter.
4. Boom!! It't done.

Don't forget to check the destination folder whether it contains desired files or not.


For any issue, feel free to connect.
