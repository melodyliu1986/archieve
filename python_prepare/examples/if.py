__author__ = 'liusong'

number = 22
guess = raw_input("Please enter an integer: ")

if guess == number:
    print "Congratulations, you guessed it."
elif guess > number:
    print "Sorry, it is higher that it, please try again."
else:
    print "Sorry, it is lower that it, please try again."

print "Done"
