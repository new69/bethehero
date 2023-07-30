import pytest

from src.domain.entity.validators.phone_number import PhoneNumber


class TestPhoneNumber:
    def test_create_a_valid_phone_number(self) -> None:
        phone_number = '+55(11)999999999'
        expected_result = PhoneNumber(phone_number)

        assert expected_result.get_value() == phone_number

    def test_create_invalid_phone_number(self) -> None:
        phone_number = '+5511999999999'

        with pytest.raises(ValueError) as excinfo:
            PhoneNumber(phone_number)

        assert str(excinfo.value) == 'Invalid phone number'
