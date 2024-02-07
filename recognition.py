import easyocr
import re


def email_recognition(file_path):
    """
    This function uses the easyocr library to recognize text in an image and extract email addresses.

    :param file_path: The path to the input image file.
    :return: A list of email addresses found in the image.
    """
    try:
        reader = easyocr.Reader(["en"])
        result = reader.readtext(file_path, detail=0)
        emails = re.findall(r'[\w\.-]+@[\w\.-]+', ' '.join([line for line in result]))
        return emails
    except Exception as e:
        print(f"An error occurred during email recognition: {str(e)}")
        return []


def write_emails(emails, file_path):
    """
    This function writes a list of email addresses to a file.

    :param emails: A list of email addresses to write to the file.
    :param file_path: The path to the output file.
    """
    try:
        with open(file_path, "w") as f:
            for email in emails:
                f.write(email + "\n")
    except Exception as e:
        print(f"An error occurred during email writing: {str(e)}")
    else:
        print(f"Emails written to {file_path}:")


def main():
    """
    This is the main function that calls the email recognition and email writing functions.
    """
    input_image_path = input("Enter the path to the input image: ")
    emails = email_recognition(file_path=input_image_path)
    if emails:
        output_file_path = input("Enter the path to the output file: ")
        write_emails(emails=emails, file_path=output_file_path)
    else:
        print("No email addresses found.")



if __name__ == '__main__':
    main()