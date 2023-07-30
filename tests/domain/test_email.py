import pytest

from src.domain.entity.validators.email import Email


class TestEmail:
    def test_create_a_valid_email(self) -> None:
        email = 'john.doe@email.com'
        expected_result = Email('john.doe@email.com')

        assert expected_result.get_value() == email

    def test_create_invalid_email(self) -> None:
        email = 'john.doe'

        with pytest.raises(ValueError) as excinfo:
            Email(email)

        assert str(excinfo.value) == 'Invalid email'
