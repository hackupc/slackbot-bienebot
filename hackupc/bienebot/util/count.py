# Global count
__count = 1


def get_count():
    """
    Retrieve global count
    :return: count
    """
    return __count


def update_count():
    """
    Increase global count
    :return: count increased
    """
    global __count
    __count += 1
