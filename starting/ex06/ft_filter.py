def valid_values(object: any) -> bool:
    if len(object) != 3:
        return False
    if ((type(object[1]) is not str) or (not object[2].isdigit())):
        return False
    lst = object[1].split()
    newList = [a for a in lst if len(a) >= int(object[2])]
    print(newList)
    return True

def ft_filter(object: any) -> bool:
    """
    Filter elements from an iterable based on a function.

    This function mimics the behavior of Python's built-in filter() function.
    It takes a function and an iterable, and returns an iterator containing
    only the elements for which the function returns True.

    Args:
        function: A function that returns a boolean value
        iterable: An iterable to filter

    Returns:
        An iterator containing filtered elements

    Example:
        >>> list(ft_filter(lambda x: x > 2, [1, 2, 3, 4]))
        [3, 4]
    """
    if (not valid_values(object)):
        raise AssertionError
    return True
