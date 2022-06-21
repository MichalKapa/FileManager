import csv
import os
import shutil
from win32com.client import Dispatch
import random
import time
import zipfile


class Model:

    def __init__(self):
        pass

    @staticmethod
    def getFilesInDirectory(path):
        return os.listdir(path)

    @staticmethod
    def createDirectory(path, dirName):
        dirPath = os.path.join(path, dirName)
        if not os.path.exists(dirPath):
            os.mkdir(dirPath)
            return "Created new folder: " + dirName

        return "Folder " + dirName + " already exists"

    @staticmethod
    def moveToDirectory(src, dst):
        os.replace(src, dst)

        return "Moved to: " + dst

    # create test file
    @staticmethod
    def createFile(path, fileName):
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
                if line:
                    self.createDirectory(outputPath, line[0])

    def sortFiles(self, configurationPath, outputDirectoryPath):
        self.createFolders(configurationPath, outputDirectoryPath, 'extensionFolders.csv')

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
            if "FileManager" not in root:
                for file in files:
                    self.moveToDirectory(path + "/" + file, outputDirectoryPath + "/" + file)

    @staticmethod
    def deleteAllEmptyDirectories(outputDirectoryPath):
        for directory in os.listdir(outputDirectoryPath):
            directoryPath = outputDirectoryPath + "/" + directory
            if os.path.isdir(directoryPath):
                if len(os.listdir(directoryPath)) == 0:
                    os.rmdir(directoryPath)
                    print("removing: " + directoryPath)

    @staticmethod
    def calculateDirectorySize(outputDirectoryPath):
        tuppleList = []
        for root, dirs, files in os.walk(outputDirectoryPath):
            path = root
            for directory in dirs:
                if "FileManager" not in root:
                    size = 0
                    for file in os.listdir(path + "/" + directory):
                        size += os.path.getsize(path + "/" + directory + "/" + file)
                    tuppleList.append((directory, size))
        return tuppleList

    @staticmethod
    def searchString(filePath, string):
        with open(filePath, 'r', encoding="ISO-8859-1") as file:
            content = file.read()
            if string.lower() in content.lower():
                return os.path.abspath(filePath)

    def searchTxtFiles(self, outputDirectoryPath, string):
        fileList = []
        for root, dirs, files in os.walk(outputDirectoryPath):
            path = root
            for file in files:
                if ".txt" in file and not "lnk" in file:
                    txtPath = self.searchString(path + "/" + file, string)
                    if txtPath is not None:
                        fileList.append(txtPath)
        return fileList

    @staticmethod
    def getFileExtensionList(configurationPath, directoryName):
        extensionList = []
        with open(configurationPath + "/" + "extensionFolders.csv") as fileObject:
            readerObject = csv.reader(fileObject, delimiter=",")
            for line in readerObject:
                if line[0] == directoryName:
                    extensionList = line[1].split(";")
                    break
        return extensionList

    def createShortcuts(self, outputDirectoryPath):
        shortcutFolder = "Shortcuts"
        absolutePath = os.path.abspath(outputDirectoryPath)
        self.createDirectory(outputDirectoryPath, shortcutFolder)

        for root, dirs, files in os.walk(absolutePath):
            if "FileManager" not in root:
                for file in files:
                    if ".lnk" not in file:
                        shortcutPath = outputDirectoryPath + "/" + shortcutFolder + "/" + file + ".lnk"
                        if not os.path.exists(shortcutPath):
                            targetPath = os.path.join(root, file)

                            shell = Dispatch('WScript.Shell')
                            shortcut = shell.CreateShortCut(shortcutPath)
                            shortcut.Targetpath = targetPath
                            shortcut.IconLocation = targetPath
                            shortcut.save()

    @staticmethod
    def compressFile(outputDirectoryPath, path, file):

        fileName = file.split(".")[0]
        inputPath = path + file
        output = outputDirectoryPath + "/Compressed files/" + fileName + ".zip"

        zf = zipfile.ZipFile(output, mode="w")

        try:
            zf.write(inputPath, file, compress_type=zipfile.ZIP_DEFLATED)
        except FileNotFoundError as e:
            print(f' *** Exception occurred during zip process - {e}')
        finally:
            zf.close()

    def compressPreparedFiles(self, outputDirectoryPath, configurationPath):

        compressFolder = "Files to compress"

        path = outputDirectoryPath + "/" + compressFolder + "/"

        for file in os.listdir(path):
            compressedOutputPath = outputDirectoryPath + "/Compressed files/" + file

            if "." in file and file.split(".")[1] in self.getFileExtensionList(configurationPath, "Compressed files"):
                self.moveToDirectory(path + file, compressedOutputPath)

            else:
                if os.path.isdir(path + file):
                    shutil.make_archive(base_dir=file, root_dir=path, format='zip', base_name=compressedOutputPath)
                    print(path + file)
                    print(compressedOutputPath)

                else:
                    self.compressFile(outputDirectoryPath, path, file)

    @staticmethod
    def getAllFilesModificationDate(configurationPath, outputDirectoryPath):
        filePathDateList = []
        folderList = []

        with open(configurationPath + "/" + "extensionFolders.csv") as fileObject:
            readerObject = csv.reader(fileObject, delimiter=",")
            for line in readerObject:
                path = outputDirectoryPath + "/" + line[0]
                folderList.append(line[0])
                for file in os.listdir(path):
                    if "FileManager" not in os.path.abspath(path):
                        date = time.ctime(os.path.getmtime(path + "/" + file))
                        filePathDateList.append((file, path, date))
            for file in os.listdir(outputDirectoryPath):
                if file not in folderList:
                    path = outputDirectoryPath + "/"
                    date = time.ctime(os.path.getmtime(path + file))
                    filePathDateList.append((file, path, date))
        return filePathDateList

    def sortOldFiles(self, configurationPath, outputDirectoryPath, mDate):
        self.createDirectory(outputDirectoryPath, "Old files")
        for filePathDate in self.getAllFilesModificationDate(configurationPath, outputDirectoryPath):
            if int((filePathDate[2].split(" "))[-1]) <= mDate:
                self.moveToDirectory(filePathDate[1] + filePathDate[0],
                                     outputDirectoryPath + "/Old files/" + filePathDate[0])
