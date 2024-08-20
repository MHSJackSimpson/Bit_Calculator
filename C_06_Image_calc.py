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


image_ans = image_calc()
print(image_ans)
