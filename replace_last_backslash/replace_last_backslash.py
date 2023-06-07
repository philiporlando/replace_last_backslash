def replace_last_backslash(path):
    """
    Replaces the last backslash '\\' in the given path string with a forward slash '/'.

    Args:
        path (str): The input path string.

    Returns:
        str: The modified path string with the last backslash replaced by a forward slash.
    """
    if "\\" in path:
        last_backslash_index = path.rindex("\\")
        path = f"{path[:last_backslash_index]}/{path[last_backslash_index+1:]}"
    return path
