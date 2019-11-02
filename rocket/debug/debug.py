from rocket.debug.reload import auto_reload


def debug(target):
    return auto_reload(target=target)
