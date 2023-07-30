import pytest

from src.domain.entity.brazilian_document import BrazilianDocument


class TestBrazilianDocument:
    def test_create_a_valid_document_number(self) -> None:
        document_number = '52.203.101/0001-63'
        expected_result = BrazilianDocument(document_number)

        assert expected_result.get_value() == document_number

    def test_create_invalid_document_number(self) -> None:
        document_number = '152.203.101/0001-63'

        with pytest.raises(ValueError) as excinfo:
            BrazilianDocument(document_number)

        assert str(excinfo.value) == 'Invalid document'
