import re

from src.domain.entity.validators.validator_interface import ValidatorInterface


class PhoneNumber(ValidatorInterface):
    def __init__(self, phone: str) -> None:
        self.phone = phone
        self.validate()

    def get_value(self) -> str:
        return self.phone

    def validate(self) -> None:
        if not re.match(r'^(\+[0-9]{1,3}|\+1[0-9]{3})(\([0-9]{2}\))([ ]?)([0-9]{4,5})([-]?)([0-9]{4})$', self.phone):
            raise ValueError('Invalid phone number')
