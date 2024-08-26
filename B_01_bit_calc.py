# asks user for file type ( Integer / image / text / xxx)
def get_filetype():
    while True:
        response = input("File type: ").lower()
        if file_type == "xxx":
            break
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


# Main routine goes here
while True:
    file_type = get_filetype()

    if file_type == 'i':

        want_image = input("Press <enter> for an integer or any key for an image")
        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"

    print(f"You chose {file_type}")
