import subprocess
import re
import os
from colorama import Fore, Style
from alive_progress import alive_bar

from atlasLogger import *

atlas = AtlasLogger()

atlas.startLog()


class FFMPEG:
    def __init__(self, ffmpegPath: str, ffprobePath: str, videoPath: str, method: str, format: str,
                 specifiedCodec: str = None):

        self.canConvert: bool = False
        self.convertCodec = None
        self.isVideo, self.isAudio = False, False

        if not len(ffmpegPath) > 0:
            self.ffmpegPath = os.path.abspath(os.path.join("ffmpeg", "ffmpeg.exe"))
            if os.path.exists(self.ffmpegPath):
                atlas.Log(f"Found FFmpeg.exe Path: [{self.ffmpegPath}]", "suc")
            else:
                atlas.Log(f"Not Found FFmpeg.exe At: [{self.ffmpegPath}]", "err")
                self.ffmpegPath = None
        else:

            if os.path.isdir(ffmpegPath):

                exeFoundFFMPEG, exePathFFMPEG = self.searchFFmpeg(ffmpegPath)

                if exeFoundFFMPEG:
                    self.ffmpegPath = os.path.join(ffmpegPath, exePathFFMPEG)
                    atlas.Log(f"Found FFmpeg.exe Path: [{self.ffmpegPath}]", "suc")
                else:
                    atlas.Log(f"Not Found FFmpeg.exe At: [{exePathFFMPEG}]", "err")
                    self.ffmpegPath = None

            else:
                self.ffmpegPath = ffmpegPath
                if os.path.exists(os.path.join(self.ffmpegPath)):
                    atlas.Log(f"Found FFmpeg.exe Path: [{self.ffmpegPath}]", "suc")
                else:
                    atlas.Log(f"Not Found FFmpeg.exe At: [{self.ffmpegPath}]", "err")
                    self.ffmpegPath = None

        if not len(ffprobePath) > 0:
            self.ffprobePath = os.path.abspath(os.path.join("ffmpeg", "ffprobe.exe"))
            if os.path.exists(self.ffprobePath):
                atlas.Log(f"Found FFprobe.exe Path: [{self.ffprobePath}]", "suc")
            else:
                atlas.Log(f"Not Found FFprobe.exe At: [{self.ffprobePath}]", "err")
                self.ffprobePath = None
        else:

            if os.path.isdir(ffprobePath):

                exeFoundFFPROBE, exePathFFPROBE = self.searchFFprobe(ffprobePath)

                if exeFoundFFPROBE:
                    self.ffprobePath = os.path.join(ffprobePath, exePathFFPROBE)
                    atlas.Log(f"Found FFprobe.exe Path: [{self.ffprobePath}]", "suc")
                else:
                    atlas.Log(f"Not Found FFprobe.exe At: [{exePathFFPROBE}]", "err")
                    self.ffprobePath = None

            else:
                self.ffprobePath = ffprobePath
                if os.path.exists(os.path.join(self.ffprobePath)):
                    atlas.Log(f"Found FFprobe.exe Path: [{self.ffprobePath}]", "suc")
                else:
                    atlas.Log(f"Not Found FFprobe.exe At: [{self.ffprobePath}]", "err")
                    self.ffprobePath = None

        if not len(videoPath) > 0:
            atlas.Log(f"Input videoPath mustn't be empty!", "err")
            self.videoPath = None
        else:
            self.videoPath = os.path.join(videoPath)
            if not os.path.exists(self.videoPath):
                atlas.Log(f"Input videoPath mustn't be invalid: [{self.videoPath}]", "err")
                self.videoPath = None
            else:
                atlas.Log(f"Input videoPath is: [{self.videoPath}]", "suc")
                for f in self.getFormatList(forceAll=True):
                    if f == self.getFormat():
                        self.format = f
                        if self.format in self.getFormatList(forceMerged=True):
                            self.isVideo, self.isAudio = True, True
                        elif self.format in self.getFormatList(forceVideo=True):
                            self.isVideo, self.isAudio = True, False
                        elif self.format in self.getFormatList(forceAudio=True):
                            self.isVideo, self.isAudio = False, True
                        break
                    else:
                        self.format = None

                if self.format:
                    atlas.Log(f"Input videoFormat is: [{self.format}]", "suc")
                else:
                    atlas.Log(f"Input videoFormat must be a video or audio format: [{self.getFormat()}]", "err")
                if self.videoPath and self.ffmpegPath and self.ffprobePath:
                    if self.format:
                        videoCodec = self.getCodec()

                        for c in self.getCodecList(forceAll=True):
                            if c == videoCodec:
                                self.videoCodec = videoCodec
                                break
                            else:
                                self.videoCodec = None
                        if self.videoCodec:
                            atlas.Log(f"Input videoCodec is: [{self.videoCodec}]", "suc")
                        else:
                            atlas.Log(
                                f"Input videoCodec mustn't be invalid: [{f"not supported codec '{videoCodec}'" if not self.videoCodec and videoCodec else 'empty'}]",
                                "err")
                    else:
                        atlas.Log(
                            f"Input videoCodec can't found any valid formats due to: [{'format error' if not self.format else 'unexpected error'}]",
                            'err')
                        self.videoCodec = None
                else:
                    atlas.Log(
                        f"An unexpected error is occured due to: [{'ffmpegPath, ffprobePath is invalid' if not self.ffmpegPath and not self.ffprobePath else 'ffmpegPath is invalid' if not self.ffmpegPath else 'ffprobePath is invalid' if not self.ffprobePath else ''}]",
                        'err')

                if not len(method) > 0:
                    atlas.Log(f"Input videoMethod mustn't be empty!", "err")
                    self.method = None
                else:
                    for item in self.getMethodList():
                        if method == item:
                            self.method = method
                            atlas.Log(f"Input videoMethod is: [{self.method}]", "suc")
                            break
                        else:
                            self.method = None

                    if not self.method:
                        atlas.Log(
                            f"Input videoMethod mustn't be invalid: [{method}]", "err")

                    if self.ffmpegPath and self.ffprobePath:
                        if not format:
                            atlas.Log(f"Convert videoFormat mustn't be empty!", "err")
                            self.convertFormat = None
                        else:
                            self.convertFormat = format
                            if self.convertFormat == self.getFormat():
                                atlas.Log(
                                    f"Convert videoFormat mustn't be same: ['{self.getFormat()}' to '{self.convertFormat}']",
                                    "err")
                                self.convertFormat = None
                            else:
                                audioFormats = self.getFormatList(forceAudio=True)
                                mergedFormats = self.getFormatList(forceAll=True)

                                if self.convertFormat in mergedFormats and self.isAudio and not self.isVideo:
                                    atlas.Log(f"Convert videoFormat is can't be convertable to video.", "err")
                                    self.convertFormat = None
                                elif self.convertFormat in audioFormats and self.isVideo and not self.isAudio:
                                    atlas.Log(f"Convert videoFormat is can't be convertable to audio.", "err")
                                    self.convertFormat = None
                                else:
                                    atlas.Log(f"Convert videoFormat is: [{self.convertFormat}]", "suc")
                        if specifiedCodec and self.convertFormat:
                            codecList = self.getFormatCodec(self.getCodecFormat(self.convertFormat))
                            if codecList:
                                for c in codecList:
                                    if specifiedCodec == c:
                                        break
                                    elif specifiedCodec in c:
                                        specifiedCodec = c
                                        break
                                for cx in self.getFormatCodec(self.getCodecFormat(specifiedCodec)):
                                    if cx == specifiedCodec:
                                        self.convertCodec = specifiedCodec
                                        break
                                    else:
                                        self.convertCodec = self.getFormatCodec(self.convertFormat)[0]
                                else:
                                    self.convertCodec = self.getFormatCodec(self.convertFormat)[0]
                            else:
                                self.convertCodec = self.getFormatCodec(self.convertFormat)[0]

                        else:
                            if self.getFormatCodec(self.convertFormat) and self.convertFormat:
                                self.convertCodec = self.getFormatCodec(self.convertFormat)[0]
                            else:
                                self.convertCodec = None

                        if self.convertCodec:
                            atlas.Log(f"Convert videoCodec is: [{self.convertCodec}]", "suc")
                        else:
                            atlas.Log(
                                f"Convert videoCodec must be have these: [{'convertFormat, convertCodec' if not self.convertFormat and not self.convertCodec else 'convertFormat' if not self.convertFormat else 'convertCodec' if not self.convertCodec else ''}]",
                                "err")
                        if self.method:
                            atlas.Log(f"Convert videoMethod is: [{self.method}]", "suc")
                        else:
                            atlas.Log(f"Convert videoMethod mustn't be invalid: [{method}]", "err")

    @staticmethod
    def searchFFmpeg(path: str) -> [bool, str]:

        searchPath: str = ""

        for exe in sorted(os.listdir(path)):
            if os.path.isdir(os.path.join(path, exe)):
                for file in os.listdir(os.path.join(path, exe)):
                    if file == "ffmpeg.exe":
                        return [True, os.path.join(exe, file)]
                    searchPath = os.path.join(path)
            else:
                if exe == "ffmpeg.exe":
                    return [True, os.path.join(exe)]
                searchPath = os.path.join(path)

        return [False, searchPath]

    @staticmethod
    def searchFFprobe(path: str) -> [bool, str]:
        searchPath: str = ""

        for exe in sorted(os.listdir(path)):
            if os.path.isdir(os.path.join(path, exe)):
                for file in os.listdir(os.path.join(path, exe)):
                    if file == "ffprobe.exe":
                        return [True, os.path.join(exe, file)]
                    searchPath = os.path.join(path)
            else:
                if exe == "ffprobe.exe":
                    return [True, os.path.join(exe)]
                searchPath = os.path.join(path)

        return [False, searchPath]

    def convertToWAV(self):

        if self.isVideo == True or self.isAudio == True:
            self.canConvert = True
        else:
            atlas.Log(f"The file must be a video or audio file!", "warn")

        if len(self.ffmpegPath) > 0 and len(self.videoPath) > 0 and self.canConvert and len(self.method) > 0:

            fileName: str = os.path.splitext(self.videoPath)[0]
            fileExt: str = os.path.splitext(self.videoPath)[1].strip('.')

            codecCMD: list[str] = [
                f"{self.ffprobePath}",
                "-v", "error",
                "-select_streams", "a",
                "-show_entries", "stream=codec_name",
                "-of", "default=noprint_wrappers=1:nokey=1",
                self.videoPath
            ]

            videoCodec = subprocess.run(codecCMD, capture_output=True, text=True).stdout.strip()

            if len(videoCodec) > 0:
                atlas.Log(f"Audio codec is: [{videoCodec}]", "suc")
            else:
                atlas.Log(f"Doesn't have an Audio Codec.", "warn")

            if videoCodec in ["prores", "vp9", "h264", "mp3", "mpeg3", "ogg", "aac"] and fileExt in ["mov", "mkv",
                                                                                                     "mp4",
                                                                                                     "webm",
                                                                                                     "m4a", "ogg",
                                                                                                     "mp3"]:
                convertCMD: list[str] = [
                    self.ffmpegPath,
                    "-i", self.videoPath,
                    "-c:a", "pcm_f32le",
                    "-y", f"{fileName}.wav"
                ]

                duration_cmd: list[str] = [
                    self.ffprobePath,
                    "-i", self.videoPath,
                    "-show_entries", "format=duration",
                    "-v", "quiet",
                    "-of", "csv=p=0"
                ]

                video_duration = float(subprocess.run(duration_cmd, capture_output=True, text=True).stdout.strip())
                atlas.Log(f"{"Video" if self.isVideo else "Audio"} duration is: [{video_duration} seconds]", "suc")

                atlas.Log(f"The {"video" if self.isVideo else "audio"} is converting to wav: [{self.videoPath}]",
                          "suc")

                process = subprocess.Popen(convertCMD, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

                if process.wait() == 0:
                    atlas.Log(
                        f"The {"video" if self.isVideo else "audio"} is successfully converted to wav: [{fileName}.wav]",
                        "suc")
                else:
                    atlas.Log(
                        f"The {"video" if self.isVideo else "audio"} failed on converting to wav: [{self.videoPath}]",
                        "err")
            else:
                atlas.Log(
                    f"The videoPath can't be converted. Unsupported codec: [{videoCodec if len(videoCodec) > 0 else "empty"}] or extension: [{fileExt if len(fileExt) > 0 else "empty"}].",
                    "err")

        else:
            atlas.Log(f"The file cannot be converted!", "err")

    def convertToMP3(self):
        if self.isVideo == True or self.isAudio == True:
            self.canConvert = True
        else:
            atlas.Log(f"The file must be a video or audio file!", "warn")

        if len(self.ffmpegPath) > 0 and len(self.videoPath) > 0 and self.canConvert and len(self.method) > 0:

            fileName: str = os.path.splitext(self.videoPath)[0]
            fileExt: str = os.path.splitext(self.videoPath)[1].strip('.')

            codecCMD: list[str] = [
                f"{self.ffprobePath}",
                "-v", "error",
                "-select_streams", "a",
                "-show_entries", "stream=codec_name",
                "-of", "default=noprint_wrappers=1:nokey=1",
                self.videoPath
            ]

            videoCodec = subprocess.run(codecCMD, capture_output=True, text=True).stdout.strip()

            if len(videoCodec) > 0:
                atlas.Log(f"Audio codec is: [{videoCodec}]", "suc")
            else:
                atlas.Log(f"Doesn't have an Audio Codec.", "warn")

            if videoCodec in ["prores", "vp9", "h264", "pcm_f32le", "pcm_f16le", "pcm_f24le",
                              "pcm_f64le", "aac"] and fileExt in ["mov", "mkv", "mp4",
                                                                  "webm",
                                                                  "m4a", "ogg", "wav"]:
                convertCMD: list[str] = [
                    self.ffmpegPath,
                    "-i", self.videoPath,
                    "-c:a", "libmp3lame",
                    "-y", f"{fileName}.mp3"
                ]

                duration_cmd: list[str] = [
                    self.ffprobePath,
                    "-i", self.videoPath,
                    "-show_entries", "format=duration",
                    "-v", "quiet",
                    "-of", "csv=p=0"
                ]

                video_duration = float(subprocess.run(duration_cmd, capture_output=True, text=True).stdout.strip())
                atlas.Log(f"{"Video" if self.isVideo else "Audio"} duration is: [{video_duration} seconds]", "suc")

                atlas.Log(f"The {"video" if self.isVideo else "audio"} is converting to mp3: [{self.videoPath}]",
                          "suc")

                process = subprocess.Popen(convertCMD, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

                if process.wait() == 0:
                    atlas.Log(
                        f"The {"video" if self.isVideo else "audio"} is successfully converted to mp3: [{fileName}.mp3]",
                        "suc")
                else:
                    atlas.Log(
                        f"The {"video" if self.isVideo else "audio"} failed on converting to mp3: [{self.videoPath}]",
                        "err")
            else:
                atlas.Log(
                    f"The videoPath can't be converted. Unsupported codec: [{videoCodec if len(videoCodec) > 0 else "empty"}] or extension: [{fileExt if len(fileExt) > 0 else "empty"}].",
                    "err")

        else:
            atlas.Log(f"The file cannot be converted!", "err")

    def getEncoderList(self, forceAll: bool = False, forceMerged: bool = False, forceVideo: bool = False,
                       forceAudio: bool = False) -> list[
                                                        str] | None:
        if forceAll:
            return [
                'libx264',
                'libx265',
                'libvpx',
                'libvpx-vp9',
                'mpeg4',
                'prores',
                'dnxhd',
                'ffv1',
                'h263',
                'h264',
                'theora',
                'vp6',
                'msmpeg4v2',
                'msmpeg4v3',
                'huffyuv',
                'qtrle',
                'aac',
                'libmp3lame',
                'libopus',
                'libvorbis',
                'ac3',
                'eac3',
                'flac',
                'alac',
                'pcm_s16le',
                'pcm_s24le',
                'amr_nb',
                'amr_wb',
                'g726',
                'dca',
                'wavpack',
                'mp2',
            ]
        if (self.isVideo and self.isAudio) or forceMerged:
            return [
                'libx264',
                'libx265',
                'libvpx',
                'libvpx-vp9',
                'mpeg4',
                'prores',
                'dnxhd',
                'ffv1',
                'h263',
                'theora',
                'h264',
            ]
        elif self.isVideo or forceVideo:
            return [
                'libx264',
                'libx265',
                'libvpx',
                'libvpx-vp9',
                'mpeg4',
                'prores',
                'dnxhd',
                'ffv1',
                'h263',
                'h264',
                'theora',
                'vp6',
                'msmpeg4v2',
                'msmpeg4v3',
                'huffyuv',
                'qtrle',
            ]
        elif self.isAudio or forceAudio:
            return [
                'aac',
                'libmp3lame',
                'libopus',
                'libvorbis',
                'ac3',
                'eac3',
                'flac',
                'alac',
                'pcm_s16le',
                'pcm_s24le',
                'amr_nb',
                'amr_wb',
                'g726',
                'dca',
                'wavpack',
                'mp2',
            ]

    def getFormatCodec(self, format: str = None) -> list[str] | None:
        match format if format else self.getCodec():
            case 'mp4':
                return ['libx264', 'libx265', 'libaom-av1', 'mpeg4', 'h264', 'h265', 'h263']
            case 'webm':
                return ['libvpx', 'libvpx-vp9', 'mpeg2video']
            case 'wmv':
                return ['wmv1', 'wmv2', 'wmv3']
            case 'ogg':
                return ['libtheora']
            case 'mov':
                return ['prores', 'prores_ks']
            case 'm4a':
                return ['aac', 'libfdk_aac', 'alac']
            case 'mp3':
                return ['libmp3lame']
            case 'opus':
                return ['libopus']
            case 'mkv':
                return ['libvorbis']
            case 'ac3':
                return ['ac3']
            case 'eac3':
                return ['eac3']
            case 'flac':
                return ['flac']
            case 'wv':
                return ['wavpack']
            case 'tta':
                return ['tta']
            case 'wav':
                return ['pcm_s16le', 'pcm_s24le', 'pcm_s32le', 'pcm_u8']
            case _:
                return None

    def getCodecFormat(self, codec: str = None) -> str | None:
        match self.videoCodec if not codec else codec:
            case 'libx264' | 'h264':
                return 'mp4'
            case 'libx265' | 'h265':
                return 'mp4'
            case 'libvpx' | 'vp8' | 'vpx':
                return 'webm'
            case 'libvpx-vp9' | 'vp9':
                return 'webm'
            case 'libaom-av1' | 'av1':
                return 'mp4'
            case 'mpeg4':
                return 'mp4'
            case 'mpeg2video' | 'mp2':
                return 'webm'
            case 'wmv1' | 'wmv2' | 'wmv3' | 'wmv':
                return 'wmv'
            case 'libtheora' | 'ogg':
                return 'ogg'
            case 'prores' | 'prores_ks' | 'rawvideo' | 'mov':
                return 'mov'
            case 'aac' | 'libfdk_aac':
                return 'm4a'
            case 'libmp3lame' | 'mpeg3' | 'mp3':
                return 'mp3'
            case 'libopus':
                return 'opus'
            case 'libvorbis' | 'mkv':
                return 'mkv'
            case 'ac3':
                return 'ac3'
            case 'eac3':
                return 'eac3'
            case 'flac':
                return 'flac'
            case 'alac':
                return 'm4a'
            case 'wavpack':
                return 'wv'
            case 'tta':
                return 'tta'
            case 'pcm_s16le' | 'pcm_s24le' | 'pcm_s32le' | 'pcm_u8' | 'rawsound' | 'wav':
                return 'wav'
            case _:
                return None

    def getCodecList(self, forceAll: bool = False, forceMerged: bool = False, forceVideo: bool = False,
                     forceAudio: bool = False) -> list[
                                                      str] | None:
        if forceAll:
            return [
                'h264',
                'h265',
                'vp9',
                'av1',
                'mpeg4',
                'mpeg2',
                'prores',
                'theora',
                'wmv',
                'avi',
                'mpeg-4',
                'mpeg-2',
                'wmv',
                'theora',
                'ffv1',
                'huffyuv',
                'lagarith',
                'prores',
                'utvideo',
                'rawvideo',
                'yuv4mpegpipe',
                'aac',
                'mp3',
                'opus',
                'vorbis',
                'ac3',
                'e-ac3',
                'amr-nb',
                'amr-wb',
                'wma',
                'flac',
                'alac',
                'wavpack',
                'tta',
                'pcm_s16le',
                'pcm_s24le',
                'pcm_s32le',
                'pcm_u8',
                'wav',
            ]
        elif (self.isVideo and self.isAudio) or forceMerged:
            return [
                'h264',
                'h265',
                'vp9',
                'av1',
                'mpeg4',
                'mpeg2',
                'prores',
                'theora',
                'wmv',
                'avi',
            ]
        elif self.isVideo or forceVideo:
            return [
                'h264',
                'h265',
                'vp8',
                'vp9',
                'av1',
                'avi',
                'mpeg-4',
                'mpeg-2',
                'wmv',
                'theora',
                'ffv1',
                'huffyuv',
                'lagarith',
                'prores',
                'utvideo',
                'rawvideo',
                'yuv4mpegpipe',
            ]
        elif self.isAudio or forceAudio:
            return [
                'aac',
                'mp3',
                'opus',
                'vorbis',
                'ac3',
                'e-ac3',
                'amr-nb',
                'amr-wb',
                'wma',
                'flac',
                'alac',
                'wavpack',
                'tta',
                'pcm_s16le',
                'pcm_s24le',
                'pcm_s32le',
                'pcm_u8',
                'wav',
            ]

    def getFormatList(self, forceAll: bool = False, forceVideo: bool = False, forceAudio: bool = False,
                      forceMerged: bool = False) -> list[
                                                        str] | None:

        if forceAll:
            return [
                'mp4',
                'mkv',
                'mov',
                'webm',
                'avi',
                'wmv',
                'flv',
                '3gp',
                '3g2',
                'mxf',
                'mpeg-ts',
                'dv',
                'ogv',
                'm4v',
                'mpegv',
                'h264',
                'h265',
                'mpeg-es',
                'ivf',
                'mp3',
                'aac',
                'wav',
                'flac',
                'alac',
                'ogg',
                'wma',
                'aiff',
                'opus',
                'amr',
                'm4a',
                'dsd',
                'ape',
            ]

        elif (self.isVideo and self.isAudio) or forceMerged:
            return [
                'mp4',
                'mkv',
                'mov',
                'webm',
                'avi',
                'wmv',
                'flv',
                '3gp',
                '3g2',
                'mxf',
                'mpeg-ts',
                'dv',
                'ogv',
            ]
        elif self.isVideo or forceVideo:
            return [
                'm4v',
                'mpegv',
                'h264',
                'h265',
                'mpeg-es',
                'ivf',
            ]
        elif self.isAudio or forceAudio:
            return [
                'mp3',
                'aac',
                'wav',
                'flac',
                'alac',
                'ogg',
                'wma',
                'aiff',
                'opus',
                'amr',
                'm4a',
                'dsd',
                'ape',
            ]

    @staticmethod
    def getMethodList():
        return [
            'veryfast',
            'fast',
            'slow',
            'veryslow',
        ]

    def getDurationCMD(self) -> list[str]:

        return [
            self.ffprobePath,
            "-i",
            self.videoPath,
            "-show_entries",
            "format=duration",
            "-v",
            "quiet",
            "-of",
            "csv=p=0"
        ]

    def getCodecCMD(self) -> list[str] | None:

        if self.isVideo:
            return [
                self.ffprobePath,
                "-v",
                "error",
                "-select_streams",
                "v:0",
                "-show_entries",
                "stream=codec_name",
                "-of",
                "csv=p=0",
                self.videoPath
            ]
        elif self.isAudio:
            return [
                self.ffprobePath,
                "-v",
                "error",
                "-select_streams",
                "a",
                "-show_entries",
                "stream=codec_name",
                "-of",
                "csv=p=0",
                self.videoPath
            ]

    def getDuration(self) -> float | None:
        if self.videoPath:
            cmd = self.getDurationCMD()
            result = float(subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE).stdout.readline().strip().decode("utf-8"))

            return result

    def getCodec(self) -> str | None:
        if self.videoPath:
            cmd = self.getCodecCMD()

            result = str.lower(
                subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readline().strip().decode(
                    "utf-8"))

            return result

    def getFormat(self) -> str | None:
        if self.videoPath:
            result = self.getNameExtension()[1]

            return result

    def getNameExtension(self) -> list[str] | None:

        if self.videoPath:
            fileName: str = os.path.splitext(self.videoPath)[0]
            fileExtension: str = os.path.splitext(self.videoPath)[1].strip('.')

            return [fileName, fileExtension]

    def getConvertCMD(self, forceMerged: bool = False, forceVideo: bool = False, forceAudio: bool = False) -> list[
                                                                                                                  str] | None:

        global codec, name, extension, format

        if self.isVideo or self.isAudio:
            codec = self.getCodec()
            name, extension = self.getNameExtension()

        if (self.isVideo and self.isAudio) or forceMerged:

            getCodec = self.getFormatCodec(extension)
            for c in getCodec:
                getFormat = self.getCodecFormat(c)

                if getFormat == extension:
                    format = getFormat
                    break
            print(format)

            exit()

        elif self.isVideo or forceVideo:
            ...
        elif self.isAudio or forceAudio:
            ...

    def convertToMP4(self):
        if self.isVideo or self.isAudio:
            self.canConvert = True

        if not self.isVideo:
            atlas.Log(f"The file must be a video file!", "warn")
            self.canConvert = False

        if len(self.ffmpegPath) > 0 and len(self.videoPath) > 0 and self.canConvert and len(self.method) > 0:

            fileName: str = os.path.splitext(self.videoPath)[0]
            fileExt: str = os.path.splitext(self.videoPath)[1].strip('.')

            codecCMD: list[str] = [
                f"{self.ffprobePath}",
                "-v", "error",
                "-select_streams", "v:0",
                "-show_entries", "stream=codec_name",
                "-of", "csv=p=0",
                self.videoPath
            ]

            videoCodec = subprocess.run(codecCMD, capture_output=True, text=True).stdout.strip()
            atlas.Log(f"Video codec is: [{videoCodec}]", "suc")

            if videoCodec in ["prores", "vp9", "h264"] and fileExt in ["mov", "mkv"]:
                convertCMD: list[str] = [
                    self.ffmpegPath,
                    "-i", self.videoPath,
                    "-c:v", "libvpx-vp9",
                    "-preset", self.method,
                    "-y", f"{fileName}.mp4"
                ]

                duration_cmd: list[str] = [
                    self.ffprobePath,
                    "-i", self.videoPath,
                    "-show_entries", "format=duration",
                    "-v", "quiet",
                    "-of", "csv=p=0"
                ]

                frames_cmd: list[str] = [
                    self.ffprobePath,
                    "-i", self.videoPath,
                    "-v", "quiet",
                    "-select_streams", "v:0",
                    "-show_entries", "stream=nb_frames",
                    "-of", "default=nokey=1:noprint_wrappers=1"
                ]
                video_duration = float(subprocess.run(duration_cmd, capture_output=True, text=True).stdout.strip())
                atlas.Log(f"Video duration is: [{video_duration} seconds]", "suc")
                video_frames = int(subprocess.run(frames_cmd, capture_output=True, text=True).stdout.strip())
                atlas.Log(f"Video frames are: [{video_frames}/frames]", "suc")

                atlas.Log(f"The video is converting to mp4: [{self.videoPath}]", "suc")

                process = subprocess.Popen(convertCMD, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

                with alive_bar(
                        int(video_frames),
                        title=f"{Style.RESET_ALL}[{Fore.CYAN}={Style.RESET_ALL}] {Fore.CYAN}Converting..{Style.RESET_ALL}",
                        bar="smooth",
                        enrich_print=False,
                        receipt=True,
                        elapsed=True,
                        monitor=True,
                        force_tty=True,
                        manual=True,
                ) as bar:
                    for line in process.stderr:
                        if "frame=" in line:
                            match = re.search(r"frame=\s*(\d+)", line)
                            if match:
                                current_frame = int(match.group(1))
                                progress = (current_frame / video_frames)
                                bar(progress)
                process_return = process.wait()
                if process_return == 0:
                    atlas.Log(f"The video is successfully converted to mp4: [{fileName}.mp4]", "suc")
                else:
                    atlas.Log(f"The video failed on converting to mp4: [{self.videoPath}]", "err")
            else:
                atlas.Log(
                    f"The videoPath can't be converted. Unsupported codec: [{videoCodec if len(videoCodec) > 0 else "empty"}] or extension: [{fileExt if len(fileExt) > 0 else "empty"}].",
                    "err")

        else:
            atlas.Log(f"The file cannot be converted!", "err")


ffmpeg = FFMPEG(r"C:\ffmpeg", r"C:\ffmpeg",
                r"C:\Users\atlasfirarda\Downloads\dummy-audio.mp4", "veryfast", "mp3", "")
ffmpeg.getConvertCMD()
atlas.stopLog()
