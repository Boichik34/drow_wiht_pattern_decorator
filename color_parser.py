
def red_parser(colors):
    if isinstance(colors, str):
        return 0.3, 0.0, 0.0
    elif float(colors[0]) < 0.8:
        return float(colors[0]) + 0.3, float(colors[1]), float(colors[2])
    elif float(colors[0]) > 0.8:
        return False


def green_parser(colors):
    if isinstance(colors, str):
        return 0.0, 0.3, 0.0
    elif float(colors[1]) < 0.8:
        return float(colors[0]), float(colors[1]) + 0.3, float(colors[2])
    elif float(colors[1]) > 0.8:
        return False


def blue_parser(colors):
    if isinstance(colors, str):
        return 0.0, 0.0, 0.3
    elif float(colors[2]) < 0.8:
        return float(colors[0]), float(colors[1]), float(colors[2]) + 0.3
    elif float(colors[2]) > 0.8:
        return False


def red_abate_parser(colors):
    if isinstance(colors, str) or float(colors[0]) < 0.1:
        return False
    elif float(colors[0]) < 0.3:
        if float(colors[1]) > 0 or float(colors[2]) > 0:
            return float(colors[0]) - 0.3, float(colors[1]), float(colors[2])
        else:
            return "white"
    elif float(colors[0]) > 0.3:
        return float(colors[0]) - 0.3, float(colors[1]), float(colors[2])


def green_abate_parser(colors):
    if isinstance(colors, str) or float(colors[1]) < 0.1:
        return False
    elif float(colors[1]) < 0.3:
        if float(colors[0]) > 0 or float(colors[2]) > 0:
            return float(colors[0]), float(colors[1]) - 0.3, float(colors[2])
        else:
            return "white"
    elif float(colors[1]) > 0.3:
        return float(colors[0]), float(colors[1]) - 0.3, float(colors[2])


def blue_abate_parser(colors):
    if isinstance(colors, str) or float(colors[2]) < 0.1:
        return False
    elif float(colors[2]) < 0.3:
        if float(colors[0]) > 0 or float(colors[1]) > 0:
            return float(colors[0]), float(colors[1]), float(colors[2]) - 0.3
        else:
            return "white"
    elif float(colors[2]) > 0.3:
        return float(colors[0]), float(colors[1]), float(colors[2]) - 0.3