Address-Validator
Simple Python script to validate whether a string looks like an email address.

This repository contains a minimal email-checking function in AddressValidator.py. The function performs basic checks for the presence of @ and a . in the string and prints whether the address is valid or not.

Files
AddressValidator.py — contains a single function email(address) that prints validation results.
Quick start
Run the script directly with Python:

python AddressValidator.py
Or import and call the function from another script:

from AddressValidator import email

email("abc@gmailcom")
Expected output for the current script
For email("abc@gmailcom") the script prints:
Invalid Email Address
because there is no . in the domain part.
How it works (current implementation)
The current email(address) function:

Uses str.find to check whether . and @ exist anywhere in the string.
Prints "This is a valid email address" if both characters exist, otherwise prints "Invalid Email Address".
The function always prints the message and returns None.
Limitations / Known issues
Validation is overly simplistic:
It only checks existence of @ and . anywhere in the string — it does not ensure @ comes before the final dot, or validate domain or local-part rules.
It prints results instead of returning a boolean, which limits reusability.
It accepts invalid addresses like ".@." or user@.com as valid if both characters exist.
It does not strip whitespace or handle Unicode, quoted local parts, or advanced RFC-compliant cases.
Suggested improvements
Return a boolean (or raise exceptions) instead of printing.
Ensure @ appears once and there's a . after the @.
Use a regular expression for a better basic validation (or use a library for full RFC compliance).
Example improved implementation (basic, more correct):

# improved_email_validator.py
import re

EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

def is_valid_email(address: str) -> bool:
    """Return True if address matches a simple email pattern, otherwise False."""
    if not isinstance(address, str):
        return False
    address = address.strip()
    return bool(EMAIL_REGEX.match(address))

if __name__ == "__main__":
    tests = [
        "pie@gmail.com",
        "xyz@gmail.com",
        "user@sub.domain.co",
        "invalid@.com",
    ]
    for t in tests:
        print(t, "->", is_valid_email(t))
Contributing
Contributions are welcome. If you want to improve validation, consider:

Adding unit tests.
Replacing print-based behavior with return values.
Documenting edge cases and examples.
License
Add a LICENSE file or choose a license (e.g. MIT) for this project.

Author / Contact
Repository owner: codebyprathamesh