__author__ = 'liusong'

while True:
    s = raw_input("Please enter something: ")
    if len(s) > 3:
        if s == "quit":
            break
        print "The length of the string is {0}".format(len(s))
    else:
        continue
