from pycpfcnpj import cpfcnpj  # type: ignore


class BrazilianDocument:
    def __init__(self, document: str) -> None:
        self.document = document
        self.__validate()

    def get_value(self) -> str:
        return self.document

    def __validate(self) -> None:
        if not cpfcnpj.validate(self.document):
            raise ValueError('Invalid document')
