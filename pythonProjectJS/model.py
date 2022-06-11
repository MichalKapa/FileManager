import csv
import os
import random


class Model:

    def __init__(self):
        pass

    def getFilesInDirectory(self, path):
        return os.listdir(path)

    def createDirectory(self, path, dirName):
        dirPath = os.path.join(path, dirName)
        if not os.path.exists(dirPath):
            os.mkdir(dirPath)
            return "Created new folder: " + dirName

        return "Folder " + dirName + " already exists"

    def moveToDirectory(self, src, dst):
        os.replace(src, dst)

        return "Moved to: " + dst

    # create test file
    def createFile(self, path, fileName):
        try:
            with open(path + fileName, 'w') as f:
                f.write('Created new file: ' + fileName)
        except FileNotFoundError:
            print("The " + path + " directory does not exist")

    def createTestFiles(self, configurationPath, directoryPath):
        with open(configurationPath + "/" + 'extensionFolders.csv') as fileObject:
            readerObject = csv.reader(fileObject, delimiter=",")
            for line in readerObject:
                for extension in line[1].split(";"):
                    self.createFile(directoryPath + "/", str(random.randint(0, 100)) + "." + extension)

    def createAllFolders(self, configurationPath, outputPath):
        self.createExtensionFolders(configurationPath, outputPath)
        self.createNameFolders(configurationPath, outputPath)
        print("All folders ready")

    def createExtensionFolders(self, configurationPath, outputPath):
        self.createFolders(configurationPath, outputPath, 'extensionFolders.csv')

    def createNameFolders(self, configurationPath, outputPath):
        self.createFolders(configurationPath, outputPath, 'nameFolders.csv')

    # get folders of files distinguished by extension or name
    def createFolders(self, path, outputPath, csvFile):
        with open(path + "/" + csvFile) as fileObject:
            readerObject = csv.reader(fileObject, delimiter=",")
            for line in readerObject:
                self.createDirectory(outputPath, line[0])

    def sortFiles(self, configurationPath, outputDirectoryPath):
        folderList = []
        folderNameList = []

        with open(configurationPath + "/" + 'nameFolders.csv') as fileObject:
            readerObject = csv.reader(fileObject, delimiter=",")
            for line in readerObject:
                folderNameList.append(line)

        with open(configurationPath + "/" + 'extensionFolders.csv') as fileObject:
            readerObject = csv.reader(fileObject, delimiter=",")
            for line in readerObject:
                folderList.append(line)

        fileList = self.getFilesInDirectory(outputDirectoryPath)
        for file in fileList:
            if not os.path.isdir(outputDirectoryPath + "/" + file):
                for folder in folderNameList:
                    if folder[1].lower() in file.lower():
                        print(self.moveToDirectory(outputDirectoryPath + "/" + file,
                                                   outputDirectoryPath + "/" + folder[0] + "/" + file))
                        break

            fileList = self.getFilesInDirectory(outputDirectoryPath)
        for file in fileList:
            fileSorted = False
            for folder in folderList:
                if fileSorted:
                    break

                for extension in folder[1].split(";"):
                    if "." + extension in file:
                        self.moveToDirectory(outputDirectoryPath + "/" + file,
                                                   outputDirectoryPath + "/" + folder[0] + "/" + file)
                        fileSorted = True
                        break
