import re


class PhoneNumber:
    def __init__(self, phone: str) -> None:
        self.phone = phone
        self.__validate()

    def get_value(self) -> str:
        return self.phone

    def __validate(self) -> None:
        if not re.match(r'^(\+[0-9]{1,3}|\+1[0-9]{3})(\([0-9]{2}\))([ ]?)([0-9]{4,5})([-]?)([0-9]{4})$', self.phone):
            raise ValueError('Invalid phone number')
