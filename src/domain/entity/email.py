import re


class Email:
    def __init__(self, email: str) -> None:
        self.email = email
        self.__validate()

    def get_value(self) -> str:
        return self.email

    def __validate(self) -> None:
        if not re.match(r'^[\w-]+(\.[\w-]+)*@([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$', self.email):
            raise ValueError('Invalid email')
