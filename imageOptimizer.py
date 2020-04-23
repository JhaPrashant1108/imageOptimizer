from PIL import Image
import os
from os import listdir
from os.path import isfile, join
from datetime import datetime
import time

class Downloader:
    def __init__(self,Order):
        self.originalPath = Order[0]
        self.quality = Order[1]
        self.mode = Order[2]
        self.modeSelector()

    def modeSelector(self):
        if self.mode == "single":
            self.singleMode()
        else:
            self.multipleMode()

    def singleMode(self):
        imagePathList = self.originalPath.split("/")
        print(imagePathList)
        imageName = imagePathList[len(imagePathList)-1]
        finalImagePath = imagePathList[0]+'\\'+imagePathList[1]+'\\'+imagePathList[2]+'\\'+'Pictures'+'\\'+ imageName.split(".")[0]+ '_Resized.' + imageName.split(".")[1]
        self.compressor(self.originalPath,finalImagePath)
    




    def multipleMode(self):
        imageList = []
        self.originalPath = self.originalPath.split('/')
        self.originalPath = "\\".join(self.originalPath)
        for file in listdir(self.originalPath):
            if file.endswith(".jpg") or file.endswith(".JPG") or file.endswith(".jpeg") or file.endswith(".JPEG") or file.endswith(".PNG") or file.endswith(".png"):
                imageList.append(join(self.originalPath, file))
        imagePathList = self.originalPath.split("\\")
        imageName = imagePathList[len(imagePathList)-1]
        pathDirectory = imagePathList[0]+'\\'+imagePathList[1]+'\\'+imagePathList[2]+'\\'+'Pictures'+'\\'+ 'Resized'+ datetime.now().strftime('_%d_%m_%Y_%H_%M_%S')
        if not os.path.exists(pathDirectory):
            os.mkdir(pathDirectory)
        else:
            print("same Folder exist")

        for i in range(len(imageList)):
            imagePath = imageList[i].split('\\')
            imageName = imagePath[len(imagePath)-1]
            finalPath = pathDirectory +'\\'+ imageName.split(".")[0]+ '_Resized.' + imageName.split(".")[1]
            self.compressor(imageList[i],finalPath)




    def compressor(self,initialPath,finalPath):
        img = Image.open(initialPath)
        img = img.resize((img.size[0],img.size[1]),Image.ANTIALIAS)
        img.save(finalPath)







#Downloader(["C:\\Users\\Prashant\\Desktop\\programming\\python\\Image_Optimizer\\originalImages\\image01.jpg","","single"])
#Downloader(["C:\\Users\\Prashant\\Desktop\\programming\\python\\Image_Optimizer\\originalImages","","multiple"])