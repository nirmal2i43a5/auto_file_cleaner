
# https://www.youtube.com/watch?v=wwJmoowLVfA
#move raw file extension into particular folder

import os


def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
        

def move(folderName,files):
    for file in files:
        os.replace(file,f"{folderName}/{file}")
        
if __name__=='__main__':    
    files = os.listdir()#all the files that is inside AUTO_FOLDER_CLEANER
    files.remove('clean.py')
    # print(files)

    createIfNotExist('Images')
    createIfNotExist('Docs')
    createIfNotExist('Media')
    createIfNotExist('others')
    #make images folder

    imgExts = ['.jpeg','.png','.jpg']

    #Extracting extension from files
    images = [file for file in files if os.path.splitext(file)[1] in imgExts]#selecting file from files that is present in imgExts
    # print(images)

    docExts = ['.txt','.docx','.doc','.pdf']

    docs = [file for file in files if os.path.splitext(file)[1] in docExts]
    # print(docs)

    mediaExts = ['.mp4','.mp3','.flv']
    medias = [file for file in files if os.path.splitext(file)[1] in mediaExts]
    # print(medias)

    others = []#eg:it gives files that is not in docExts and others
    for file in files:
        ext = os.path.splitext(file)[1]
        if (ext not in docExts) and (ext not in imgExts) and (ext not in mediaExts) and os.path.isfile(file):
            others.append(file)      
        
    move("Images",images)
    move("Docs",docs)
    move("Media",medias)
    move("others",others)