import easyocr
import argparse
import re

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="path to input image")
ap.add_argument("-o", "--output", required=True, help="path to output file")
args = vars(ap.parse_args())

def email_recognition():
    """
    This function uses the easyocr library to recognize text in an image and extract email addresses.

    :return: A list of email addresses found in the image.
    """
    try:
        reader = easyocr.Reader(["en"])
        result = reader.readtext(args["input"], detail=0)
        emails = re.findall(r'[\w\.-]+@[\w\.-]+', ' '.join([line for line in result]))
        return emails
    except Exception as e:
        print(f"An error occurred during email recognition: {str(e)}")


def write_emails(emails):
    """
    This function writes a list of email addresses to a file.

    :param emails: A list of email addresses to write to the file.
    """
    try:
        with open(args["output"], "w") as f:
            for email in emails:
                f.write(email + "\n")
    except Exception as e:
        print(f"An error occurred during email writing: {str(e)}")
        return []
    else:
        print(f"Emails written to {args['output']}:")

def main():
    """
    This is the main function that calls the email recognition and email writing functions.
    """
    emails = email_recognition()
    if emails:
        write_emails(emails=emails)
    else:
        print("No email addresses found.")


if __name__ == '__main__':
    main()