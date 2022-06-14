import random

from model import Model
from view import View


class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View(self)
        self.path = "../"
        self.outputDirectory = "fileManagerOutput"
        self.outputDirectoryPath = "../fileManagerOutput"
        self.configurationPath = "../configuration"

    def main(self):
        # self.view.main()
        pass


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

    print(app.model.getPhotos(app.configurationPath, app.outputDirectoryPath))

    app.model.findOldestFile(app.model.getPhotos(app.configurationPath, app.outputDirectoryPath))

    app.main()
