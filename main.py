import re

def find_all_emails(input_string):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    matches = re.findall(email_pattern, input_string)
    if matches:
        return matches
    else:
        raise ValueError("No email addresses found in the input string.")

if __name__ == "__main__":
    try:
        user_input = input("Enter a string to search for emails: ")
        emails = find_all_emails(user_input)
        print("Emails found:")
        for email in emails:
            print(f" - {email}")
    except ValueError as e:
        print(f"Error: {e}")
