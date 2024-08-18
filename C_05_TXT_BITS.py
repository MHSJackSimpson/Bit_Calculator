def calc_text_bits():
    # get text from user
    response = input("Enter some text...")

    # calculate bits needed
    num_chars = len(response)
    num_bits = num_chars * 8

    # Set up answer and return it
    answer = (f"{response} has {num_chars} characters."
              f"\n We need {num_chars} x 8 bits to represent it"
              f"\nwhich is {num_bits} bits")

    return answer


# Main routine goes here
text_ans = calc_text_bits
print(text_ans)
