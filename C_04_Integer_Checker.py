# Ask user for width and loop until they
# enter a number more than zero
def int_check(question, low):

    error = "Please enter a number with a value greater than 0 and without a decimal :)\n"
    while True:

        try:
            # ask the user for a number
            response = int(input(question))

            # check that the number is more than zero
            if response >= low:
               return response
            else:
                print(error)
        except ValueError:
            print(error)


# main routine goes here
for item in range(0, 2):
    integer = int_check("integer: ",0)
    print(integer)

print()

for item in range(0, 2):
    height = int_check("height: ",0)
    print(height)

print()

for item in range(0, 2):
    width = int_check("width: ",0)
    print(width)

print()
