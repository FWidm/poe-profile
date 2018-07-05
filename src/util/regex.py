import re


def strip_translation_prefix(string):
    regex = r"^.*>([A-Za-z ]*)"
    subst = r"\1"

    result = re.sub(regex, subst, string, 0)
    if result:
        return result
    else:
        return string
