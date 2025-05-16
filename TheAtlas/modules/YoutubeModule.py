from modules.LoggerModule import log, banner
from modules.RequirementModule import installRequirement

from yt_dlp import YoutubeDL
from yt_dlp import DownloadError

from inquirer import Text as IText
from inquirer import List as IList
from inquirer import prompt as IPrompt
from inquirer import themes as ITheme

from alive_progress import alive_bar

from operator import contains
import inquirer
import os
import shutil
import re
import requests
import locale
import json


class DummyLogger:
    def error(msg):
        return

    def warning(msg):
        return

    def debug(msg):
        return


class YoutubeModule:
    def __init__(
        self,
        langModule: LanguageModule = None,
        videoUrl: str = None,
        outPath: str = None,
        format: str = None,
    ):

        if langModule:
            self.langModule = langModule

        log(langModule.getDefaultLangPath(), 1)

        self.ytdlDict: dict = None
        self.languageDict: dict = None
        self.optionsDict: dict = None

        self.languagePath: str = None
        self.ITheme: dict = {
            "Question": {
                "mark_color": "bright_white",
                "brackets_color": "bright_yellow",
            },
            "List": {
                "selection_color": "bold_yellow",
                "selection_cursor": "->",
                "unselected_color": "gray",
            },
        }

        self.videoTitle: str = None

        self.tempVideoPath: str = None
        self.tempAudioPath: str = None

        self.outVideoPath: str = None
        self.outAudioPath: str = None

        self.videoUrl: str = None
        self.downloadUrl: str = None

        self.selectedFormat: str = None
        self.selectedWidth: int = None
        self.selectedHeight: int = None

        if not self.languagePath:
            self.languagePath = getLangPath()

        log(self.languagePath, 0)
        return

        if not self.languageDict:
            self.languageDict = ConfigModule.getJsonDict()

        if videoUrl:
            if self.CheckUrl(self.GetInfoDict, videoUrl, self.defaultOptions):
                self.videoUrl = videoUrl

        if outPath:
            self.outPath = outPath

        if format:
            self.selectedFormat = format

    def SetUrl(self) -> bool:

        if self.videoUrl:
            return True

        answer = [
            IText(
                name="url",
                message="Video URL",
            )
        ]

        url: str = IPrompt(answer, theme=ITheme.load_theme_from_dict(self.ITheme))[
            "url"
        ]

        if self.CheckUrl(self.GetInfoDict, url, self.defaultOptions):

            self.videoUrl = url

            return True

        self.videoUrl = None

        return False

    def SetTitle(self) -> bool:
        if not self.videoUrl:
            return False

        if self.videoTitle:
            return True

        if not self.selectedFormat:
            return False

        try:

            explicitChars = r'/\<>&?:=|"'

            title: str = self.GetTitle().__str__()

            for explicit in explicitChars:
                title = title.replace(explicit, "")

            title = title.replace("  ", " ")

            self.videoTitle = title

            return True
        except BaseException:
            self.videoTitle = None
            return False

    def GetTitle(self) -> str:

        if not self.videoUrl:
            return None

        try:

            infoDict: dict = self.GetInfoDict(self.defaultOptions, self.videoUrl)

            title: str = infoDict["title"]

            return title

        except BaseException:
            return None

    def GetResolutions(self) -> list[(int, int)]:

        if not self.videoUrl:
            return None

        resolutionList: list = []

        try:

            infoDict: dict = self.GetInfoDict(self.defaultOptions, self.videoUrl)
            formatList = infoDict.get("formats", [])

            for format in formatList:
                w, h = format.get("width"), format.get("height")

                if w == None or h == None:
                    continue

                if w < 1280 and h < 720:
                    continue

                if contains(resolutionList, (w, h)):
                    continue

                resolutionList.append((w, h))

            return sorted(resolutionList, reverse=True)

        except BaseException:
            return None

    def SetFormat(self) -> bool:

        if not self.videoUrl:
            return False

        choices: list = ["mp4", "webm", "mp3", "wav"]

        try:

            protocols: list = self.GetProtocols()

            formatDict: dict = self.GetFormats()

            selectedProtocol: str = "m3u8_native"
            selectedFormat: str = "mp4"
            log("s", 0)

            onlyAudio: bool = False

            if not self.selectedFormat:
                log("s", 1)
                question = [
                    IList(name="format", message="Select Format", choices=choices)
                ]

                answer = IPrompt(
                    question, theme=ITheme.load_theme_from_dict(self.ITheme)
                )["format"]

                self.selectedFormat = answer

            if not (contains(protocols, selectedProtocol)):
                log("s", 2)
                return False

            if contains(["mp4", "webm"], self.selectedFormat):

                SelectResolution()

            for format in formatDict:

                formatProto: str = format.get("protocol")
                formatExt: str = format.get("video_ext")
                formatUrl: str = format.get("url")
                formatVCodec: str = format.get("vcodec")

                if not (formatProto == selectedProtocol):
                    continue

                if contains(["mp3", "wav"], self.selectedFormat):
                    onlyAudio = True

                if formatVCodec == "none":
                    formatNote: str = format.get("format_note")

                    if not (contains(["Default, high"], formatNote)):
                        continue

                    self.downloadUrl = formatUrl

                    if not (onlyAudio):
                        continue

                    break

                if not (formatExt == selectedFormat):
                    continue

                formatWidth, formatHeight = format.get("width"), format.get("height")

                if not (formatWidth == self.selectedWidth) and not (
                    formatHeight == self.selectedHeight
                ):
                    continue

                self.downloadUrl = formatUrl

                break

            return False

        except BaseException as ex:
            log(f"{ex}", 3)
            self.selectedFormat = None

            return False

    def GetProtocols(self) -> list[str]:

        if not self.videoUrl:
            return None

        protoList: list = []

        try:

            formatDict: dict = self.GetFormats()

            for format in formatDict:

                protocol: str = format.get("protocol")

                if protocol == None:
                    continue

                if contains(protoList, protocol):
                    continue

                protoList.append(protocol)

            return sorted(protoList, reverse=True)
        except BaseException:
            return None

    def GetFormats(self) -> dict:

        if not self.videoUrl:
            return None

        try:

            infoDict: dict = self.GetInfoDict(self.defaultOptions, self.videoUrl)
            formatDict: dict = infoDict.get("formats", [])

            return formatDict

        except BaseException:

            return None

    def SetResolution(self) -> bool:

        if not self.videoUrl:
            return False

        resolutions: list = self.GetResolutions()

        if not resolutions:
            return False

        choices: list = []

        for width, height in resolutions:

            resolution: str = f"{width}x{height}"

            if width >= 3840:
                choices.append((f"{resolution} (4K)"))
            elif width >= 2160:
                choices.append((f"{resolution} (2K)"))
            elif width >= 1920:
                choices.append((f"{resolution} (FHD)"))
            elif width >= 1280:
                choices.append((f"{resolution} (HD)"))
            else:
                choices.append((f"{resolution} (SD)"))

        questionDict: dict = {
            "kind": "list",
            "name": "resolution",
            "message": "Select Resolution",
            "choices": choices,
        }

        question = [inquirer.load_from_dict(questionDict)]

        answer = IPrompt(question, theme=ITheme.load_theme_from_dict(self.ITheme))[
            "resolution"
        ].split("x")

        self.selectedWidth, self.selectedHeight = int(answer[0]), int(
            answer[1].split(" ")[0]
        )

        return True

    def GetOptions(self, default: True):

        if not default:
            if not self.selectedFormat:
                return None

            if not self.selectedWidth:
                return None

            if not self.selectedHeight:
                return None

        return {
            "quiet": True,
            "no_warnings": True,
            "ignoreerrors": True,
            "listformats": False,
            "clean_infojson": True,
            "logger": DummyLogger,
        }

    @staticmethod
    def GetInfoDict(options: dict = None, url: str = None) -> dict:

        if not options:
            return None

        if not url:
            return None

        try:

            with YoutubeDL(options) as ytdl:

                info = ytdl.extract_info(url, download=False)

                if not info:
                    return None

                return info
        except BaseException:

            return None

    @staticmethod
    def CheckUrl(GetInfoDict=None, url: str = None, options: dict = None) -> bool:

        if not GetInfoDict:
            return False

        if not url:
            return False

        if not options:
            return False

        info: dict = GetInfoDict(options, url)

        if info:
            return True

        return False


module = YoutubeModule()


def SelectResolution() -> bool:

    # banner() - breaks visuality

    if not (module.SetResolution()):
        return False

    return True


def SelectFormat() -> bool:

    # banner() - breaks visuality

    if not (module.SetFormat()):
        return False

    return True


def SelectUrl(url: str = None) -> bool:

    if url:
        module.videoUrl = url

    # banner() - breaks visuality

    if not (module.SetUrl()):
        return False

    return True


def SetTempPath(path: str = None) -> bool:

    if not (path):
        return False

    module.tempPath = path

    return True


def SetVideoPath(path: str = None) -> bool:

    if not (path):
        return False

    module.videoPath = path

    return True


def SetAudioPath(path: str = None) -> bool:

    if not (path):
        return False

    module.audioPath = path

    return True


def SetTitle() -> bool:

    if not (module.SetTitle()):
        log(f"sad", 1)
        return False

    return True
