# Generates headings (eg: ----- Heading -----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
-Choose a file type (Integer, Image or Text)
-put the numbers or text into the program.
-type "xxx" to exit the program.
    ''')

# Main routine goes here


want_instructions = input("Press <enter> to read the instructions " "or any key to continue ")

if want_instructions == "":
    instructions()

print("program continues")


# asks user for file type ( Integer / image / text / xxx)

def get_filetype():
    while True:
        response = input("File type: ").lower()

        # check for 'i' or the exit code
        if response == "xxx" or response == "i":
            return response

        elif response in ['integer', 'int']:
            return "integer"

        elif response in ['image', 'img', 'picture', 'p']:
            return "image"

        elif response in ['text', 'txt', 't']:
            return "text"

        else:
            print("Please enter a valid file type")
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


# calc how many bits are needed to represent an integer
def image_calc():
    height = int_check("height: ", 1)
    width = int_check("width: ", 1)

    num_pixels = width * height
    num_bits = num_pixels * 24

    answer = (f"Number of pixels: {width} x {height} = {num_pixels}"
              f"\nNumber of bits: {num_pixels} x 24 = {num_bits}")

    return answer


def integer_calc():
    integer = int_check("Integer: ", 0)
    raw_binary = bin(integer)
    binary = raw_binary[2:]
    num_bits = len(binary)

    answer = f"{integer} in binary is {binary}. " \
             f"\nWe need {num_bits} to represent it."
    return answer


def calc_text_bits():
    # get text from user
    response = input("Enter some text: ")

    # calculate bits needed
    num_chars = len(response)
    num_bits = num_chars * 8

    # Set up answer and return it
    answer = (f"{response} has {num_chars} characters."
              f"\n We need {num_chars} x 8 bits to represent it"
              f"\nwhich is {num_bits} bits")

    return answer


# Main routine goes here
while True:
    file_type = get_filetype()

    if file_type == 'i':

        want_image = input("Press <enter> for an integer or any key for an image")
        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"

    if file_type == "image":
        image_ans = image_calc()
        print(image_ans)
    elif file_type == "integer":
        integer_ans = integer_calc()
        print(integer_ans)
    else:
        text_ans = calc_text_bits()
        print(text_ans)
    if file_type == "xxx":
        break
