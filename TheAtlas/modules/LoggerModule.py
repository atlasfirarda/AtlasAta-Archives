from modules.ColorModule import blue, green, yellow, red
from modules.FileModule import CreateFile, GetFileData, EditFileData, FormatFile

from datetime import datetime as DTime
import os


class LoggerModule:

    def __init__(
        self,
        text: str,
        level: int = 0,
    ):
        self.text = None

        self.levelText = None

        self.logDir = self.LogDirPathMap()
        self.logPath = self.LogPathMap()

        if text:
            self.text = text
        if level >= 0 and level <= 3:
            self.levelText = self.LevelMap(level)

        if not (self.CheckExists(self.logDir)):
            os.mkdir(self.logDir)

        if not (self.CheckExists(self.logPath)):
            CreateFile(self.logDir, self.DateMap(), ".log")

    def log(self) -> bool:

        if not (self.text) or not (self.levelText):
            return False

        fileData = GetFileData(self.logPath)

        fileData.append(f"{self.levelText} {self.text}")

        EditFileData(self.logPath, fileData)

        FormatFile(self.logPath, 1)

        print(f"{self.ColorLevelMap(self.levelText)} {self.text}")

    @staticmethod
    def DateMap() -> str:
        return f"{DTime.now().strftime('%d-%m-%Y')}"

    def LogPathMap(self) -> str:

        return os.path.join(self.LogDirPathMap(), f"{self.DateMap()}.log")

    def LogDirPathMap(self) -> str:

        return os.path.join(os.path.abspath(os.path.dirname(__name__)), "logs")

    @staticmethod
    def LevelMap(level: int = 0) -> str:

        match (level):
            case 0:
                return f"[INFO]"
            case 1:
                return f"[DONE]"
            case 2:
                return f"[WARN]"
            case 3:
                return f"[ERROR]"

    @staticmethod
    def ColorLevelMap(level: str = "[INFO]") -> str:

        match (level):
            case "[INFO]":
                return f"{blue("[INFO]")}"
            case "[DONE]":
                return f"{green("[DONE]")}"
            case "[WARN]":
                return f"{yellow("[WARN]")}"
            case "[ERROR]":
                return f"{red("[ERROR]")}"

    @staticmethod
    def CheckExists(path: str) -> bool:
        if not (path):
            return False

        return os.path.exists(path)


def log(text: str, level: int) -> bool:

    logger = LoggerModule(text, level)

    return logger.log()


def banner():

    show: str = rf""" /$$$$$$$$/$$                  /$$$$$$    /$$     /$$                    
|__  $$__/ $$                 /$$__  $$  | $$    | $$                    
   | $$  | $$$$$$$   /$$$$$$ | $$  \ $$ /$$$$$$  | $$  /$$$$$$   /$$$$$$$
   | $$  | $$__  $$ /$$__  $$| $$$$$$$$|_  $$_/  | $$ |____  $$ /$$_____/
   | $$  | $$  \ $$| $$$$$$$$| $$__  $$  | $$    | $$  /$$$$$$$|  $$$$$$ 
   | $$  | $$  | $$| $$_____/| $$  | $$  | $$ /$$| $$ /$$__  $$ \____  $$
   | $$  | $$  | $$|  $$$$$$$| $$  | $$  |  $$$$/| $$|  $$$$$$$ /$$$$$$$/
   |__/  |__/  |__/ \_______/|__/  |__/   \___/  |__/ \_______/|_______/ 
   """
    os.system("cls")
    print(yellow(show))
