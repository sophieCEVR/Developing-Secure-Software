# function to substitute all untrusted characters with
# their corresponding html code. e.g. < is &#60;


def sub(character):
    switcher = {
        " ": "&#32;",
        "!": "&#33;",
        '"': "&#34;",
        "#": "&#35;",
        "$": "&#36;",
        "%": "&#37;",
        "&": "&#38;",
        "'": "&#39;",
        "(": "&#40;",
        ")": "&#41;",
        "*": "&#42;",
        "+": "&#43;",
        ",": "&#44;",
        "-": "&#45;",
        ".": "&#46;",
        "/": "&#47;",
        ":": "&#58;",
        ";": "&#59;",
        "<": "&#60;",
        "=": "&#61;",
        ">": "&#62;",
        "?": "&#63;",
        "@": "&#64;",
        "[": "&#91;",
        "\\": "&#92;",
        "]": "&#93;",
        "^": "&#94;",
        "_": "&#95;",
        "`": "&#96;",
        "{": "&#123;",
        "|": "&#124;",
        "}": "&#125;",
        "~": "&#126;",
        "€": "&#128;"
    }
    return switcher.get(character, character)
    # arg1 returns the replaced character if it matches one in the switcher (e.g. !"£$%)
    # arg2 returns the original character if no substitution is needed (e.g. A-z, 0-9)


def all(data):
    dirty = str(data)
    clean = ""
    for i in range(len(dirty)):
        clean = clean + str(sub(dirty[i]))
    return clean
