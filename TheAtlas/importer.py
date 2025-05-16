from modules.RequirementModule import installRequirements
from modules.LoggerModule import log, banner


def importStart() -> bool:

    banner()

    if installRequirements(
        [
            "yt-dlp",
            "inquirer",
            "datetime",
            "requests",
        ]
    ):

        ...
        # from modules.YoutubeModule import (
        #     SelectUrl,
        #     SelectFormat,
        #     SetTitle,
        #     module,
        # )

        # if not SelectUrl("https://www.youtube.com/watch?v=THInIdodWQQ"):
        #     ...
        # if not SelectFormat():
        #     ...
        # if not SetTitle():
        #     ...
