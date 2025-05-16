import os
import shutil


class FileHelper:

    def __init__(
        self,
        filePath: str = None,
        folderPath: str = None,
    ):

        self.filePath = None
        self.folderPath = None

        if (filePath) and (self.CheckExists(filePath)):
            self.filePath = filePath

        if (folderPath) and (self.CheckExists(folderPath)):
            self.folderPath = folderPath

    @staticmethod
    def CheckExists(path: str) -> bool:
        if not (path):
            return False

        return os.path.exists(path)

    def GetFileData(self) -> list:
        if not (self.filePath):
            return None
        try:
            with open(self.filePath, "r+", encoding="utf-8") as file:
                return file.readlines()
        except OSError as ex:
            return None

    def EditFileData(self, data: list) -> bool:
        if (not (self.filePath)) or (not (data)):
            return False

        try:
            with open(self.filePath, "w+", encoding="utf-8") as file:
                file.writelines(data)
                return True
        except OSError as ex:
            return False

    def CreateFile(
        self,
        name: str,
        extension: str,
        data: list = None,
    ) -> bool:
        if (not (self.folderPath)) or (not (name)) or (not (extension)):
            return False

        pathMap = os.path.join(self.folderPath, f"{name}{extension}")

        if self.CheckExists(pathMap):
            return False

        try:
            with open(pathMap, "w+", encoding="utf-8") as file:
                if data:
                    file.writelines(data)
                return True
        except OSError as ex:
            return False

    def DeleteFile(self) -> bool:

        try:
            if self.filePath:
                os.remove(self.filePath)
            elif self.folderPath:
                shutil.rmtree(self.folderPath)
            else:
                return False
            return True
        except OSError as ex:
            return False

    def FormatFile(self, blank_space: int = 0) -> bool:

        if not (self.filePath):
            return False

        fileData: list = self.GetFileData()

        if not (fileData):
            return False

        formattedData: list = []

        for data in fileData:
            if data == "\n":
                continue
            formattedData.append(f"{data.strip("\n")}")
            for _ in range(0, blank_space + 1, 1):
                formattedData.append("\n")

        return self.EditFileData(formattedData)


def GetFileData(path: str) -> list:

    helper = FileHelper(path)

    return helper.GetFileData()


def EditFileData(path: str, data: list) -> bool:

    helper = FileHelper(path)

    return helper.EditFileData(data)


def CreateFile(
    folderPath: str,
    name: str,
    extension: str,
    data: list = None,
) -> bool:

    helper = FileHelper(None, folderPath)

    return helper.CreateFile(name, extension, data)


def DeleteFile(
    filePath: str = None,
    folderPath: str = None,
) -> bool:

    helper = FileHelper(filePath, folderPath)

    return helper.DeleteFile()


def FormatFile(path: str, blank_space: int = 0) -> bool:

    helper = FileHelper(path, None)

    return helper.FormatFile(blank_space)
