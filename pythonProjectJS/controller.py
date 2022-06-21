
from model import Model
from view import View


class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View(self)
        self.outputDirectoryPath = "../.."
        self.configurationPath = "../configuration"

    def main(self):
        self.view.main()
        pass

    @staticmethod
    def createFoldersButton():
        print("Create folders")
        app.model.createAllFolders(app.configurationPath, app.outputDirectoryPath)

    @staticmethod
    def sortFilesButton():
        print("Sort files")
        app.model.sortFiles(app.configurationPath, app.outputDirectoryPath)

    def addFolderButton(self):
        folderName = self.view.folderNameEntry.get()
        recognizedText= self.view.recognizedTextEntry.get()
        print("Add new folder: " + folderName + " " + recognizedText)
        app.model.addCsvFolder(app.configurationPath, folderName, recognizedText, app.outputDirectoryPath)

    @staticmethod
    def extractFilesButton():
        print("Extract files")
        app.model.emptyAllDirectories(app.outputDirectoryPath)

    @staticmethod
    def deleteEmptyButton():
        print("Delete empty")
        app.model.deleteAllEmptyDirectories(app.outputDirectoryPath)

    def searchTextButton(self):
        search = self.view.inputTextEntry.get()
        print("Search text: " + search)
        self.view.dislplaySearchTextResults(app.model.searchTxtFiles(app.outputDirectoryPath, search))

    @staticmethod
    def createShortcutsButton():
        print("Create shortcuts")
        app.model.createShortcuts(app.outputDirectoryPath)

    def moveOldButton(self):
        year = self.view.yearEntry.get()
        if year == "":
            year = "0"

        print("Move older or equal: " + year)
        app.model.sortOldFiles(app.configurationPath, app.outputDirectoryPath, int(year))

    @staticmethod
    def compressFilesButton():
        print("Compress files")
        app.model.compressPreparedFiles(app.outputDirectoryPath, app.configurationPath)

    @staticmethod
    def calculateSizeButton():
        print("Calculate size")
        app.view.displaySizeGraph(app.model.calculateDirectorySize(app.outputDirectoryPath))


if __name__ == '__main__':
    app = Controller()
    # print(app.model.createDirectory(app.path, app.outputDirectory))

    # app.model.createAllFolders(app.configurationPath, app.outputDirectoryPath)

    # test files
    # app.model.createTestFiles(app.configurationPath, app.outputDirectoryPath)

    # app.model.sortFiles(app.configurationPath, app.outputDirectoryPath)

    # app.model.addCsvFolder(app.configurationPath, "Secret files", "seCret", app.outputDirectoryPath)

    # app.model.emptyAllDirectories(app.outputDirectoryPath)

    # app.model.deleteAllEmptyDirectories(app.outputDirectoryPath)

    # app.model.calculateDirectorySize(app.outputDirectoryPath)

    # print(app.model.searchTxtFiles(app.outputDirectoryPath, "created"))

    # app.model.createShortcuts(app.outputDirectoryPath)

    # app.model.compressPreparedFiles(app.outputDirectoryPath, app.configurationPath)

    # app.model.sortOldFiles(app.configurationPath, app.outputDirectoryPath, 2021)

    # print(app.model.searchTxtFiles(app.outputDirectoryPath, ""))

    app.main()
