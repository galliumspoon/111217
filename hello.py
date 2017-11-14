name = raw_input("What's your name? ")
age = raw_input("What's your age? ")

print 'Hello {0}!'.format(name)
try:
    if float(age) >= 18:
        vote = raw_input("Have you registered to vote yet? (y/n) ")
        while vote != "y" or vote != "n":
            print("y or n only please")
            vote = raw_input("Have you registered to vote yet? (y/n) ")
        if vote == "y":
            print("Good job! :)")
        elif vote == "n":
            print ("Please do. ;(")
    else:
        print("I can't believe you're {0}!".format(age))

except ValueError:
    print("I'm sorry, but please but a numerical value for your age.")
