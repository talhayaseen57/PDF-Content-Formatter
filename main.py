# This is my main Python script.

def pdf_content_formatter(content):
    """
    This is the method which formate the copied content from PDF.
    """
    new_content = content.replace("\n", " ")
    print("Your formatted content is bellow:\n"+"--"*20)
    print(new_content)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    paragraph = ""

    print("Enter your copied content bellow:\n"
          ">> '''Press Ctrl+V and then Enter key twice''' <<")

    while True:
        line = input()
        if line.strip():  # Check if the line is not empty
            paragraph += line + "\n"  # Add the line to the user_input variable
        else:
            # If the line is empty, it means the user pressed Enter without typing anything
            # You can decide how many empty lines indicate the end of input
            empty_line_count = 0

            # Count consecutive empty lines
            while empty_line_count < 2:  # Change the number to set the threshold
                empty_line = input()
                if not empty_line.strip():
                    empty_line_count += 1
                else:
                    # If a non-empty line is entered, reset the count
                    empty_line_count = 0
                    paragraph += "\n"  # Add a newline to the user_input

            break

    pdf_content_formatter(paragraph)
