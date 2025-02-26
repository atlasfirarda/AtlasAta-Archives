import os
import time

from colorTexts import *


class AtlasLogger():
    def __init__(self):

        self.logFolder = os.path.abspath(os.path.join("logs"))
        self.logFileName: str = f"log-{time.localtime().tm_mday}.{time.localtime().tm_mon}.{time.localtime().tm_year.__str__()[2:]}.log"
        self.logFile = os.path.abspath(os.path.join(self.logFolder, self.logFileName))
        self.logState = False

        self.data: str = ""

    def startLog(self):

        self.logState = True

        if not os.path.exists(self.logFolder):
            os.makedirs(self.logFolder, exist_ok=True)
        else:
            if not os.path.exists(self.logFile):
                with open(self.logFile, "x+", encoding="utf-8") as log:
                    self.data += f"{time.localtime().tm_hour}.{time.localtime().tm_min}.{time.localtime().tm_sec}: --- STARTED TO LOGGING ---"
                    self.data += "\n"
                    log.writelines(self.data)
                    log.close()
            else:
                with open(self.logFile, "w+", encoding="utf-8") as log:
                    self.data += f"{time.localtime().tm_hour}.{time.localtime().tm_min}.{time.localtime().tm_sec}: --- STARTED TO LOGGING ---\n"
                    log.writelines(self.data)
                    log.close()

    def stopLog(self):

        if self.logState:
            self.logState = False

            with open(self.logFile, "w+", encoding="utf-8") as logWrite:
                self.data += "\n"
                self.data += f"{time.localtime().tm_hour}.{time.localtime().tm_min}.{time.localtime().tm_sec}: --- STOPPED TO LOGGING ---\n"
                logWrite.writelines(self.data)
                logWrite.close()

    def Log(self, text: str, type: str):

        if self.logState:

            if not len(text) > 0:
                return
            else:
                if len(type) > 0:
                    if type == "success" or type == "suc":
                        toPrint = f"[{green("+")}] {cyan(text)}"
                        toLog = f"[SUCCESS] {text}"
                        print(toPrint)
                        with open(self.logFile, "r+", encoding="utf-8") as log:
                            self.data += "\n"
                            self.data += f"{time.localtime().tm_hour}.{time.localtime().tm_min}.{time.localtime().tm_sec}: {toLog.__repr__().replace("'", "").replace('"', '')}\n"
                            log.writelines(self.data)
                    elif type == "warning" or type == "warn":
                        toPrint = f"[{yellow("?")}] {yellow(text)}"
                        toLog = f"[WARNING] {text}"
                        print(toPrint)
                        with open(self.logFile, "r+", encoding="utf-8") as log:
                            self.data += "\n"
                            self.data += f"{time.localtime().tm_hour}.{time.localtime().tm_min}.{time.localtime().tm_sec}: {toLog.__repr__().replace("'", "").replace('"', '')}\n"
                            log.writelines(self.data)
                    elif type == "error" or type == "err":
                        toPrint = f"[{red("!")}] {red(text)}"
                        toLog = f"[ERROR] {text}"
                        print(toPrint)
                        with open(self.logFile, "r+", encoding="utf-8") as log:
                            self.data += "\n"
                            self.data += f"{time.localtime().tm_hour}.{time.localtime().tm_min}.{time.localtime().tm_sec}: {toLog.__repr__().replace("'", "").replace('"', '')}\n"
                            log.writelines(self.data)
                else:
                    toLog = text
                    print(toLog)
                    with open(self.logFile, "r+", encoding="utf-8") as log:
                        self.data += "\n"
                        self.data += f"{time.localtime().tm_hour}.{time.localtime().tm_min}.{time.localtime().tm_sec}: {toLog.__repr__().replace("'", "").replace('"', '')}\n"
                        log.writelines(self.data)
        else:
            return
