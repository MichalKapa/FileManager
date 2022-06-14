import csv
import os
import random
import time


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

    def addCsvFolder(self, configurationPath, folderName, phrase, outputPath):
        f = open(configurationPath + '/nameFolders.csv', 'a')
        writer = csv.writer(f)
        row = [folderName, phrase]
        writer.writerow(row)
        f.close()
        self.createNameFolders(configurationPath, outputPath)

    def emptyAllDirectories(self, outputDirectoryPath):
        for root, dirs, files in os.walk(outputDirectoryPath):
            path = root
            for file in files:
                self.moveToDirectory(path + "/" + file, outputDirectoryPath + "/" + file)

    def deleteAllEmptyDirectories(self, outputDirectoryPath):
        for directory in os.listdir(outputDirectoryPath):
            directoryPath = outputDirectoryPath + "/" + directory
            if os.path.isdir(directoryPath):
                if len(os.listdir(directoryPath)) == 0:
                    os.rmdir(directoryPath)
                    print("removing: " + directoryPath)

    def calculateDirectorySize(self, outputDirectoryPath):
        tuppleList = []
        for root, dirs, files in os.walk(outputDirectoryPath):
            path = root
            for directory in dirs:
                size = 0
                for file in os.listdir(path + "/" + directory):
                    size += os.path.getsize(path + "/" + directory + "/" + file)
                tuppleList.append((directory, size))
        # for tupple in tuppleList:
        #     print(tupple[0] + " " + str(tupple[1]))
        return tuppleList

    def searchString(self, filePath, string):
        with open(filePath, 'r') as file:
            content = file.read()
            if string.lower() in content.lower():
                return os.path.abspath(filePath)

    def searchTxtFiles(self, outputDirectoryPath, string):
        fileList = []
        for root, dirs, files in os.walk(outputDirectoryPath):
            for directory in dirs:
                path = root + "/" + directory
                for file in os.listdir(path):
                    if ".txt" in file:
                        fileList.append(self.searchString(path + "/" + file, string))
        return fileList

    def getFileExtensionList(self, configurationPath, directoryName):
        extensionList = []
        with open(configurationPath + "/" + "extensionFolders.csv") as fileObject:
            readerObject = csv.reader(fileObject, delimiter=",")
            for line in readerObject:
                if line[0] == directoryName:
                    extensionList = line[1].split(";")
                    break
        return extensionList

    def getPhotos(self, configurationPath, outputDirectoryPath):
        filePathDateList = []
        imageExtensionList = self.getFileExtensionList(configurationPath, "Images")

        for root, dirs, files in os.walk(outputDirectoryPath):
            path = root
            for file in files:
                for extension in imageExtensionList:
                    if "." + extension in file:
                        # print(file + " " + path)
                        date = time.ctime(os.path.getctime(path + "/" + file))
                        filePathDateList.append((file, path, date))
        return filePathDateList

    def createPhotoAlbums(self, outputDirectoryPath):
        pass
    # WIP

    def findOldestFile(self, files):
        oldestFile = files[0]
        for file in files:
            if file[2] < oldestFile[2]:
                oldestFile = file
        print("oldest file: " + oldestFile[0] + oldestFile[1] + oldestFile[2])
