import requests


def getLatestVersion(requirement) -> str:

    if not requirement:
        return None

    try:
        url: str = f"https://pypi.org/pypi/{requirement}/json"
        response = requests.get(url)

        if response.status_code == 200:
            version = response.json()["info"]["version"]
            return version
        else:
            return None
    except:
        return None


try:
    import colored

    del colored
except ImportError:
    import subprocess
    import sys

    subprocess.check_call(
        [
            sys.executable,
            "-m",
            "pip",
            "--quiet",
            "install",
            f"colored=={getLatestVersion("colored")}",
        ]
    )

from colored import Fore, style


def green(text) -> str:
    if not text:
        return None

    return "%s%s%s" % (Fore.rgb(54, 245, 45), text, style("reset"))


def red(text) -> str:
    if not text:
        return None

    return "%s%s%s" % (Fore.rgb(245, 54, 45), text, style("reset"))


def yellow(text) -> str:
    if not text:
        return None

    return "%s%s%s" % (Fore.rgb(235, 255, 0), text, style("reset"))


def blue(text) -> str:
    if not text:
        return None

    return "%s%s%s" % (Fore.rgb(93, 171, 245), text, style("reset"))


def bold(text) -> str:
    if not text:
        return None

    return "%s%s%s" % (style("bold"), text, style("reset"))
