import pytest
from replace_last_backslash import replace_last_backslash


def test_replace_last_backslash():
    assert (
        replace_last_backslash("D:the\\string\\in\\this\\path\\fix.jpg")
        == "D:the\\string\\in\\this\\path/fix.jpg"
    )
    assert replace_last_backslash("C:hi\\every\\one.jpg") == "C:hi\\every/one.jpg"
    assert replace_last_backslash("C:some\\path\\") == "C:some\\path/"
    assert replace_last_backslash("no_backslash") == "no_backslash"
    assert replace_last_backslash("") == ""

    # Testing a string where all characters are backslashes
    assert replace_last_backslash("\\\\\\\\") == "\\\\\\/"
    # Testing a string with mixed slashes ("/" and "\\")
    assert replace_last_backslash("C:/Users\\John\\Desktop") == "C:/Users\\John/Desktop"


def test_replace_last_backslash_with_multiple_backslashes():
    assert replace_last_backslash("A\\B\\C\\D\\E\\F") == "A\\B\\C\\D\\E/F"
    assert replace_last_backslash("X\\\\Y\\\\Z") == "X\\\\Y\\/Z"
    assert (
        replace_last_backslash("\\\\server\\share\\file.txt")
        == "\\\\server\\share/file.txt"
    )


def test_replace_last_backslash_with_special_characters():
    assert (
        replace_last_backslash("E:\\path\\with\\spaces\\file name.txt")
        == "E:\\path\\with\\spaces/file name.txt"
    )
    assert (
        replace_last_backslash("C:\\path\\with\\underscore\\file_name.txt")
        == "C:\\path\\with\\underscore/file_name.txt"
    )
    assert (
        replace_last_backslash("D:\\path\\with\\parentheses\\(file).txt")
        == "D:\\path\\with\\parentheses/(file).txt"
    )


def test_replace_last_backslash_with_empty_string():
    assert replace_last_backslash("") == ""


def test_replace_last_backslash_with_strings_without_backslashes():
    assert replace_last_backslash("no_backslash") == "no_backslash"
    assert replace_last_backslash("forward/slash/only") == "forward/slash/only"
    assert replace_last_backslash("normal string without slashes") == "normal string without slashes"

