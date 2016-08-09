__author__ = 'liusong'

import re


def test_method():
    print "============test match==========="
    print re.match("a", "abc")

    print "============test search==========="
    print re.search("a", "abc")

    print "============test findall=========="
    print re.findall("a", "abcabcaaa")


def test_file(file_path, pattern):
    with open(file_path) as f:
        for l in f.readlines():
            if re.match(pattern, l) is not None:
                print l

if __name__ == "__main__":
    #test_method()
    '''
    # A|B, match A or B
    print "================pattern1==================="
    test_pattern1 = "^abc{3,5}d$|11"
    test_file("/home/liusong/code/archieve/test_doc", test_pattern1)

    # ?, match 0 or 1 repetition of RE
    print "================pattern2==================="
    test_pattern2 = "a?"
    test_file("/home/liusong/code/archieve/test_doc", test_pattern2)

    # +, match 1 or more repetition of RE
    print "================pattern3==================="
    test_pattern3 = "a+"
    test_file("/home/liusong/code/archieve/test_doc", test_pattern3)

    #{n, m}, match n to m repetition of RE

    # [], [a-z] match all characters from a to z, [0-9] match all numbers from 0 to 9
    test_pattern4 = "[0-3]"
    test_file("/home/liusong/code/archieve/test_doc", test_pattern4)

    # [], [a-z] match all characters from a to z, [0-9] match all numbers from 0 to 9
    test_pattern4 = "[0-9]"
    test_file("/home/liusong/code/archieve/test_doc", test_pattern4)

    # [^], [^a-z] match all characters except from a to z, [0-9] match all numbers except from 0 to 9
    test_pattern4 = "[^0-9]"
    test_file("/home/liusong/code/archieve/test_doc", test_pattern4)

    # \d for number, \w for words, \s for blank char
    # \D for non number, \w for non words, \s for non blank char
    test_pattern4 = "\D"
    test_file("/home/liusong/code/archieve/test_doc", test_pattern4)
    '''

    # match for ^^$$, start with ^ and ^ match for 1 or more repetition, end with $ and $ match for 1 or more repetition.
    test_pattern4 = "^\^+\$+$"
    test_file("/home/liusong/code/archieve/test_doc", test_pattern4)


