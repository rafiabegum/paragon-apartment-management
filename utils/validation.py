# Rafia Begum
# 24043914

import re


class Validation:

    @staticmethod
    def is_empty(value):
        """Check if a field is empty."""
        return value.strip() == ""

    @staticmethod
    def validate_email(email):
        """Validate email format."""
        pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
        return re.match(pattern, email) is not None

    @staticmethod
    def validate_phone(phone):
        """Validate UK phone number (11 digits starting with 07)."""
        pattern = r'^07\d{9}$'
        return re.match(pattern, phone) is not None

    @staticmethod
    def validate_ni_number(ni_number):
        """
        Validate National Insurance number.
        Example format:
        QQ123456C
        """
        pattern = r'^[A-Z]{2}\d{6}[A-Z]$'
        return re.match(pattern, ni_number) is not None

    @staticmethod
    def validate_positive_number(value):
        """Check if value is a positive number."""
        try:
            return float(value) > 0
        except ValueError:
            return False

    @staticmethod
    def validate_rooms(value):
        """Rooms must be between 1 and 10."""
        try:
            rooms = int(value)
            return 1 <= rooms <= 10
        except ValueError:
            return False


if __name__ == "__main__":

    print("Email:", Validation.validate_email("admin@pams.com"))

    print("Phone:", Validation.validate_phone("07123456789"))

    print("NI Number:", Validation.validate_ni_number("QQ123456C"))

    print("Positive Rent:", Validation.validate_positive_number("950"))

    print("Rooms:", Validation.validate_rooms("2"))