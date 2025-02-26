from colored import fg, attr
import random


def green(text):
    return "%s%s%s" % (fg("green"), text, attr("reset"))


def red(text):
    return "%s%s%s" % (fg("red"), text, attr("reset"))


def yellow(text):
    return "%s%s%s" % (fg("yellow"), text, attr("reset"))


def blue(text):
    return "%s%s%s" % (fg("blue"), text, attr("reset"))


def magenta(text):
    return "%s%s%s" % (fg("magenta"), text, attr("reset"))


def cyan(text):
    return "%s%s%s" % (fg("cyan"), text, attr("reset"))
