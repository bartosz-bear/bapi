import locale
import io

def guess_encoding(file):

    """guess the encoding of the given file"""
    with io.open(file, "rb") as f:
        data = f.read(5)

    if data.startswith(b"\xEF\xBB\xBF"):  # UTF-8 with a "BOM"
        return "utf-8-sig"

    elif data.startswith(b"\xFF\xFE") or data.startswith(b"\xFE\xFF"):
        return "utf-16"

    else:  # guessing utf-8 doesn't work in Windows, so we just give it a try:
        try:
            with io.open(file, encoding="utf-8") as f:
                return "utf-8"
        except:
            return locale.getdefaultlocale()[1]