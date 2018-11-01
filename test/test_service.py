from webresume.webresume.service import Service
from unittest.mock import MagicMock
mock_return_value = 10
service_to_test = Service()

def set_bad_random_mock_value(value):
    global mock_return_value, service_to_test
    mock_return_value = value
    service_to_test.bad_random = MagicMock(return_value=mock_return_value)

set_bad_random_mock_value(mock_return_value)

# test the mock is correct
def test_bad_random():
    assert(service_to_test.bad_random() == mock_return_value)
    set_bad_random_mock_value(6)
    assert(service_to_test.bad_random() == mock_return_value)

def test_divide():
    # should throw division error when divide by zero
    try:
        service_to_test.divide(0)
        assert(False) # should have thrown ZeroDivError, fail
    except ZeroDivisionError:
        assert(True)
    except:
        assert(False) # should have thrown ZeroDivError, fail

    # should divide mocked value by y
    result = service_to_test.divide(2)
    assert result == mock_return_value / 2

    # should return negative value when divided by negative
    result = service_to_test.divide(-1)
    assert result == mock_return_value / -1
    

def test_abs_plus():
    # returns abs value of a positive plus one
    result = service_to_test.abs_plus(1)
    assert result == 1 + 1

    result = service_to_test.abs_plus(2)
    assert result == 2 + 1

    # returns abs value of negative plus one
    result = service_to_test.abs_plus(-1)
    assert result == 1 + 1

def test_complicated_function():
    divide_mock_value = 4
    service_to_test.divide = MagicMock(return_value=divide_mock_value)
    result = service_to_test.complicated_function(5)
    service_to_test.divide.assert_called_with(5)
    assert result[0] == divide_mock_value
    assert result[1] == mock_return_value % 2