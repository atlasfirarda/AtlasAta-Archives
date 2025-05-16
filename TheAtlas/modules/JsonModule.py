from modules.LoggerModule import log

from json import dump as JDump
from json import load as JLoad
from json import JSONDecodeError as JDecodeError

import os


class JsonHelper:

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

        if not os.path.exists(path):
            return False

        return True

    @staticmethod
    def FormatMap(path: str) -> tuple[str, str]:

        if not (path):
            return None

        name, extension = os.path.splitext(os.path.basename(path))

        return (name, extension)

    def GetJsonDict(self) -> dict:
        if not (self.filePath):
            return None

        _, extension = self.FormatMap(self.filePath)
        if not (extension == ".json"):
            return None

        try:
            with open(self.filePath, "r+", encoding="utf-8") as file:
                return JLoad(file)
        except (JDecodeError, OSError) as ex:
            return None

    def EditJsonDict(self, data: dict) -> bool:
        if not (self.filePath):
            return False
        try:
            with open(self.filePath, "w+", encoding="utf-8") as file:
                JDump(data, file, indent=4, ensure_ascii=False)
                return True
        except (TypeError, OSError) as ex:
            print(ex)
            return False

    def GetJsonKeys(self) -> list:
        if not (self.filePath):
            return None

        fileData: dict = self.GetJsonDict()

        if not fileData:
            return None

        listKeys: list = []

        for key in fileData.keys():
            listKeys.append(key)

        return listKeys

    def GetJsonValues(self) -> list:
        if not (self.filePath):
            return None

        fileData: dict = self.GetJsonDict()

        if not fileData:
            return None

        listValues: list = []

        for value in fileData.values():
            listValues.append(value)
        return listValues

    def CreateJson(self, name: str, data: dict = None) -> bool:
        if (not (name)) or (not (self.folderPath)):
            return False

        pathMap: str = os.path.join(self.folderPath, f"{name}.json")

        try:
            with open(pathMap, "w+", encoding="utf-8") as file:
                if data:
                    JDump(data, file)
                return True
        except (TypeError, OSError) as ex:
            return False

    def AddJsonKey(self, key: str, value: str = None) -> bool:
        if (not (self.filePath)) or (not (key)):
            return False

        fileData: dict = self.GetJsonDict()

        if not fileData:
            return False

        if key in fileData.keys():
            return False

        fileData.update({key: value})

        return self.EditJsonDict(fileData)

    def AddJsonValue(self, key: str, value: str) -> bool:
        if (not (self.filePath)) or (not (key)) or (not (value)):
            return False

        fileData: dict = self.GetJsonDict()

        if not (fileData):
            return False

        if not (key in fileData.keys()):
            return False

        values: list = []

        if isinstance(fileData[key], list):
            for v in fileData[key]:
                values.append(v)
            values.append(value)
        else:
            values: list = [fileData[key], value]

        fileData.update({key: values})

        return self.EditJsonDict(fileData)

    def DeleteJsonKey(self, key: str) -> bool:
        if (not (self.filePath)) or (not (key)):
            return False

        fileData: dict = self.GetJsonDict()

        if not (fileData):
            return False

        if not (key in fileData.keys()):
            return False

        fileData.pop(key)

        return self.EditJsonDict(fileData)

    def DeleteJsonValue(self, key: str, value: str | list) -> bool:
        if (not (self.filePath)) or (not (key)) or (not (value)):
            return False

        fileData: dict = self.GetJsonDict()

        if not (fileData):
            return False

        if not (fileData[key]):
            return False

        try:

            values = fileData[key]

            if not isinstance(values, list):
                if values != value:
                    return False
                fileData[key] = None
            else:
                if isinstance(value, list):
                    filtered = [v for v in values if v not in value]
                else:
                    filtered = [v for v in values if v != value]

                if filtered == values:
                    return False

                fileData[key] = filtered

        except ValueError as ex:
            return False

        return self.EditJsonDict(fileData)


def GetJsonDict(path: str) -> dict:

    helper = JsonHelper(path, None)

    return helper.GetJsonDict()


def EditJsonDict(path: str, data: dict) -> bool:

    helper = JsonHelper(path, None)

    return helper.EditJsonDict(data)


def GetJsonKeys(path: str) -> list:

    helper = JsonHelper(path, None)

    return helper.GetJsonKeys()


def GetJsonValues(path: str) -> list:

    helper = JsonHelper(path, None)

    return helper.GetJsonValues()


def AddJsonKey(path: str, key: str, value: str = None) -> bool:

    helper = JsonHelper(path, None)

    return helper.AddJsonKey(key, value)


def AddJsonValue(path: str, key: str, value: str) -> bool:

    helper = JsonHelper(path, None)

    return helper.AddJsonValue(key, value)


def DeleteJsonKey(path: str, key: str) -> bool:

    helper = JsonHelper(path, None)

    return helper.DeleteJsonKey(key)


def DeleteJsonValue(path: str, key: str, value: str) -> bool:

    helper = JsonHelper(path, None)

    return helper.DeleteJsonValue(key, value)
