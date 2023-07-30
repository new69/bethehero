from pycpfcnpj import cpfcnpj  # type: ignore

from src.domain.entity.validators.validator_interface import ValidatorInterface


class BrazilianDocument(ValidatorInterface):
    def __init__(self, document: str) -> None:
        self.document = document
        self.validate()

    def get_value(self) -> str:
        return self.document

    def validate(self) -> None:
        if not cpfcnpj.validate(self.document):
            raise ValueError('Invalid document')
