"""File with custom project exceptions"""

class InvalidDataFormatException(Exception):
    """Raises when recieved data not include sepatators "=" and "&"."""

    message = "Invalid data format"
